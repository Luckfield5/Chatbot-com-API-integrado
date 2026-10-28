from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="Você é um assistente prestativo que responde em português."
    ),
)

print("Chatbot iniciado! Digite 'sair' para encerrar.")
print("Olá como posso ajudar?")

while True:
    pergunta = input("Digite seu assunto: ")

    if pergunta.lower() == "sair":
        print("Até mais!")
        break

    try:
        resposta = chat.send_message(pergunta)
    except Exception as erro:
        print("Erro ao falar com a API:", erro)
        continue

    print("Bot:", resposta.text)