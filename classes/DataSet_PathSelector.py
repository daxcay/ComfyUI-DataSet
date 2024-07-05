import os

def search_and_select_files(search_in_directory, search_for_extension, select_from_directory, select_extension):
    # Search for files with the specified extension in the search_in_directory
    search_results = [file for file in os.listdir(search_in_directory) if file.endswith(search_for_extension)]
    search_results_names = {os.path.splitext(file)[0] for file in search_results}    
    # List all files with the specified extension in the select_from_directory
    selection_files = [file for file in os.listdir(select_from_directory) if file.endswith(select_extension)]
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
                "search_for_extension": ("STRING", {"multiline": False, "default": ""}),
                "select_from_directory": ("STRING", {"multiline": False, "default": ""}),                
                "select_extension": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT",)
    RETURN_NAMES = ("SelectedNamesWithExtension","SelectedNamesWithoutExtension", "SelectedPaths")
    OUTPUT_IS_LIST = (True, True, True)
    OUTPUT_NODE = True
    FUNCTION = "make_list"
    CATEGORY = "🔶DATASET🔶"

    def make_list(self, search_in_directory, search_for_extension, select_from_directory, select_extension):

        try:

            if not os.path.exists(search_in_directory):
               print(f"The folder '{search_in_directory}' does not exist.")
               return ([], [], 0)

            if not os.path.exists(select_from_directory):
               print(f"The folder '{select_from_directory}' does not exist.")
               return ([], [], 0)
            
            search_for_extension = search_for_extension if search_for_extension.startswith('.') else '.' + search_for_extension
            select_extension = select_extension if select_extension.startswith('.') else '.' + select_extension

            a,b,c = search_and_select_files(search_in_directory, search_for_extension, select_from_directory, select_extension)
            return (a,b,c)

        except Exception as e:
            print(f"An error occurred: {e}")
            return ([], [], [])

N_CLASS_MAPPINGS = {
    "DataSet_PathSelector": DataSet_PathSelector,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_PathSelector": "DataSet_PathSelector",
}