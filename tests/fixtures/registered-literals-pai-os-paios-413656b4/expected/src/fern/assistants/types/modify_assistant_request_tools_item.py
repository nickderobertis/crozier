

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.function_object import FunctionObject


class ModifyAssistantRequestToolsItem_CodeInterpreter(UniversalBaseModel):
    type: typing.Literal["code_interpreter"] = "code_interpreter"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModifyAssistantRequestToolsItem_Retrieval(UniversalBaseModel):
    type: typing.Literal["retrieval"] = "retrieval"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModifyAssistantRequestToolsItem_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    function: FunctionObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModifyAssistantRequestToolsItem = typing_extensions.Annotated[
    typing.Union[
        ModifyAssistantRequestToolsItem_CodeInterpreter,
        ModifyAssistantRequestToolsItem_Retrieval,
        ModifyAssistantRequestToolsItem_Function,
    ],
    pydantic.Field(discriminator="type"),
]
