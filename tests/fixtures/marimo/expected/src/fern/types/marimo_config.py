

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ai_config import AiConfig
from .cache_config import CacheConfig
from .completion_config import CompletionConfig
from .datasources_config import DatasourcesConfig
from .diagnostics_config import DiagnosticsConfig
from .display_config import DisplayConfig
from .formatting_config import FormattingConfig
from .keymap_config import KeymapConfig
from .language_servers_config import LanguageServersConfig
from .lint_config import LintConfig
from .mcp_config import McpConfig
from .package_management_config import PackageManagementConfig
from .runtime_config import RuntimeConfig
from .save_config import SaveConfig
from .server_config import ServerConfig
from .sharing_config import SharingConfig
from .signing_config import SigningConfig
from .snippets_config import SnippetsConfig
from .venv_config import VenvConfig


class MarimoConfig(UniversalBaseModel):
    """
    Configuration for the marimo editor
    """

    ai: typing.Optional[AiConfig] = None
    cache: typing.Optional[CacheConfig] = None
    completion: CompletionConfig
    datasources: typing.Optional[DatasourcesConfig] = None
    diagnostics: typing.Optional[DiagnosticsConfig] = None
    display: DisplayConfig
    experimental: typing.Optional[typing.Dict[str, typing.Any]] = None
    formatting: FormattingConfig
    keymap: KeymapConfig
    language_servers: typing.Optional[LanguageServersConfig] = None
    lint: typing.Optional[LintConfig] = None
    mcp: typing.Optional[McpConfig] = None
    package_management: PackageManagementConfig
    runtime: RuntimeConfig
    save: SaveConfig
    server: ServerConfig
    sharing: typing.Optional[SharingConfig] = None
    signing: typing.Optional[SigningConfig] = None
    snippets: typing.Optional[SnippetsConfig] = None
    venv: typing.Optional[VenvConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
