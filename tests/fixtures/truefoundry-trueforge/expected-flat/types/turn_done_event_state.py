

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


class TurnDoneEventState_Cancelled(UniversalBaseModel):
    """
    Terminal turn state (done, cancelled, or error).
    """

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


class TurnDoneEventState_Done(UniversalBaseModel):
    """
    Terminal turn state (done, cancelled, or error).
    """

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


class TurnDoneEventState_Error(UniversalBaseModel):
    """
    Terminal turn state (done, cancelled, or error).
    """

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


TurnDoneEventState = typing_extensions.Annotated[
    typing.Union[TurnDoneEventState_Cancelled, TurnDoneEventState_Done, TurnDoneEventState_Error],
    pydantic.Field(discriminator="status"),
]
