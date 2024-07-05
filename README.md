![COMFY-UI](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/f9d6fcf0-9ab8-40bd-8997-303bf3b0f994)

# ComfyUI-DataSet

Data Research, Preparation, and Manipulation Nodes for Model Trainers, Artists, Designers, and Animators.

![workflow (4)](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/9bc9aceb-1d36-454a-9c0a-d462152af88f)

### Installation

##### Using `comfy-cli` (https://github.com/yoland68/comfy-cli)
- `comfy node registry-install ComfyUI-DataSet`
- https://registry.comfy.org/publishers/daxcay/nodes/comfyui-dataset
  
##### Manual Method
- Go to your Comfyui > Custom Nodes folder
- Run CMD from folder path box or right click on empty area and click open in terminal.
- Copy and Paste this command `git clone https://github.com/daxcay/ComfyUI-DataSet.git`
- Then go inside ComfyUI-DataSet with cmd or open new.
- and type `pip install -r requirements.txt` to install the requirements.

##### Automatic Method with [Comfy Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- Inside ComfyUI > Click Manager Button on Side.
- Click `Custom Nodes Manager` and  Search for `DataSet` and Install this node:
- ![image](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/796bf982-20fc-4859-8096-7138d207214e)
- Restart ComfyUI and it should be good to go

##### Recommended Plugin
- **ComfyUI-JDCN** (https://github.com/daxcay/ComfyUI-JDCN) 

##### You can find DataSet under this category:
![image](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/4930b434-1993-47c4-bd71-d16f762f94a4)


# DataSet_Visualizer

  ![Screenshot 2024-07-05 123511](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/e9ade9f8-0856-408d-8ffe-224c523b9371)

  The `DataSet_Visualizer` node is designed to visualize datasets by generating a word cloud, a network graph, and a frequency table from tag contents provided in text files.

  #### Input Parameters
  - **TextFileContents**: (STRING, required) - The contents of the text file to be processed.
  - **Seperator**: (['comma', 'colon', 'space', 'pipe'], required) - The delimiter used to separate tags in the text file. Acceptable values are: 'comma' for `,` 'colon' for `;` 'space' for a ` ` 'pipe' for `|`
  - **WordCloudTop**: (INT, default: 1, min: 1, max: 9999, required) - The number of top tags to include in the word cloud visualization.
  - **NetworkGraphTop**: (INT, default: 1, min: 1, max: 9999, required) - The number of top tag co-occurrences to include in the network graph visualization.
  - **FrequencyGraphTop**: (INT, default: 1, min: 1, max: 9999, required) - The number of top tags to include in the frequency table.

  #### Outputs
  - **GraphsPaths**: (STRING, list) - The file paths of the generated visualizations. It includes paths for: Word cloud image, Network graph image, Frequency table image
  - **GraphsImages**: (IMAGE, list) - The generated images for the visualizations.

# DataSet_CopyFiles

  ![Screenshot 2024-07-05 123444](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/ce92523a-e7ae-42f5-be82-f75964d0f1bc)

  The `DataSet_CopyFiles` node provides a methods to copy files from a source folder to a destination folder based on different copying modes: blind copy and copy by matching destination files.
  
  #### Input Parameters
  - **source_folder**: (STRING, default: "directory path", required) - The path of the source folder containing files to be copied.
  - **destination_folder**: (STRING, default: "directory path", required) - The path of the destination folder where files will be copied.
  - **copy_mode**: (['BlindCopy', 'CopyByDestinationFiles'], required) - The mode of copying files:
    - 'BlindCopy': Copies all files from the source to the destination folder.
    - 'CopyByDestinationFiles': Copies files from the source folder to the destination only if there is a matching file (based on the base name) already present in the destination.

# DataSet_FindAndReplace

  ![Screenshot 2024-07-05 123439](https://github.com/daxcay/ComfyUI-DataSet/assets/164315771/649d1ed9-edf2-4983-bf31-8aeaaf2be814)
  
  The `DataSet_FindAndReplace` node facilitates finding and replacing specific text patterns within text file contents.
  
  #### Input Parameters
  - **TextFileContents**: (`STRING`, required) - The contents of the text file(s) where the search and replace operation will be performed.
  - **SearchFor**: (`STRING`, default: "concept", required) - The text pattern to search for within the `TextFileContents`. Supports multiline input.
  - **ReplaceWith**: (`STRING`, default: "concept", required) - The replacement text for the `SearchFor` pattern. Supports multiline input.
  
  ### Outputs
  - **TextFileContents**: (`STRING`, list) - The modified contents of the text file(s) after performing the find and replace operation.
  

## Credits

🔶 Daxton Caylor - ComfyUI Node Developer 
- Discord - daxtoncaylor
- Email - daxtoncaylor@gmail.com
- Discord server: https://discord.gg/Z44Zjpurjp
- Commission Status:  🟢 **Open** 🟢

🔶 https://github.com/rafstahelin
- Node Request & Testing

## Support for DataSet ❤️
- Buy me a coffee: https://buymeacoffee.com/daxtoncaylor
- If you like to suppport me you can donate me on paypal: https://paypal.me/daxtoncaylor
