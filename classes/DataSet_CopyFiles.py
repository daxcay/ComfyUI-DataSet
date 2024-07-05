import os
import shutil

def blind_copy(source, destination):
    os.makedirs(destination, exist_ok=True)
    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        dest_file = os.path.join(destination, filename)
        if os.path.isfile(source_file):
            try:
                shutil.copy(source_file, dest_file)
                print(f"Copied {source_file} to {dest_file}")
            except Exception as e:
                print(f"Failed to copy {source_file} to {dest_file}: {e}")

def copy_by_destination_files(source, destination):
    os.makedirs(destination, exist_ok=True)
    dest_files = set(os.listdir(destination))
    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        if os.path.isfile(source_file):
            file_base_name = os.path.splitext(filename)[0]
            dest_file_match = any(os.path.splitext(dest_filename)[0] == file_base_name for dest_filename in dest_files)
            if dest_file_match and filename not in dest_files:
                try:
                    shutil.copy(source_file, destination)
                    print(f"Copied {source_file} to {destination}")
                except Exception as e:
                    print(f"Failed to copy {source_file} to {destination}: {e}")

class DataSet_CopyFiles:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "source_folder": ("STRING", {"default": "directory path"}),
                "destination_folder": ("STRING", {"default": "directory path"}),
                "copy_mode": (['BlindCopy','CopyByDestinationFiles'],),
            },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "SaveIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DATASET🔶"

    def SaveIT(self, source_folder, destination_folder, copy_mode):
        try:

            mode = copy_mode

            if mode == 'BlindCopy':
                blind_copy(source_folder, destination_folder)
            elif mode == 'CopyByDestinationFiles':
                copy_by_destination_files(source_folder, destination_folder)

        except Exception as e:
            print(f"Error saving: {e}")

        return ()

N_CLASS_MAPPINGS = {
    "DataSet_CopyFiles": DataSet_CopyFiles,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_CopyFiles": "DataSet_CopyFiles",
}
