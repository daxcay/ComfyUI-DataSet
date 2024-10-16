from groq import Groq
import requests
import os

def getGroqModels(key):

    url = "https://api.groq.com/openai/v1/models"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response = response.json()

    return [item['id'] for item in response['data'] if 'id' in item]


api_key = os.environ.get("GROQ_API_KEY")
api_models = getGroqModels(api_key)


class DataSet_GroqChat:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (api_models, {"default": api_models[0]}),
                "system_prompt": ("STRING", {"multiline": True, "default": ""}),
                "user_prompt": ("STRING", {"multiline": True, "default": ""}),
                "max_tokens": ("INT", {"default": 1024})
            }
        }

    FUNCTION = "generate"
    RETURN_TYPES = ("STRING",)

    def generate(self, model, system_prompt, user_prompt, max_tokens):
        try:

            api_client = Groq(
                api_key=api_key,
            )

            chat_completion = api_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
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
    "DataSet_GroqChat": DataSet_GroqChat,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_GroqChat": "DataSet_GroqChat",
}
