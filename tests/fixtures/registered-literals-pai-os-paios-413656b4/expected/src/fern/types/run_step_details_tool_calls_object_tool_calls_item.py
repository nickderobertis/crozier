

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_tool_calls_code_object_code_interpreter import RunStepDetailsToolCallsCodeObjectCodeInterpreter
from .run_step_details_tool_calls_function_object_function import RunStepDetailsToolCallsFunctionObjectFunction


class RunStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter(UniversalBaseModel):
    type: typing.Literal["code_interpreter"] = "code_interpreter"
    id: str
    code_interpreter: RunStepDetailsToolCallsCodeObjectCodeInterpreter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepDetailsToolCallsObjectToolCallsItem_Retrieval(UniversalBaseModel):
    type: typing.Literal["retrieval"] = "retrieval"
    id: str
    retrieval: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepDetailsToolCallsObjectToolCallsItem_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    id: str
    function: RunStepDetailsToolCallsFunctionObjectFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStepDetailsToolCallsObjectToolCallsItem = typing_extensions.Annotated[
    typing.Union[
        RunStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter,
        RunStepDetailsToolCallsObjectToolCallsItem_Retrieval,
        RunStepDetailsToolCallsObjectToolCallsItem_Function,
    ],
    pydantic.Field(discriminator="type"),
]
