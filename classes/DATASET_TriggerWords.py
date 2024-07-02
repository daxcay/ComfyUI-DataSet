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

class DATASET_TriggerWords:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "content": ("STRING",{"forceInput": True}),
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

    def FindIT(self, content, search):
        try:

            search = search[0]
            words = []
            
            for sentence in content:
                if search == "trigger_word_only": 
                    words.append(find_trigger_words(sentence, False))
                elif search == "trigger_word_phrase":
                    words.append(find_trigger_words(sentence, True))            

        except Exception as e:
            print(f"Error saving: {e}")

        return (words,)
    
N_CLASS_MAPPINGS = {
    "DATASET_TriggerWords": DATASET_TriggerWords,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DATASET_TriggerWords": "DATASET_TriggerWords",
}
