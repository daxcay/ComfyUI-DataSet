import os
import json
import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from comfy.cli_args import args

class DataSet_SaveImage:

    def __init__(self):
        self.compression = 4

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Images": ("IMAGE",),
                "ImageFilePrefix": ("STRING", {"default": "Image"}),
                "destination": ("STRING", {}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "BatchSave"
    OUTPUT_NODE = True
    CATEGORY = "🔶DATASET🔶"

    def BatchSave(self, Images, ImageFilePrefix, destination, prompt=None, extra_pnginfo=None):
        try:
            ImageFilePrefix = ImageFilePrefix[0]
            Directory = destination[0]

            if not os.path.exists(Directory):
                os.makedirs(Directory)

            for i, image in enumerate(Images):
                image = image.cpu().numpy()

                # Handle image shape to be (H, W, C)
                if image.ndim == 4:  # If the image has a batch dimension
                    image = image[0]

                if image.ndim == 3 and image.shape[0] == 1:  # If the image has an extra dimension
                    image = image[0]

                image = (image * 255).astype(np.uint8)
                img = Image.fromarray(image)
                metadata = None
                if not args.disable_metadata:
                    metadata = PngInfo()
                    if prompt is not None:
                        metadata.add_text("prompt", json.dumps(prompt))
                    if extra_pnginfo is not None and isinstance(extra_pnginfo, dict):
                        for key, value in extra_pnginfo.items():
                            metadata.add_text(key, json.dumps(value))

                # Generate filename with padding of 4 digits
                filename = f"{ImageFilePrefix}_{str(i).zfill(4)}.png"
                file_path = os.path.join(Directory, filename)
                img.save(file_path, pnginfo=metadata, compress_level=self.compression)

        except Exception as e:
            print(f"Error saving image: {e}")

        return ()

N_CLASS_MAPPINGS = {
    "DataSet_SaveImage": DataSet_SaveImage,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_SaveImage": "DataSet_SaveImage",
}
