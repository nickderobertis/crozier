

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .letta_stop_reason_message_type import LettaStopReasonMessageType
from .stop_reason_type import StopReasonType


class LettaStopReason(UniversalBaseModel):
    """
    The stop reason from Letta indicating why agent loop stopped execution.
    """

    message_type: typing.Optional[LettaStopReasonMessageType] = pydantic.Field(default=None)
    """
    The type of the message.
    """

    stop_reason: StopReasonType = pydantic.Field()
    """
    The reason why execution stopped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
