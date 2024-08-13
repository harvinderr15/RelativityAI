import requests

def query_tts(payload, hf_tts_api_key):
    API_URL_TTS = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
    headers_tts = {"Authorization": f"Bearer {hf_tts_api_key}"}
    response = requests.post(API_URL_TTS, headers=headers_tts, json=payload)
    return response.content
