
import base64
import requests

# OpenAI Config
api_key = "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"


def upload_image_and_ask(image_path):

    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    

    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview", 
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Give me a human like one sentence answer for the question. Question: What am I holding"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }   
        ],
        "max_tokens": 50,
        "temperature": 0.3
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    response_data = response.json()
    print(response_data)
    if 'choices' in response_data and len(response_data['choices']) > 0:
        answer = response_data['choices'][0]['message']['content']
        return answer
    else:
        return "No response"