import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_world_description():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Опис світу dark fantasy після виверження вулкану або ядерної війни...",
        max_tokens=200
    )
    return response.choices[0].text.strip()
