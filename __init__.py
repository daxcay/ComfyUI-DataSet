# By Daxton Caylor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
@author: Daxton Caylor
@title: ComfyUI-DataSet
@nickname: ComfyUI-DataSet
@description: Advanced Training Data Research, Preparation, and Manipulation Nodes for Expert Model Trainers, Artists, Designers, and Animators.
"""

from .classes.DataSet_Visualizer import N_CLASS_MAPPINGS as VisualizerMappings, N_DISPLAY_NAME_MAPPINGS as VisualizerNameMappings
from .classes.DataSet_TextFilesLoad import N_CLASS_MAPPINGS as TextFilesLoadMappings, N_DISPLAY_NAME_MAPPINGS as TextFilesLoadNameMappings
from .classes.DataSet_TextFilesLoadFromList import N_CLASS_MAPPINGS as TextFilesLoadFromListMappings, N_DISPLAY_NAME_MAPPINGS as TextFilesLoadFromListNameMappings
from .classes.DataSet_CopyFiles import N_CLASS_MAPPINGS as CopyFilesMappings, N_DISPLAY_NAME_MAPPINGS as CopyFilesNameMappings
from .classes.DataSet_TriggerWords import N_CLASS_MAPPINGS as TriggerWordsMappings,  N_DISPLAY_NAME_MAPPINGS as TriggerWordsNameMappings
from .classes.DataSet_TextFilesSave import N_CLASS_MAPPINGS as TextFilesSaveMappings, N_DISPLAY_NAME_MAPPINGS as TextFilesSaveNameMappings
from .classes.DataSet_ConceptManager import N_CLASS_MAPPINGS as ConceptManagerMappings, N_DISPLAY_NAME_MAPPINGS as ConceptManagerNameMappings
from .classes.DataSet_FindAndReplace import N_CLASS_MAPPINGS as FindAndReplaceMappings, N_DISPLAY_NAME_MAPPINGS as FindAndReplaceNameMappings
from .classes.DataSet_PathSelector import N_CLASS_MAPPINGS as PathSelectorMappings, N_DISPLAY_NAME_MAPPINGS as PathSelectorNameMappings
from .classes.DataSet_LoadImage import N_CLASS_MAPPINGS as LoadImageMappings,  N_DISPLAY_NAME_MAPPINGS as LoadImageNameMappings
from .classes.DataSet_SaveImage import N_CLASS_MAPPINGS as SaveImageMappings,  N_DISPLAY_NAME_MAPPINGS as SaveImageNameMappings
from .classes.DataSet_OpenAIChat import N_CLASS_MAPPINGS as OpenAIChatMappings, N_DISPLAY_NAME_MAPPINGS as OpenAIChatNameMappings
from .classes.DataSet_OpenAIChatImage import N_CLASS_MAPPINGS as OpenAIChatImageMappings,  N_DISPLAY_NAME_MAPPINGS as OpenAIChatImageNameMappings
from .classes.DataSet_OpenAIChatImageBatch import N_CLASS_MAPPINGS as OpenAIChatImageBatchMappings,  N_DISPLAY_NAME_MAPPINGS as OpenAIChatImageBatchNameMappings

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(VisualizerMappings)
NODE_CLASS_MAPPINGS.update(CopyFilesMappings)
NODE_CLASS_MAPPINGS.update(TriggerWordsMappings)
NODE_CLASS_MAPPINGS.update(TextFilesLoadFromListMappings)
NODE_CLASS_MAPPINGS.update(TextFilesLoadMappings)
NODE_CLASS_MAPPINGS.update(TextFilesSaveMappings)
NODE_CLASS_MAPPINGS.update(FindAndReplaceMappings)
NODE_CLASS_MAPPINGS.update(PathSelectorMappings)
NODE_CLASS_MAPPINGS.update(ConceptManagerMappings)
NODE_CLASS_MAPPINGS.update(LoadImageMappings)
NODE_CLASS_MAPPINGS.update(SaveImageMappings)
NODE_CLASS_MAPPINGS.update(OpenAIChatMappings)
NODE_CLASS_MAPPINGS.update(OpenAIChatImageMappings)
NODE_CLASS_MAPPINGS.update(OpenAIChatImageBatchMappings)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(VisualizerNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(CopyFilesNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TriggerWordsNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TextFilesLoadNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TextFilesLoadFromListNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TextFilesSaveNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(FindAndReplaceNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(PathSelectorNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ConceptManagerNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(LoadImageNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SaveImageNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(OpenAIChatNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(OpenAIChatImageNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(OpenAIChatImageBatchNameMappings)

WEB_DIRECTORY = "./web"