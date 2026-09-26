

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_state_running_time import ToolStateRunningTime


class ToolStateRunning(UniversalBaseModel):
    input: typing.Dict[str, typing.Any]
    title: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    time: ToolStateRunningTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
