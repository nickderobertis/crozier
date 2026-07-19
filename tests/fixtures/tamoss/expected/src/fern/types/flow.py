

import typing

from .flow_audio import FlowAudio
from .flow_data import FlowData
from .flow_image import FlowImage
from .flow_multi import FlowMulti
from .flow_video import FlowVideo

Flow = typing.Union[FlowVideo, FlowAudio, FlowImage, FlowData, FlowMulti]
