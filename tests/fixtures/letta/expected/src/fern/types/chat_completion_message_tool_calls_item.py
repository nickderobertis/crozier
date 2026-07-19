

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_output import CustomOutput
from .function_output import FunctionOutput


class ChatCompletionMessageToolCallsItem_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    id: str
    function: FunctionOutput

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionMessageToolCallsItem_Custom(UniversalBaseModel):
    type: typing.Literal["custom"] = "custom"
    id: str
    custom: CustomOutput

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionMessageToolCallsItem = typing_extensions.Annotated[
    typing.Union[ChatCompletionMessageToolCallsItem_Function, ChatCompletionMessageToolCallsItem_Custom],
    pydantic.Field(discriminator="type"),
]
