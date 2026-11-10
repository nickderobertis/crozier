

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_tool_calls_code_object_code_interpreter import (
    RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter,
)
from .run_step_delta_step_details_tool_calls_function_object_function import (
    RunStepDeltaStepDetailsToolCallsFunctionObjectFunction,
)


class RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter(UniversalBaseModel):
    type: typing.Literal["code_interpreter"] = "code_interpreter"
    index: int
    id: typing.Optional[str] = None
    code_interpreter: typing.Optional[RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Retrieval(UniversalBaseModel):
    type: typing.Literal["retrieval"] = "retrieval"
    index: int
    id: typing.Optional[str] = None
    retrieval: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    index: int
    id: typing.Optional[str] = None
    function: typing.Optional[RunStepDeltaStepDetailsToolCallsFunctionObjectFunction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStepDeltaStepDetailsToolCallsObjectToolCallsItem = typing_extensions.Annotated[
    typing.Union[
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter,
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Retrieval,
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Function,
    ],
    pydantic.Field(discriminator="type"),
]
