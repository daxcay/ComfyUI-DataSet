import os
import anthropic

class DataSet_ClaudeAIChat:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        api_models = [ "claude-3-5-sonnet-latest", "claude-3-5-haiku-latest", "claude-3-opus-latest" ]

        return {
            "required": {
                "model": (api_models, {"default": api_models[0]}),
                # "system_prompt": ("STRING", {"multiline": True, "default": ""}),
                "user_prompt": ("STRING", {"multiline": True, "default": ""}),
                "max_tokens": ("INT", {"default": 1024})
            }
        }

    FUNCTION = "generate"
    RETURN_TYPES = ("STRING",)

    def generate(self, model, user_prompt, max_tokens):
        try:

            api_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

            chat_completion = api_client.messages.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
                max_tokens=max_tokens,
            )

            msg = ""
            
            for message in chat_completion.content:
                if message.type == 'text':
                    msg = message.text

            return (msg,)

        except Exception as e:
            return (f"Error: {str(e)}",)
    
N_CLASS_MAPPINGS = {
    "DataSet_ClaudeAIChat": DataSet_ClaudeAIChat,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_ClaudeAIChat": "DataSet_ClaudeAIChat",
}
