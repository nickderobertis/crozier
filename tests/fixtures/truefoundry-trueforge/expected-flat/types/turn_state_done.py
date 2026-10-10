

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_required_event import ActionRequiredEvent
from .model_message_event import ModelMessageEvent
from .turn_metrics import TurnMetrics


class TurnStateDone(UniversalBaseModel):
    completed_at: str = pydantic.Field()
    """
    ISO 8601 time when the turn reached a terminal state.
    """

    metrics: typing.Optional[TurnMetrics] = None
    output: typing.Optional[ModelMessageEvent] = pydantic.Field(default=None)
    """
    Final `model.message` for the turn, or null when the turn ended paused without a final message.
    """

    required_actions: typing.List[ActionRequiredEvent] = pydantic.Field()
    """
    Pending actions (`tool.approval_required`, `tool.response_required`, `mcp.auth_required`); empty when none.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
