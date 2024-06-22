import { app } from "../../scripts/app.js";

let DataSet = {
    name: "ComfyUI-Dataset",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if(nodeData.name.indexOf('DATASET') == 0) {
            nodeData.input.required['seed'] = ["INT", {"default": 0, "min": 0, "max": 18446744073709552000}]
        }
	},
}

app.registerExtension(DataSet);