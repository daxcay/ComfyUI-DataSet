from groq import Groq
import requests
import os
import base64
import io
from PIL import Image
import numpy as np


def getGroqModels(key):
    try:
        url = "https://api.groq.com/openai/v1/models"
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response = response.json()
        return [item['id'] for item in response['data'] if 'id' in item]
    except (requests.exceptions.RequestException, KeyError, ValueError):
        return ['Key Invalid']

api_key = os.environ.get("GROQ_API_KEY")
api_models = getGroqModels(api_key)


class DataSet_GroqChatImage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "model": (api_models, {"default": api_models[0]}),
                "user_prompt": ("STRING", {"multiline": True, "default": ""}),
                "max_tokens": ("INT", {"default": 1024})
            }
        }

    FUNCTION = "generate"
    RETURN_TYPES = ("STRING",)

    def to_base64(self, image):
        image = image[0]
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    def generate(self, image, model, user_prompt, max_tokens):
        try:

            base64img = self.to_base64(image)

            api_client = Groq(
                api_key=api_key,
            )

            chat_completion = api_client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": user_prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64img}",
                                },
                            },
                        ],
                    }
                ],
                model=model,
                temperature=0.5,
                max_tokens=max_tokens,
                top_p=1,
                stop=None,
                stream=False,
            )

            return (chat_completion.choices[0].message.content,)

        except Exception as e:
            return (f"Error: {str(e)}",)


N_CLASS_MAPPINGS = {
    "DataSet_GroqChatImage": DataSet_GroqChatImage,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_GroqChatImage": "DataSet_GroqChatImage",
}
