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

class DataSet_TextFilesLoad:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory": ("STRING", {"default":"directory_path"}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING","STRING","STRING",)
    RETURN_NAMES = ("TextFileNames","TextFileNamesWithoutExtension","TextFilePaths","TextFileContents",)
    OUTPUT_IS_LIST = (True, True, True, True,)
    FUNCTION = "LoadIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DATASET🔶"

    def LoadIT(self, directory):
        
        try:

            directory = directory[0]

            file_paths = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]
            file_names = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]
            file_names_without_extension = [os.path.splitext(f)[0] for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]
            file_contents = []

            for file_path in file_paths:
                content = read_text_file(file_path)
                if(content):
                    file_contents.append(content)
                else:
                    print(f'Error reading file: {file_path}')

            return (file_names, file_names_without_extension, file_paths, file_contents,)        

        except Exception as e:
            return (file_names, file_names_without_extension, file_paths, file_contents,)


N_CLASS_MAPPINGS = {
    "DataSet_TextFilesLoad": DataSet_TextFilesLoad,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_TextFilesLoad": "DataSet_TextFilesLoad",
}
