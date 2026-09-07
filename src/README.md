# Passo a passo da Execução

## Setup do Ollama

```
# 1. Instalar Ollama (https://ollama.com/)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código completo

Todo código fonte está no arquivo `app.py`

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas requests

# Garantir se o Ollama está rodando
ollama serve

# Rodar a aplicação
streamlit run .\src\app.py
```
