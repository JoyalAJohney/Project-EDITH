import requests
import json
import base64

def upload_image_and_ask(image_path):
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    url = "http://localhost:11434/api/generate"

    base_prompt = '''
        You should never use the word 'image' in your response, 
        Always generate Human like responses,
        Assume you are talking to the person in the image and the questions are coming from the person in the image,
        Provide your responses in 10 words or less,
        Your response should never cross 10 words
    '''

    payload = {
        "model": "llava",
        "prompt": base_prompt + "Question: What am I holding?",
        "stream": False,
        "images": [image_base64],
        "temperature": 0.7
    }

    response = requests.post(url, data=json.dumps(payload))
    json_respone_dict = json.loads(response.text)

    return json_respone_dict.get("response", "No response available")