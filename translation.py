import requests

def translate_text(payload, hf_translate_api_key):
    API_URL_TRANSLATE = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-hi"
    headers_translate = {"Authorization": f"Bearer {hf_translate_api_key}"}
    response = requests.post(API_URL_TRANSLATE, headers=headers_translate, json=payload)
    
    # Check if the response contains JSON content
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}", "content": response.text}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}", "content": response.text}
    except ValueError:
        return {"error": "Failed to decode JSON response", "content": response.text}
