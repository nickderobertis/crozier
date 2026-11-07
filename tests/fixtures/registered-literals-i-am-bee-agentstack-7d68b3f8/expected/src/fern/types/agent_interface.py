

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentInterface(UniversalBaseModel):
    """
    Declares a combination of a target URL and a transport protocol for interacting with the agent.
    This allows agents to expose the same functionality over multiple transport mechanisms.
    """

    transport: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
