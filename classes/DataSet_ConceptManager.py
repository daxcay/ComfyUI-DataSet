import random


def append_text(tags, combined_texts):
    tags_list = [tag.strip() for tag in tags.split(',')]
    text_pos_list = [text_pos.strip().split()
                     for text_pos in combined_texts.split(',')]

    for text_pos in text_pos_list:
        num_pos = len(text_pos) - 1
        text = " ".join(text_pos[0:num_pos])

        pos_str = text_pos[num_pos]

        if pos_str == "#":
            pos = random.randint(0, len(tags_list))
        else:
            pos = int(pos_str)

        if pos == 0:
            tags_list.insert(0, text)
        else:
            tags_list.insert(pos, text)

    new_tags = ', '.join(tags_list)
    return new_tags


def getWords(combined_texts):

    text_pos_list = [text_pos.strip().split()
                     for text_pos in combined_texts.split(',')]

    words = []

    for text_pos in text_pos_list:
        num_pos = len(text_pos) - 1
        text = " ".join(text_pos[0:num_pos])
        words.append(text)

    joined_words = ',\n'.join(words)
    return joined_words


def remove_text(tags, combined_texts):
    tags_list = [tag.strip() for tag in tags.split(',')]
    text_pos_list = [text_pos.strip().split()
                     for text_pos in combined_texts.split(',')]

    for text_pos in text_pos_list:
        num_pos = len(text_pos) - 1
        text = " ".join(text_pos[0:num_pos])
        if text in tags_list:
            tags_list.remove(text)

    new_tags = ', '.join(tags_list)
    return new_tags


class DataSet_ConceptManager:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TextFileContents": ("STRING", {"forceInput": True}),
                "Mode": (['add', 'remove'],),
                "Concepts": ("STRING", {"multiline": True, "default": "concept"}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("TextFileContents", "Words",)
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "SaveIT"
    OUTPUT_NODE = True
    CATEGORY = "🔶DATASET🔶"

    def SaveIT(self, TextFileContents, Mode, Concepts):
        try:
            edited = []
            words = []

            for content in TextFileContents:
                if Mode[0] == "add":
                    edited.append(append_text(content, Concepts[0]))
                elif Mode[0] == "remove":
                    edited.append(remove_text(content, Concepts[0]))

            words = getWords(Concepts[0])

        except Exception as e:
            print(f"Error saving: {e}")

        return (edited, words, )


N_CLASS_MAPPINGS = {
    "DataSet_ConceptManager": DataSet_ConceptManager,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DataSet_ConceptManager": "DataSet_ConceptManager",
}
