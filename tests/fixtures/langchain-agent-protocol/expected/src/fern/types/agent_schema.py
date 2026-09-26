

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentSchema(UniversalBaseModel):
    """
    Defines the structure and properties of an agent.
    """

    agent_id: str = pydantic.Field()
    """
    The ID of the agent.
    """

    input_schema: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The schema for the agent input. In JSON Schema format.
    """

    output_schema: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The schema for the agent output. In JSON Schema format.
    """

    state_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The schema for the agent's internal state. In JSON Schema format.
    """

    config_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The schema for the agent config. In JSON Schema format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
