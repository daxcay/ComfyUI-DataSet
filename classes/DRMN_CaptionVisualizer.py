import os
import torch
import numpy as np
from PIL import Image, ImageSequence
import os
from os.path import isfile, join
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx
from collections import Counter, defaultdict
from itertools import combinations
import pandas as pd

def generate_wordcloud_and_network_graph(file_paths, output_dir, top_n_wordcloud=100, top_n_network=100, top_n_table=10):
    word_counter = Counter()
    tag_cooccurrences = Counter()

    for file_path in file_paths:
        with open(file_path, 'r') as f:
            tags = f.read().strip().split(',')
            word_counter.update(tags)
            for tag1 in tags:
                for tag2 in tags:
                    if tag1 != tag2:
                        tag_cooccurrences[(tag1, tag2)] += 1

    # Word cloud generation
    top_wordcloud_tags = dict(word_counter.most_common(top_n_wordcloud))
    wordcloud = WordCloud(width=1920, height=1080, background_color='white').generate_from_frequencies(top_wordcloud_tags)

    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    output_wordcloud_file = join(output_dir, 'wordcloud.png')
    plt.savefig(output_wordcloud_file, bbox_inches='tight', pad_inches=0)
    plt.close()

    print("Word cloud saved as", output_wordcloud_file)

    # Network graph generation

    G = nx.Graph()
    tags_cooccurrence = defaultdict(int)

    for file in file_paths:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            tags = list(set(content.split(',')))
            for tag_pair in combinations(tags, 2):
                if tag_pair[0].strip() and tag_pair[1].strip():
                    tags_cooccurrence[tag_pair] += 1

    top_cooccurrences = sorted(tags_cooccurrence.items(), key=lambda x: x[1], reverse=True)[:top_n_network]

    for (tag1, tag2), weight in top_cooccurrences:
        G.add_edge(tag1.strip(), tag2.strip(), weight=weight)

    plt.figure(figsize=(24, 12))
    gradio_blue = '#0B0F19'
    plt.gca().set_facecolor(gradio_blue)

    degrees = dict(G.degree)
    node_size = [v * 100 for v in degrees.values()]
    node_color = [degrees[n] for n in G.nodes]

    edge_width = [G[u][v]['weight'] / 100 for u, v in G.edges]
    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=node_size,
                           node_color=node_color, cmap=plt.cm.plasma, alpha=0.8)

    nx.draw_networkx_edges(G, pos, width=edge_width, alpha=0.3, edge_color='w')
    nx.draw_networkx_labels(G, pos, font_size=12,
                            font_weight='bold', font_color='white',
                            font_family='sans-serif')

    plt.axis('off')

    output_network_graph_file = join(output_dir, 'network_graph.png')
    plt.savefig(output_network_graph_file, pad_inches=0, dpi=300, bbox_inches='tight', facecolor=gradio_blue)
    plt.close()

    print("Network graph saved as", output_network_graph_file)

    # Tag frequency table
    tag_freq_table = pd.DataFrame.from_dict(word_counter, orient='index', columns=['Frequency'])
    tag_freq_table = tag_freq_table.sort_values(by='Frequency', ascending=False)
    tag_freq_table.reset_index(inplace=True)
    tag_freq_table.columns = ['Tag', 'Frequency']

    plt.figure(figsize=(12, 6))
    bars = plt.bar(tag_freq_table['Tag'][:top_n_table], tag_freq_table['Frequency'][:top_n_table], color='skyblue')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', color='black')

    plt.xlabel('Tag')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig(join(output_dir, 'tag_frequency_table.png'))
    plt.close()

    # plt.figure(figsize=(12, 6))
    # plt.bar(tag_freq_table['Tag'][:top_n_table], tag_freq_table['Frequency'][:top_n_table], color='skyblue')
    # plt.xlabel('Tag')
    # plt.ylabel('Frequency')
    # plt.xticks(rotation=45, ha='right')
    # plt.tight_layout()
    # plt.savefig(join(output_dir, 'tag_frequency_table.png'))
    # plt.close()

    print("Tag frequency table saved as", join(output_dir, 'tag_frequency_table.png'))

    return output_wordcloud_file, output_network_graph_file, join(output_dir, 'tag_frequency_table.png')

def pilToImage(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


def load_image(image_path):

    try:
        img = Image.open(image_path)
        image = img.convert("RGB")
        loaded_image = pilToImage(image)
    except Exception as e:
        print(f"Error loading image from '{image_path}': {e}")

    return loaded_image


def create_empty_image(width=100, height=100, color=(255, 255, 255)):
    try:
        empty_image = Image.new("RGB", (width, height), color)
    except Exception as e:
        print(f"Error creating empty image: {e}")
        empty_image = None

    return empty_image


class DRMN_CaptionVisualizer:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TextFilePathList": ("STRING", {"forceInput": True}),
                "WordCloudTop": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "NetworkGraphTop": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "FrequencyGraphTop": ("INT", {"default": 1, "min": 1, "max": 9999})
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Images",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "Visualize"
    OUTPUT_NODE = True
    CATEGORY = "JDCN Dataset Tools"

    def Visualize(self, TextFilePathList, WordCloudTop, NetworkGraphTop, FrequencyGraphTop):

        try:

            directory_path = os.path.dirname(TextFilePathList[0])
            visualize_path = os.path.join(directory_path, "visualize")
            os.makedirs(visualize_path, exist_ok=True)
            wc, ng, fg = generate_wordcloud_and_network_graph(TextFilePathList, visualize_path, WordCloudTop[0], NetworkGraphTop[0], FrequencyGraphTop[0])
            return ([wc, ng, fg],)

        except Exception as e:
            print(f"Error saving: {e}")

        return (["", "", ""],)


N_CLASS_MAPPINGS = {
    "DRMN_CaptionVisualizer": DRMN_CaptionVisualizer,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DRMN_CaptionVisualizer": "DRMN_CaptionVisualizer",
}
