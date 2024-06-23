import os
import json
import json
import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from comfy.cli_args import args

class DATASET_SaveImage:

    def __init__(self):
        self.compression = 4

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Images": ("IMAGE",),
                "Directory": ("STRING", {}),
                "Filename": ("STRING", {"default": "Image"}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    RETURN_TYPES = ()
    FUNCTION = "BatchSave"
    OUTPUT_NODE = True
    CATEGORY = "🔵 JDCN 🔵"

    def BatchSave(self, Images, Directory, Filename, prompt=None, extra_pnginfo=None):

        try:

            Directory = Directory
            Filename = Filename

            if not os.path.exists(Directory):
                os.makedirs(Directory)

            for image in Images:                

                image = image.cpu().numpy()
                image = (image * 255).astype(np.uint8)
                img = Image.fromarray(image)
                metadata = None
                if not args.disable_metadata:
                    metadata = PngInfo()
                    if prompt is not None:
                        metadata.add_text("prompt", json.dumps(prompt))
                    if extra_pnginfo is not None:
                        for x in extra_pnginfo:
                            metadata.add_text(x, json.dumps(extra_pnginfo[x]))

                file_path = os.path.join(Directory,Filename)
                img.save(file_path, pnginfo=metadata, compress_level=self.compression)

        except Exception as e:
            print(f"Error saving image: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "DATASET_SaveImage": DATASET_SaveImage,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DATASET_SaveImage": "DATASET_SaveImage",
}
