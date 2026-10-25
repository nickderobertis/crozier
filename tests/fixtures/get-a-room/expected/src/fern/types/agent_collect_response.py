

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_collect_response_role import AgentCollectResponseRole
from .sha256 import Sha256


class AgentCollectResponse(UniversalBaseModel):
    role: AgentCollectResponseRole
    collected: bool
    sha256: Sha256
    next_actions: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
