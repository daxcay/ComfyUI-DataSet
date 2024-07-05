# ComfyUI-DataSet
</br>
Data research, preparation, and manipulation nodes for model trainers and artists.

</br>

##### Drag & drop image into your workspace for node layout

![COMFY-UI-DATASET](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/f7984a60-3ba3-4292-b720-d9a9706903c3)

</br>

## Installation

#### Using `comfy-cli` (https://github.com/yoland68/comfy-cli)
  - `comfy node registry-install ComfyUI-DataSet`
  - https://registry.comfy.org/publishers/daxcay/nodes/comfyui-dataset
  
#### Manual Method
  - Go to your Comfyui > Custom Nodes folder path > Run CMD
  - Copy and Paste this command git clone ```https://github.com/daxcay/ComfyUI-DataSet.git```
  - Then go inside ComfyUI-DataSet with cmd or open new.
  - type ```pip install -r requirements.txt``` to install the dependencies

#### Automatic Method with [Comfy Manager](https://github.com/ltdrdata/ComfyUI-Manager)
  - Inside ComfyUI > Click Manager Button on Side.
  - Click `Custom Nodes Manager` and  Search for `DataSet` and Install this node:
    
    ![image](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/796bf982-20fc-4859-8096-7138d207214e)
    
  - Restart ComfyUI and it should be good to go

#### Recommended Plugin
  - **ComfyUI-JDCN** (https://github.com/daxcay/ComfyUI-JDCN) 

</br>

### You can find DataSet under this category:
  ![image](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/4930b434-1993-47c4-bd71-d16f762f94a4)

</br>

## DataSet_Visualizer

The DataSet_Visualizer node is designed to visualize dataset captions. It generates graphs offering various perspectives on token analysis. The word cloud represents token frequency with different sized fonts. The network graph illustrates the relationships between tokens. The frequency graph provides an exact metric of how often each token appears in your captions.

![Screenshot 2024-07-05 195633](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/3b6ef307-6d86-48e4-b9a0-d59610aeeb82)

  #### Inputs
  - **TextFileContents**(STRING, required): the contents of the text file to be processed.
  - **Seperator**(['comma', 'colon', 'space', 'pipe'], required): the delimiter used to separate tags in the text file.
  - **WordCloudTop**(INT, min: 1, max: 9999, required): the number of top tokens to be plotted in WordCloud.
  - **NetworkGraphTop**(INT, min: 1, max: 9999, required): the number of top tokens having the highest interconnections within the captions.
  - **FrequencyGraphTop**(INT, min: 1, max: 9999, required): the number of top tags with highest frequency from highest to lowest.

  #### Outputs
  - **GraphsPaths**(STRING, list): the file paths of the generated visualizations. It includes paths for: WordCloud image, NetworkGraph image, FrequencyTable image
  - **GraphsImages**(IMAGE, list): the generated images for the visualizations which can be used with PreviewImage and SaveImage node.

</br>

## DataSet_CopyFiles

The `DataSet_CopyFiles` node provides a method to copy files from a source folder to a destination folder using different modes: `BlindCopy` and `CopyByDestinationFiles`.

![Screenshot 2024-07-05 195651](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/7176f6b8-8e88-4c64-bb78-cb53afe8e368)
  
  #### Inputs
  - **source_folder** (STRING, default: "directory path", required): source folder path to the files.
  - **destination_folder** (STRING, default: "directory path", required): destination folder path for the files copied.
  - **copy_mode** (['BlindCopy', 'CopyByDestinationFiles'], required):
    - `BlindCopy`: copies all files from source to the destination folder.
    - `CopyByDestinationFiles`: copies files from source folder to the destination only if there is a matching file (based on the base name) already present in the destination.

</br>

## DataSet_TriggerWords

The `DataSet_TriggerWords` node is designed to identify and extract trigger words or phrases from text file contents. Trigger words are identified based on the presence of digits within the words.

![Screenshot 2024-07-05 195619](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/1ab3f438-6b47-4054-8b99-107fdb04d1d4)

  #### Inputs
  - **TextFileContents** (`STRING`, required): the contents of the text file(s) to be processed.
  - **search**(`['trigger_word_only', 'trigger_word_phrase']`, required): the mode of searching for trigger words:
    - `'trigger_word_only'`: extracts individual trigger words containing digits.
    - `'trigger_word_phrase'`: extracts entire phrases up to the next comma if any word in the phrase contains a digit.
  
  #### Outputs
  - **Words**: (`STRING`, list) - the extracted trigger words or phrases from the text file(s).

</br>

## DataSet_TextFilesLoadFromList

  The `DataSet_TextFilesLoadFromList` node is designed to load and read contents from a list of text file paths. It extracts file names, file names without extensions, file paths, and file contents.

![Screenshot 2024-07-05 204333](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/a674f684-85f3-4f34-8c3e-b1b34bf89bac)

  
  #### Inputs
  - **TextFilePathsList**(`STRING`, required): a list of file paths to the text files to be loaded. Only paths ending with `.txt` will be processed.
  
  #### Outputs
  - **TextFileNames**(`STRING`, list): the names of the text files.
  - **TextFileNamesWithoutExtension**(`STRING`, list): the names of the text files without their extensions.
  - **TextFilePaths**(`STRING`, list): the file paths of the text files.
  - **TextFileContents**(`STRING`, list): the contents of the text files.

</br>

## DataSet_TextFilesLoad

  The `DataSet_TextFilesLoad` node is designed to load and read contents from text files within a specified directory. It extracts file names, file names without extensions, file paths, and file contents.

![Screenshot 2024-07-05 204321](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/a136dec1-38d1-454e-9f0e-014837428225)

  
  #### Inputs
  - **directory**(`STRING`, required): the directory path where the text files are located. The path should be specified as a string.
  
  #### Outputs
  - **TextFileNames**(`STRING`, list): the names of the text files in the directory.
  - **TextFileNamesWithoutExtension**(`STRING`, list): the names of the text files without their extensions.
  - **TextFilePaths**(`STRING`, list): the file paths of the text files in the directory.
  - **TextFileContents**(`STRING`, list): the contents of the text files in the directory.

</br>

## DataSet_TextFilesSave

  The `DataSet_TextFilesSave` node is designed to save text file contents to a specified directory with various saving modes. It supports overwriting, merging, creating new files, and merging before saving new files.

![Screenshot 2024-07-05 195656](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/303fee7e-5b1a-4343-95a8-dfb8c9aebf6c)
  
  #### Inputs
  - **TextFileNames**(`STRING`, required): the names of the text files to be saved.
  - **TextFileContents**(`STRING`, required): the contents of the text files to be saved.
  - **destination**(`STRING`, required): the directory path where the text files will be saved.
  - **save_mode**(['Overwrite', 'Merge', 'SaveNew', 'MergeAndSaveNew'], required): the mode of saving the files:
    - `Overwrite`: overwrites existing files with the same name.
    - `Merge`: appends content to existing files with the same name.
    - `SaveNew`: saves new files with a unique name if a file with the same name already exists.
    - `MergeAndSaveNew`: merges content with existing files and then saves as a new file with a unique name if a file with the same name already exists.
  
</br>

## DataSet_FindAndReplace

  The `DataSet_FindAndReplace` node facilitates finding and replacing specific text patterns within text file contents.

![Screenshot 2024-07-05 195639](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/12b9c2a7-54ea-4d01-ae2b-53898865ca7f)
  
  #### Inputs
  - **TextFileContents**(`STRING`, required): the contents of the text file(s) where the search and replace operation will be performed.
  - **SearchFor**(`STRING`, default: "concept", required): the text pattern to search for within the `TextFileContents`. Supports multiline input.
  - **ReplaceWith**(`STRING`, default: "concept", required): the replacement text for the `SearchFor` pattern. Supports multiline input.
  
  #### Outputs
  - **TextFileContents**(`STRING`, list): the modified contents of the text file(s) after performing the find and replace operation.

</br>

## DataSet_PathSelector

  The `DataSet_PathSelector` node is designed to search for files with specific extensions in one directory and then select files with matching names (excluding extensions) from another directory.

![Screenshot 2024-07-05 204328](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/181cca81-8a67-40a4-99ef-56c6dc8c0c76)
  
  #### Inputs
  - **search_in_directory**(`STRING`, required): the directory to search for files.
  - **search_for_extensions**(`STRING`, required): the extensions of files to search for, separated by commas (e.g., `.txt, .csv`).
  - **select_from_directory**(`STRING`, required): the directory to select matching files from.
  - **select_extensions**(`STRING`, required): the extensions of files to select, separated by commas (e.g., `.txt, .csv`).
  
  #### Outputs
  - **SelectedNamesWithExtension**(`STRING`, list): the names of the selected files with their extensions.
  - **SelectedNamesWithoutExtension**(`STRING`, list): the names of the selected files without their extensions.
  - **SelectedPaths**(`STRING`, list): the full paths of the selected files.

</br>

## DataSet_ConceptManager

  The `DataSet_ConceptManager` node is designed to manage concepts within text file contents. It allows adding or removing specified concepts at defined positions.

![Screenshot 2024-07-05 195624](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/de1c1dd8-b688-435c-96cd-3368b4f13162)
  
  #### Inputs
  - **TextFileContents**(`STRING`, required): the contents of the text file(s) to be processed.
  - **Mode**(`STRING`, required): the mode of operation: `'add'` to add concepts or `'remove'` to remove concepts.
  - **Concepts**(`STRING`, required): the concepts to add or remove, formatted as text-position pairs (e.g., `"concept1 0, concept2 2"` for adding, `"concept1, concept2"` for removing).
  
  #### Outputs
  - **TextFileContents**(`STRING`, list): the modified contents of the text file(s) after adding or removing concepts.

</br>

## DataSet_OpenAIChat

  The `DataSet_OpenAIChat` node integrates with the OpenAI API to generate responses based on given prompts using various GPT models.

![Screenshot 2024-07-05 195559](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/0876389a-6617-4974-9705-4240ddcf7545)
  
  #### Inputs
  - **model**(STRING, required): the OpenAI model to use for generating responses. Options include `"gpt-4"`, `"gpt-4-32k"`, `"gpt-3.5-turbo"`, and others.
  - **api_url**(STRING, default: `"https://api.openai.com/v1"`): the base URL of the OpenAI API.
  - **api_key**(STRING, required): the API key required for authentication with the OpenAI API.
  - **prompt**(STRING, default: ""): the prompt to start the conversation or generate responses.
  - **token_length**(INT, default: 1024): the maximum number of tokens (words) in the generated response.
  
  #### Outputs
  - **STRING**: the generated response from the OpenAI model based on the provided prompt.

</br>

## DataSet_LoadImage

  The `DataSet_LoadImage` node provides functionality to load and process images from a specified directory using Pillow and numpy.

![Screenshot 2024-07-05 204341](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/9530778f-1998-4a37-8708-3a2ab562c6ff)  

  #### Inputs
  - **image** (STRING, required): the name of the image file to load from the input directory.
  
  #### Outputs
  - **IMAGE**: the loaded image.
  - **MASK**: the mask associated with the image.
  - **STRING**: the name of the image file.
  - **STRING**: the name of the image file without extension.
  - **STRING**: the full path of the image file.
  - **STRING**: the directory path of the image file.

</br>

## DataSet_SaveImage

  The `DataSet_SaveImage` node facilitates batch saving of images to a specified directory with optional PNG metadata using Pillow and numpy.

![Screenshot 2024-07-05 195646](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/e7aed0b4-526a-4b74-94c7-bc2c417063d6)
  
  #### Inputs
  - **Images**(IMAGE, required): list of images to save.
  - **ImageFilePrefix**(STRING, default: "Image"): prefix for the saved image filenames.
  - **destination**(STRING): directory path where images will be saved.
  
</br>

## DataSet_OpenAIChatImage

  The `DataSet_OpenAIChatImage` node integrates image input with OpenAI's chat API for generating text-based responses.

![Screenshot 2024-07-05 195607](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/8a9313e4-9f73-4b9c-a483-63491af41f3f)
  
  #### Inputs
  - **image**(IMAGE, required): image to be processed.
  - **image_detail**(STRING, default: "high":  detail level of the image ("low" or "high").
  - **prompt**(STRING, default: ""): text prompt for the AI model.
  - **model**(STRING, default: "gpt-4o"): OpenAI model to use ("gpt-4o", "gpt-4", etc.).
  - **api_url**(STRING, default: "https://api.openai.com/v1"): OpenAI API endpoint URL.
  - **api_key**(STRING): OpenAI API key for authentication.
  - **token_length**(INT, default: 1024): maximum token length for the generated response.
  
  #### Outputs
  - STRING: Text-based response generated by the AI model.

</br>

## DataSet_OpenAIChatImageBatch

  The `DataSet_OpenAIChatImageBatch` class extends the functionality of `DataSet_OpenAIChatImage` to process batches of images with OpenAI's chat API for generating text-based responses.  

![Screenshot 2024-07-05 195615](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/5fe30dba-c9e0-4fb1-a97f-306210831502)

  #### Inputs
  - **images**(IMAGE, required): list of images to be processed.
  - **image_detail**(STRING, default: "high"): detail level of the images ("low" or "high").
  - **prompt**(STRING, default: ""): text prompt for the AI model.
  - **model**(STRING, default: "gpt-4o"): OpenAI model to use ("gpt-4o", "gpt-4", etc.).
  - **api_url**(STRING, default: "https://api.openai.com/v1"): OpenAI API endpoint URL.
  - **api_key**(STRING): OpenAI API key for authentication.
  - **token_length**(INT, default: 1024): maximum token length for the generated response.
  
  #### Outputs
  - STRING: List of text-based responses generated by the AI model for each input image.

</br>

## Credits ❤️

### Daxton Caylor - ComfyUI Node Developer 
  
  ### Contact
   - **Twitter**: @daxcay27
   - **Email** - daxtoncaylor@gmail.com
   - **Discord** - daxtoncaylor
   - **DiscordServer**: https://discord.gg/Z44Zjpurjp
  
  ### Support
   - **Buy me a coffee**: https://buymeacoffee.com/daxtoncaylor
   - **Support me on paypal**: https://paypal.me/daxtoncaylor

