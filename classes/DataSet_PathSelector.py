import os

def normalize_extensions(extensions):
    return [ext if ext.startswith('.') else '.' + ext for ext in extensions]

def search_and_select_files(search_in_directory, search_for_extensions, select_from_directory, select_extensions):
    # Normalize extensions
    search_for_extensions = normalize_extensions(search_for_extensions.split(','))
    select_extensions = normalize_extensions(select_extensions.split(','))

    # Search for files with the specified extensions in the search_in_directory
    search_results = [
        file for file in os.listdir(search_in_directory) 
        if any(file.endswith(ext) for ext in search_for_extensions)
    ]
    search_results_names = {os.path.splitext(file)[0] for file in search_results}

    # List all files with the specified extensions in the select_from_directory
    selection_files = [
        file for file in os.listdir(select_from_directory) 
        if any(file.endswith(ext) for ext in select_extensions)
    ]
    selection_files_dict = {os.path.splitext(file)[0]: file for file in selection_files}

    # Find the matching files based on the names
    matching_files = [selection_files_dict[name] for name in search_results_names if name in selection_files_dict]

    # Prepare the return values
    matching_files_full_paths = [os.path.join(select_from_directory, file) for file in matching_files]
    matching_files_with_extensions = matching_files
    matching_files_without_extensions = [os.path.splitext(file)[0] for file in matching_files]

    return (matching_files_with_extensions, matching_files_without_extensions, matching_files_full_paths)

class DataSet_PathSelector:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "search_in_directory": ("STRING", {"multiline": False, "default": ""}),
                "search_for_extensions": ("STRING", {"multiline": False, "default": ""}),
                "select_from_directory": ("STRING", {"multiline": False, "default": ""}),                
                "select_extensions": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING",)
    RETURN_NAMES = ("SelectedNamesWithExtension", "SelectedNamesWithoutExtension", "SelectedPaths")
    OUTPUT_IS_LIST = (True, True, True)
    OUTPUT_NODE = True
    FUNCTION = "make_list"
    CATEGORY = "🔶DATASET🔶"

    def make_list(self, search_in_directory, search_for_extensions, select_from_directory, select_extensions):
        try:
            if not os.path.exists(search_in_directory):
                print(f"The folder '{search_in_directory}' does not exist.")
                return ([], [], [])

            if not os.path.exists(select_from_directory):
                print(f"The folder '{select_from_directory}' does not exist.")
                return ([], [], [])

            a, b, c = search_and_select_files(search_in_directory, search_for_extensions, select_from_directory, select_extensions)
            return (a, b, c)

        except Exception as e:
            print(f"An error occurred: {e}")
            return ([], [], [])

N_CLASS_MAPPINGS = {
    "DataSet_PathSelector": DataSet_PathSelector,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_PathSelector": "DataSet_PathSelector",
}
