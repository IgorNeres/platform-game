# 🎮 Err@ 410 — Platformer Game (PGZero)

**Err@ 410** é um jogo de plataforma em visão lateral desenvolvido com **PGZero** e **Python 3.11.9**.  
O projeto foi criado como parte de um **teste para tutores**, seguindo regras rígidas de bibliotecas permitidas, organização de código e animações de sprite.

O jogador deve explorar o cenário, evitar inimigos e armadilhas, coletar a chave e abrir o baú para vencer.

---

## 🧠 Características do jogo

- 🎮 Gênero: **Platformer**
- 🧍‍♂️ Herói com animação de:
  - parado (idle)
  - andando
  - pulando
- 👾 Inimigos terrestres e voadores com animação
- 🔊 Música de fundo e efeitos sonoros (ligar/desligar)
- 🖱️ Menu principal com botões clicáveis
- 🗝️ Objetivo: pegar a chave e abrir o baú
- 💀 Armadilhas e colisões com game over

---

## 📦 Tecnologias utilizadas

- **Python 3.11.9**
- **PGZero**
- Bibliotecas permitidas:
  - `random`
  - `pygame.Rect` (apenas a classe `Rect`)

❌ Nenhuma outra biblioteca externa é utilizada.

---

## 🚀 Instalação e Execução

### 🐍 1. Instalar o Python 3.11.9

Acesse o site oficial do Python:  
👉 **https://www.python.org/downloads/release/python-3119/**

Baixe a versão compatível com seu sistema operacional.

#### Durante a instalação (Windows):
- ✅ Marque a opção **"Add Python to PATH"**
- Clique em **"Install Now"**

#### Verifique a instalação:
```bash
python --version
```
**Saída esperada:**
```
Python 3.11.9
```

### 📦 2. Atualizar o pip (recomendado)
```bash
python -m pip install --upgrade pip
```

### 🎮 3. Instalar o PGZero
```bash
pip install pgzero
```
O PGZero instalará automaticamente as dependências necessárias.

### ✅ 4. Verificar a instalação
```bash
pgzrun --version
```
Se não houver erros, a instalação foi concluída com sucesso 🎉

### ▶️ 5. Executar o jogo
Dentro da pasta do projeto, execute:
```bash
pgzrun game.py
```

⚠️ **Importante:**  
Não execute com `python game.py`.  
Sempre use `pgzrun` para jogos PGZero.

---

## 🎮 Controles

- **⬅️ ➡️ Setas esquerda/direita** — mover
- **␣ Espaço** — pular
- **🖱️ Mouse** — menu e botões
- **🔊 Botão de som** — ligar/desligar áudio

---

## 📁 Estrutura do projeto
```
Err@410/
│
├── game.py
├── images/
│   ├── hero_idle_0.png
│   ├── hero_idle_1.png
│   ├── hero_walk_0.png
│   ├── hero_walk_1.png
│   ├── enemy_walk_0.png
│   ├── enemy_walk_1.png
│   ├── enemy_flying_0.png
│   ├── enemy_flying_1.png
│   └── ...
│
└── sounds/
│   ├── menu_music.mp3
│   ├── game_music.mp3
│   ├── jump.wav
│   ├── defeat.wav
│   └── ...
│
└── music/
    ├── menu_music.mp3
    ├── game_music.mp3
```

---

## 🎵 Música e Créditos

As músicas utilizadas neste projeto são gratuitas para uso conforme descrito pelos autores nas páginas de origem.

### 🎶 Música 1
**Título:** Powerup!  
**Artista:** Jeremy Blake  
**Fonte:** Jeremy Blake - Powerup! ♫ NO COPYRIGHT 8-bit Music
**Link:** https://www.youtube.com/watch?v=l7SwiFWOQqM

### 🎶 Música 2
**Título:** MAZE
**Artista:** Density & Time
**Fonte:** Density & Time - MAZE ♫ NO COPYRIGHT 8-bit Music 
**Link:** https://www.youtube.com/watch?v=OuRvOCf9mJ4

Todos os direitos permanecem com seus respectivos criadores.  
Este projeto é educacional e não comercial.

---

## 🛠️ Possíveis problemas

### **Comando `pgzrun` não reconhecido**
- Reinicie o terminal
- Verifique se o Python está no PATH
- No Linux/MacOS, use `python3` e `pip3`

### **Erro de dependências**
```bash
# Reinstale o PGZero
pip install --force-reinstall pgzero

# Ou instale manualmente o Pygame compatível
pip install pygame==2.5.0
```

### **Arquivos de som não carregam**
- Certifique-se de que os arquivos estão na pasta `sounds/`
- Verifique se os formatos são suportados (`.ogg`)

---

## 🧪 Observações técnicas

- O projeto utiliza classes próprias para personagens e animações
- O código segue boas práticas de organização e legibilidade
- Nenhum trecho foi copiado de terceiros

---

## 🏁 Conclusão

**Err@ 410** é um projeto completo, funcional e didático, desenvolvido para demonstrar domínio de PGZero, animações de sprite, lógica de jogo e organização de código.

Divirta-se jogando! 🎮✨
