# 🎮 Instalando PGZero com Python 3.11.9

Este projeto utiliza **PGZero**, uma biblioteca baseada em Pygame para criação de jogos em Python.  
Siga os passos abaixo para instalar corretamente usando **Python 3.11.9**.

## 🐍 1. Instalar o Python 3.11.9

Acesse o site oficial do Python:  
👉 **https://www.python.org/downloads/release/python-3119/**

Baixe a versão compatível com seu sistema operacional.

### Durante a instalação (Windows):
- ✅ Marque a opção **"Add Python to PATH"**
- Clique em **"Install Now"**

### Verifique a instalação no terminal ou prompt de comando:
```bash
python --version
```
**Saída esperada:**
```
Python 3.11.9
```

## 📦 2. Atualizar o pip (recomendado)

Antes de instalar o PGZero, atualize o gerenciador de pacotes:
```bash
python -m pip install --upgrade pip
```

## 🎮 3. Instalar o PGZero

Execute o comando abaixo:
```bash
pip install pgzero
```
Isso instalará automaticamente o PGZero e suas dependências, incluindo o Pygame compatível com o Python 3.11.

## ✅ 4. Verificar se o PGZero foi instalado corretamente

No terminal, execute:
```bash
pgzrun --version
```
Se não houver erros, a instalação foi concluída com sucesso 🎉

## ▶️ 5. Executar um jogo com PGZero

Crie um arquivo chamado `main.py` (ou qualquer nome) e execute:
```bash
pgzrun main.py
```

⚠️ **Importante:**  
Não execute jogos PGZero com `python main.py`, sempre use `pgzrun`.

---

## 🛠️ Possíveis problemas

### **Comando `pgzrun` não reconhecido**
- Reinicie o terminal
- Verifique se o Python está no PATH

### **Erro de dependências no Windows**
- Certifique-se de estar usando **Python 64 bits**
- Reinstale o PGZero com:
```bash
pip install --force-reinstall pgzero
```

### **Erro ao instalar em Linux/MacOS**
Use `python3` e `pip3` em vez de `python` e `pip`:
```bash
python3 --version
python3 -m pip install pgzero
pgzrun main.py
```
