

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TerminateSessionResponseData(UniversalBaseModel):
    terminated: bool = pydantic.Field()
    """
    Whether a session was terminated
    """

    affected_agents: int = pydantic.Field()
    """
    Number of agents that lost access
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
