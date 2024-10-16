import os
import json
import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from comfy.cli_args import args

def save_images_with_metadata(image_tensors, names, destination, img_format='png', quality=95, disable_metadata=True, extra_pnginfo=None, prompt=None, compression=4):

    if not os.path.exists(destination):
        os.makedirs(destination)

    for i, tensor in enumerate(image_tensors):
        image = tensor.cpu().numpy()
        if image.ndim == 4:
            image = image[0]
        if image.ndim == 3 and image.shape[0] == 1:
            image = image[0]
        image = (image * 255).astype(np.uint8)
        img = Image.fromarray(image)
        metadata = None
        if not disable_metadata and img_format.lower() == 'png':
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None and isinstance(extra_pnginfo, dict):
                for key, value in extra_pnginfo.items():
                    metadata.add_text(key, json.dumps(value))

        img_name = f"{names[i]}.{img_format}"
        img_path = os.path.join(destination, img_name)

        if img_format.lower() in ['jpeg', 'jpg']:
            img.save(img_path, format='jpeg', quality=quality)
        elif img_format.lower() == 'png':
            img.save(img_path, pnginfo=metadata, compress_level=compression)
        else:
            img.save(img_path, format=img_format.upper())


class DataSet_SaveImagePro:

    def __init__(self):
        self.compression = 4

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "names": ("STRING",),
                "destination": ("STRING", {}),
                "image_format": (['png', 'jpg'],),
                "image_quality": ("INT", {"default": 100, "min": 1, "max": 100}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "BatchSave"
    OUTPUT_NODE = True
    CATEGORY = "🔶DATASET🔶"

    def BatchSave(self, images, names, destination, image_format, image_quality, prompt=None, extra_pnginfo=None):

        try:
            
            save_images_with_metadata(images,names,destination[0],image_format[0],image_quality[0],False,extra_pnginfo,prompt,self.compression)

        except Exception as e:
            print(f"Error saving image: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "DataSet_SaveImagePro": DataSet_SaveImagePro,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_SaveImagePro": "DataSet_SaveImagePro",
}
