class DataSet_FindAndReplace:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TextFileContents": ("STRING", {"forceInput": True}),
                "SearchFor": ("STRING", {"multiline": True, "default": "concept"}),
                "ReplaceWith": ("STRING", {"multiline": True, "default": "concept"})
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("TextFileContents",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "SaR"
    OUTPUT_NODE = True
    CATEGORY = "🔶DATASET🔶"

    def SaR(self, TextFileContents, SearchFor, ReplaceWith):
        edited = []
        for content in TextFileContents:
            edited.append(content.replace(SearchFor[0], ReplaceWith[0]))        
        return (edited,)

N_CLASS_MAPPINGS = {
    "DataSet_FindAndReplace": DataSet_FindAndReplace,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_FindAndReplace": "DataSet_FindAndReplace",
}
