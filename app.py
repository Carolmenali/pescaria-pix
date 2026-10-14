import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

st.set_page_config(page_title="Pescaria do Pix", page_icon="🎣")
st.title("🎣 Pescaria do Pix!")
st.write("Toque nos peixes antes que eles fujam da tela!")

# Configuração do WhatsApp
seu_numero = "5515999999999" 
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
        touch-action: manipulation; /* Evita o zoom na tela ao dar toques rápidos no celular */
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

    function createFish() {{
        if (!gameActive) return;

        const fish = document.createElement('div');
        const emojis = ['🐟', '🐠', '🐡'];
        fish.innerText = emojis[Math.floor(Math.random() * emojis.length)];
        fish.className = 'fish';
        
        // Sorteia a altura em que o peixe vai aparecer
        const startY = Math.random() * 280 + 40;
        fish.style.top = startY + 'px';
        
        // Define se vem da esquerda ou da direita
        const fromLeft = Math.random() > 0.5;
        fish.style.left = fromLeft ? '-70px' : '100%';
        if (!fromLeft) fish.style.transform = 'scaleX(-1)'; // Vira o peixe de lado
        
        board.appendChild(fish);

        // Define a velocidade (entre 2 e 4 segundos para cruzar a tela)
        const duration = Math.random() * 2000 + 2000; 
        fish.style.transitionDuration = duration + 'ms';

        // Inicia o movimento
        setTimeout(() => {{
            fish.style.left = fromLeft ? '100%' : '-70px';
        }}, 50);

        // O que acontece quando ele toca no peixe
        fish.onpointerdown = function() {{
            if (!gameActive) return;
            score++;
            scoreSpan.innerText = score;
            fish.remove(); // O peixe some
            
            if (score >= maxScore) {{
                gameActive = false;
                winScreen.style.display = 'flex'; // Mostra a tela de vitória
            }}
        }};

        // Limpa o peixe da memória se ele fugir e sair da tela
        setTimeout(() => {{
            if (fish.parentNode) fish.remove();
        }}, duration + 100);

        // Agenda o nascimento do próximo peixe
        const nextSpawn = Math.random() * 700 + 300;
        setTimeout(createFish, nextSpawn);
    }}

    // Inicia o jogo soltando os primeiros peixes
    setTimeout(createFish, 500);
    setTimeout(createFish, 1200);
    setTimeout(createFish, 1800);

</script>
</body>
</html>
"""

# Renderiza o minigame dentro da página do Streamlit
components.html(html_game, height=450)