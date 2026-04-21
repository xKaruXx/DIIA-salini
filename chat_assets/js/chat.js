// chat_assets/js/chat.js
// JavaScript para el chat de CORADIR

document.addEventListener('DOMContentLoaded', function() {
    // ===== ELEMENTOS DEL DOM =====
    const messagesContainer = document.getElementById('chatMessages');
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const micButton = document.getElementById('micButton');
    
    // ===== VARIABLES DE ESTADO =====
    let socket = null;
    let isConnected = false;
    let isTyping = false;
    let waitingForResponse = false;
    let chatToken = null;
    
    // ===== VARIABLES DE AUDIO =====
    let mediaRecorder = null;
    let audioChunks = [];
    let isRecording = false;
    let recordingStartTime = null;
    let recordingTimeout = null;
    let isProcessingAudio = false;
    
    // ===== CONFIGURACIÓN =====
    const MIN_RECORDING_DURATION = 500; // 0.5 segundos mínimo
    const MAX_RECORDING_DURATION = 120000; // 2 minutos máximo
    const TOUCH_DELAY = 100; // Delay para evitar conflictos touch/mouse

    // ===== DETECCIÓN DE DISPOSITIVO =====
    let isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    let lastTouchTime = 0;

    // ===== FUNCIONES DE AUDIO =====
    
    async function startRecording() {
        if (isRecording || waitingForResponse || isProcessingAudio) {
            console.log('Grabación bloqueada:', { isRecording, waitingForResponse, isProcessingAudio });
            return;
        }
        
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            console.error('API MediaDevices no disponible');
            showConnectionStatus('Tu navegador no soporta grabación de audio o requiere HTTPS', true);
            return;
        }

        try {
            console.log('Iniciando grabación...');
            
            const stream = await navigator.mediaDevices.getUserMedia({ 
                audio: {
                    echoCancellation: true,
                    noiseSuppression: true,
                    sampleRate: 16000
                } 
            });
            
            const options = {
                mimeType: MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 
                         'audio/webm;codecs=opus' : 'audio/webm'
            };
            
            mediaRecorder = new MediaRecorder(stream, options);
            audioChunks = [];
            recordingStartTime = Date.now();
            
            mediaRecorder.ondataavailable = event => {
                if (event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };
            
            mediaRecorder.onstop = async () => {
                console.log('Grabación detenida');
                await handleRecordingStop();
            };
            
            mediaRecorder.onerror = (event) => {
                console.error('Error en MediaRecorder:', event.error);
                resetRecordingState();
                showConnectionStatus('Error durante la grabación', true);
            };
            
            mediaRecorder.start(100);
            isRecording = true;
            
            micButton.classList.add('recording');
            micButton.innerHTML = '<i class="fas fa-stop"></i>';
            // Mensaje diferente según dispositivo
            const message = isTouchDevice ? 
                'Grabando... Toca de nuevo para enviar' : 
                'Grabando... Suelta para enviar';
            showConnectionStatus(message, false);
            
            recordingTimeout = setTimeout(() => {
                if (isRecording) {
                    console.log('Grabación detenida por timeout');
                    stopRecording();
                }
            }, MAX_RECORDING_DURATION);
            
        } catch (error) {
            console.error('Error al acceder al micrófono:', error);
            resetRecordingState();
            
            let errorMessage = 'Error al acceder al micrófono.';
            if (error.name === 'NotAllowedError') {
                errorMessage = 'Permiso de micrófono denegado. Verifica los permisos.';
            } else if (error.name === 'NotFoundError') {
                errorMessage = 'No se encontró micrófono en tu dispositivo.';
            }
            
            showConnectionStatus(errorMessage, true);
        }
    }

    function stopRecording() {
        if (!isRecording || !mediaRecorder) {
            console.log('No hay grabación activa para detener');
            return;
        }
        
        console.log('Deteniendo grabación...');
        
        if (recordingTimeout) {
            clearTimeout(recordingTimeout);
            recordingTimeout = null;
        }
        
        try {
            if (mediaRecorder.state === 'recording') {
                mediaRecorder.stop();
            }
            
            if (mediaRecorder.stream) {
                mediaRecorder.stream.getTracks().forEach(track => track.stop());
            }
        } catch (error) {
            console.error('Error al detener grabación:', error);
            resetRecordingState();
        }
    }

    async function handleRecordingStop() {
        const recordingDuration = Date.now() - recordingStartTime;
        console.log('Duración de grabación:', recordingDuration + 'ms');
        
        isRecording = false;
        micButton.classList.remove('recording');
        micButton.innerHTML = '<i class="fas fa-microphone"></i>';
        
        if (recordingDuration < MIN_RECORDING_DURATION) {
            console.log('Grabación muy corta, descartando');
            hideConnectionStatus();
            // Mensaje de error diferente según dispositivo
            const errorMessage = isTouchDevice ? 
                'Grabación muy corta. Toca para grabar, toca de nuevo para enviar.' : 
                'Grabación muy corta. Mantén presionado y suelta para enviar.';
            showConnectionStatus(errorMessage, true);
            setTimeout(hideConnectionStatus, 3000);
            return;
        }
        
        if (audioChunks.length === 0) {
            console.log('No hay datos de audio, descartando');
            hideConnectionStatus();
            showConnectionStatus('No se capturó audio. Intenta de nuevo.', true);
            setTimeout(hideConnectionStatus, 3000);
            return;
        }
        
        const audioBlob = new Blob(audioChunks, { 
            type: mediaRecorder.mimeType || 'audio/webm' 
        });
        
        console.log('Audio blob creado:', audioBlob.size + ' bytes');
        
        if (audioBlob.size === 0) {
            console.log('Blob de audio vacío, descartando');
            hideConnectionStatus();
            showConnectionStatus('Audio vacío. Intenta de nuevo.', true);
            setTimeout(hideConnectionStatus, 3000);
            return;
        }
        
        isProcessingAudio = true;
        await sendAudioToServer(audioBlob);
    }

    async function sendAudioToServer(audioBlob) {
        try {
            if (!socket || !isConnected) {
                throw new Error('No hay conexión WebSocket activa');
            }
            
            console.log('Enviando audio al servidor...');
            
            waitingForResponse = true;
            messageInput.disabled = true;
            messageInput.classList.add('input-waiting');
            messageInput.placeholder = 'Procesando audio...';
            sendButton.disabled = true;
            micButton.disabled = true;
            
            addMessage('user', '🎤 Mensaje de voz');
            showConnectionStatus('Enviando audio...', false);
            
            const reader = new FileReader();
            reader.readAsDataURL(audioBlob);
            
            reader.onloadend = function() {
                const base64data = reader.result;
                
                const audioMessage = {
                    message_type: "audio",
                    audio_data: base64data,
                    duration: Date.now() - recordingStartTime,
                    size: audioBlob.size
                };
                
                console.log('Enviando mensaje de audio:', {
                    duration: audioMessage.duration,
                    size: audioMessage.size
                });
                
                socket.send(JSON.stringify(audioMessage));
                hideConnectionStatus();
            };
            
            reader.onerror = function() {
                throw new Error('Error al procesar el archivo de audio');
            };
            
        } catch (error) {
            console.error('Error al enviar audio:', error);
            showConnectionStatus('Error al enviar audio: ' + error.message, true);
            setTimeout(hideConnectionStatus, 3000);
            enableControls();
        } finally {
            isProcessingAudio = false;
        }
    }

    function resetRecordingState() {
        isRecording = false;
        isProcessingAudio = false;
        recordingStartTime = null;
        
        if (recordingTimeout) {
            clearTimeout(recordingTimeout);
            recordingTimeout = null;
        }
        
        if (mediaRecorder && mediaRecorder.stream) {
            mediaRecorder.stream.getTracks().forEach(track => track.stop());
        }
        
        mediaRecorder = null;
        audioChunks = [];
        
        micButton.classList.remove('recording');
        micButton.innerHTML = '<i class="fas fa-microphone"></i>';
        micButton.disabled = false;
    }

    function enableControls() {
        waitingForResponse = false;
        messageInput.disabled = false;
        messageInput.classList.remove('input-waiting');
        messageInput.placeholder = 'Escribe tu mensaje...';
        sendButton.disabled = false;
        micButton.disabled = false;
    }

    // ===== MANEJADORES DE EVENTOS DE AUDIO =====
    
    function handleRecordStart(e) {
        e.preventDefault();
        
        if (isTouchDevice) {
            const now = Date.now();
            if (now - lastTouchTime < TOUCH_DELAY) {
                return;
            }
            lastTouchTime = now;
        }
        
        console.log('Iniciando grabación por evento:', e.type);
        startRecording();
    }

    function handleRecordStop(e) {
        e.preventDefault();
        
        if (!isRecording) {
            return;
        }
        
        console.log('Deteniendo grabación por evento:', e.type);
        stopRecording();
    }

    // ===== FUNCIONES DE UTILIDAD =====
    
    function getTokenFromUrl() {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('token');
    }

    function getClientId() {
        let clientIdData = null;
        try {
            clientIdData = JSON.parse(localStorage.getItem('chatClientData'));
        } catch (e) {
            clientIdData = null;
        }
        
        const now = new Date().getTime();
        const expirationDays = 30;
        const expirationMs = expirationDays * 24 * 60 * 60 * 1000;
        
        let clientId = null;
        if (clientIdData && clientIdData.expiry > now) {
            clientId = clientIdData.id;
        } else {
            clientId = getCookie('chatClientId');
        }
        
        if (!clientId) {
            clientId = generateUUID();
            
            const expiry = now + expirationMs;
            localStorage.setItem('chatClientData', JSON.stringify({
                id: clientId,
                expiry: expiry
            }));
            
            setCookie('chatClientId', clientId, expirationDays);
        }
        
        return clientId;
    }

    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? match[2] : null;
    }

    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = `${name}=${value}; expires=${expires.toUTCString()}; path=/`;
    }

    function generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            const r = Math.random() * 16 | 0;
            const v = c === 'x' ? r : (r & 0x3 | 8);
            return v.toString(16);
        });
    }

    // ===== FUNCIONES DE INTERFAZ =====
    
    // Esto mejora la presentación de los mensajes, o sea ** por listas por ejemplo, mejor el front 
    function processMarkdown(text) {
        // PRIMERO: Procesar URLs ANTES de convertir \n a <br>
        text = text.replace(/(https?:\/\/[^\s<>"']+[^\s<>"'.,!?;:])/g, '<a href="$1" target="_blank">$1</a>');
        
        // SEGUNDO: Convertir saltos de línea a <br>
        text = text.replace(/\n/g, '<br>');
        
        // TERCERO: Procesar listas (lo que ya tenías)
        text = text.replace(/- (.*?)(<br>|$)/g, '<li>$1</li>');
        text = text.replace(/(<li>.*?<\/li>)+/g, '<ul>$&</ul>');
        
        // CUARTO: Procesar markdown de texto
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
        
        // QUINTO: Limpiar <br> dentro de listas
        text = text.replace(/<li>(.*?)<br><\/li>/g, '<li>$1</li>');
        
        return text;
    }

    function addMessage(sender, message) {
        const welcomeContainer = document.querySelector('.welcome-container');
        if (welcomeContainer) {
            welcomeContainer.remove();
        }

        const messageElement = document.createElement('div');
        messageElement.className = `message ${sender}`;
        
        if (sender === 'bot') {
            message = processMarkdown(message);
        }
        
        messageElement.innerHTML = message;
        messagesContainer.appendChild(messageElement);
        scrollToBottom();
    }

    function showTypingIndicator() {
        if (!isTyping) {
            isTyping = true;
            const typingElement = document.createElement('div');
            typingElement.className = 'typing-indicator';
            typingElement.id = 'typingIndicator';
            typingElement.innerHTML = '<span></span><span></span><span></span>';
            messagesContainer.appendChild(typingElement);
            scrollToBottom();
        }
    }

    function hideTypingIndicator() {
        const typingElement = document.getElementById('typingIndicator');
        if (typingElement) {
            typingElement.remove();
            isTyping = false;
        }
    }

    function showConnectionStatus(message, isError = true) {
        let statusElement = document.getElementById('connectionStatus');
        
        if (!statusElement) {
            statusElement = document.createElement('div');
            statusElement.className = 'connection-status';
            statusElement.id = 'connectionStatus';
            document.querySelector('.chat-input').before(statusElement);
        }
        
        statusElement.textContent = message;
        statusElement.style.backgroundColor = isError ? '#ffeeee' : '#eeffee';
        statusElement.style.color = isError ? '#cc0000' : '#00cc00';
    }

    function hideConnectionStatus() {
        const statusElement = document.getElementById('connectionStatus');
        if (statusElement) {
            statusElement.remove();
        }
    }

    function scrollToBottom() {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    // ===== FUNCIÓN DE ENVÍO DE MENSAJES =====
    
    function sendMessage() {
        const message = messageInput.value.trim();
        
        if (!message || !isConnected || waitingForResponse) {
            return;
        }
        
        waitingForResponse = true;
        messageInput.classList.add('input-waiting');
        messageInput.placeholder = 'Escribiendo...';
        messageInput.disabled = true;
        sendButton.disabled = true;
        
        socket.send(JSON.stringify({ message: message }));
        addMessage('user', message);
        messageInput.value = '';
    }

    // ===== CONEXIÓN WEBSOCKET =====
    
    function connectWebSocket() {
        const clientId = getClientId();
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        
        chatToken = getTokenFromUrl();
        if (!chatToken) {
            showConnectionStatus('No se proporcionó un token de acceso válido');
            return;
        }
        
        const wsUrl = `${protocol}//${window.location.host}/ws/${clientId}?token=${encodeURIComponent(chatToken)}`;
        
        showConnectionStatus('Conectando...', false);
        
        socket = new WebSocket(wsUrl);
        
        socket.onopen = function() {
            console.log('Conexión WebSocket establecida');
            isConnected = true;
            hideConnectionStatus();
            messageInput.disabled = false;
            sendButton.disabled = false;
            messageInput.focus();
        };
        
        socket.onmessage = function(event) {
            try {
                const data = JSON.parse(event.data);
                
                hideConnectionStatus();

                if (data.type === 'typing') {
                    showTypingIndicator();
                } else if (data.type === 'message') {
                    hideTypingIndicator();
                    addMessage('bot', data.message);
                    enableControls();
                    messageInput.focus();
                } else if (data.type === 'enable_input') {
                    enableControls();
                }
            } catch (error) {
                console.error('Error al procesar mensaje:', error);
                hideTypingIndicator();
                hideConnectionStatus();
                enableControls();
            }
        };
        
        socket.onclose = function(event) {
            console.log('Conexión WebSocket cerrada', event.code, event.reason);
            isConnected = false;
            
            if (event.code === 1008 && event.reason.includes('Token')) {
                showConnectionStatus('Error de autenticación: ' + event.reason + '. Intenta recargar la página.');
            } else {
                showConnectionStatus('Desconectado. Intenta recargar la página.');
            }
            
            messageInput.disabled = true;
            sendButton.disabled = true;
        };
        
        socket.onerror = function(error) {
            console.error('Error en WebSocket:', error);
            showConnectionStatus('Error de conexión. Intenta recargar la página.');
        };
    }

    // ===== INICIALIZACIÓN DE EVENTOS =====
    
    function initializeEvents() {
        // Eventos de envío de mensajes
        sendButton.addEventListener('click', sendMessage);
        
        messageInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter' && !waitingForResponse) {
                event.preventDefault();
                sendMessage();
            }
        });
        
        // Eventos de audio según tipo de dispositivo
        if (isTouchDevice) {
            micButton.addEventListener('touchstart', handleRecordStart, { passive: false });
            micButton.addEventListener('touchend', handleRecordStop, { passive: false });
            micButton.addEventListener('touchcancel', handleRecordStop, { passive: false });
        } else {
            micButton.addEventListener('mousedown', handleRecordStart);
            micButton.addEventListener('mouseup', handleRecordStop);
            micButton.addEventListener('mouseleave', handleRecordStop);
        }

        // Prevenir eventos duplicados
        micButton.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
        });

        // Eventos de limpieza
        window.addEventListener('beforeunload', function() {
            resetRecordingState();
        });
        
        window.addEventListener('blur', function() {
            if (isRecording) {
                console.log('Ventana perdió foco, deteniendo grabación');
                stopRecording();
            }
        });
    }

    // ===== INICIALIZACIÓN =====
    
    // Inicializar eventos
    initializeEvents();
    
    // Conectar al WebSocket
    connectWebSocket();
});