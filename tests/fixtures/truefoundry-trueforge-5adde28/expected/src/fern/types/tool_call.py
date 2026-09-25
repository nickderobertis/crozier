

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .raw_tool_call import RawToolCall
from .tool_info import ToolInfo


class ToolCall(RawToolCall):
    tool_info: ToolInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
