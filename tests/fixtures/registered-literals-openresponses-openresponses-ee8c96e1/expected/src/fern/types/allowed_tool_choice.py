

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .allowed_tool_choice_type import AllowedToolChoiceType
from .function_tool_choice import FunctionToolChoice
from .tool_choice_value_enum import ToolChoiceValueEnum


class AllowedToolChoice(UniversalBaseModel):
    type: AllowedToolChoiceType
    tools: typing.List[FunctionToolChoice]
    mode: ToolChoiceValueEnum

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
