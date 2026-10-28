# Chatbot no terminal com Gemini

##Instale as dependências:

pip install -r requirements.txt

Ou use os comandos no terminal:
py -m pip install anthropic python-dotenv
python -m pip install google-genai python-dotenv

Chatbot em Python que usa a API do Google Gemini e mantém o histórico da conversa.

## O que ele faz

- Recebe suas perguntas pelo terminal
- Envia para o modelo Gemini e mostra a resposta
- Lembra do que foi dito antes na mesma conversa
- Digite `sair` para encerrar

## Como rodar

1. Clone o repositório e entre na pasta
2. Crie e ative o ambiente virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` na raiz com a sua chave (gerada em aistudio.google.com/apikey):
   ```
   GEMINI_API_KEY=sua-chave-aqui
   ```
5. Rode:
   ```
   python chatbot.py
   ```

## Tecnologias

- Python
- google-genai
- python-dotenv

## O que aprendi

Neste projeto aprendi a consumir a API do Gemini em Python, entender
que o modelo precisa receber o histórico da conversa para ter contexto,
e proteger a chave de API usando um arquivo .env e o .gitignore.
Também pratiquei ambiente virtual, tratamento de erros e publicação no GitHub.
