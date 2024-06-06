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


def save_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File saved successfully at {file_path}")


class DRMN_SearchAndReplace:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TextFilePathList": ("STRING", {"forceInput": True}),
                "SearchFor": ("STRING", {"multiline": True, "default": "concept"}),
                "ReplaceWith": ("STRING", {"multiline": True, "default": "concept"})
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "SaR"
    OUTPUT_NODE = True
    CATEGORY = "🔶DRMN🔶"

    def SaR(self, TextFilePathList, SearchFor, ReplaceWith):

        try:

            directory_path = os.path.dirname(TextFilePathList[0])
            backup_path = os.path.join(directory_path, "sr_backup")
            os.makedirs(backup_path, exist_ok=True)

            for file_path in TextFilePathList:

                base_name = os.path.basename(file_path)
                save_path = os.path.join(backup_path, base_name)

                content = read_text_file(file_path)
                save_file(save_path, content)

                content = content.replace(SearchFor[0], ReplaceWith[0])
                save_file(file_path, content)

            return ()

        except Exception as e:
            print(f"Error saving: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "DRMN_SearchAndReplace": DRMN_SearchAndReplace,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DRMN_SearchAndReplace": "DRMN_SearchAndReplace",
}
