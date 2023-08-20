import openai

from core.config import settings


class ChatGPT:
    def __init__(self):
        self.token = settings.OPENAI_TOKEN

    def get_answer(self, text: str):
        openai.api_key = self.token
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
            temperature=1,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return result


chat_gpt = ChatGPT()
