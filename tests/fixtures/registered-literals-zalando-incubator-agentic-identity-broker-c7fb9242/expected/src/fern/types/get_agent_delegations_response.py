

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_delegation import AgentDelegation


class GetAgentDelegationsResponse(UniversalBaseModel):
    data: typing.List[AgentDelegation] = pydantic.Field()
    """
    Array of agent delegations. Empty array if user has no active delegations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
