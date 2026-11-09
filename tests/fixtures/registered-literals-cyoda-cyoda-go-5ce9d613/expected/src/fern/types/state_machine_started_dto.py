

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .state_machine_event_dto import StateMachineEventDto


class StateMachineStartedDto(StateMachineEventDto):
    state: str = pydantic.Field()
    """
    The state of the entity when the state machine flow was started
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
