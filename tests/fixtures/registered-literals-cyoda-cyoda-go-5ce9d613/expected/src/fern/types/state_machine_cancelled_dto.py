

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .state_machine_event_dto import StateMachineEventDto


class StateMachineCancelledDto(StateMachineEventDto):
    reason: str = pydantic.Field()
    """
    Reason for cancellation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
