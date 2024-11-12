import base64
import io
from PIL import Image
import numpy as np
import anthropic
import os

api_key = os.environ.get("ANTHROPIC_API_KEY")


class DataSet_ClaudeAIChatImage:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        api_models = ["claude-3-5-sonnet-latest",
                      "claude-3-5-haiku-latest", "claude-3-opus-latest"]

        return {
            "required": {
                "image": ("IMAGE",),
                "model": (api_models, {"default": api_models[0]}),
                # "system_prompt": ("STRING", {"multiline": True, "default": ""}),
                "user_prompt": ("STRING", {"multiline": True, "default": ""}),
                "max_tokens": ("INT", {"default": 1024})
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

    def generate(self, image, model, user_prompt, max_tokens):
        try:

            base64img = self.to_base64(image)
            api_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

            chat_completion = api_client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": base64img,
                                },
                            },
                            {"type": "text", "text": user_prompt}
                        ],
                    }
                ],
            )

            msg = ""
            
            for message in chat_completion.content:
                if message.type == 'text':
                    msg = message.text

            return (msg,)


        except Exception as e:
            return (f"Error: {str(e)}",)


N_CLASS_MAPPINGS = {
    "DataSet_ClaudeAIChatImage": DataSet_ClaudeAIChatImage,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_ClaudeAIChatImage": "DataSet_ClaudeAIChatImage",
}
