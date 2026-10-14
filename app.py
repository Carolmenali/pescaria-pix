import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

st.set_page_config(page_title="Pescaria do Pix", page_icon="🎣")
st.title("🎣 Pescaria do Pix!")
st.write("Toque nos peixes antes que eles fujam da tela!")

# Configuração do WhatsApp
seu_numero = "5515" 
mensagem = "Oi tia! Terminei a pescaria, peguei os 30 peixes! 🎣 Já pode mandar meu Pix de Dia das Crianças! 😎"
mensagem_codificada = urllib.parse.quote(mensagem)
link_whatsapp = f"https://wa.me/{seu_numero}?text={mensagem_codificada}"

# Código do Jogo Interativo (HTML + JavaScript)
html_game = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
    #game-board {{
        width: 100%;
        height: 400px;
        background: linear-gradient(180deg, #87CEEB 0%, #1E90FF 100%);
        position: relative;
        overflow: hidden;
        border-radius: 15px;
        border: 3px solid #005f99;
        touch-action: manipulation;
    }}
    .fish {{
        position: absolute;
        font-size: 50px;
        cursor: pointer;
        user-select: none;
        transition: left linear;
    }}
    #score-board {{
        position: absolute;
        top: 10px;
        left: 10px;
        background: rgba(255, 255, 255, 0.9);
        padding: 5px 15px;
        border-radius: 10px;
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: 18px;
        z-index: 10;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
    }}
    #win-screen {{
        display: none;
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(255, 255, 255, 0.95);
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 20;
        font-family: Arial, sans-serif;
        text-align: center;
    }}
    .btn-whatsapp {{
        background-color: #25D366;
        color: white;
        padding: 15px 25px;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
        z-index: 30;
    }}
    .balloon {{
        position: absolute;
        font-size: 40px;
        bottom: -50px;
        animation: floatUp 3s ease-in forwards;
        z-index: 25;
    }}
    @keyframes floatUp {{
        0% {{ transform: translateY(0) rotate(-5deg); opacity: 1; }}
        50% {{ transform: translateY(-250px) rotate(5deg); }}
        100% {{ transform: translateY(-500px) rotate(-5deg); opacity: 0; }}
    }}
</style>
</head>
<body>

<div id="game-board">
    <div id="score-board">Peixes: <span id="score">0</span> / 30</div>
    
    <div id="win-screen">
        <h2 style="color: #333; margin-bottom: 0;">🎉 Boa pescaria!</h2>
        <p style="font-size: 60px; margin: 10px 0;">🎣🏆</p>
        <a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">📲 Resgatar Pix no WhatsApp</a>
    </div>
</div>

<script>
    const board = document.getElementById('game-board');
    const scoreSpan = document.getElementById('score');
    const winScreen = document.getElementById('win-screen');
    
    let score = 0;
    const maxScore = 30;
    let gameActive = true;

    // Função que cria a chuva de balões na tela de vitória
    function shootBalloons() {{
        for(let i=0; i<20; i++) {{
            let balloon = document.createElement('div');
            balloon.className = 'balloon';
            balloon.innerText = '🎈';
            balloon.style.left = Math.random() * 90 + '%';
            // Varia a velocidade e o momento que cada balão sobe
            balloon.style.animationDuration = (Math.random() * 2 + 2) + 's';
            balloon.style.animationDelay = (Math.random() * 0.5) + 's';
            winScreen.appendChild(balloon);
        }}
    }}

    function createFish() {{
        if (!gameActive) return;

        const fish = document.createElement('div');
        const emojis = ['🐟', '🐠', '🐡'];
        fish.innerText = emojis[Math.floor(Math.random() * emojis.length)];
        fish.className = 'fish';
        
        const startY = Math.random() * 280 + 40;
        fish.style.top = startY + 'px';
        
        const fromLeft = Math.random() > 0.5;
        fish.style.left = fromLeft ? '-70px' : '100%';
        if (!fromLeft) fish.style.transform = 'scaleX(-1)'; 
        
        board.appendChild(fish);

        const duration = Math.random() * 2000 + 2000; 
        fish.style.transitionDuration = duration + 'ms';

        setTimeout(() => {{
            fish.style.left = fromLeft ? '100%' : '-70px';
        }}, 50);

        fish.onpointerdown = function() {{
            if (!gameActive) return;
            score++;
            scoreSpan.innerText = score;
            fish.remove(); 
            
            if (score >= maxScore) {{
                gameActive = false;
                winScreen.style.display = 'flex'; 
                shootBalloons(); // Chama os balões quando ele ganha!
            }}
        }};

        setTimeout(() => {{
            if (fish.parentNode) fish.remove();
        }}, duration + 100);

        const nextSpawn = Math.random() * 700 + 300;
        setTimeout(createFish, nextSpawn);
    }}

    setTimeout(createFish, 500);
    setTimeout(createFish, 1200);
    setTimeout(createFish, 1800);

</script>
</body>
</html>
"""

# Renderiza o minigame dentro da página do Streamlit
components.html(html_game, height=450)