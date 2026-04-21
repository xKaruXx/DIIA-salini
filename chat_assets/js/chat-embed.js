// chat_assets/js/chat-embed.js
// Widget embed para el chat de CORADIR (sin reCAPTCHA)

(function() {
    // ===== CONFIGURACIÓN =====
    let CHAT_SERVER_URL;
    let chatToken = null;
    let chatOpened = false;
    let bubbleShown = false;
    let userInteracted = false;

    // URLs del servidor (ajustar según entorno)
    CHAT_SERVER_URL = "https://botmov.coradir.ai"
    //CHAT_SERVER_URL = "http://localhost:8850"
    
    // ===== FUNCIONES DE AUDIO =====
    
    function playPopSound() {
        if (!userInteracted) return;
        
        try {
            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            
            oscillator.type = 'sine';
            oscillator.frequency.setValueAtTime(600, audioCtx.currentTime);
            
            gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
            gainNode.gain.linearRampToValueAtTime(0.3, audioCtx.currentTime + 0.02);
            gainNode.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 0.2);
            
            oscillator.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            
            oscillator.start();
            oscillator.stop(audioCtx.currentTime + 0.2);
        } catch (e) {
            console.log('Error al reproducir sonido:', e);
        }
    }

    // ===== DETECCIÓN DE INTERACCIÓN DEL USUARIO =====
    
    document.addEventListener('click', () => userInteracted = true);
    document.addEventListener('touchstart', () => userInteracted = true);
    document.addEventListener('scroll', () => userInteracted = true);
    document.addEventListener('keydown', () => userInteracted = true);
    document.addEventListener('mousemove', () => userInteracted = true);
    
    // ===== FUNCIONES DE TOKEN (SIMPLIFICADAS) =====
    
    async function getToken() {
        try {
            const url = `${CHAT_SERVER_URL}/generate-token`;
            
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Referer': window.location.href  
                },
                credentials: 'include'
            });
            
            if (!response.ok) {
                console.error('Error al obtener token:', response.statusText);
                return null;
            }
            
            const data = await response.json();
            chatToken = data.token;
            
            const expiresAt = Date.now() + (data.expires_in * 1000);
            localStorage.setItem('coradir_chat_token_energia_deploy', chatToken);
            localStorage.setItem('coradir_chat_token_energia_expires_deploy', expiresAt.toString());
            
            return chatToken;
        } catch (error) {
            console.error('Error al solicitar token:', error);
            return null;
        }
    }
    
    async function ensureValidToken() {
        const storedToken = localStorage.getItem('coradir_chat_token_energia_deploy');
        const expiresAtStr = localStorage.getItem('coradir_chat_token_energia_expires_deploy');
        
        if (storedToken && expiresAtStr) {
            const expiresAt = parseInt(expiresAtStr);
            
            if (Date.now() < expiresAt - (5 * 60 * 1000)) {
                chatToken = storedToken;
                return chatToken;
            }
        }
        
        return await getToken();
    }
    
    // ===== FUNCIONES DE BURBUJA DE MENSAJE =====
    
    function showChatBubble() {
        if (chatOpened || bubbleShown) return;
        
        bubbleShown = true;
        playPopSound();
        
        const bubble = document.createElement('div');
        bubble.id = 'coradir-chat-bubble';
        bubble.innerHTML = `
            <div class="bubble-content">
                <span class="bubble-avatar">C</span>
                <div class="bubble-message">¡Hola! Soy Cora.<br>¿En qué puedo ayudarte hoy?</div>
            </div>
            <button class="bubble-close" aria-label="Cerrar mensaje">×</button>
        `;
        document.getElementById('coradir-chat-widget').appendChild(bubble);
        
        setTimeout(() => {
            bubble.classList.add('bubble-visible');
        }, 100);
        
        bubble.addEventListener('click', (e) => {
            if (e.target.classList.contains('bubble-close')) {
                hideChatBubble();
            } else {
                const chatButton = document.getElementById('coradir-chat-button');
                if (chatButton) {
                    chatButton.click();
                }
                hideChatBubble();
            }
        });
        
        setTimeout(hideChatBubble, 15000);
    }
    
    function hideChatBubble() {
        const bubble = document.getElementById('coradir-chat-bubble');
        if (bubble) {
            bubble.classList.remove('bubble-visible');
            setTimeout(() => {
                bubble.remove();
            }, 300);
        }
    }
    
    // ===== FUNCIÓN PRINCIPAL PARA CREAR EL WIDGET =====
    
    async function createChatWidget() {
        if (document.getElementById('coradir-chat-widget')) {
            return;
        }

        const token = await ensureValidToken();
        if (!token) {
            console.error('No se pudo obtener un token válido para el chat');
            return;
        }

        // Cargar CSS del embed
        await loadEmbedCSS();

        // Intentar cargar Font Awesome si no está cargado
        if (!document.querySelector('link[href*="font-awesome"]')) {
            const fontAwesome = document.createElement('link');
            fontAwesome.rel = 'stylesheet';
            fontAwesome.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css';
            document.head.appendChild(fontAwesome);
        }

        // Crear contenedor principal
        const widgetContainer = document.createElement('div');
        widgetContainer.id = 'coradir-chat-widget';
        
        // Crear botón flotante
        const chatButton = document.createElement('button');
        chatButton.id = 'coradir-chat-button';
        chatButton.innerHTML = '<i class="fas fa-comments"></i>';
        chatButton.setAttribute('aria-label', 'Abrir chat');
        chatButton.title = 'Asistente Virtual CORADIR';
        
        // Crear contenedor del iframe
        const iframeContainer = document.createElement('div');
        iframeContainer.id = 'coradir-chat-iframe-container';
        
        // Añadir elementos al DOM
        widgetContainer.appendChild(chatButton);
        document.body.appendChild(widgetContainer);
        document.body.appendChild(iframeContainer);
        
        // Evento del botón
        chatButton.addEventListener('click', async function() {
            this.classList.remove('pulse');
            chatOpened = true;

            const token = await ensureValidToken();
            if (!token) {
                console.error('No se pudo obtener un token válido para el chat');
                return;
            }
            
            if (!document.getElementById('coradir-chat-iframe')) {
                const iframe = document.createElement('iframe');
                iframe.id = 'coradir-chat-iframe';
                iframe.src = `${CHAT_SERVER_URL}/chat?token=${encodeURIComponent(token)}`;
                iframe.title = 'Chat de CORADIR';
                iframe.setAttribute('loading', 'lazy');
                iframe.setAttribute('allow', 'microphone');
                iframeContainer.appendChild(iframe);
            }
            
            iframeContainer.classList.toggle('coradir-chat-visible');
            chatOpened = iframeContainer.classList.contains('coradir-chat-visible');
            
            if (chatOpened) {
                hideChatBubble();
            }
        });
        
        setTimeout(showChatBubble, 5000);
    }

    // ===== FUNCIÓN PARA CARGAR CSS DEL EMBED =====
    
    async function loadEmbedCSS() {
        // Verificar si ya está cargado
        if (document.querySelector('link[href*="chat-embed.css"]')) {
            return;
        }
        
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = `${CHAT_SERVER_URL}/chat_assets/css/chat-embed.css`;
        
        return new Promise((resolve, reject) => {
            link.onload = () => {
                console.log('CSS del embed cargado correctamente');
                resolve();
            };
            link.onerror = () => {
                console.warn('No se pudo cargar el CSS del embed, usando estilos inline');
                // Fallback: crear estilos mínimos inline
                createFallbackStyles();
                resolve();
            };
            document.head.appendChild(link);
        });
    }

    // ===== ESTILOS DE FALLBACK =====
    
    function createFallbackStyles() {
        const style = document.createElement('style');
        style.textContent = `
            #coradir-chat-widget{position:fixed;bottom:20px;right:20px;z-index:9999;font-family:Arial,sans-serif}
            #coradir-chat-button{width:60px;height:60px;border-radius:50%;background:#2E8B57;color:white;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:0 4px 8px rgba(0,0,0,0.2);transition:all 0.3s ease}
            #coradir-chat-button:hover{transform:scale(1.05);background:#237446}
            #coradir-chat-iframe-container{position:fixed;bottom:90px;right:20px;width:350px;height:520px;z-index:9999;display:none;box-shadow:0 4px 12px rgba(0,0,0,0.15);border-radius:10px;overflow:hidden}
            #coradir-chat-iframe{width:100%;height:100%;border:none}
            .coradir-chat-visible{display:block!important}
        `;
        document.head.appendChild(style);
    }

    // ===== ANIMACIÓN DEL BOTÓN =====
    
    function startButtonPulse() {
        setTimeout(function() {
            const chatButton = document.getElementById('coradir-chat-button');
            if (chatButton && !chatOpened) {
                chatButton.classList.add('pulse');
                
                setTimeout(function() {
                    if (chatButton) {
                        chatButton.classList.remove('pulse');
                    }
                }, 12000);
            }
            
            setInterval(function() {
                const btn = document.getElementById('coradir-chat-button');
                if (btn && !chatOpened) {
                    btn.classList.add('pulse');
                    
                    setTimeout(function() {
                        if (btn) {
                            btn.classList.remove('pulse');
                        }
                    }, 12000);
                }
            }, 30000);
        }, 15000);
    }

    // ===== INICIALIZACIÓN =====
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            createChatWidget();
            startButtonPulse();
        });
    } else {
        createChatWidget();
        startButtonPulse();
    }
})();