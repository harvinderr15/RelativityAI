import openai
import requests

class NLP:
    def __init__(self, openai_api_key, hf_tts_api_key, hf_translate_api_key):
        openai.api_key = openai_api_key
        self.hf_tts_api_key = hf_tts_api_key
        self.hf_translate_api_key = hf_translate_api_key

    def generate_response(self, context, user_input):
        prompt = f"Context: {context}\n\nQuestion: {user_input}\nAnswer:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You:" + user_input}]
        )
        return response.choices[0].message['content'].strip()
