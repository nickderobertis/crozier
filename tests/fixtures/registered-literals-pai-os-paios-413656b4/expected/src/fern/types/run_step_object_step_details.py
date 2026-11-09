

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_message_creation_object_message_creation import (
    RunStepDetailsMessageCreationObjectMessageCreation,
)
from .run_step_details_tool_calls_object_tool_calls_item import RunStepDetailsToolCallsObjectToolCallsItem


class RunStepObjectStepDetails_MessageCreation(UniversalBaseModel):
    """
    The details of the run step.
    """

    type: typing.Literal["message_creation"] = "message_creation"
    message_creation: RunStepDetailsMessageCreationObjectMessageCreation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepObjectStepDetails_ToolCalls(UniversalBaseModel):
    """
    The details of the run step.
    """

    type: typing.Literal["tool_calls"] = "tool_calls"
    tool_calls: typing.List[RunStepDetailsToolCallsObjectToolCallsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStepObjectStepDetails = typing_extensions.Annotated[
    typing.Union[RunStepObjectStepDetails_MessageCreation, RunStepObjectStepDetails_ToolCalls],
    pydantic.Field(discriminator="type"),
]
