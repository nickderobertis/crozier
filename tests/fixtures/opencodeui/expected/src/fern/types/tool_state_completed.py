

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_part import FilePart
from .tool_state_completed_time import ToolStateCompletedTime


class ToolStateCompleted(UniversalBaseModel):
    input: typing.Dict[str, typing.Any]
    output: str
    title: str
    metadata: typing.Dict[str, typing.Any]
    time: ToolStateCompletedTime
    attachments: typing.Optional[typing.List[FilePart]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
