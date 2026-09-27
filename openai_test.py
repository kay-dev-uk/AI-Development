import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

def question_answer():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
    conversation = []

    try:
        while True:
            user_input = input("Q: ")
            if user_input.lower() in ('exit', 'quit'):
                break

            conversation.append({"role": "user", "content": user_input})
            response = client.responses.create(
                model="gpt-4o-mini",
                instructions = "You are a smart technical assistant. You will respond to questions concisely and correctly",
                input=conversation
            )
            reply = response.output_text
            print(reply)

            conversation.append({"role": "assistant", "content": reply})
    except Exception as e:
        print(f"Error: {e}")

question_answer()