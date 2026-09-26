

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.agent import Agent
from .types.app_log_request_level import AppLogRequestLevel
from .types.app_skills_response_item import AppSkillsResponseItem
from .types.assistant_message import AssistantMessage
from .types.auth import Auth
from .types.command import Command
from .types.config import Config
from .types.config_agent import ConfigAgent
from .types.config_autoupdate import ConfigAutoupdate
from .types.config_command_value import ConfigCommandValue
from .types.config_compaction import ConfigCompaction
from .types.config_enterprise import ConfigEnterprise
from .types.config_experimental import ConfigExperimental
from .types.config_formatter import ConfigFormatter
from .types.config_lsp import ConfigLsp
from .types.config_mcp_value import ConfigMcpValue
from .types.config_mode import ConfigMode
from .types.config_providers_response import ConfigProvidersResponse
from .types.config_share import ConfigShare
from .types.config_skills import ConfigSkills
from .types.config_tui import ConfigTui
from .types.config_watcher import ConfigWatcher
from .types.event import Event
from .types.file import File
from .types.file_content import FileContent
from .types.file_diff import FileDiff
from .types.file_node import FileNode
from .types.find_files_request_dirs import FindFilesRequestDirs
from .types.find_files_request_type import FindFilesRequestType
from .types.find_text_response_item import FindTextResponseItem
from .types.formatter_status import FormatterStatus
from .types.global_event import GlobalEvent
from .types.global_health_response import GlobalHealthResponse
from .types.keybinds_config import KeybindsConfig
from .types.layout_config import LayoutConfig
from .types.log_level import LogLevel
from .types.lsp_status import LspStatus
from .types.mcp_add_request_config import McpAddRequestConfig
from .types.mcp_auth_remove_response import McpAuthRemoveResponse
from .types.mcp_auth_start_response import McpAuthStartResponse
from .types.mcp_resource import McpResource
from .types.mcp_status import McpStatus
from .types.part import Part
from .types.path import Path
from .types.permission_config import PermissionConfig
from .types.permission_reply_request_reply import PermissionReplyRequestReply
from .types.permission_request import PermissionRequest
from .types.permission_respond_request_response import PermissionRespondRequestResponse
from .types.permission_ruleset import PermissionRuleset
from .types.project import Project
from .types.project_update_request_commands import ProjectUpdateRequestCommands
from .types.project_update_request_icon import ProjectUpdateRequestIcon
from .types.provider_auth_authorization import ProviderAuthAuthorization
from .types.provider_auth_method import ProviderAuthMethod
from .types.provider_config import ProviderConfig
from .types.provider_list_response import ProviderListResponse
from .types.pty import Pty
from .types.pty_update_request_size import PtyUpdateRequestSize
from .types.question_answer import QuestionAnswer
from .types.question_request import QuestionRequest
from .types.server_config import ServerConfig
from .types.session import Session
from .types.session_command_request_parts_item import SessionCommandRequestPartsItem
from .types.session_command_response import SessionCommandResponse
from .types.session_message_response import SessionMessageResponse
from .types.session_messages_response_item import SessionMessagesResponseItem
from .types.session_prompt_async_request_model import SessionPromptAsyncRequestModel
from .types.session_prompt_async_request_parts_item import SessionPromptAsyncRequestPartsItem
from .types.session_prompt_request_model import SessionPromptRequestModel
from .types.session_prompt_request_parts_item import SessionPromptRequestPartsItem
from .types.session_prompt_response import SessionPromptResponse
from .types.session_shell_request_model import SessionShellRequestModel
from .types.session_status import SessionStatus
from .types.session_update_request_time import SessionUpdateRequestTime
from .types.symbol import Symbol
from .types.todo import Todo
from .types.tool_i_ds import ToolIDs
from .types.tool_list import ToolList
from .types.tui_control_next_response import TuiControlNextResponse
from .types.tui_publish_request_body import TuiPublishRequestBody
from .types.tui_show_toast_request_variant import TuiShowToastRequestVariant
from .types.vcs_info import VcsInfo
from .types.worktree import Worktree

if typing.TYPE_CHECKING:
    from .session.client import AsyncSessionClient, SessionClient

OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._session: typing.Optional[SessionClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def global_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalHealthResponse:
        """
        Get health information about the OpenCode server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalHealthResponse
            Health information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.global_health()
        """
        _response = self._raw_client.global_health(request_options=request_options)
        return _response.data

    def global_event(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[GlobalEvent]:
        """
        Subscribe to global events from the OpenCode system using server-sent events.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[GlobalEvent]
            Event stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.global_event()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.global_event(request_options=request_options) as r:
            yield from r.data

    def global_config_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Retrieve the current global OpenCode configuration settings and preferences.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Get global config info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.global_config_get()
        """
        _response = self._raw_client.global_config_get(request_options=request_options)
        return _response.data

    def global_config_update(
        self,
        *,
        schema: typing.Optional[str] = OMIT,
        theme: typing.Optional[str] = OMIT,
        keybinds: typing.Optional[KeybindsConfig] = OMIT,
        log_level: typing.Optional[LogLevel] = OMIT,
        tui: typing.Optional[ConfigTui] = OMIT,
        server: typing.Optional[ServerConfig] = OMIT,
        command: typing.Optional[typing.Dict[str, ConfigCommandValue]] = OMIT,
        skills: typing.Optional[ConfigSkills] = OMIT,
        watcher: typing.Optional[ConfigWatcher] = OMIT,
        plugin: typing.Optional[typing.Sequence[str]] = OMIT,
        snapshot: typing.Optional[bool] = OMIT,
        share: typing.Optional[ConfigShare] = OMIT,
        autoshare: typing.Optional[bool] = OMIT,
        autoupdate: typing.Optional[ConfigAutoupdate] = OMIT,
        disabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        model: typing.Optional[str] = OMIT,
        small_model: typing.Optional[str] = OMIT,
        default_agent: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        mode: typing.Optional[ConfigMode] = OMIT,
        agent: typing.Optional[ConfigAgent] = OMIT,
        provider: typing.Optional[typing.Dict[str, ProviderConfig]] = OMIT,
        mcp: typing.Optional[typing.Dict[str, ConfigMcpValue]] = OMIT,
        formatter: typing.Optional[ConfigFormatter] = OMIT,
        lsp: typing.Optional[ConfigLsp] = OMIT,
        instructions: typing.Optional[typing.Sequence[str]] = OMIT,
        layout: typing.Optional[LayoutConfig] = OMIT,
        permission: typing.Optional[PermissionConfig] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        enterprise: typing.Optional[ConfigEnterprise] = OMIT,
        compaction: typing.Optional[ConfigCompaction] = OMIT,
        experimental: typing.Optional[ConfigExperimental] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Config:
        """
        Update global OpenCode configuration settings and preferences.

        Parameters
        ----------
        schema : typing.Optional[str]
            JSON schema reference for configuration validation

        theme : typing.Optional[str]
            Theme name to use for the interface

        keybinds : typing.Optional[KeybindsConfig]

        log_level : typing.Optional[LogLevel]

        tui : typing.Optional[ConfigTui]
            TUI specific settings

        server : typing.Optional[ServerConfig]

        command : typing.Optional[typing.Dict[str, ConfigCommandValue]]
            Command configuration, see https://opencode.ai/docs/commands

        skills : typing.Optional[ConfigSkills]
            Additional skill folder paths

        watcher : typing.Optional[ConfigWatcher]

        plugin : typing.Optional[typing.Sequence[str]]

        snapshot : typing.Optional[bool]

        share : typing.Optional[ConfigShare]
            Control sharing behavior:'manual' allows manual sharing via commands, 'auto' enables automatic sharing, 'disabled' disables all sharing

        autoshare : typing.Optional[bool]
            @deprecated Use 'share' field instead. Share newly created sessions automatically

        autoupdate : typing.Optional[ConfigAutoupdate]
            Automatically update to the latest version. Set to true to auto-update, false to disable, or 'notify' to show update notifications

        disabled_providers : typing.Optional[typing.Sequence[str]]
            Disable providers that are loaded automatically

        enabled_providers : typing.Optional[typing.Sequence[str]]
            When set, ONLY these providers will be enabled. All other providers will be ignored

        model : typing.Optional[str]
            Model to use in the format of provider/model, eg anthropic/claude-2

        small_model : typing.Optional[str]
            Small model to use for tasks like title generation in the format of provider/model

        default_agent : typing.Optional[str]
            Default agent to use when none is specified. Must be a primary agent. Falls back to 'build' if not set or if the specified agent is invalid.

        username : typing.Optional[str]
            Custom username to display in conversations instead of system username

        mode : typing.Optional[ConfigMode]
            @deprecated Use `agent` field instead.

        agent : typing.Optional[ConfigAgent]
            Agent configuration, see https://opencode.ai/docs/agents

        provider : typing.Optional[typing.Dict[str, ProviderConfig]]
            Custom provider configurations and model overrides

        mcp : typing.Optional[typing.Dict[str, ConfigMcpValue]]
            MCP (Model Context Protocol) server configurations

        formatter : typing.Optional[ConfigFormatter]

        lsp : typing.Optional[ConfigLsp]

        instructions : typing.Optional[typing.Sequence[str]]
            Additional instruction files or patterns to include

        layout : typing.Optional[LayoutConfig]

        permission : typing.Optional[PermissionConfig]

        tools : typing.Optional[typing.Dict[str, bool]]

        enterprise : typing.Optional[ConfigEnterprise]

        compaction : typing.Optional[ConfigCompaction]

        experimental : typing.Optional[ConfigExperimental]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Successfully updated global config

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.global_config_update()
        """
        _response = self._raw_client.global_config_update(
            schema=schema,
            theme=theme,
            keybinds=keybinds,
            log_level=log_level,
            tui=tui,
            server=server,
            command=command,
            skills=skills,
            watcher=watcher,
            plugin=plugin,
            snapshot=snapshot,
            share=share,
            autoshare=autoshare,
            autoupdate=autoupdate,
            disabled_providers=disabled_providers,
            enabled_providers=enabled_providers,
            model=model,
            small_model=small_model,
            default_agent=default_agent,
            username=username,
            mode=mode,
            agent=agent,
            provider=provider,
            mcp=mcp,
            formatter=formatter,
            lsp=lsp,
            instructions=instructions,
            layout=layout,
            permission=permission,
            tools=tools,
            enterprise=enterprise,
            compaction=compaction,
            experimental=experimental,
            request_options=request_options,
        )
        return _response.data

    def global_dispose(self, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Clean up and dispose all OpenCode instances, releasing all resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Global disposed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.global_dispose()
        """
        _response = self._raw_client.global_dispose(request_options=request_options)
        return _response.data

    def auth_set(
        self, provider_id: str, *, request: Auth, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Set authentication credentials

        Parameters
        ----------
        provider_id : str

        request : Auth

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully set authentication credentials

        Examples
        --------
        from fern import Auth_Oauth, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth_set(
            provider_id="providerID",
            request=Auth_Oauth(
                refresh="refresh",
                access="access",
                expires=1.1,
            ),
        )
        """
        _response = self._raw_client.auth_set(provider_id, request=request, request_options=request_options)
        return _response.data

    def auth_remove(self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Remove authentication credentials

        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully removed authentication credentials

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth_remove(
            provider_id="providerID",
        )
        """
        _response = self._raw_client.auth_remove(provider_id, request_options=request_options)
        return _response.data

    def project_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Project]:
        """
        Get a list of projects that have been opened with OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Project]
            List of projects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.project_list()
        """
        _response = self._raw_client.project_list(directory=directory, request_options=request_options)
        return _response.data

    def project_current(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Retrieve the currently active project that OpenCode is working with.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Current project information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.project_current()
        """
        _response = self._raw_client.project_current(directory=directory, request_options=request_options)
        return _response.data

    def project_update(
        self,
        project_id: str,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[ProjectUpdateRequestIcon] = OMIT,
        commands: typing.Optional[ProjectUpdateRequestCommands] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Update project properties such as name, icon, and commands.

        Parameters
        ----------
        project_id : str

        directory : typing.Optional[str]

        name : typing.Optional[str]

        icon : typing.Optional[ProjectUpdateRequestIcon]

        commands : typing.Optional[ProjectUpdateRequestCommands]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Updated project information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.project_update(
            project_id="projectID",
        )
        """
        _response = self._raw_client.project_update(
            project_id, directory=directory, name=name, icon=icon, commands=commands, request_options=request_options
        )
        return _response.data

    def pty_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Pty]:
        """
        Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Pty]
            List of sessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pty_list()
        """
        _response = self._raw_client.pty_list(directory=directory, request_options=request_options)
        return _response.data

    def pty_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        command: typing.Optional[str] = OMIT,
        args: typing.Optional[typing.Sequence[str]] = OMIT,
        cwd: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        env: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pty:
        """
        Create a new pseudo-terminal (PTY) session for running shell commands and processes.

        Parameters
        ----------
        directory : typing.Optional[str]

        command : typing.Optional[str]

        args : typing.Optional[typing.Sequence[str]]

        cwd : typing.Optional[str]

        title : typing.Optional[str]

        env : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pty
            Created session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pty_create()
        """
        _response = self._raw_client.pty_create(
            directory=directory,
            command=command,
            args=args,
            cwd=cwd,
            title=title,
            env=env,
            request_options=request_options,
        )
        return _response.data

    def pty_get(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pty:
        """
        Retrieve detailed information about a specific pseudo-terminal (PTY) session.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pty
            Session info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pty_get(
            pty_id="ptyID",
        )
        """
        _response = self._raw_client.pty_get(pty_id, directory=directory, request_options=request_options)
        return _response.data

    def pty_update(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        size: typing.Optional[PtyUpdateRequestSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pty:
        """
        Update properties of an existing pseudo-terminal (PTY) session.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        title : typing.Optional[str]

        size : typing.Optional[PtyUpdateRequestSize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pty
            Updated session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pty_update(
            pty_id="ptyID",
        )
        """
        _response = self._raw_client.pty_update(
            pty_id, directory=directory, title=title, size=size, request_options=request_options
        )
        return _response.data

    def pty_remove(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Remove and terminate a specific pseudo-terminal (PTY) session.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Session removed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pty_remove(
            pty_id="ptyID",
        )
        """
        _response = self._raw_client.pty_remove(pty_id, directory=directory, request_options=request_options)
        return _response.data

    def pty_connect(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Establish a WebSocket connection to interact with a pseudo-terminal (PTY) session in real-time.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Connected session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pty_connect(
            pty_id="ptyID",
        )
        """
        _response = self._raw_client.pty_connect(pty_id, directory=directory, request_options=request_options)
        return _response.data

    def config_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Config:
        """
        Retrieve the current OpenCode configuration settings and preferences.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Get config info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.config_get()
        """
        _response = self._raw_client.config_get(directory=directory, request_options=request_options)
        return _response.data

    def config_update(
        self,
        *,
        directory: typing.Optional[str] = None,
        schema: typing.Optional[str] = OMIT,
        theme: typing.Optional[str] = OMIT,
        keybinds: typing.Optional[KeybindsConfig] = OMIT,
        log_level: typing.Optional[LogLevel] = OMIT,
        tui: typing.Optional[ConfigTui] = OMIT,
        server: typing.Optional[ServerConfig] = OMIT,
        command: typing.Optional[typing.Dict[str, ConfigCommandValue]] = OMIT,
        skills: typing.Optional[ConfigSkills] = OMIT,
        watcher: typing.Optional[ConfigWatcher] = OMIT,
        plugin: typing.Optional[typing.Sequence[str]] = OMIT,
        snapshot: typing.Optional[bool] = OMIT,
        share: typing.Optional[ConfigShare] = OMIT,
        autoshare: typing.Optional[bool] = OMIT,
        autoupdate: typing.Optional[ConfigAutoupdate] = OMIT,
        disabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        model: typing.Optional[str] = OMIT,
        small_model: typing.Optional[str] = OMIT,
        default_agent: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        mode: typing.Optional[ConfigMode] = OMIT,
        agent: typing.Optional[ConfigAgent] = OMIT,
        provider: typing.Optional[typing.Dict[str, ProviderConfig]] = OMIT,
        mcp: typing.Optional[typing.Dict[str, ConfigMcpValue]] = OMIT,
        formatter: typing.Optional[ConfigFormatter] = OMIT,
        lsp: typing.Optional[ConfigLsp] = OMIT,
        instructions: typing.Optional[typing.Sequence[str]] = OMIT,
        layout: typing.Optional[LayoutConfig] = OMIT,
        permission: typing.Optional[PermissionConfig] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        enterprise: typing.Optional[ConfigEnterprise] = OMIT,
        compaction: typing.Optional[ConfigCompaction] = OMIT,
        experimental: typing.Optional[ConfigExperimental] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Config:
        """
        Update OpenCode configuration settings and preferences.

        Parameters
        ----------
        directory : typing.Optional[str]

        schema : typing.Optional[str]
            JSON schema reference for configuration validation

        theme : typing.Optional[str]
            Theme name to use for the interface

        keybinds : typing.Optional[KeybindsConfig]

        log_level : typing.Optional[LogLevel]

        tui : typing.Optional[ConfigTui]
            TUI specific settings

        server : typing.Optional[ServerConfig]

        command : typing.Optional[typing.Dict[str, ConfigCommandValue]]
            Command configuration, see https://opencode.ai/docs/commands

        skills : typing.Optional[ConfigSkills]
            Additional skill folder paths

        watcher : typing.Optional[ConfigWatcher]

        plugin : typing.Optional[typing.Sequence[str]]

        snapshot : typing.Optional[bool]

        share : typing.Optional[ConfigShare]
            Control sharing behavior:'manual' allows manual sharing via commands, 'auto' enables automatic sharing, 'disabled' disables all sharing

        autoshare : typing.Optional[bool]
            @deprecated Use 'share' field instead. Share newly created sessions automatically

        autoupdate : typing.Optional[ConfigAutoupdate]
            Automatically update to the latest version. Set to true to auto-update, false to disable, or 'notify' to show update notifications

        disabled_providers : typing.Optional[typing.Sequence[str]]
            Disable providers that are loaded automatically

        enabled_providers : typing.Optional[typing.Sequence[str]]
            When set, ONLY these providers will be enabled. All other providers will be ignored

        model : typing.Optional[str]
            Model to use in the format of provider/model, eg anthropic/claude-2

        small_model : typing.Optional[str]
            Small model to use for tasks like title generation in the format of provider/model

        default_agent : typing.Optional[str]
            Default agent to use when none is specified. Must be a primary agent. Falls back to 'build' if not set or if the specified agent is invalid.

        username : typing.Optional[str]
            Custom username to display in conversations instead of system username

        mode : typing.Optional[ConfigMode]
            @deprecated Use `agent` field instead.

        agent : typing.Optional[ConfigAgent]
            Agent configuration, see https://opencode.ai/docs/agents

        provider : typing.Optional[typing.Dict[str, ProviderConfig]]
            Custom provider configurations and model overrides

        mcp : typing.Optional[typing.Dict[str, ConfigMcpValue]]
            MCP (Model Context Protocol) server configurations

        formatter : typing.Optional[ConfigFormatter]

        lsp : typing.Optional[ConfigLsp]

        instructions : typing.Optional[typing.Sequence[str]]
            Additional instruction files or patterns to include

        layout : typing.Optional[LayoutConfig]

        permission : typing.Optional[PermissionConfig]

        tools : typing.Optional[typing.Dict[str, bool]]

        enterprise : typing.Optional[ConfigEnterprise]

        compaction : typing.Optional[ConfigCompaction]

        experimental : typing.Optional[ConfigExperimental]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Successfully updated config

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.config_update()
        """
        _response = self._raw_client.config_update(
            directory=directory,
            schema=schema,
            theme=theme,
            keybinds=keybinds,
            log_level=log_level,
            tui=tui,
            server=server,
            command=command,
            skills=skills,
            watcher=watcher,
            plugin=plugin,
            snapshot=snapshot,
            share=share,
            autoshare=autoshare,
            autoupdate=autoupdate,
            disabled_providers=disabled_providers,
            enabled_providers=enabled_providers,
            model=model,
            small_model=small_model,
            default_agent=default_agent,
            username=username,
            mode=mode,
            agent=agent,
            provider=provider,
            mcp=mcp,
            formatter=formatter,
            lsp=lsp,
            instructions=instructions,
            layout=layout,
            permission=permission,
            tools=tools,
            enterprise=enterprise,
            compaction=compaction,
            experimental=experimental,
            request_options=request_options,
        )
        return _response.data

    def config_providers(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigProvidersResponse:
        """
        Get a list of all configured AI providers and their default models.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigProvidersResponse
            List of providers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.config_providers()
        """
        _response = self._raw_client.config_providers(directory=directory, request_options=request_options)
        return _response.data

    def tool_ids(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolIDs:
        """
        Get a list of all available tool IDs, including both built-in tools and dynamically registered tools.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolIDs
            Tool IDs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tool_ids()
        """
        _response = self._raw_client.tool_ids(directory=directory, request_options=request_options)
        return _response.data

    def tool_list(
        self,
        *,
        provider: str,
        model: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolList:
        """
        Get a list of available tools with their JSON schema parameters for a specific provider and model combination.

        Parameters
        ----------
        provider : str

        model : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolList
            Tools

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tool_list(
            provider="provider",
            model="model",
        )
        """
        _response = self._raw_client.tool_list(
            provider=provider, model=model, directory=directory, request_options=request_options
        )
        return _response.data

    def worktree_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        List all sandbox worktrees for the current project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of worktree directories

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.worktree_list()
        """
        _response = self._raw_client.worktree_list(directory=directory, request_options=request_options)
        return _response.data

    def worktree_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        start_command: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Worktree:
        """
        Create a new git worktree for the current project and run any configured startup scripts.

        Parameters
        ----------
        directory : typing.Optional[str]

        name : typing.Optional[str]

        start_command : typing.Optional[str]
            Additional startup script to run after the project's start command

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Worktree
            Worktree created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.worktree_create()
        """
        _response = self._raw_client.worktree_create(
            directory=directory, name=name, start_command=start_command, request_options=request_options
        )
        return _response.data

    def worktree_remove(
        self,
        *,
        worktree_remove_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Remove a git worktree and delete its branch.

        Parameters
        ----------
        worktree_remove_input_directory : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Worktree removed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.worktree_remove(
            worktree_remove_input_directory="directory",
        )
        """
        _response = self._raw_client.worktree_remove(
            worktree_remove_input_directory=worktree_remove_input_directory,
            directory=directory,
            request_options=request_options,
        )
        return _response.data

    def worktree_reset(
        self,
        *,
        worktree_reset_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Reset a worktree branch to the primary default branch.

        Parameters
        ----------
        worktree_reset_input_directory : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Worktree reset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.worktree_reset(
            worktree_reset_input_directory="directory",
        )
        """
        _response = self._raw_client.worktree_reset(
            worktree_reset_input_directory=worktree_reset_input_directory,
            directory=directory,
            request_options=request_options,
        )
        return _response.data

    def experimental_resource_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, McpResource]:
        """
        Get all available MCP resources from connected servers. Optionally filter by name.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, McpResource]
            MCP resources

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experimental_resource_list()
        """
        _response = self._raw_client.experimental_resource_list(directory=directory, request_options=request_options)
        return _response.data

    def session_list(
        self,
        *,
        directory: typing.Optional[str] = None,
        roots: typing.Optional[bool] = None,
        start: typing.Optional[float] = None,
        search: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Session]:
        """
        Get a list of all OpenCode sessions, sorted by most recently updated.

        Parameters
        ----------
        directory : typing.Optional[str]
            Filter sessions by project directory

        roots : typing.Optional[bool]
            Only return root sessions (no parentID)

        start : typing.Optional[float]
            Filter sessions updated on or after this timestamp (milliseconds since epoch)

        search : typing.Optional[str]
            Filter sessions by title (case-insensitive)

        limit : typing.Optional[float]
            Maximum number of sessions to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Session]
            List of sessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_list()
        """
        _response = self._raw_client.session_list(
            directory=directory, roots=roots, start=start, search=search, limit=limit, request_options=request_options
        )
        return _response.data

    def session_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        permission: typing.Optional[PermissionRuleset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Create a new OpenCode session for interacting with AI assistants and managing conversations.

        Parameters
        ----------
        directory : typing.Optional[str]

        parent_id : typing.Optional[str]

        title : typing.Optional[str]

        permission : typing.Optional[PermissionRuleset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully created session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_create()
        """
        _response = self._raw_client.session_create(
            directory=directory,
            parent_id=parent_id,
            title=title,
            permission=permission,
            request_options=request_options,
        )
        return _response.data

    def session_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, SessionStatus]:
        """
        Retrieve the current status of all sessions, including active, idle, and completed states.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, SessionStatus]
            Get session status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_status()
        """
        _response = self._raw_client.session_status(directory=directory, request_options=request_options)
        return _response.data

    def session_delete(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Delete a session and permanently remove all associated data, including messages and history.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully deleted session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_delete(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_delete(session_id, directory=directory, request_options=request_options)
        return _response.data

    def session_update(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        time: typing.Optional[SessionUpdateRequestTime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Update properties of an existing session, such as title or other metadata.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        title : typing.Optional[str]

        time : typing.Optional[SessionUpdateRequestTime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully updated session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_update(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_update(
            session_id, directory=directory, title=title, time=time, request_options=request_options
        )
        return _response.data

    def session_todo(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Todo]:
        """
        Retrieve the todo list associated with a specific session, showing tasks and action items.

        Parameters
        ----------
        session_id : str
            Session ID

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Todo]
            Todo list

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_todo(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_todo(session_id, directory=directory, request_options=request_options)
        return _response.data

    def session_init(
        self,
        session_id: str,
        *,
        model_id: str,
        provider_id: str,
        message_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Analyze the current application and create an AGENTS.md file with project-specific agent configurations.

        Parameters
        ----------
        session_id : str
            Session ID

        model_id : str

        provider_id : str

        message_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_init(
            session_id="sessionID",
            model_id="modelID",
            provider_id="providerID",
            message_id="messageID",
        )
        """
        _response = self._raw_client.session_init(
            session_id,
            model_id=model_id,
            provider_id=provider_id,
            message_id=message_id,
            directory=directory,
            request_options=request_options,
        )
        return _response.data

    def session_fork(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Create a new session by forking an existing session at a specific message point.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_fork(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_fork(
            session_id, directory=directory, message_id=message_id, request_options=request_options
        )
        return _response.data

    def session_abort(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Abort an active session and stop any ongoing AI processing or command execution.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Aborted session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_abort(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_abort(session_id, directory=directory, request_options=request_options)
        return _response.data

    def session_share(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Create a shareable link for a session, allowing others to view the conversation.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully shared session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_share(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_share(session_id, directory=directory, request_options=request_options)
        return _response.data

    def session_unshare(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Remove the shareable link for a session, making it private again.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully unshared session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_unshare(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_unshare(session_id, directory=directory, request_options=request_options)
        return _response.data

    def session_diff(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileDiff]:
        """
        Get the file changes (diff) that resulted from a specific user message in the session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileDiff]
            Successfully retrieved diff

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_diff(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_diff(
            session_id, directory=directory, message_id=message_id, request_options=request_options
        )
        return _response.data

    def session_summarize(
        self,
        session_id: str,
        *,
        provider_id: str,
        model_id: str,
        directory: typing.Optional[str] = None,
        auto: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Generate a concise summary of the session using AI compaction to preserve key information.

        Parameters
        ----------
        session_id : str
            Session ID

        provider_id : str

        model_id : str

        directory : typing.Optional[str]

        auto : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Summarized session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_summarize(
            session_id="sessionID",
            provider_id="providerID",
            model_id="modelID",
        )
        """
        _response = self._raw_client.session_summarize(
            session_id,
            provider_id=provider_id,
            model_id=model_id,
            directory=directory,
            auto=auto,
            request_options=request_options,
        )
        return _response.data

    def session_messages(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SessionMessagesResponseItem]:
        """
        Retrieve all messages in a session, including user prompts and AI responses.

        Parameters
        ----------
        session_id : str
            Session ID

        directory : typing.Optional[str]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SessionMessagesResponseItem]
            List of messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_messages(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_messages(
            session_id, directory=directory, limit=limit, request_options=request_options
        )
        return _response.data

    def session_prompt(
        self,
        session_id: str,
        *,
        parts: typing.Sequence[SessionPromptRequestPartsItem],
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        model: typing.Optional[SessionPromptRequestModel] = OMIT,
        agent: typing.Optional[str] = OMIT,
        no_reply: typing.Optional[bool] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        system: typing.Optional[str] = OMIT,
        variant: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionPromptResponse:
        """
        Create and send a new message to a session, streaming the AI response.

        Parameters
        ----------
        session_id : str
            Session ID

        parts : typing.Sequence[SessionPromptRequestPartsItem]

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        model : typing.Optional[SessionPromptRequestModel]

        agent : typing.Optional[str]

        no_reply : typing.Optional[bool]

        tools : typing.Optional[typing.Dict[str, bool]]
            @deprecated tools and permissions have been merged, you can set permissions on the session itself now

        system : typing.Optional[str]

        variant : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionPromptResponse
            Created message

        Examples
        --------
        from fern import FernApi, SessionPromptRequestPartsItem_Text

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_prompt(
            session_id="sessionID",
            parts=[
                SessionPromptRequestPartsItem_Text(
                    text="text",
                )
            ],
        )
        """
        _response = self._raw_client.session_prompt(
            session_id,
            parts=parts,
            directory=directory,
            message_id=message_id,
            model=model,
            agent=agent,
            no_reply=no_reply,
            tools=tools,
            system=system,
            variant=variant,
            request_options=request_options,
        )
        return _response.data

    def session_message(
        self,
        session_id: str,
        message_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionMessageResponse:
        """
        Retrieve a specific message from a session by its message ID.

        Parameters
        ----------
        session_id : str
            Session ID

        message_id : str
            Message ID

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionMessageResponse
            Message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_message(
            session_id="sessionID",
            message_id="messageID",
        )
        """
        _response = self._raw_client.session_message(
            session_id, message_id, directory=directory, request_options=request_options
        )
        return _response.data

    def part_delete(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Delete a part from a message

        Parameters
        ----------
        session_id : str
            Session ID

        message_id : str
            Message ID

        part_id : str
            Part ID

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully deleted part

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.part_delete(
            session_id="sessionID",
            message_id="messageID",
            part_id="partID",
        )
        """
        _response = self._raw_client.part_delete(
            session_id, message_id, part_id, directory=directory, request_options=request_options
        )
        return _response.data

    def part_update(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        request: Part,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Part:
        """
        Update a part in a message

        Parameters
        ----------
        session_id : str
            Session ID

        message_id : str
            Message ID

        part_id : str
            Part ID

        request : Part

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Part
            Successfully updated part

        Examples
        --------
        from fern import FernApi, Part_Text

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.part_update(
            session_id="sessionID",
            message_id="messageID",
            part_id="partID",
            request=Part_Text(
                id="id",
                session_id="sessionID",
                message_id="messageID",
                text="text",
            ),
        )
        """
        _response = self._raw_client.part_update(
            session_id, message_id, part_id, request=request, directory=directory, request_options=request_options
        )
        return _response.data

    def session_prompt_async(
        self,
        session_id: str,
        *,
        parts: typing.Sequence[SessionPromptAsyncRequestPartsItem],
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        model: typing.Optional[SessionPromptAsyncRequestModel] = OMIT,
        agent: typing.Optional[str] = OMIT,
        no_reply: typing.Optional[bool] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        system: typing.Optional[str] = OMIT,
        variant: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create and send a new message to a session asynchronously, starting the session if needed and returning immediately.

        Parameters
        ----------
        session_id : str
            Session ID

        parts : typing.Sequence[SessionPromptAsyncRequestPartsItem]

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        model : typing.Optional[SessionPromptAsyncRequestModel]

        agent : typing.Optional[str]

        no_reply : typing.Optional[bool]

        tools : typing.Optional[typing.Dict[str, bool]]
            @deprecated tools and permissions have been merged, you can set permissions on the session itself now

        system : typing.Optional[str]

        variant : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, SessionPromptAsyncRequestPartsItem_Text

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_prompt_async(
            session_id="sessionID",
            parts=[
                SessionPromptAsyncRequestPartsItem_Text(
                    text="text",
                )
            ],
        )
        """
        _response = self._raw_client.session_prompt_async(
            session_id,
            parts=parts,
            directory=directory,
            message_id=message_id,
            model=model,
            agent=agent,
            no_reply=no_reply,
            tools=tools,
            system=system,
            variant=variant,
            request_options=request_options,
        )
        return _response.data

    def session_command(
        self,
        session_id: str,
        *,
        arguments: str,
        command: str,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        agent: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        variant: typing.Optional[str] = OMIT,
        parts: typing.Optional[typing.Sequence[SessionCommandRequestPartsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionCommandResponse:
        """
        Send a new command to a session for execution by the AI assistant.

        Parameters
        ----------
        session_id : str
            Session ID

        arguments : str

        command : str

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        agent : typing.Optional[str]

        model : typing.Optional[str]

        variant : typing.Optional[str]

        parts : typing.Optional[typing.Sequence[SessionCommandRequestPartsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionCommandResponse
            Created message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_command(
            session_id="sessionID",
            arguments="arguments",
            command="command",
        )
        """
        _response = self._raw_client.session_command(
            session_id,
            arguments=arguments,
            command=command,
            directory=directory,
            message_id=message_id,
            agent=agent,
            model=model,
            variant=variant,
            parts=parts,
            request_options=request_options,
        )
        return _response.data

    def session_shell(
        self,
        session_id: str,
        *,
        agent: str,
        command: str,
        directory: typing.Optional[str] = None,
        model: typing.Optional[SessionShellRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssistantMessage:
        """
        Execute a shell command within the session context and return the AI's response.

        Parameters
        ----------
        session_id : str
            Session ID

        agent : str

        command : str

        directory : typing.Optional[str]

        model : typing.Optional[SessionShellRequestModel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssistantMessage
            Created message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_shell(
            session_id="sessionID",
            agent="agent",
            command="command",
        )
        """
        _response = self._raw_client.session_shell(
            session_id, agent=agent, command=command, directory=directory, model=model, request_options=request_options
        )
        return _response.data

    def session_revert(
        self,
        session_id: str,
        *,
        message_id: str,
        directory: typing.Optional[str] = None,
        part_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Revert a specific message in a session, undoing its effects and restoring the previous state.

        Parameters
        ----------
        session_id : str

        message_id : str

        directory : typing.Optional[str]

        part_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Updated session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_revert(
            session_id="sessionID",
            message_id="messageID",
        )
        """
        _response = self._raw_client.session_revert(
            session_id, message_id=message_id, directory=directory, part_id=part_id, request_options=request_options
        )
        return _response.data

    def session_unrevert(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Restore all previously reverted messages in a session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Updated session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session_unrevert(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.session_unrevert(session_id, directory=directory, request_options=request_options)
        return _response.data

    def permission_respond(
        self,
        session_id: str,
        permission_id: str,
        *,
        response: PermissionRespondRequestResponse,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Approve or deny a permission request from the AI assistant.

        Parameters
        ----------
        session_id : str

        permission_id : str

        response : PermissionRespondRequestResponse

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Permission processed successfully

        Examples
        --------
        from fern import FernApi, PermissionRespondRequestResponse

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.permission_respond(
            session_id="sessionID",
            permission_id="permissionID",
            response=PermissionRespondRequestResponse.ONCE,
        )
        """
        _response = self._raw_client.permission_respond(
            session_id, permission_id, response=response, directory=directory, request_options=request_options
        )
        return _response.data

    def permission_reply(
        self,
        request_id: str,
        *,
        reply: PermissionReplyRequestReply,
        directory: typing.Optional[str] = None,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Approve or deny a permission request from the AI assistant.

        Parameters
        ----------
        request_id : str

        reply : PermissionReplyRequestReply

        directory : typing.Optional[str]

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Permission processed successfully

        Examples
        --------
        from fern import FernApi, PermissionReplyRequestReply

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.permission_reply(
            request_id="requestID",
            reply=PermissionReplyRequestReply.ONCE,
        )
        """
        _response = self._raw_client.permission_reply(
            request_id, reply=reply, directory=directory, message=message, request_options=request_options
        )
        return _response.data

    def permission_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PermissionRequest]:
        """
        Get all pending permission requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PermissionRequest]
            List of pending permissions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.permission_list()
        """
        _response = self._raw_client.permission_list(directory=directory, request_options=request_options)
        return _response.data

    def question_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QuestionRequest]:
        """
        Get all pending question requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QuestionRequest]
            List of pending questions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.question_list()
        """
        _response = self._raw_client.question_list(directory=directory, request_options=request_options)
        return _response.data

    def question_reply(
        self,
        request_id: str,
        *,
        answers: typing.Sequence[QuestionAnswer],
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Provide answers to a question request from the AI assistant.

        Parameters
        ----------
        request_id : str

        answers : typing.Sequence[QuestionAnswer]
            User answers in order of questions (each answer is an array of selected labels)

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Question answered successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.question_reply(
            request_id="requestID",
            answers=[["answers"]],
        )
        """
        _response = self._raw_client.question_reply(
            request_id, answers=answers, directory=directory, request_options=request_options
        )
        return _response.data

    def question_reject(
        self,
        request_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Reject a question request from the AI assistant.

        Parameters
        ----------
        request_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Question rejected successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.question_reject(
            request_id="requestID",
        )
        """
        _response = self._raw_client.question_reject(request_id, directory=directory, request_options=request_options)
        return _response.data

    def provider_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderListResponse:
        """
        Get a list of all available AI providers, including both available and connected ones.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderListResponse
            List of providers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_list()
        """
        _response = self._raw_client.provider_list(directory=directory, request_options=request_options)
        return _response.data

    def provider_auth(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.List[ProviderAuthMethod]]:
        """
        Retrieve available authentication methods for all AI providers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[ProviderAuthMethod]]
            Provider auth methods

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_auth()
        """
        _response = self._raw_client.provider_auth(directory=directory, request_options=request_options)
        return _response.data

    def provider_oauth_authorize(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderAuthAuthorization:
        """
        Initiate OAuth authorization for a specific AI provider to get an authorization URL.

        Parameters
        ----------
        provider_id : str
            Provider ID

        method : float
            Auth method index

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderAuthAuthorization
            Authorization URL and method

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_oauth_authorize(
            provider_id="providerID",
            method=1.1,
        )
        """
        _response = self._raw_client.provider_oauth_authorize(
            provider_id, method=method, directory=directory, request_options=request_options
        )
        return _response.data

    def provider_oauth_callback(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Handle the OAuth callback from a provider after user authorization.

        Parameters
        ----------
        provider_id : str
            Provider ID

        method : float
            Auth method index

        directory : typing.Optional[str]

        code : typing.Optional[str]
            OAuth authorization code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OAuth callback processed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_oauth_callback(
            provider_id="providerID",
            method=1.1,
        )
        """
        _response = self._raw_client.provider_oauth_callback(
            provider_id, method=method, directory=directory, code=code, request_options=request_options
        )
        return _response.data

    def find_text(
        self,
        *,
        pattern: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FindTextResponseItem]:
        """
        Search for text patterns across files in the project using ripgrep.

        Parameters
        ----------
        pattern : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FindTextResponseItem]
            Matches

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_text(
            pattern="pattern",
        )
        """
        _response = self._raw_client.find_text(pattern=pattern, directory=directory, request_options=request_options)
        return _response.data

    def find_files(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        dirs: typing.Optional[FindFilesRequestDirs] = None,
        type: typing.Optional[FindFilesRequestType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Search for files or directories by name or pattern in the project directory.

        Parameters
        ----------
        query : str

        directory : typing.Optional[str]

        dirs : typing.Optional[FindFilesRequestDirs]

        type : typing.Optional[FindFilesRequestType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            File paths

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_files(
            query="query",
        )
        """
        _response = self._raw_client.find_files(
            query=query, directory=directory, dirs=dirs, type=type, limit=limit, request_options=request_options
        )
        return _response.data

    def find_symbols(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Symbol]:
        """
        Search for workspace symbols like functions, classes, and variables using LSP.

        Parameters
        ----------
        query : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Symbol]
            Symbols

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_symbols(
            query="query",
        )
        """
        _response = self._raw_client.find_symbols(query=query, directory=directory, request_options=request_options)
        return _response.data

    def file_list(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileNode]:
        """
        List files and directories in a specified path.

        Parameters
        ----------
        path : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileNode]
            Files and directories

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.file_list(
            path="path",
        )
        """
        _response = self._raw_client.file_list(path=path, directory=directory, request_options=request_options)
        return _response.data

    def file_read(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileContent:
        """
        Read the content of a specified file.

        Parameters
        ----------
        path : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileContent
            File content

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.file_read(
            path="path",
        )
        """
        _response = self._raw_client.file_read(path=path, directory=directory, request_options=request_options)
        return _response.data

    def file_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[File]:
        """
        Get the git status of all files in the project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]
            File status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.file_status()
        """
        _response = self._raw_client.file_status(directory=directory, request_options=request_options)
        return _response.data

    def mcp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, McpStatus]:
        """
        Get the status of all Model Context Protocol (MCP) servers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, McpStatus]
            MCP server status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_status()
        """
        _response = self._raw_client.mcp_status(directory=directory, request_options=request_options)
        return _response.data

    def mcp_add(
        self,
        *,
        name: str,
        config: McpAddRequestConfig,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, McpStatus]:
        """
        Dynamically add a new Model Context Protocol (MCP) server to the system.

        Parameters
        ----------
        name : str

        config : McpAddRequestConfig

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, McpStatus]
            MCP server added successfully

        Examples
        --------
        from fern import FernApi, McpAddRequestConfig_Local

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_add(
            name="name",
            config=McpAddRequestConfig_Local(
                command=["command"],
            ),
        )
        """
        _response = self._raw_client.mcp_add(
            name=name, config=config, directory=directory, request_options=request_options
        )
        return _response.data

    def mcp_auth_start(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpAuthStartResponse:
        """
        Start OAuth authentication flow for a Model Context Protocol (MCP) server.

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpAuthStartResponse
            OAuth flow started

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_auth_start(
            name="name",
        )
        """
        _response = self._raw_client.mcp_auth_start(name, directory=directory, request_options=request_options)
        return _response.data

    def mcp_auth_remove(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpAuthRemoveResponse:
        """
        Remove OAuth credentials for an MCP server

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpAuthRemoveResponse
            OAuth credentials removed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_auth_remove(
            name="name",
        )
        """
        _response = self._raw_client.mcp_auth_remove(name, directory=directory, request_options=request_options)
        return _response.data

    def mcp_auth_callback(
        self,
        name: str,
        *,
        code: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpStatus:
        """
        Complete OAuth authentication for a Model Context Protocol (MCP) server using the authorization code.

        Parameters
        ----------
        name : str

        code : str
            Authorization code from OAuth callback

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpStatus
            OAuth authentication completed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_auth_callback(
            name="name",
            code="code",
        )
        """
        _response = self._raw_client.mcp_auth_callback(
            name, code=code, directory=directory, request_options=request_options
        )
        return _response.data

    def mcp_auth_authenticate(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpStatus:
        """
        Start OAuth flow and wait for callback (opens browser)

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpStatus
            OAuth authentication completed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_auth_authenticate(
            name="name",
        )
        """
        _response = self._raw_client.mcp_auth_authenticate(name, directory=directory, request_options=request_options)
        return _response.data

    def mcp_connect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Connect an MCP server

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            MCP server connected successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_connect(
            name="name",
        )
        """
        _response = self._raw_client.mcp_connect(name, directory=directory, request_options=request_options)
        return _response.data

    def mcp_disconnect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Disconnect an MCP server

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            MCP server disconnected successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_disconnect(
            name="name",
        )
        """
        _response = self._raw_client.mcp_disconnect(name, directory=directory, request_options=request_options)
        return _response.data

    def tui_append_prompt(
        self,
        *,
        text: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Append prompt to the TUI

        Parameters
        ----------
        text : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Prompt processed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_append_prompt(
            text="text",
        )
        """
        _response = self._raw_client.tui_append_prompt(text=text, directory=directory, request_options=request_options)
        return _response.data

    def tui_open_help(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the help dialog in the TUI to display user assistance information.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Help dialog opened successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_open_help()
        """
        _response = self._raw_client.tui_open_help(directory=directory, request_options=request_options)
        return _response.data

    def tui_open_sessions(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the session dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Session dialog opened successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_open_sessions()
        """
        _response = self._raw_client.tui_open_sessions(directory=directory, request_options=request_options)
        return _response.data

    def tui_open_themes(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the theme dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Theme dialog opened successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_open_themes()
        """
        _response = self._raw_client.tui_open_themes(directory=directory, request_options=request_options)
        return _response.data

    def tui_open_models(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the model dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Model dialog opened successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_open_models()
        """
        _response = self._raw_client.tui_open_models(directory=directory, request_options=request_options)
        return _response.data

    def tui_submit_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Submit the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Prompt submitted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_submit_prompt()
        """
        _response = self._raw_client.tui_submit_prompt(directory=directory, request_options=request_options)
        return _response.data

    def tui_clear_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clear the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Prompt cleared successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_clear_prompt()
        """
        _response = self._raw_client.tui_clear_prompt(directory=directory, request_options=request_options)
        return _response.data

    def tui_execute_command(
        self,
        *,
        command: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Execute a TUI command (e.g. agent_cycle)

        Parameters
        ----------
        command : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Command executed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_execute_command(
            command="command",
        )
        """
        _response = self._raw_client.tui_execute_command(
            command=command, directory=directory, request_options=request_options
        )
        return _response.data

    def tui_show_toast(
        self,
        *,
        message: str,
        variant: TuiShowToastRequestVariant,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        duration: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Show a toast notification in the TUI

        Parameters
        ----------
        message : str

        variant : TuiShowToastRequestVariant

        directory : typing.Optional[str]

        title : typing.Optional[str]

        duration : typing.Optional[float]
            Duration in milliseconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Toast notification shown successfully

        Examples
        --------
        from fern import FernApi, TuiShowToastRequestVariant

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_show_toast(
            message="message",
            variant=TuiShowToastRequestVariant.INFO,
        )
        """
        _response = self._raw_client.tui_show_toast(
            message=message,
            variant=variant,
            directory=directory,
            title=title,
            duration=duration,
            request_options=request_options,
        )
        return _response.data

    def tui_publish(
        self,
        *,
        request: TuiPublishRequestBody,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Publish a TUI event

        Parameters
        ----------
        request : TuiPublishRequestBody

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Event published successfully

        Examples
        --------
        from fern import (
            EventTuiPromptAppendProperties,
            FernApi,
            TuiPublishRequestBody_TuiPromptAppend,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_publish(
            request=TuiPublishRequestBody_TuiPromptAppend(
                properties=EventTuiPromptAppendProperties(
                    text="text",
                ),
            ),
        )
        """
        _response = self._raw_client.tui_publish(request=request, directory=directory, request_options=request_options)
        return _response.data

    def tui_select_session(
        self,
        *,
        session_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Navigate the TUI to display the specified session.

        Parameters
        ----------
        session_id : str
            Session ID to navigate to

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Session selected successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_select_session(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.tui_select_session(
            session_id=session_id, directory=directory, request_options=request_options
        )
        return _response.data

    def tui_control_next(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TuiControlNextResponse:
        """
        Retrieve the next TUI (Terminal User Interface) request from the queue for processing.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TuiControlNextResponse
            Next TUI request

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_control_next()
        """
        _response = self._raw_client.tui_control_next(directory=directory, request_options=request_options)
        return _response.data

    def tui_control_response(
        self,
        *,
        request: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Submit a response to the TUI request queue to complete a pending request.

        Parameters
        ----------
        request : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Response submitted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tui_control_response(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.tui_control_response(
            request=request, directory=directory, request_options=request_options
        )
        return _response.data

    def instance_dispose(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clean up and dispose the current OpenCode instance, releasing all resources.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Instance disposed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.instance_dispose()
        """
        _response = self._raw_client.instance_dispose(directory=directory, request_options=request_options)
        return _response.data

    def path_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Path:
        """
        Retrieve the current working directory and related path information for the OpenCode instance.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Path
            Path

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.path_get()
        """
        _response = self._raw_client.path_get(directory=directory, request_options=request_options)
        return _response.data

    def vcs_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> VcsInfo:
        """
        Retrieve version control system (VCS) information for the current project, such as git branch.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VcsInfo
            VCS info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.vcs_get()
        """
        _response = self._raw_client.vcs_get(directory=directory, request_options=request_options)
        return _response.data

    def command_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Command]:
        """
        Get a list of all available commands in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Command]
            List of commands

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.command_list()
        """
        _response = self._raw_client.command_list(directory=directory, request_options=request_options)
        return _response.data

    def app_log(
        self,
        *,
        service: str,
        level: AppLogRequestLevel,
        message: str,
        directory: typing.Optional[str] = None,
        extra: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Write a log entry to the server logs with specified level and metadata.

        Parameters
        ----------
        service : str
            Service name for the log entry

        level : AppLogRequestLevel
            Log level

        message : str
            Log message

        directory : typing.Optional[str]

        extra : typing.Optional[typing.Dict[str, typing.Any]]
            Additional metadata for the log entry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Log entry written successfully

        Examples
        --------
        from fern import AppLogRequestLevel, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.app_log(
            service="service",
            level=AppLogRequestLevel.DEBUG,
            message="message",
        )
        """
        _response = self._raw_client.app_log(
            service=service,
            level=level,
            message=message,
            directory=directory,
            extra=extra,
            request_options=request_options,
        )
        return _response.data

    def app_agents(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Agent]:
        """
        Get a list of all available AI agents in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Agent]
            List of agents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.app_agents()
        """
        _response = self._raw_client.app_agents(directory=directory, request_options=request_options)
        return _response.data

    def app_skills(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AppSkillsResponseItem]:
        """
        Get a list of all available skills in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AppSkillsResponseItem]
            List of skills

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.app_skills()
        """
        _response = self._raw_client.app_skills(directory=directory, request_options=request_options)
        return _response.data

    def lsp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LspStatus]:
        """
        Get LSP server status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LspStatus]
            LSP server status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lsp_status()
        """
        _response = self._raw_client.lsp_status(directory=directory, request_options=request_options)
        return _response.data

    def formatter_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FormatterStatus]:
        """
        Get formatter status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FormatterStatus]
            Formatter status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.formatter_status()
        """
        _response = self._raw_client.formatter_status(directory=directory, request_options=request_options)
        return _response.data

    def event_subscribe(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[Event]:
        """
        Get events

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[Event]
            Event stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.event_subscribe()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.event_subscribe(directory=directory, request_options=request_options) as r:
            yield from r.data

    @property
    def session(self):
        if self._session is None:
            from .session.client import SessionClient

            self._session = SessionClient(client_wrapper=self._client_wrapper)
        return self._session


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._session: typing.Optional[AsyncSessionClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def global_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalHealthResponse:
        """
        Get health information about the OpenCode server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalHealthResponse
            Health information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.global_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_health(request_options=request_options)
        return _response.data

    async def global_event(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[GlobalEvent]:
        """
        Subscribe to global events from the OpenCode system using server-sent events.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[GlobalEvent]
            Event stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.global_event()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.global_event(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def global_config_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Retrieve the current global OpenCode configuration settings and preferences.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Get global config info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.global_config_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_config_get(request_options=request_options)
        return _response.data

    async def global_config_update(
        self,
        *,
        schema: typing.Optional[str] = OMIT,
        theme: typing.Optional[str] = OMIT,
        keybinds: typing.Optional[KeybindsConfig] = OMIT,
        log_level: typing.Optional[LogLevel] = OMIT,
        tui: typing.Optional[ConfigTui] = OMIT,
        server: typing.Optional[ServerConfig] = OMIT,
        command: typing.Optional[typing.Dict[str, ConfigCommandValue]] = OMIT,
        skills: typing.Optional[ConfigSkills] = OMIT,
        watcher: typing.Optional[ConfigWatcher] = OMIT,
        plugin: typing.Optional[typing.Sequence[str]] = OMIT,
        snapshot: typing.Optional[bool] = OMIT,
        share: typing.Optional[ConfigShare] = OMIT,
        autoshare: typing.Optional[bool] = OMIT,
        autoupdate: typing.Optional[ConfigAutoupdate] = OMIT,
        disabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        model: typing.Optional[str] = OMIT,
        small_model: typing.Optional[str] = OMIT,
        default_agent: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        mode: typing.Optional[ConfigMode] = OMIT,
        agent: typing.Optional[ConfigAgent] = OMIT,
        provider: typing.Optional[typing.Dict[str, ProviderConfig]] = OMIT,
        mcp: typing.Optional[typing.Dict[str, ConfigMcpValue]] = OMIT,
        formatter: typing.Optional[ConfigFormatter] = OMIT,
        lsp: typing.Optional[ConfigLsp] = OMIT,
        instructions: typing.Optional[typing.Sequence[str]] = OMIT,
        layout: typing.Optional[LayoutConfig] = OMIT,
        permission: typing.Optional[PermissionConfig] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        enterprise: typing.Optional[ConfigEnterprise] = OMIT,
        compaction: typing.Optional[ConfigCompaction] = OMIT,
        experimental: typing.Optional[ConfigExperimental] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Config:
        """
        Update global OpenCode configuration settings and preferences.

        Parameters
        ----------
        schema : typing.Optional[str]
            JSON schema reference for configuration validation

        theme : typing.Optional[str]
            Theme name to use for the interface

        keybinds : typing.Optional[KeybindsConfig]

        log_level : typing.Optional[LogLevel]

        tui : typing.Optional[ConfigTui]
            TUI specific settings

        server : typing.Optional[ServerConfig]

        command : typing.Optional[typing.Dict[str, ConfigCommandValue]]
            Command configuration, see https://opencode.ai/docs/commands

        skills : typing.Optional[ConfigSkills]
            Additional skill folder paths

        watcher : typing.Optional[ConfigWatcher]

        plugin : typing.Optional[typing.Sequence[str]]

        snapshot : typing.Optional[bool]

        share : typing.Optional[ConfigShare]
            Control sharing behavior:'manual' allows manual sharing via commands, 'auto' enables automatic sharing, 'disabled' disables all sharing

        autoshare : typing.Optional[bool]
            @deprecated Use 'share' field instead. Share newly created sessions automatically

        autoupdate : typing.Optional[ConfigAutoupdate]
            Automatically update to the latest version. Set to true to auto-update, false to disable, or 'notify' to show update notifications

        disabled_providers : typing.Optional[typing.Sequence[str]]
            Disable providers that are loaded automatically

        enabled_providers : typing.Optional[typing.Sequence[str]]
            When set, ONLY these providers will be enabled. All other providers will be ignored

        model : typing.Optional[str]
            Model to use in the format of provider/model, eg anthropic/claude-2

        small_model : typing.Optional[str]
            Small model to use for tasks like title generation in the format of provider/model

        default_agent : typing.Optional[str]
            Default agent to use when none is specified. Must be a primary agent. Falls back to 'build' if not set or if the specified agent is invalid.

        username : typing.Optional[str]
            Custom username to display in conversations instead of system username

        mode : typing.Optional[ConfigMode]
            @deprecated Use `agent` field instead.

        agent : typing.Optional[ConfigAgent]
            Agent configuration, see https://opencode.ai/docs/agents

        provider : typing.Optional[typing.Dict[str, ProviderConfig]]
            Custom provider configurations and model overrides

        mcp : typing.Optional[typing.Dict[str, ConfigMcpValue]]
            MCP (Model Context Protocol) server configurations

        formatter : typing.Optional[ConfigFormatter]

        lsp : typing.Optional[ConfigLsp]

        instructions : typing.Optional[typing.Sequence[str]]
            Additional instruction files or patterns to include

        layout : typing.Optional[LayoutConfig]

        permission : typing.Optional[PermissionConfig]

        tools : typing.Optional[typing.Dict[str, bool]]

        enterprise : typing.Optional[ConfigEnterprise]

        compaction : typing.Optional[ConfigCompaction]

        experimental : typing.Optional[ConfigExperimental]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Successfully updated global config

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.global_config_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_config_update(
            schema=schema,
            theme=theme,
            keybinds=keybinds,
            log_level=log_level,
            tui=tui,
            server=server,
            command=command,
            skills=skills,
            watcher=watcher,
            plugin=plugin,
            snapshot=snapshot,
            share=share,
            autoshare=autoshare,
            autoupdate=autoupdate,
            disabled_providers=disabled_providers,
            enabled_providers=enabled_providers,
            model=model,
            small_model=small_model,
            default_agent=default_agent,
            username=username,
            mode=mode,
            agent=agent,
            provider=provider,
            mcp=mcp,
            formatter=formatter,
            lsp=lsp,
            instructions=instructions,
            layout=layout,
            permission=permission,
            tools=tools,
            enterprise=enterprise,
            compaction=compaction,
            experimental=experimental,
            request_options=request_options,
        )
        return _response.data

    async def global_dispose(self, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Clean up and dispose all OpenCode instances, releasing all resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Global disposed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.global_dispose()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_dispose(request_options=request_options)
        return _response.data

    async def auth_set(
        self, provider_id: str, *, request: Auth, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Set authentication credentials

        Parameters
        ----------
        provider_id : str

        request : Auth

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully set authentication credentials

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Auth_Oauth

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth_set(
                provider_id="providerID",
                request=Auth_Oauth(
                    refresh="refresh",
                    access="access",
                    expires=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_set(provider_id, request=request, request_options=request_options)
        return _response.data

    async def auth_remove(self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Remove authentication credentials

        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully removed authentication credentials

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth_remove(
                provider_id="providerID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_remove(provider_id, request_options=request_options)
        return _response.data

    async def project_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Project]:
        """
        Get a list of projects that have been opened with OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Project]
            List of projects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.project_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.project_list(directory=directory, request_options=request_options)
        return _response.data

    async def project_current(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Retrieve the currently active project that OpenCode is working with.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Current project information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.project_current()


        asyncio.run(main())
        """
        _response = await self._raw_client.project_current(directory=directory, request_options=request_options)
        return _response.data

    async def project_update(
        self,
        project_id: str,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[ProjectUpdateRequestIcon] = OMIT,
        commands: typing.Optional[ProjectUpdateRequestCommands] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Project:
        """
        Update project properties such as name, icon, and commands.

        Parameters
        ----------
        project_id : str

        directory : typing.Optional[str]

        name : typing.Optional[str]

        icon : typing.Optional[ProjectUpdateRequestIcon]

        commands : typing.Optional[ProjectUpdateRequestCommands]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Updated project information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.project_update(
                project_id="projectID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.project_update(
            project_id, directory=directory, name=name, icon=icon, commands=commands, request_options=request_options
        )
        return _response.data

    async def pty_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Pty]:
        """
        Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Pty]
            List of sessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pty_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.pty_list(directory=directory, request_options=request_options)
        return _response.data

    async def pty_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        command: typing.Optional[str] = OMIT,
        args: typing.Optional[typing.Sequence[str]] = OMIT,
        cwd: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        env: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pty:
        """
        Create a new pseudo-terminal (PTY) session for running shell commands and processes.

        Parameters
        ----------
        directory : typing.Optional[str]

        command : typing.Optional[str]

        args : typing.Optional[typing.Sequence[str]]

        cwd : typing.Optional[str]

        title : typing.Optional[str]

        env : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pty
            Created session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pty_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.pty_create(
            directory=directory,
            command=command,
            args=args,
            cwd=cwd,
            title=title,
            env=env,
            request_options=request_options,
        )
        return _response.data

    async def pty_get(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pty:
        """
        Retrieve detailed information about a specific pseudo-terminal (PTY) session.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pty
            Session info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pty_get(
                pty_id="ptyID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pty_get(pty_id, directory=directory, request_options=request_options)
        return _response.data

    async def pty_update(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        size: typing.Optional[PtyUpdateRequestSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pty:
        """
        Update properties of an existing pseudo-terminal (PTY) session.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        title : typing.Optional[str]

        size : typing.Optional[PtyUpdateRequestSize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pty
            Updated session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pty_update(
                pty_id="ptyID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pty_update(
            pty_id, directory=directory, title=title, size=size, request_options=request_options
        )
        return _response.data

    async def pty_remove(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Remove and terminate a specific pseudo-terminal (PTY) session.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Session removed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pty_remove(
                pty_id="ptyID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pty_remove(pty_id, directory=directory, request_options=request_options)
        return _response.data

    async def pty_connect(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Establish a WebSocket connection to interact with a pseudo-terminal (PTY) session in real-time.

        Parameters
        ----------
        pty_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Connected session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pty_connect(
                pty_id="ptyID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pty_connect(pty_id, directory=directory, request_options=request_options)
        return _response.data

    async def config_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Config:
        """
        Retrieve the current OpenCode configuration settings and preferences.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Get config info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.config_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.config_get(directory=directory, request_options=request_options)
        return _response.data

    async def config_update(
        self,
        *,
        directory: typing.Optional[str] = None,
        schema: typing.Optional[str] = OMIT,
        theme: typing.Optional[str] = OMIT,
        keybinds: typing.Optional[KeybindsConfig] = OMIT,
        log_level: typing.Optional[LogLevel] = OMIT,
        tui: typing.Optional[ConfigTui] = OMIT,
        server: typing.Optional[ServerConfig] = OMIT,
        command: typing.Optional[typing.Dict[str, ConfigCommandValue]] = OMIT,
        skills: typing.Optional[ConfigSkills] = OMIT,
        watcher: typing.Optional[ConfigWatcher] = OMIT,
        plugin: typing.Optional[typing.Sequence[str]] = OMIT,
        snapshot: typing.Optional[bool] = OMIT,
        share: typing.Optional[ConfigShare] = OMIT,
        autoshare: typing.Optional[bool] = OMIT,
        autoupdate: typing.Optional[ConfigAutoupdate] = OMIT,
        disabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled_providers: typing.Optional[typing.Sequence[str]] = OMIT,
        model: typing.Optional[str] = OMIT,
        small_model: typing.Optional[str] = OMIT,
        default_agent: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        mode: typing.Optional[ConfigMode] = OMIT,
        agent: typing.Optional[ConfigAgent] = OMIT,
        provider: typing.Optional[typing.Dict[str, ProviderConfig]] = OMIT,
        mcp: typing.Optional[typing.Dict[str, ConfigMcpValue]] = OMIT,
        formatter: typing.Optional[ConfigFormatter] = OMIT,
        lsp: typing.Optional[ConfigLsp] = OMIT,
        instructions: typing.Optional[typing.Sequence[str]] = OMIT,
        layout: typing.Optional[LayoutConfig] = OMIT,
        permission: typing.Optional[PermissionConfig] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        enterprise: typing.Optional[ConfigEnterprise] = OMIT,
        compaction: typing.Optional[ConfigCompaction] = OMIT,
        experimental: typing.Optional[ConfigExperimental] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Config:
        """
        Update OpenCode configuration settings and preferences.

        Parameters
        ----------
        directory : typing.Optional[str]

        schema : typing.Optional[str]
            JSON schema reference for configuration validation

        theme : typing.Optional[str]
            Theme name to use for the interface

        keybinds : typing.Optional[KeybindsConfig]

        log_level : typing.Optional[LogLevel]

        tui : typing.Optional[ConfigTui]
            TUI specific settings

        server : typing.Optional[ServerConfig]

        command : typing.Optional[typing.Dict[str, ConfigCommandValue]]
            Command configuration, see https://opencode.ai/docs/commands

        skills : typing.Optional[ConfigSkills]
            Additional skill folder paths

        watcher : typing.Optional[ConfigWatcher]

        plugin : typing.Optional[typing.Sequence[str]]

        snapshot : typing.Optional[bool]

        share : typing.Optional[ConfigShare]
            Control sharing behavior:'manual' allows manual sharing via commands, 'auto' enables automatic sharing, 'disabled' disables all sharing

        autoshare : typing.Optional[bool]
            @deprecated Use 'share' field instead. Share newly created sessions automatically

        autoupdate : typing.Optional[ConfigAutoupdate]
            Automatically update to the latest version. Set to true to auto-update, false to disable, or 'notify' to show update notifications

        disabled_providers : typing.Optional[typing.Sequence[str]]
            Disable providers that are loaded automatically

        enabled_providers : typing.Optional[typing.Sequence[str]]
            When set, ONLY these providers will be enabled. All other providers will be ignored

        model : typing.Optional[str]
            Model to use in the format of provider/model, eg anthropic/claude-2

        small_model : typing.Optional[str]
            Small model to use for tasks like title generation in the format of provider/model

        default_agent : typing.Optional[str]
            Default agent to use when none is specified. Must be a primary agent. Falls back to 'build' if not set or if the specified agent is invalid.

        username : typing.Optional[str]
            Custom username to display in conversations instead of system username

        mode : typing.Optional[ConfigMode]
            @deprecated Use `agent` field instead.

        agent : typing.Optional[ConfigAgent]
            Agent configuration, see https://opencode.ai/docs/agents

        provider : typing.Optional[typing.Dict[str, ProviderConfig]]
            Custom provider configurations and model overrides

        mcp : typing.Optional[typing.Dict[str, ConfigMcpValue]]
            MCP (Model Context Protocol) server configurations

        formatter : typing.Optional[ConfigFormatter]

        lsp : typing.Optional[ConfigLsp]

        instructions : typing.Optional[typing.Sequence[str]]
            Additional instruction files or patterns to include

        layout : typing.Optional[LayoutConfig]

        permission : typing.Optional[PermissionConfig]

        tools : typing.Optional[typing.Dict[str, bool]]

        enterprise : typing.Optional[ConfigEnterprise]

        compaction : typing.Optional[ConfigCompaction]

        experimental : typing.Optional[ConfigExperimental]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Successfully updated config

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.config_update()


        asyncio.run(main())
        """
        _response = await self._raw_client.config_update(
            directory=directory,
            schema=schema,
            theme=theme,
            keybinds=keybinds,
            log_level=log_level,
            tui=tui,
            server=server,
            command=command,
            skills=skills,
            watcher=watcher,
            plugin=plugin,
            snapshot=snapshot,
            share=share,
            autoshare=autoshare,
            autoupdate=autoupdate,
            disabled_providers=disabled_providers,
            enabled_providers=enabled_providers,
            model=model,
            small_model=small_model,
            default_agent=default_agent,
            username=username,
            mode=mode,
            agent=agent,
            provider=provider,
            mcp=mcp,
            formatter=formatter,
            lsp=lsp,
            instructions=instructions,
            layout=layout,
            permission=permission,
            tools=tools,
            enterprise=enterprise,
            compaction=compaction,
            experimental=experimental,
            request_options=request_options,
        )
        return _response.data

    async def config_providers(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigProvidersResponse:
        """
        Get a list of all configured AI providers and their default models.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigProvidersResponse
            List of providers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.config_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.config_providers(directory=directory, request_options=request_options)
        return _response.data

    async def tool_ids(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolIDs:
        """
        Get a list of all available tool IDs, including both built-in tools and dynamically registered tools.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolIDs
            Tool IDs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tool_ids()


        asyncio.run(main())
        """
        _response = await self._raw_client.tool_ids(directory=directory, request_options=request_options)
        return _response.data

    async def tool_list(
        self,
        *,
        provider: str,
        model: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolList:
        """
        Get a list of available tools with their JSON schema parameters for a specific provider and model combination.

        Parameters
        ----------
        provider : str

        model : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolList
            Tools

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tool_list(
                provider="provider",
                model="model",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tool_list(
            provider=provider, model=model, directory=directory, request_options=request_options
        )
        return _response.data

    async def worktree_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        List all sandbox worktrees for the current project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of worktree directories

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.worktree_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.worktree_list(directory=directory, request_options=request_options)
        return _response.data

    async def worktree_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        start_command: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Worktree:
        """
        Create a new git worktree for the current project and run any configured startup scripts.

        Parameters
        ----------
        directory : typing.Optional[str]

        name : typing.Optional[str]

        start_command : typing.Optional[str]
            Additional startup script to run after the project's start command

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Worktree
            Worktree created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.worktree_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.worktree_create(
            directory=directory, name=name, start_command=start_command, request_options=request_options
        )
        return _response.data

    async def worktree_remove(
        self,
        *,
        worktree_remove_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Remove a git worktree and delete its branch.

        Parameters
        ----------
        worktree_remove_input_directory : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Worktree removed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.worktree_remove(
                worktree_remove_input_directory="directory",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.worktree_remove(
            worktree_remove_input_directory=worktree_remove_input_directory,
            directory=directory,
            request_options=request_options,
        )
        return _response.data

    async def worktree_reset(
        self,
        *,
        worktree_reset_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Reset a worktree branch to the primary default branch.

        Parameters
        ----------
        worktree_reset_input_directory : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Worktree reset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.worktree_reset(
                worktree_reset_input_directory="directory",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.worktree_reset(
            worktree_reset_input_directory=worktree_reset_input_directory,
            directory=directory,
            request_options=request_options,
        )
        return _response.data

    async def experimental_resource_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, McpResource]:
        """
        Get all available MCP resources from connected servers. Optionally filter by name.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, McpResource]
            MCP resources

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experimental_resource_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.experimental_resource_list(
            directory=directory, request_options=request_options
        )
        return _response.data

    async def session_list(
        self,
        *,
        directory: typing.Optional[str] = None,
        roots: typing.Optional[bool] = None,
        start: typing.Optional[float] = None,
        search: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Session]:
        """
        Get a list of all OpenCode sessions, sorted by most recently updated.

        Parameters
        ----------
        directory : typing.Optional[str]
            Filter sessions by project directory

        roots : typing.Optional[bool]
            Only return root sessions (no parentID)

        start : typing.Optional[float]
            Filter sessions updated on or after this timestamp (milliseconds since epoch)

        search : typing.Optional[str]
            Filter sessions by title (case-insensitive)

        limit : typing.Optional[float]
            Maximum number of sessions to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Session]
            List of sessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.session_list(
            directory=directory, roots=roots, start=start, search=search, limit=limit, request_options=request_options
        )
        return _response.data

    async def session_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        permission: typing.Optional[PermissionRuleset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Create a new OpenCode session for interacting with AI assistants and managing conversations.

        Parameters
        ----------
        directory : typing.Optional[str]

        parent_id : typing.Optional[str]

        title : typing.Optional[str]

        permission : typing.Optional[PermissionRuleset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully created session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.session_create(
            directory=directory,
            parent_id=parent_id,
            title=title,
            permission=permission,
            request_options=request_options,
        )
        return _response.data

    async def session_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, SessionStatus]:
        """
        Retrieve the current status of all sessions, including active, idle, and completed states.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, SessionStatus]
            Get session status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.session_status(directory=directory, request_options=request_options)
        return _response.data

    async def session_delete(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Delete a session and permanently remove all associated data, including messages and history.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully deleted session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_delete(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_delete(
            session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def session_update(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        time: typing.Optional[SessionUpdateRequestTime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Update properties of an existing session, such as title or other metadata.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        title : typing.Optional[str]

        time : typing.Optional[SessionUpdateRequestTime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully updated session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_update(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_update(
            session_id, directory=directory, title=title, time=time, request_options=request_options
        )
        return _response.data

    async def session_todo(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Todo]:
        """
        Retrieve the todo list associated with a specific session, showing tasks and action items.

        Parameters
        ----------
        session_id : str
            Session ID

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Todo]
            Todo list

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_todo(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_todo(
            session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def session_init(
        self,
        session_id: str,
        *,
        model_id: str,
        provider_id: str,
        message_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Analyze the current application and create an AGENTS.md file with project-specific agent configurations.

        Parameters
        ----------
        session_id : str
            Session ID

        model_id : str

        provider_id : str

        message_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_init(
                session_id="sessionID",
                model_id="modelID",
                provider_id="providerID",
                message_id="messageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_init(
            session_id,
            model_id=model_id,
            provider_id=provider_id,
            message_id=message_id,
            directory=directory,
            request_options=request_options,
        )
        return _response.data

    async def session_fork(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Create a new session by forking an existing session at a specific message point.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_fork(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_fork(
            session_id, directory=directory, message_id=message_id, request_options=request_options
        )
        return _response.data

    async def session_abort(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Abort an active session and stop any ongoing AI processing or command execution.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Aborted session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_abort(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_abort(
            session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def session_share(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Create a shareable link for a session, allowing others to view the conversation.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully shared session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_share(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_share(
            session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def session_unshare(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Remove the shareable link for a session, making it private again.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Successfully unshared session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_unshare(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_unshare(
            session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def session_diff(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileDiff]:
        """
        Get the file changes (diff) that resulted from a specific user message in the session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileDiff]
            Successfully retrieved diff

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_diff(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_diff(
            session_id, directory=directory, message_id=message_id, request_options=request_options
        )
        return _response.data

    async def session_summarize(
        self,
        session_id: str,
        *,
        provider_id: str,
        model_id: str,
        directory: typing.Optional[str] = None,
        auto: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Generate a concise summary of the session using AI compaction to preserve key information.

        Parameters
        ----------
        session_id : str
            Session ID

        provider_id : str

        model_id : str

        directory : typing.Optional[str]

        auto : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Summarized session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_summarize(
                session_id="sessionID",
                provider_id="providerID",
                model_id="modelID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_summarize(
            session_id,
            provider_id=provider_id,
            model_id=model_id,
            directory=directory,
            auto=auto,
            request_options=request_options,
        )
        return _response.data

    async def session_messages(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SessionMessagesResponseItem]:
        """
        Retrieve all messages in a session, including user prompts and AI responses.

        Parameters
        ----------
        session_id : str
            Session ID

        directory : typing.Optional[str]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SessionMessagesResponseItem]
            List of messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_messages(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_messages(
            session_id, directory=directory, limit=limit, request_options=request_options
        )
        return _response.data

    async def session_prompt(
        self,
        session_id: str,
        *,
        parts: typing.Sequence[SessionPromptRequestPartsItem],
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        model: typing.Optional[SessionPromptRequestModel] = OMIT,
        agent: typing.Optional[str] = OMIT,
        no_reply: typing.Optional[bool] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        system: typing.Optional[str] = OMIT,
        variant: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionPromptResponse:
        """
        Create and send a new message to a session, streaming the AI response.

        Parameters
        ----------
        session_id : str
            Session ID

        parts : typing.Sequence[SessionPromptRequestPartsItem]

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        model : typing.Optional[SessionPromptRequestModel]

        agent : typing.Optional[str]

        no_reply : typing.Optional[bool]

        tools : typing.Optional[typing.Dict[str, bool]]
            @deprecated tools and permissions have been merged, you can set permissions on the session itself now

        system : typing.Optional[str]

        variant : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionPromptResponse
            Created message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SessionPromptRequestPartsItem_Text

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_prompt(
                session_id="sessionID",
                parts=[
                    SessionPromptRequestPartsItem_Text(
                        text="text",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_prompt(
            session_id,
            parts=parts,
            directory=directory,
            message_id=message_id,
            model=model,
            agent=agent,
            no_reply=no_reply,
            tools=tools,
            system=system,
            variant=variant,
            request_options=request_options,
        )
        return _response.data

    async def session_message(
        self,
        session_id: str,
        message_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionMessageResponse:
        """
        Retrieve a specific message from a session by its message ID.

        Parameters
        ----------
        session_id : str
            Session ID

        message_id : str
            Message ID

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionMessageResponse
            Message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_message(
                session_id="sessionID",
                message_id="messageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_message(
            session_id, message_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def part_delete(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Delete a part from a message

        Parameters
        ----------
        session_id : str
            Session ID

        message_id : str
            Message ID

        part_id : str
            Part ID

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successfully deleted part

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.part_delete(
                session_id="sessionID",
                message_id="messageID",
                part_id="partID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.part_delete(
            session_id, message_id, part_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def part_update(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        request: Part,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Part:
        """
        Update a part in a message

        Parameters
        ----------
        session_id : str
            Session ID

        message_id : str
            Message ID

        part_id : str
            Part ID

        request : Part

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Part
            Successfully updated part

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Part_Text

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.part_update(
                session_id="sessionID",
                message_id="messageID",
                part_id="partID",
                request=Part_Text(
                    id="id",
                    session_id="sessionID",
                    message_id="messageID",
                    text="text",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.part_update(
            session_id, message_id, part_id, request=request, directory=directory, request_options=request_options
        )
        return _response.data

    async def session_prompt_async(
        self,
        session_id: str,
        *,
        parts: typing.Sequence[SessionPromptAsyncRequestPartsItem],
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        model: typing.Optional[SessionPromptAsyncRequestModel] = OMIT,
        agent: typing.Optional[str] = OMIT,
        no_reply: typing.Optional[bool] = OMIT,
        tools: typing.Optional[typing.Dict[str, bool]] = OMIT,
        system: typing.Optional[str] = OMIT,
        variant: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create and send a new message to a session asynchronously, starting the session if needed and returning immediately.

        Parameters
        ----------
        session_id : str
            Session ID

        parts : typing.Sequence[SessionPromptAsyncRequestPartsItem]

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        model : typing.Optional[SessionPromptAsyncRequestModel]

        agent : typing.Optional[str]

        no_reply : typing.Optional[bool]

        tools : typing.Optional[typing.Dict[str, bool]]
            @deprecated tools and permissions have been merged, you can set permissions on the session itself now

        system : typing.Optional[str]

        variant : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SessionPromptAsyncRequestPartsItem_Text

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_prompt_async(
                session_id="sessionID",
                parts=[
                    SessionPromptAsyncRequestPartsItem_Text(
                        text="text",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_prompt_async(
            session_id,
            parts=parts,
            directory=directory,
            message_id=message_id,
            model=model,
            agent=agent,
            no_reply=no_reply,
            tools=tools,
            system=system,
            variant=variant,
            request_options=request_options,
        )
        return _response.data

    async def session_command(
        self,
        session_id: str,
        *,
        arguments: str,
        command: str,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        agent: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        variant: typing.Optional[str] = OMIT,
        parts: typing.Optional[typing.Sequence[SessionCommandRequestPartsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionCommandResponse:
        """
        Send a new command to a session for execution by the AI assistant.

        Parameters
        ----------
        session_id : str
            Session ID

        arguments : str

        command : str

        directory : typing.Optional[str]

        message_id : typing.Optional[str]

        agent : typing.Optional[str]

        model : typing.Optional[str]

        variant : typing.Optional[str]

        parts : typing.Optional[typing.Sequence[SessionCommandRequestPartsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionCommandResponse
            Created message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_command(
                session_id="sessionID",
                arguments="arguments",
                command="command",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_command(
            session_id,
            arguments=arguments,
            command=command,
            directory=directory,
            message_id=message_id,
            agent=agent,
            model=model,
            variant=variant,
            parts=parts,
            request_options=request_options,
        )
        return _response.data

    async def session_shell(
        self,
        session_id: str,
        *,
        agent: str,
        command: str,
        directory: typing.Optional[str] = None,
        model: typing.Optional[SessionShellRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssistantMessage:
        """
        Execute a shell command within the session context and return the AI's response.

        Parameters
        ----------
        session_id : str
            Session ID

        agent : str

        command : str

        directory : typing.Optional[str]

        model : typing.Optional[SessionShellRequestModel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssistantMessage
            Created message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_shell(
                session_id="sessionID",
                agent="agent",
                command="command",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_shell(
            session_id, agent=agent, command=command, directory=directory, model=model, request_options=request_options
        )
        return _response.data

    async def session_revert(
        self,
        session_id: str,
        *,
        message_id: str,
        directory: typing.Optional[str] = None,
        part_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Revert a specific message in a session, undoing its effects and restoring the previous state.

        Parameters
        ----------
        session_id : str

        message_id : str

        directory : typing.Optional[str]

        part_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Updated session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_revert(
                session_id="sessionID",
                message_id="messageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_revert(
            session_id, message_id=message_id, directory=directory, part_id=part_id, request_options=request_options
        )
        return _response.data

    async def session_unrevert(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Restore all previously reverted messages in a session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Updated session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session_unrevert(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.session_unrevert(
            session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def permission_respond(
        self,
        session_id: str,
        permission_id: str,
        *,
        response: PermissionRespondRequestResponse,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Approve or deny a permission request from the AI assistant.

        Parameters
        ----------
        session_id : str

        permission_id : str

        response : PermissionRespondRequestResponse

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Permission processed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PermissionRespondRequestResponse

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.permission_respond(
                session_id="sessionID",
                permission_id="permissionID",
                response=PermissionRespondRequestResponse.ONCE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permission_respond(
            session_id, permission_id, response=response, directory=directory, request_options=request_options
        )
        return _response.data

    async def permission_reply(
        self,
        request_id: str,
        *,
        reply: PermissionReplyRequestReply,
        directory: typing.Optional[str] = None,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Approve or deny a permission request from the AI assistant.

        Parameters
        ----------
        request_id : str

        reply : PermissionReplyRequestReply

        directory : typing.Optional[str]

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Permission processed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PermissionReplyRequestReply

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.permission_reply(
                request_id="requestID",
                reply=PermissionReplyRequestReply.ONCE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permission_reply(
            request_id, reply=reply, directory=directory, message=message, request_options=request_options
        )
        return _response.data

    async def permission_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PermissionRequest]:
        """
        Get all pending permission requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PermissionRequest]
            List of pending permissions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.permission_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.permission_list(directory=directory, request_options=request_options)
        return _response.data

    async def question_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[QuestionRequest]:
        """
        Get all pending question requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[QuestionRequest]
            List of pending questions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.question_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.question_list(directory=directory, request_options=request_options)
        return _response.data

    async def question_reply(
        self,
        request_id: str,
        *,
        answers: typing.Sequence[QuestionAnswer],
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Provide answers to a question request from the AI assistant.

        Parameters
        ----------
        request_id : str

        answers : typing.Sequence[QuestionAnswer]
            User answers in order of questions (each answer is an array of selected labels)

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Question answered successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.question_reply(
                request_id="requestID",
                answers=[["answers"]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.question_reply(
            request_id, answers=answers, directory=directory, request_options=request_options
        )
        return _response.data

    async def question_reject(
        self,
        request_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Reject a question request from the AI assistant.

        Parameters
        ----------
        request_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Question rejected successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.question_reject(
                request_id="requestID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.question_reject(
            request_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def provider_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderListResponse:
        """
        Get a list of all available AI providers, including both available and connected ones.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderListResponse
            List of providers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_list(directory=directory, request_options=request_options)
        return _response.data

    async def provider_auth(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.List[ProviderAuthMethod]]:
        """
        Retrieve available authentication methods for all AI providers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[ProviderAuthMethod]]
            Provider auth methods

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_auth()


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_auth(directory=directory, request_options=request_options)
        return _response.data

    async def provider_oauth_authorize(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderAuthAuthorization:
        """
        Initiate OAuth authorization for a specific AI provider to get an authorization URL.

        Parameters
        ----------
        provider_id : str
            Provider ID

        method : float
            Auth method index

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderAuthAuthorization
            Authorization URL and method

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_oauth_authorize(
                provider_id="providerID",
                method=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_oauth_authorize(
            provider_id, method=method, directory=directory, request_options=request_options
        )
        return _response.data

    async def provider_oauth_callback(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Handle the OAuth callback from a provider after user authorization.

        Parameters
        ----------
        provider_id : str
            Provider ID

        method : float
            Auth method index

        directory : typing.Optional[str]

        code : typing.Optional[str]
            OAuth authorization code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OAuth callback processed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_oauth_callback(
                provider_id="providerID",
                method=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_oauth_callback(
            provider_id, method=method, directory=directory, code=code, request_options=request_options
        )
        return _response.data

    async def find_text(
        self,
        *,
        pattern: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FindTextResponseItem]:
        """
        Search for text patterns across files in the project using ripgrep.

        Parameters
        ----------
        pattern : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FindTextResponseItem]
            Matches

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_text(
                pattern="pattern",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_text(
            pattern=pattern, directory=directory, request_options=request_options
        )
        return _response.data

    async def find_files(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        dirs: typing.Optional[FindFilesRequestDirs] = None,
        type: typing.Optional[FindFilesRequestType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Search for files or directories by name or pattern in the project directory.

        Parameters
        ----------
        query : str

        directory : typing.Optional[str]

        dirs : typing.Optional[FindFilesRequestDirs]

        type : typing.Optional[FindFilesRequestType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            File paths

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_files(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_files(
            query=query, directory=directory, dirs=dirs, type=type, limit=limit, request_options=request_options
        )
        return _response.data

    async def find_symbols(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Symbol]:
        """
        Search for workspace symbols like functions, classes, and variables using LSP.

        Parameters
        ----------
        query : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Symbol]
            Symbols

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_symbols(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_symbols(
            query=query, directory=directory, request_options=request_options
        )
        return _response.data

    async def file_list(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileNode]:
        """
        List files and directories in a specified path.

        Parameters
        ----------
        path : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileNode]
            Files and directories

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.file_list(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_list(path=path, directory=directory, request_options=request_options)
        return _response.data

    async def file_read(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileContent:
        """
        Read the content of a specified file.

        Parameters
        ----------
        path : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileContent
            File content

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.file_read(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_read(path=path, directory=directory, request_options=request_options)
        return _response.data

    async def file_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[File]:
        """
        Get the git status of all files in the project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[File]
            File status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.file_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.file_status(directory=directory, request_options=request_options)
        return _response.data

    async def mcp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, McpStatus]:
        """
        Get the status of all Model Context Protocol (MCP) servers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, McpStatus]
            MCP server status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_status(directory=directory, request_options=request_options)
        return _response.data

    async def mcp_add(
        self,
        *,
        name: str,
        config: McpAddRequestConfig,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, McpStatus]:
        """
        Dynamically add a new Model Context Protocol (MCP) server to the system.

        Parameters
        ----------
        name : str

        config : McpAddRequestConfig

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, McpStatus]
            MCP server added successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, McpAddRequestConfig_Local

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_add(
                name="name",
                config=McpAddRequestConfig_Local(
                    command=["command"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_add(
            name=name, config=config, directory=directory, request_options=request_options
        )
        return _response.data

    async def mcp_auth_start(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpAuthStartResponse:
        """
        Start OAuth authentication flow for a Model Context Protocol (MCP) server.

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpAuthStartResponse
            OAuth flow started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_auth_start(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_auth_start(name, directory=directory, request_options=request_options)
        return _response.data

    async def mcp_auth_remove(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpAuthRemoveResponse:
        """
        Remove OAuth credentials for an MCP server

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpAuthRemoveResponse
            OAuth credentials removed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_auth_remove(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_auth_remove(name, directory=directory, request_options=request_options)
        return _response.data

    async def mcp_auth_callback(
        self,
        name: str,
        *,
        code: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpStatus:
        """
        Complete OAuth authentication for a Model Context Protocol (MCP) server using the authorization code.

        Parameters
        ----------
        name : str

        code : str
            Authorization code from OAuth callback

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpStatus
            OAuth authentication completed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_auth_callback(
                name="name",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_auth_callback(
            name, code=code, directory=directory, request_options=request_options
        )
        return _response.data

    async def mcp_auth_authenticate(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpStatus:
        """
        Start OAuth flow and wait for callback (opens browser)

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpStatus
            OAuth authentication completed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_auth_authenticate(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_auth_authenticate(
            name, directory=directory, request_options=request_options
        )
        return _response.data

    async def mcp_connect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Connect an MCP server

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            MCP server connected successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_connect(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_connect(name, directory=directory, request_options=request_options)
        return _response.data

    async def mcp_disconnect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Disconnect an MCP server

        Parameters
        ----------
        name : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            MCP server disconnected successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_disconnect(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_disconnect(name, directory=directory, request_options=request_options)
        return _response.data

    async def tui_append_prompt(
        self,
        *,
        text: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Append prompt to the TUI

        Parameters
        ----------
        text : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Prompt processed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_append_prompt(
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_append_prompt(
            text=text, directory=directory, request_options=request_options
        )
        return _response.data

    async def tui_open_help(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the help dialog in the TUI to display user assistance information.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Help dialog opened successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_open_help()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_open_help(directory=directory, request_options=request_options)
        return _response.data

    async def tui_open_sessions(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the session dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Session dialog opened successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_open_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_open_sessions(directory=directory, request_options=request_options)
        return _response.data

    async def tui_open_themes(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the theme dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Theme dialog opened successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_open_themes()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_open_themes(directory=directory, request_options=request_options)
        return _response.data

    async def tui_open_models(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Open the model dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Model dialog opened successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_open_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_open_models(directory=directory, request_options=request_options)
        return _response.data

    async def tui_submit_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Submit the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Prompt submitted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_submit_prompt()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_submit_prompt(directory=directory, request_options=request_options)
        return _response.data

    async def tui_clear_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clear the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Prompt cleared successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_clear_prompt()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_clear_prompt(directory=directory, request_options=request_options)
        return _response.data

    async def tui_execute_command(
        self,
        *,
        command: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Execute a TUI command (e.g. agent_cycle)

        Parameters
        ----------
        command : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Command executed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_execute_command(
                command="command",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_execute_command(
            command=command, directory=directory, request_options=request_options
        )
        return _response.data

    async def tui_show_toast(
        self,
        *,
        message: str,
        variant: TuiShowToastRequestVariant,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        duration: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Show a toast notification in the TUI

        Parameters
        ----------
        message : str

        variant : TuiShowToastRequestVariant

        directory : typing.Optional[str]

        title : typing.Optional[str]

        duration : typing.Optional[float]
            Duration in milliseconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Toast notification shown successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TuiShowToastRequestVariant

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_show_toast(
                message="message",
                variant=TuiShowToastRequestVariant.INFO,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_show_toast(
            message=message,
            variant=variant,
            directory=directory,
            title=title,
            duration=duration,
            request_options=request_options,
        )
        return _response.data

    async def tui_publish(
        self,
        *,
        request: TuiPublishRequestBody,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Publish a TUI event

        Parameters
        ----------
        request : TuiPublishRequestBody

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Event published successfully

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            EventTuiPromptAppendProperties,
            TuiPublishRequestBody_TuiPromptAppend,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_publish(
                request=TuiPublishRequestBody_TuiPromptAppend(
                    properties=EventTuiPromptAppendProperties(
                        text="text",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_publish(
            request=request, directory=directory, request_options=request_options
        )
        return _response.data

    async def tui_select_session(
        self,
        *,
        session_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Navigate the TUI to display the specified session.

        Parameters
        ----------
        session_id : str
            Session ID to navigate to

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Session selected successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_select_session(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_select_session(
            session_id=session_id, directory=directory, request_options=request_options
        )
        return _response.data

    async def tui_control_next(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TuiControlNextResponse:
        """
        Retrieve the next TUI (Terminal User Interface) request from the queue for processing.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TuiControlNextResponse
            Next TUI request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_control_next()


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_control_next(directory=directory, request_options=request_options)
        return _response.data

    async def tui_control_response(
        self,
        *,
        request: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Submit a response to the TUI request queue to complete a pending request.

        Parameters
        ----------
        request : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Response submitted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tui_control_response(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tui_control_response(
            request=request, directory=directory, request_options=request_options
        )
        return _response.data

    async def instance_dispose(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clean up and dispose the current OpenCode instance, releasing all resources.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Instance disposed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.instance_dispose()


        asyncio.run(main())
        """
        _response = await self._raw_client.instance_dispose(directory=directory, request_options=request_options)
        return _response.data

    async def path_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Path:
        """
        Retrieve the current working directory and related path information for the OpenCode instance.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Path
            Path

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.path_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.path_get(directory=directory, request_options=request_options)
        return _response.data

    async def vcs_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> VcsInfo:
        """
        Retrieve version control system (VCS) information for the current project, such as git branch.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VcsInfo
            VCS info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vcs_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.vcs_get(directory=directory, request_options=request_options)
        return _response.data

    async def command_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Command]:
        """
        Get a list of all available commands in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Command]
            List of commands

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.command_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.command_list(directory=directory, request_options=request_options)
        return _response.data

    async def app_log(
        self,
        *,
        service: str,
        level: AppLogRequestLevel,
        message: str,
        directory: typing.Optional[str] = None,
        extra: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Write a log entry to the server logs with specified level and metadata.

        Parameters
        ----------
        service : str
            Service name for the log entry

        level : AppLogRequestLevel
            Log level

        message : str
            Log message

        directory : typing.Optional[str]

        extra : typing.Optional[typing.Dict[str, typing.Any]]
            Additional metadata for the log entry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Log entry written successfully

        Examples
        --------
        import asyncio

        from fern import AppLogRequestLevel, AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.app_log(
                service="service",
                level=AppLogRequestLevel.DEBUG,
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_log(
            service=service,
            level=level,
            message=message,
            directory=directory,
            extra=extra,
            request_options=request_options,
        )
        return _response.data

    async def app_agents(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Agent]:
        """
        Get a list of all available AI agents in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Agent]
            List of agents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.app_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.app_agents(directory=directory, request_options=request_options)
        return _response.data

    async def app_skills(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AppSkillsResponseItem]:
        """
        Get a list of all available skills in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AppSkillsResponseItem]
            List of skills

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.app_skills()


        asyncio.run(main())
        """
        _response = await self._raw_client.app_skills(directory=directory, request_options=request_options)
        return _response.data

    async def lsp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LspStatus]:
        """
        Get LSP server status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LspStatus]
            LSP server status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lsp_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.lsp_status(directory=directory, request_options=request_options)
        return _response.data

    async def formatter_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FormatterStatus]:
        """
        Get formatter status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FormatterStatus]
            Formatter status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.formatter_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.formatter_status(directory=directory, request_options=request_options)
        return _response.data

    async def event_subscribe(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[Event]:
        """
        Get events

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[Event]
            Event stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.event_subscribe()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.event_subscribe(directory=directory, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    @property
    def session(self):
        if self._session is None:
            from .session.client import AsyncSessionClient

            self._session = AsyncSessionClient(client_wrapper=self._client_wrapper)
        return self._session
