

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_config import AgentConfig


class ConfigMode(UniversalBaseModel):
    """
    @deprecated Use `agent` field instead.
    """

    build: typing.Optional[AgentConfig] = None
    plan: typing.Optional[AgentConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
