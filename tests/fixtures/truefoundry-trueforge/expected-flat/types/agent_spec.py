

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .initial_user_message import InitialUserMessage
from .mcp_server import McpServer
from .model import Model
from .response_format import ResponseFormat
from .runtime_config import RuntimeConfig
from .skill import Skill


class AgentSpec(UniversalBaseModel):
    """
    Complete agent definition used inline on a session or saved as a named agent.
    """

    config: typing.Optional[RuntimeConfig] = None
    instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional system prompt — the agent's role, behavior, and constraints.
    """

    mcp_servers: typing.Optional[typing.List[McpServer]] = pydantic.Field(default=None)
    """
    Optional MCP servers attached by configured name.
    """

    messages: typing.Optional[typing.List[InitialUserMessage]] = pydantic.Field(default=None)
    """
    Optional initial user messages injected at the start of every session.
    """

    model: Model
    response_format: typing.Optional[ResponseFormat] = None
    skills: typing.Optional[typing.List[Skill]] = pydantic.Field(default=None)
    """
    Optional name-only skill references. Requires `config.sandbox.enabled: true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
