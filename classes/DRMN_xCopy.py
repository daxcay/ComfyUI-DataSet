import os
import shutil

def blind_copy(source, destination):
    os.makedirs(destination, exist_ok=True)
    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination)

def copy_by_destination_files(source, destination):
    os.makedirs(destination, exist_ok=True)
    dest_files = set(os.listdir(destination))
    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        if os.path.isfile(source_file):
            file_base_name = os.path.splitext(filename)[0]
            dest_file_match = any(os.path.splitext(dest_filename)[0] == file_base_name for dest_filename in dest_files)
            if dest_file_match and filename not in dest_files:
                shutil.copy(source_file, destination)

class DRMN_xCopy:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "source_folder": ("STRING", {"default": "directory path"}),
                "destination_folder": ("STRING", {"default": "directory path"}),
                "mode": (['BlindCopy','CopyByDestinationFiles'],),
            },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "SaveIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DRMN🔶"

    def SaveIT(self, source_folder, destination_folder, mode):
        try:

            if mode == 'BlindCopy':
                blind_copy(source_folder, destination_folder)
            elif mode == 'CopyByDestinationFiles':
                copy_by_destination_files(source_folder, destination_folder)

        except Exception as e:
            print(f"Error saving: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "DRMN_xCopy": DRMN_xCopy,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DRMN_xCopy": "DRMN_xCopy",
}
