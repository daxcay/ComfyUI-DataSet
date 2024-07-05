def find_trigger_words(input_str, include_till_comma=False):
    parts = [part.strip() for part in input_str.split(',')]    
    trigger_words = []
    for part in parts:
        words = part.split()
        for word in words:
            if any(char.isdigit() for char in word):
                if include_till_comma:
                    trigger_words.append(part)
                else:
                    trigger_words.append(word)
    
    return ', '.join(trigger_words)

class DataSet_TriggerWords:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TextFileContents": ("STRING",{"forceInput": True}),
                "search": (['trigger_word_only','trigger_word_phrase'],),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Words",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "FindIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DATASET🔶"

    def FindIT(self, TextFileContents, search):
        try:

            search = search[0]
            words = []
            
            for content in TextFileContents:
                if search == "trigger_word_only": 
                    words.append(find_trigger_words(content, False))
                elif search == "trigger_word_phrase":
                    words.append(find_trigger_words(content, True))            

        except Exception as e:
            print(f"Error saving: {e}")

        return (words,)
    
N_CLASS_MAPPINGS = {
    "DataSet_TriggerWords": DataSet_TriggerWords,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_TriggerWords": "DataSet_TriggerWords",
}
