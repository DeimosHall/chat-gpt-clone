import os
import openai
import sys

openai.api_key = sys.argv[1]

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."

def chat_response(prompt: str):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=350,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text

print("Type exit to finish chatting\n")

while True:
    question = input("You: ")
    prompt += f"\n\nHuman: {question} \nAI:"

    if(question == "exit"):
        exit()

    print(f"AI: {chat_response(prompt)}")