

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_finish_response_next_actions_item import AgentFinishResponseNextActionsItem
from .agent_finish_response_role import AgentFinishResponseRole
from .sha256 import Sha256


class AgentFinishResponse(UniversalBaseModel):
    role: AgentFinishResponseRole
    sha256: Sha256
    next_actions: typing.List[AgentFinishResponseNextActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
