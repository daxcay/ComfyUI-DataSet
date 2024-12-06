import base64
import io
from PIL import Image
import numpy as np
from openai import OpenAI
import os

class DataSet_OpenAIChatImageBatch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "image_detail": (["low","high"], {"default": "high"}),
                "prompt": ("STRING", {"multiline": True, "default": ""}),
                "model": (["gpt-4o","gpt-4", "gpt-4-32k", "gpt-3.5-turbo", "gpt-4-0125-preview", "gpt-4-turbo-preview", "gpt-4-1106-preview", "gpt-4-0613"], {"default": "gpt-4o"}),
                "api_url": ("STRING", {"multiline": False, "default": "https://api.openai.com/v1"}),
                "token_length": ("INT", {"default": 1024})
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "generate"
    CATEGORY = "🔶DATASET🔶"

    def to_base64(self, image):
        image = image[0]
        i = 255. * image.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    def generate(self, images, image_detail, prompt, model, api_url, token_length):

        try:

            image_detail = image_detail[0]
            model = model[0]
            api_url = api_url[0]
            prompt = prompt[0]
            token_length = token_length[0]

            answers = []

            api_key = os.environ.get("OPENAI_API_KEY")
            ai = OpenAI(api_key=api_key, base_url=api_url)

            for image in images:
                base64img = self.to_base64(image)
                if not api_key:
                    return "OpenAI API key is required."
                request = [{"role": "system","content": "You are GPT-4."}]
                request.append({"role": "user","content": [{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64img}", "detail": image_detail}}]})
                request.append({"role": "user","content": prompt})
                response = ai.chat.completions.create(model=model,messages=request,max_tokens=token_length)
                answer = response.choices[0].message.content
                answers.append(answer)

            return (answers,)

        except Exception as e:
            return (f"Error: {str(e)}",)

N_CLASS_MAPPINGS = {
    "DataSet_OpenAIChatImageBatch": DataSet_OpenAIChatImageBatch,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_OpenAIChatImageBatch": "DataSet_OpenAIChatImageBatch",
}
