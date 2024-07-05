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

class DataSet_TextFilesLoadFromList:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TextFilePathsList": ("STRING", {"forceInput":True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING","STRING","STRING",)
    RETURN_NAMES = ("TextFileNames","TextFileNamesWithoutExtension","TextFilePaths","TextFileContents",)
    OUTPUT_IS_LIST = (True, True, True, True,)
    FUNCTION = "LoadIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DATASET🔶"

    def LoadIT(self, TextFilePathsList):
        
        try:

            file_paths = [path for path in TextFilePathsList if path.endswith('.txt')]
            file_names = [os.path.basename(path) for path in file_paths]
            file_names_without_ext = [os.path.splitext(os.path.basename(path))[0] for path in file_paths]
            file_contents = []

            for file_path in file_paths:
                content = read_text_file(file_path)
                if(content):
                    file_contents.append(content)
                else:
                    print(f'Error reading file: {file_path}')

            return (file_names, file_names_without_ext, file_paths, file_contents,)        

        except Exception as e:
            return ([],[],[])


N_CLASS_MAPPINGS = {
    "DataSet_TextFilesLoadFromList": DataSet_TextFilesLoadFromList,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_TextFilesLoadFromList": "DataSet_TextFilesLoadFromList",
}
