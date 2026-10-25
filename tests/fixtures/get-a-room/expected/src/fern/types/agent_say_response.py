

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_say_response_next_actions_item import AgentSayResponseNextActionsItem
from .agent_say_response_role import AgentSayResponseRole
from .room_message import RoomMessage


class AgentSayResponse(UniversalBaseModel):
    role: AgentSayResponseRole
    message: RoomMessage
    next_actions: typing.List[AgentSayResponseNextActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
