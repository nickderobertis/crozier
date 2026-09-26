

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_capabilities import AgentCapabilities


class Agent(UniversalBaseModel):
    agent_id: str = pydantic.Field()
    """
    The ID of the agent.
    """

    name: str = pydantic.Field()
    """
    The name of the agent
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the agent.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The agent metadata.
    """

    capabilities: AgentCapabilities = pydantic.Field()
    """
    Describes which protocol features the agent supports. In addition to the standard capabilities (prefixed with ap.), implementations can declare custom capabilities, named in reverse domain notation (eg. com.example.some.capability).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
