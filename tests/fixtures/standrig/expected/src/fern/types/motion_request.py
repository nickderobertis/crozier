

import typing

from .motion_request_clip import MotionRequestClip
from .motion_request_loop import MotionRequestLoop
from .motion_request_one import MotionRequestOne
from .motion_request_time import MotionRequestTime

MotionRequest = typing.Union[MotionRequestClip, MotionRequestOne, MotionRequestTime, MotionRequestLoop]
