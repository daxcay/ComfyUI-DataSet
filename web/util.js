import { app } from "../../scripts/app.js";

let groups = {
    "loaders": ['DataSet_TextFilesLoad', 'DataSet_TextFilesLoadFromList', 'DataSet_LoadImage', 'DataSet_PathSelector'],
    "processors": ['DataSet_Visualizer', 'DataSet_FindAndReplace', 'DataSet_ConceptManager', 'DataSet_TriggerWords', 'DataSet_OpenAIChatImageBatch', 'DataSet_OpenAIChatImage', 'DataSet_OpenAIChat'],
    "handlers": ['DataSet_TextFilesSave', 'DataSet_SaveImage', 'DataSet_SaveImagePro', 'DataSet_CopyFiles'],
}

let groupsNodesColor = {
    "loaders": "#823329",
    "processors": "#1a472a",
    "handlers": "#084c61"
}

function getColorByName(name) {
    for (let group in groups) {
        if (groups[group].includes(name)) {
            return groupsNodesColor[group];
        }
    }
    return null;
}

function isInGroup(name, group) {
    if (groups[group]) {
        return groups[group].includes(name);
    }
    return false;
}

function onNodeAdded(node, app) {
    let color = getColorByName(node.title)
    if (color) {
        node.bgcolor = color
        node.color = "#232c33"
    }
}

let DataSet = {
    name: "ComfyUI-Dataset",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (isInGroup(nodeData.name, "loaders") || isInGroup(nodeData.name, "processors") || isInGroup(nodeData.name, "handlers")) {
            nodeData.input.required['seed'] = ["INT", { "default": 0, "min": 0, "max": 18446744073709552000 }]
        }
    },
    loadedGraphNode(node, app) {
        onNodeAdded(node, app)
    },
}

app.registerExtension(DataSet);