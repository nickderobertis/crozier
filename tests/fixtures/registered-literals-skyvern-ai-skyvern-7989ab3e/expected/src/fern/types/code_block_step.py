

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_type import ActionType


class CodeBlockStep(UniversalBaseModel):
    description: typing.Optional[str] = None
    action_type: typing.Optional[ActionType] = None
    line_start: typing.Optional[int] = None
    line_end: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
