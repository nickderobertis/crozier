

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .config_agent import ConfigAgent
from .config_autoupdate import ConfigAutoupdate
from .config_command_value import ConfigCommandValue
from .config_compaction import ConfigCompaction
from .config_enterprise import ConfigEnterprise
from .config_experimental import ConfigExperimental
from .config_formatter import ConfigFormatter
from .config_lsp import ConfigLsp
from .config_mcp_value import ConfigMcpValue
from .config_mode import ConfigMode
from .config_share import ConfigShare
from .config_skills import ConfigSkills
from .config_tui import ConfigTui
from .config_watcher import ConfigWatcher
from .keybinds_config import KeybindsConfig
from .layout_config import LayoutConfig
from .log_level import LogLevel
from .permission_config import PermissionConfig
from .provider_config import ProviderConfig
from .server_config import ServerConfig


class Config(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="$schema"),
        pydantic.Field(alias="$schema", description="JSON schema reference for configuration validation"),
    ] = None
    """
    JSON schema reference for configuration validation
    """

    theme: typing.Optional[str] = pydantic.Field(default=None)
    """
    Theme name to use for the interface
    """

    keybinds: typing.Optional[KeybindsConfig] = None
    log_level: typing_extensions.Annotated[
        typing.Optional[LogLevel], FieldMetadata(alias="logLevel"), pydantic.Field(alias="logLevel")
    ] = None
    tui: typing.Optional[ConfigTui] = pydantic.Field(default=None)
    """
    TUI specific settings
    """

    server: typing.Optional[ServerConfig] = None
    command: typing.Optional[typing.Dict[str, ConfigCommandValue]] = pydantic.Field(default=None)
    """
    Command configuration, see https://opencode.ai/docs/commands
    """

    skills: typing.Optional[ConfigSkills] = pydantic.Field(default=None)
    """
    Additional skill folder paths
    """

    watcher: typing.Optional[ConfigWatcher] = None
    plugin: typing.Optional[typing.List[str]] = None
    snapshot: typing.Optional[bool] = None
    share: typing.Optional[ConfigShare] = pydantic.Field(default=None)
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto' enables automatic sharing, 'disabled' disables all sharing
    """

    autoshare: typing.Optional[bool] = pydantic.Field(default=None)
    """
    @deprecated Use 'share' field instead. Share newly created sessions automatically
    """

    autoupdate: typing.Optional[ConfigAutoupdate] = pydantic.Field(default=None)
    """
    Automatically update to the latest version. Set to true to auto-update, false to disable, or 'notify' to show update notifications
    """

    disabled_providers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Disable providers that are loaded automatically
    """

    enabled_providers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    When set, ONLY these providers will be enabled. All other providers will be ignored
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model to use in the format of provider/model, eg anthropic/claude-2
    """

    small_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Small model to use for tasks like title generation in the format of provider/model
    """

    default_agent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default agent to use when none is specified. Must be a primary agent. Falls back to 'build' if not set or if the specified agent is invalid.
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom username to display in conversations instead of system username
    """

    mode: typing.Optional[ConfigMode] = pydantic.Field(default=None)
    """
    @deprecated Use `agent` field instead.
    """

    agent: typing.Optional[ConfigAgent] = pydantic.Field(default=None)
    """
    Agent configuration, see https://opencode.ai/docs/agents
    """

    provider: typing.Optional[typing.Dict[str, ProviderConfig]] = pydantic.Field(default=None)
    """
    Custom provider configurations and model overrides
    """

    mcp: typing.Optional[typing.Dict[str, ConfigMcpValue]] = pydantic.Field(default=None)
    """
    MCP (Model Context Protocol) server configurations
    """

    formatter: typing.Optional[ConfigFormatter] = None
    lsp: typing.Optional[ConfigLsp] = None
    instructions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Additional instruction files or patterns to include
    """

    layout: typing.Optional[LayoutConfig] = None
    permission: typing.Optional[PermissionConfig] = None
    tools: typing.Optional[typing.Dict[str, bool]] = None
    enterprise: typing.Optional[ConfigEnterprise] = None
    compaction: typing.Optional[ConfigCompaction] = None
    experimental: typing.Optional[ConfigExperimental] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
