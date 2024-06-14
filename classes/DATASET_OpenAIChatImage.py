import base64
import io
from PIL import Image
import numpy as np
from openai import OpenAI

class DATASET_OpenAIChatImage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "image_detail": (["low","high"], {"default": "high"}),
                "prompt": ("STRING", {"multiline": True, "default": ""}),
                "model": (["gpt-4o","gpt-4", "gpt-4-32k", "gpt-3.5-turbo", "gpt-4-0125-preview", "gpt-4-turbo-preview", "gpt-4-1106-preview", "gpt-4-0613"], {"default": "gpt-4o"}),
                "api_url": ("STRING", {"multiline": False, "default": "https://api.openai.com/v1"}),
                "api_key": ("STRING", {"multiline": False}),
                "token_length": ("INT", {"default": 1024})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "🔶DATASET🔶"

    def to_base64(self, image):
        image = image[0]
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    def generate(self, image, image_detail, model, api_url, api_key, prompt, token_length):
        try:
            ai = OpenAI(api_key=api_key, base_url=api_url)
            base64img = self.to_base64(image)
            if not api_key:
                return "OpenAI API key is required."
            request = [{"role": "system","content": "You are GPT-4"}]
            request.extend({"role": "user","content": [{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64img}", "detail": image_detail}}]})
            request.extend({"role": "user","content": prompt})
            response = ai.chat.completions.create(model=model,messages=request,max_tokens=token_length)
            answer = response.choices[0].message.content
            return (answer,)
        except Exception as e:
            return (f"Error: {str(e)}",)

N_CLASS_MAPPINGS = {
    "DATASET_OpenAIChatImage": DATASET_OpenAIChatImage,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DATASET_OpenAIChatImage": "DATASET_OpenAIChatImage",
}