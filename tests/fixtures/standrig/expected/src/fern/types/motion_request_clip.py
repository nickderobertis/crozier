

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_request_clip_action import MotionRequestClipAction
from .motion_request_clip_clip import MotionRequestClipClip


class MotionRequestClip(UniversalBaseModel):
    action: MotionRequestClipAction
    clip: MotionRequestClipClip

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
