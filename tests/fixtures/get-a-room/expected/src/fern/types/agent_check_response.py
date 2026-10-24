

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_check_response_next_actions_item import AgentCheckResponseNextActionsItem
from .agent_check_response_role import AgentCheckResponseRole
from .room_message import RoomMessage
from .room_status import RoomStatus


class AgentCheckResponse(UniversalBaseModel):
    role: AgentCheckResponseRole
    status: RoomStatus
    messages: typing.List[RoomMessage]
    next_cursor: int
    next_actions: typing.List[AgentCheckResponseNextActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
