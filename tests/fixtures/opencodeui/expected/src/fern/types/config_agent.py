

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_config import AgentConfig


class ConfigAgent(UniversalBaseModel):
    """
    Agent configuration, see https://opencode.ai/docs/agents
    """

    plan: typing.Optional[AgentConfig] = None
    build: typing.Optional[AgentConfig] = None
    general: typing.Optional[AgentConfig] = None
    explore: typing.Optional[AgentConfig] = None
    title: typing.Optional[AgentConfig] = None
    summary: typing.Optional[AgentConfig] = None
    compaction: typing.Optional[AgentConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
