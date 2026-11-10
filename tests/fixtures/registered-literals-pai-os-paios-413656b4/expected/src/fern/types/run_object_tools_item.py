

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_object import FunctionObject


class RunObjectToolsItem_CodeInterpreter(UniversalBaseModel):
    type: typing.Literal["code_interpreter"] = "code_interpreter"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunObjectToolsItem_Retrieval(UniversalBaseModel):
    type: typing.Literal["retrieval"] = "retrieval"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunObjectToolsItem_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    function: FunctionObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunObjectToolsItem = typing_extensions.Annotated[
    typing.Union[RunObjectToolsItem_CodeInterpreter, RunObjectToolsItem_Retrieval, RunObjectToolsItem_Function],
    pydantic.Field(discriminator="type"),
]
