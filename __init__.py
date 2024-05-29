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
@title: ComfyUI-DRMN
@nickname: ComfyUI-DRMN
@description: Data Research And Manipulators Nodes for Model Trainers, Artists, Designers and Animators.
"""

from .classes.DRMN_TXTFileSaver import N_CLASS_MAPPINGS as TXTFileSaverMappings, N_DISPLAY_NAME_MAPPINGS as TXTFileSaverNameMappings
from .classes.DRMN_TagManipulatorByImageNames import N_CLASS_MAPPINGS as TagManipulatorByImageNamesMappings, N_DISPLAY_NAME_MAPPINGS as TagManipulatorByImageNamesNameMappings
from .classes.DRMN_CaptionVisualizer import N_CLASS_MAPPINGS as CaptionVisualizerMappings, N_DISPLAY_NAME_MAPPINGS as CaptionVisualizerNameMappings
from .classes.DRMN_SearchAndReplace import N_CLASS_MAPPINGS as SearchAndReplaceMappings, N_DISPLAY_NAME_MAPPINGS as SearchAndReplaceNameMappings
from .classes.DRMN_xCopy import N_CLASS_MAPPINGS as xCopyMappings, N_DISPLAY_NAME_MAPPINGS as xCopyNameMappings

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(TXTFileSaverMappings)
NODE_CLASS_MAPPINGS.update(TagManipulatorByImageNamesMappings)
NODE_CLASS_MAPPINGS.update(CaptionVisualizerMappings)
NODE_CLASS_MAPPINGS.update(SearchAndReplaceMappings)
NODE_CLASS_MAPPINGS.update(xCopyMappings)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(TXTFileSaverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TagManipulatorByImageNamesNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(CaptionVisualizerNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SearchAndReplaceNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(xCopyNameMappings)

WEB_DIRECTORY = "./web"