

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_required_event import ActionRequiredEvent
from .model_message_event import ModelMessageEvent
from .turn_metrics import TurnMetrics
from .turn_state_cancelled_metrics import TurnStateCancelledMetrics
from .turn_state_cancelled_reason import TurnStateCancelledReason
from .turn_state_error_metrics import TurnStateErrorMetrics


class TurnState_Cancelled(UniversalBaseModel):
    status: typing.Literal["cancelled"] = "cancelled"
    completed_at: str
    metrics: typing.Optional[TurnStateCancelledMetrics] = None
    reason: TurnStateCancelledReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnState_Done(UniversalBaseModel):
    status: typing.Literal["done"] = "done"
    completed_at: str
    metrics: typing.Optional[TurnMetrics] = None
    output: typing.Optional[ModelMessageEvent] = None
    required_actions: typing.List[ActionRequiredEvent]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnState_Error(UniversalBaseModel):
    status: typing.Literal["error"] = "error"
    completed_at: str
    message: str
    metrics: typing.Optional[TurnStateErrorMetrics] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnState_Running(UniversalBaseModel):
    status: typing.Literal["running"] = "running"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TurnState = typing_extensions.Annotated[
    typing.Union[TurnState_Cancelled, TurnState_Done, TurnState_Error, TurnState_Running],
    pydantic.Field(discriminator="status"),
]
