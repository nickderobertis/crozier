

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_object import RunStepDeltaObject
from .run_step_object import RunStepObject


class RunStepStreamEvent_ThreadRunStepCreated(UniversalBaseModel):
    event: typing.Literal["thread.run.step.created"] = "thread.run.step.created"
    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepStreamEvent_ThreadRunStepInProgress(UniversalBaseModel):
    event: typing.Literal["thread.run.step.in_progress"] = "thread.run.step.in_progress"
    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepStreamEvent_ThreadRunStepDelta(UniversalBaseModel):
    event: typing.Literal["thread.run.step.delta"] = "thread.run.step.delta"
    data: RunStepDeltaObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepStreamEvent_ThreadRunStepCompleted(UniversalBaseModel):
    event: typing.Literal["thread.run.step.completed"] = "thread.run.step.completed"
    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepStreamEvent_ThreadRunStepFailed(UniversalBaseModel):
    event: typing.Literal["thread.run.step.failed"] = "thread.run.step.failed"
    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepStreamEvent_ThreadRunStepCancelled(UniversalBaseModel):
    event: typing.Literal["thread.run.step.cancelled"] = "thread.run.step.cancelled"
    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStepStreamEvent_ThreadRunStepExpired(UniversalBaseModel):
    event: typing.Literal["thread.run.step.expired"] = "thread.run.step.expired"
    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStepStreamEvent = typing_extensions.Annotated[
    typing.Union[
        RunStepStreamEvent_ThreadRunStepCreated,
        RunStepStreamEvent_ThreadRunStepInProgress,
        RunStepStreamEvent_ThreadRunStepDelta,
        RunStepStreamEvent_ThreadRunStepCompleted,
        RunStepStreamEvent_ThreadRunStepFailed,
        RunStepStreamEvent_ThreadRunStepCancelled,
        RunStepStreamEvent_ThreadRunStepExpired,
    ],
    pydantic.Field(discriminator="event"),
]
