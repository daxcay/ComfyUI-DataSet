![BANNER](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/dadc0da1-cd5b-485f-88a7-294888fb8f71)

# ComfyUI-DRMN

ComfyUI-DRMN, Data Research And Manipulators Nodes for Model Trainers, Artists, Designers and Animators. Captions, Visualizers, Text Manipulators

You can contact me on my discord server: [https://discord.gg/GZVGqSHT](https://discord.gg/aGQmh62T)

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/b7d4a51d-6f23-43cc-bc40-c8ae469199e2)

## 1. DRMN_CaptionVisualizer

This node helps anyone to visualize captions in 3 different forms: word cloud, networkgraph and frequency graph.

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/56c86908-8055-495f-a433-2e09dd3b3e5c)

### Workflow

[CaptionVisualizer.json](https://github.com/daxcay/ComfyUI-DRMN/files/15160084/CaptionVisualizer.json)

### Inputs

```
TextFilePathList: List of file paths ['path','path','path']
```
```
WordCloudTop: Integer will select top N data to make world cloud
```
```
NetworkGraphTop: Integer will select top N data to make network graph
```
```
FrequencyGraphTop: Integer will select top N data to make freqency graph
```

### Output

3 Images of **Word Cloud, Network graph, and Frequency graph** respectively.
Images are also saved in ```visualize``` folder where the caption files are stored. 

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/3371d531-ad4c-4e72-ae00-43d71e4a87a6)


## 2. DRMN_TXTFileSaver

Saves text file in an innovative way. has mode Merge | Overwrite | SaveNew | MergeAndSaveNew. 
Useful for caption creators and manipulators. 

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/de0fcc4a-0947-4655-906e-0bcf7421e283)

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/435400d0-c9dd-46ad-8192-22398f8f3247)

### Inputs

```
content: content string type
```
```
filename: name of the file without .txt extension
```
```
directory: the directory where the file will be saved
```
```
mode: Merge | Overwrite | SaveNew | MergeAndSaveNew
```

If directory does not exists new directory will be created.

#### Modes Explaination
  1. **Merge**: Old text in file content appended by new text content.
  2. **Overwrite**: Only new text content in file (if directory is a new directory without file it will create new file).
  3. **SaveNew**: Make a numbered file of original name with new text content.
  4. **MergeAndSaveNew**: Old text in file content appended by new text content and make SaveNew.
     
### Output

Text file in directory.

## 3. DRMN_TagManipulatorByImageNames

There may be a possiblity where you named your caption file with the same name as your image file (without extension 😅). 
This node is useful then. You can add a concept in all the caption files at once.

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/55cca034-7ef0-45a7-b872-8732242a884f)

### Inputs

```
ImageNames: List of image names
```

Image names can be generated using this JDCN node

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/1a35dd7e-e754-45e6-8d53-9493c7da5c7d)

```
Tags directory: directory of the caption files.
```
```
Backup: when true a backup folder with last version of file will be saved in tags directory given.
```
```
Concept: the concept you want to add in caption files.
```

### Concept writing format

```
concept int,concept int,concept int
```

where ```concept``` can be any string and ```int``` is the position of the "," in caption file where the addition will take place.


For example,
```
Caption:  a young woman, in red tshirt and black pant, day 

Concept: age 24 1,sunny 2

Result: a young woman, age 24, sunny, in red tshirt and black pant, day
```

```sunny``` should be after ```pant,``` but ended up after ```age 24``` because 2nd comma position was now 3rd after adding ```age 24```.


Concept will be written like this:

```
Caption:  a young woman, in red tshirt and black pant, day 

Concept: age 24 1,sunny 3

Result: a young woman, age 24, in red tshirt and black pant, sunny, day
```

In case you made an error you can use backup folder files.

### Output

Tags directory will have something like this.

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/15d27de2-6b99-4a32-92c4-3796ff4ae4d1)


## 3. DRMN_SearchAndReplace

Helps anyone manipulate caption files to search for a given text in ```SearchFor``` and replace it with the given ```ReplaceWith``` text.

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/8bec970d-4de9-4c99-a491-b490cdd64072)

### Inputs

```
TextFilePathList: text file path list
```
You can use this to get the file path list

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/db148bff-46c0-4fe2-b0c5-0cc91c2d71d8)

```
SearchFor: search for a string you give. it can be any thing (no regex simple plain string 😅)
```
```
ReplaceWith: replaces ```SearchFor```. it can be any thing (no regex simple plain string 😅)
```

### Output

Text file in directory.
Backup of all file is saved in ```sr_backup``` folder where the caption files are stored. 

__________________________________________________________________________________________________________________________________________

# Installation

1) Manual Method
- Go to your Comfyui > Custom Nodes folder
- Run CMD from folder path box or right click on empty area and click open in terminal.
- Copy and Paste this command `git clone https://github.com/daxcay/ComfyUI-DRMN.git`
- Then go inside ComfyUI-DRMN with cmd or open new.
- and type `pip install -r requirements.txt` to install the requirements.

2) Automatic Method with [Comfy Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- Inside ComfyUI > Click Manager Button on Side.
- Click `Install Custom Node` and Search for DRMN and Install this node:

![image](https://github.com/daxcay/ComfyUI-DRMN/assets/164315771/4fdcf3cc-186d-4e36-9ffb-d34a1b48de2c)

- Restart ComfyUI and it should be good to go

3) Recommended Plugin

   **ComfyUI-JDCN** (https://github.com/daxcay/ComfyUI-JDCN) 

__________________________________________________________________________________________________________________________________________

# CREDITS

◉ Daxton Caylor - ComfyUI Node Developer 
- Discord - daxtoncaylor
- Email - daxtoncaylor@gmail.com
- You can contact me on my discord server: [https://discord.gg/GZVGqSHT](https://discord.gg/aGQmh62T)
- Commission Status:  🟢 **Open** 🟢

◉ https://github.com/rafstahelin
- Node Request & Testing

# Support for DRMN ❤️

If you like to suppport me you can donate me on paypal: https://paypal.me/daxtoncaylor
