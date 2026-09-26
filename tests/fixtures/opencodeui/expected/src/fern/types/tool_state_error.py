

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_state_error_time import ToolStateErrorTime


class ToolStateError(UniversalBaseModel):
    input: typing.Dict[str, typing.Any]
    error: str
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    time: ToolStateErrorTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
