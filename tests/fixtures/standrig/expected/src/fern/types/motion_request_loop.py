

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .motion_request_loop_action import MotionRequestLoopAction


class MotionRequestLoop(UniversalBaseModel):
    action: MotionRequestLoopAction
    speed: typing.Optional[float] = None
    loop: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
