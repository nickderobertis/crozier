

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_object import RunObject


class RunStreamEvent_ThreadRunCreated(UniversalBaseModel):
    event: typing.Literal["thread.run.created"] = "thread.run.created"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunQueued(UniversalBaseModel):
    event: typing.Literal["thread.run.queued"] = "thread.run.queued"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunInProgress(UniversalBaseModel):
    event: typing.Literal["thread.run.in_progress"] = "thread.run.in_progress"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunRequiresAction(UniversalBaseModel):
    event: typing.Literal["thread.run.requires_action"] = "thread.run.requires_action"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunCompleted(UniversalBaseModel):
    event: typing.Literal["thread.run.completed"] = "thread.run.completed"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunFailed(UniversalBaseModel):
    event: typing.Literal["thread.run.failed"] = "thread.run.failed"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunCancelling(UniversalBaseModel):
    event: typing.Literal["thread.run.cancelling"] = "thread.run.cancelling"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunCancelled(UniversalBaseModel):
    event: typing.Literal["thread.run.cancelled"] = "thread.run.cancelled"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RunStreamEvent_ThreadRunExpired(UniversalBaseModel):
    event: typing.Literal["thread.run.expired"] = "thread.run.expired"
    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RunStreamEvent = typing_extensions.Annotated[
    typing.Union[
        RunStreamEvent_ThreadRunCreated,
        RunStreamEvent_ThreadRunQueued,
        RunStreamEvent_ThreadRunInProgress,
        RunStreamEvent_ThreadRunRequiresAction,
        RunStreamEvent_ThreadRunCompleted,
        RunStreamEvent_ThreadRunFailed,
        RunStreamEvent_ThreadRunCancelling,
        RunStreamEvent_ThreadRunCancelled,
        RunStreamEvent_ThreadRunExpired,
    ],
    pydantic.Field(discriminator="event"),
]
