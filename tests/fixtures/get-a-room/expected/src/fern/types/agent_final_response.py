

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_final_response_next_actions_item import AgentFinalResponseNextActionsItem
from .agent_final_response_role import AgentFinalResponseRole
from .sha256 import Sha256


class AgentFinalResponse(UniversalBaseModel):
    role: AgentFinalResponseRole
    markdown: str
    sha256: Sha256
    next_actions: typing.List[AgentFinalResponseNextActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
