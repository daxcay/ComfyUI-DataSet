import os

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

class DATASET_TXTFileLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_paths": ("STRING", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("content",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "LoadIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DATASET🔶"

    def LoadIT(self, file_paths):

        files = []

        for file_path in file_paths:
            content = read_text_file(file_path)
            if(content):
                files.append(content)
            else:
                print(f'Error reading file: {file_path}')

        return (files,)
    
    @classmethod
    def IS_CHANGED(s, file_paths):       
       return os.urandom(16).hex()


N_CLASS_MAPPINGS = {
    "DATASET_TXTFileLoader": DATASET_TXTFileLoader,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DATASET_TXTFileLoader": "DATASET_TXTFileLoader",
}
