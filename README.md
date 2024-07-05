# ComfyUI-DataSet

</br>

Data Research, Preparation, and Manipulation Nodes for Model Trainers, Artists, Designers, and Animators.

</br>

![COMFY-UI-DATASET](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/1ebeb79a-5d47-4f13-bfe9-d579bc7986a7)

##### you can drag this to comfy

</br>

## Installation

#### Using `comfy-cli` (https://github.com/yoland68/comfy-cli)
  - `comfy node registry-install ComfyUI-DataSet`
  - https://registry.comfy.org/publishers/daxcay/nodes/comfyui-dataset
  
#### Manual Method
  - Go to your Comfyui > Custom Nodes folder
  - Run CMD from folder path box or right click on empty area and click open in terminal.
  - Copy and Paste this command `git clone https://github.com/daxcay/ComfyUI-DataSet.git`
  - Then go inside ComfyUI-DataSet with cmd or open new.
  - and type `pip install -r requirements.txt` to install the requirements.

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

![Screenshot 2024-07-05 195633](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/3b6ef307-6d86-48e4-b9a0-d59610aeeb82)

  The `DataSet_Visualizer` node is designed to visualize datasets by generating a word cloud, a network graph, and a frequency table from tag contents provided in text files.

  #### Inputs
  - **TextFileContents**: (STRING, required) - The contents of the text file to be processed.
  - **Seperator**: (['comma', 'colon', 'space', 'pipe'], required) - The delimiter used to separate tags in the text file. Acceptable values are: 'comma' for `,` 'colon' for `;` 'space' for a ` ` 'pipe' for `|`
  - **WordCloudTop**: (INT, default: 1, min: 1, max: 9999, required) - The number of top tags to include in the word cloud visualization.
  - **NetworkGraphTop**: (INT, default: 1, min: 1, max: 9999, required) - The number of top tag co-occurrences to include in the network graph visualization.
  - **FrequencyGraphTop**: (INT, default: 1, min: 1, max: 9999, required) - The number of top tags to include in the frequency table.

  #### Outputs
  - **GraphsPaths**: (STRING, list) - The file paths of the generated visualizations. It includes paths for: Word cloud image, Network graph image, Frequency table image
  - **GraphsImages**: (IMAGE, list) - The generated images for the visualizations.

</br>

## DataSet_CopyFiles

![Screenshot 2024-07-05 195651](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/7176f6b8-8e88-4c64-bb78-cb53afe8e368)

  The `DataSet_CopyFiles` node provides a methods to copy files from a source folder to a destination folder based on different copying modes: blind copy and copy by matching destination files.
  
  #### Inputs
  - **source_folder**: (STRING, default: "directory path", required) - The path of the source folder containing files to be copied.
  - **destination_folder**: (STRING, default: "directory path", required) - The path of the destination folder where files will be copied.
  - **copy_mode**: (['BlindCopy', 'CopyByDestinationFiles'], required) - The mode of copying files:
    - 'BlindCopy': Copies all files from the source to the destination folder.
    - 'CopyByDestinationFiles': Copies files from the source folder to the destination only if there is a matching file (based on the base name) already present in the destination.

</br>

## DataSet_TriggerWords

![Screenshot 2024-07-05 195619](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/1ab3f438-6b47-4054-8b99-107fdb04d1d4)

The `DataSet_TriggerWords` node is designed to identify and extract trigger words or phrases from text file contents. Trigger words are identified based on the presence of digits within the words.

  #### Inputs
  - **TextFileContents**: (`STRING`, required) - The contents of the text file(s) to be processed.
  - **search**: (`['trigger_word_only', 'trigger_word_phrase']`, required) - The mode of searching for trigger words:
    - `'trigger_word_only'`: Extracts individual trigger words containing digits.
    - `'trigger_word_phrase'`: Extracts entire phrases up to the next comma if any word in the phrase contains a digit.
  
  #### Outputs
  - **Words**: (`STRING`, list) - The extracted trigger words or phrases from the text file(s).

</br>

## DataSet_TextFilesLoadFromList

![Screenshot 2024-07-05 195544](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/fa596e21-e5fd-40ac-a351-e2fa9949fcf9)

  The `DataSet_TextFilesLoadFromList` node is designed to load and read contents from a list of text file paths. It extracts file names, file names without extensions, file paths, and file contents.
  
  #### Inputs
  - **TextFilePathsList**: (`STRING`, required) - A list of file paths to the text files to be loaded. Only paths ending with `.txt` will be processed.
  
  #### Outputs
  - **TextFileNames**: (`STRING`, list) - The names of the text files.
  - **TextFileNamesWithoutExtension**: (`STRING`, list) - The names of the text files without their extensions.
  - **TextFilePaths**: (`STRING`, list) - The file paths of the text files.
  - **TextFileContents**: (`STRING`, list) - The contents of the text files.

</br>

## DataSet_TextFilesLoad

![Screenshot 2024-07-05 195531](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/f16b6575-0be6-4945-8afb-11d54f40649e)

  The `DataSet_TextFilesLoad` node is designed to load and read contents from text files within a specified directory. It extracts file names, file names without extensions, file paths, and file contents.
  
  #### Inputs
  - **directory**: (`STRING`, required) - The directory path where the text files are located. The path should be specified as a string.
  
  #### Outputs
  - **TextFileNames**: (`STRING`, list) - The names of the text files in the directory.
  - **TextFileNamesWithoutExtension**: (`STRING`, list) - The names of the text files without their extensions.
  - **TextFilePaths**: (`STRING`, list) - The file paths of the text files in the directory.
  - **TextFileContents**: (`STRING`, list) - The contents of the text files in the directory.

</br>

## DataSet_TextFilesSave

![Screenshot 2024-07-05 195656](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/303fee7e-5b1a-4343-95a8-dfb8c9aebf6c)

  ### Overview
  The `DataSet_TextFilesSave` node is designed to save text file contents to a specified directory with various saving modes. It supports overwriting, merging, creating new files, and merging before saving new files.
  
  #### Inputs
  - **TextFileNames**: (`STRING`, required) - The names of the text files to be saved.
  - **TextFileContents**: (`STRING`, required) - The contents of the text files to be saved.
  - **destination**: (`STRING`, required) - The directory path where the text files will be saved.
  - **save_mode**: (['Overwrite', 'Merge', 'SaveNew', 'MergeAndSaveNew'], required) - The mode of saving the files:
    - `Overwrite`: Overwrites existing files with the same name.
    - `Merge`: Appends content to existing files with the same name.
    - `SaveNew`: Saves new files with a unique name if a file with the same name already exists.
    - `MergeAndSaveNew`: Merges content with existing files and then saves as a new file with a unique name if a file with the same name already exists.
  
  #### Outputs
  - This class does not produce any output types.

</br>

## DataSet_FindAndReplace

![Screenshot 2024-07-05 195639](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/12b9c2a7-54ea-4d01-ae2b-53898865ca7f)
  
  The `DataSet_FindAndReplace` node facilitates finding and replacing specific text patterns within text file contents.
  
  #### Inputs
  - **TextFileContents**: (`STRING`, required) - The contents of the text file(s) where the search and replace operation will be performed.
  - **SearchFor**: (`STRING`, default: "concept", required) - The text pattern to search for within the `TextFileContents`. Supports multiline input.
  - **ReplaceWith**: (`STRING`, default: "concept", required) - The replacement text for the `SearchFor` pattern. Supports multiline input.
  
  #### Outputs
  - **TextFileContents**: (`STRING`, list) - The modified contents of the text file(s) after performing the find and replace operation.

</br>

## DataSet_PathSelector

![Screenshot 2024-07-05 195538](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/ef4602bf-d0d6-46b5-aa1e-027f2d2cff7d)

  The `DataSet_PathSelector` node is designed to search for files with specific extensions in one directory and then select files with matching names (excluding extensions) from another directory.
  
  #### Inputs
  - **search_in_directory**: (`STRING`, required) - The directory to search for files.
  - **search_for_extensions**: (`STRING`, required) - The extensions of files to search for, separated by commas (e.g., `.txt, .csv`).
  - **select_from_directory**: (`STRING`, required) - The directory to select matching files from.
  - **select_extensions**: (`STRING`, required) - The extensions of files to select, separated by commas (e.g., `.txt, .csv`).
  
  #### Outputs
  - **SelectedNamesWithExtension**: (`STRING`, list) - The names of the selected files with their extensions.
  - **SelectedNamesWithoutExtension**: (`STRING`, list) - The names of the selected files without their extensions.
  - **SelectedPaths**: (`STRING`, list) - The full paths of the selected files.

</br>

## DataSet_ConceptManager

![Screenshot 2024-07-05 195624](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/de1c1dd8-b688-435c-96cd-3368b4f13162)

  The `DataSet_ConceptManager` node is designed to manage concepts within text file contents. It allows adding or removing specified concepts at defined positions.
  
  #### Inputs
  - **TextFileContents**: (`STRING`, required) - The contents of the text file(s) to be processed.
  - **Mode**: (`STRING`, required) - The mode of operation: `'add'` to add concepts or `'remove'` to remove concepts.
  - **Concepts**: (`STRING`, required) - The concepts to add or remove, formatted as text-position pairs (e.g., `"concept1 0, concept2 2"` for adding, `"concept1, concept2"` for removing).
  
  #### Outputs
  - **TextFileContents**: (`STRING`, list) - The modified contents of the text file(s) after adding or removing concepts.

</br>

## DataSet_OpenAIChat

![Screenshot 2024-07-05 195559](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/0876389a-6617-4974-9705-4240ddcf7545)

  The `DataSet_OpenAIChat` node integrates with the OpenAI API to generate responses based on given prompts using various GPT models.
  
  #### Inputs
  - **model**: (STRING, required) - The OpenAI model to use for generating responses. Options include `"gpt-4"`, `"gpt-4-32k"`, `"gpt-3.5-turbo"`, and others.
  - **api_url**: (STRING, default: `"https://api.openai.com/v1"`) - The base URL of the OpenAI API.
  - **api_key**: (STRING, required) - The API key required for authentication with the OpenAI API.
  - **prompt**: (STRING, default: "") - The prompt to start the conversation or generate responses.
  - **token_length**: (INT, default: 1024) - The maximum number of tokens (words) in the generated response.
  
  #### Outputs
  - **STRING**: The generated response from the OpenAI model based on the provided prompt.

</br>

## DataSet_LoadImage

![Screenshot 2024-07-05 195550](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/3a1ce311-8c37-430c-9620-0719cf721aba)

  The `DataSet_LoadImage` node provides functionality to load and process images from a specified directory using Pillow and numpy.
  
  #### Inputs
  - **image**: (STRING, required) - The name of the image file to load from the input directory.
  
  #### Outputs
  - **IMAGE**: The loaded image.
  - **MASK**: The mask associated with the image.
  - **STRING**: The name of the image file.
  - **STRING**: The name of the image file without extension.
  - **STRING**: The full path of the image file.
  - **STRING**: The directory path of the image file.

</br>

## DataSet_SaveImage

![Screenshot 2024-07-05 195646](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/e7aed0b4-526a-4b74-94c7-bc2c417063d6)

  The `DataSet_SaveImage` node facilitates batch saving of images to a specified directory with optional PNG metadata using Pillow and numpy.
  
  #### Inputs
  - **Images**: (IMAGE, required) - List of images to save.
  - **ImageFilePrefix**: (STRING, default: "Image") - Prefix for the saved image filenames.
  - **destination**: (STRING) - Directory path where images will be saved.
  
  #### Hidden Parameters
  - **prompt**: (PROMPT) - Optional prompt metadata for PNG files.
  - **extra_pnginfo**: (EXTRA_PNGINFO) - Additional metadata information in dictionary format for PNG files.
  
  #### Outputs
  - None

</br>

## DataSet_OpenAIChatImage

![Screenshot 2024-07-05 195607](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/8a9313e4-9f73-4b9c-a483-63491af41f3f)

  The `DataSet_OpenAIChatImage` node integrates image input with OpenAI's chat API for generating text-based responses.
  
  #### Inputs
  - **image**: (IMAGE, required) - Image to be processed.
  - **image_detail**: (STRING, default: "high") - Detail level of the image ("low" or "high").
  - **prompt**: (STRING, default: "") - Text prompt for the AI model.
  - **model**: (STRING, default: "gpt-4o") - OpenAI model to use ("gpt-4o", "gpt-4", etc.).
  - **api_url**: (STRING, default: "https://api.openai.com/v1") - OpenAI API endpoint URL.
  - **api_key**: (STRING) - OpenAI API key for authentication.
  - **token_length**: (INT, default: 1024) - Maximum token length for the generated response.
  
  #### Outputs
  - STRING: Text-based response generated by the AI model.

</br>

## DataSet_OpenAIChatImageBatch

![Screenshot 2024-07-05 195615](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/5fe30dba-c9e0-4fb1-a97f-306210831502)

  The `DataSet_OpenAIChatImageBatch` class extends the functionality of `DataSet_OpenAIChatImage` to process batches of images with OpenAI's chat API for generating text-based responses.
  
  #### Inputs
  - **images**: (IMAGE, required) - List of images to be processed.
  - **image_detail**: (STRING, default: "high") - Detail level of the images ("low" or "high").
  - **prompt**: (STRING, default: "") - Text prompt for the AI model.
  - **model**: (STRING, default: "gpt-4o") - OpenAI model to use ("gpt-4o", "gpt-4", etc.).
  - **api_url**: (STRING, default: "https://api.openai.com/v1") - OpenAI API endpoint URL.
  - **api_key**: (STRING) - OpenAI API key for authentication.
  - **token_length**: (INT, default: 1024) - Maximum token length for the generated response.
  
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

