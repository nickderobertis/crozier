

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.http_sse._api import EventSource
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as, parse_sse_obj
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.not_found_error import NotFoundError
from .types.agent import Agent
from .types.app_log_request_level import AppLogRequestLevel
from .types.app_skills_response_item import AppSkillsResponseItem
from .types.assistant_message import AssistantMessage
from .types.auth import Auth
from .types.bad_request_error_body import BadRequestErrorBody
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
from .types.not_found_error_body import NotFoundErrorBody
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def global_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalHealthResponse]:
        """
        Get health information about the OpenCode server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalHealthResponse]
            Health information
        """
        _response = self._client_wrapper.httpx_client.request(
            "global/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalHealthResponse,
                    parse_obj_as(
                        type_=GlobalHealthResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def global_event(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[GlobalEvent]]]:
        """
        Subscribe to global events from the OpenCode system using server-sent events.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[GlobalEvent]]]
            Event stream
        """
        with self._client_wrapper.httpx_client.stream(
            "global/event",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[GlobalEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        GlobalEvent,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=GlobalEvent,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def global_config_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Config]:
        """
        Retrieve the current global OpenCode configuration settings and preferences.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Config]
            Get global config info
        """
        _response = self._client_wrapper.httpx_client.request(
            "global/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Config]:
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
        HttpResponse[Config]
            Successfully updated global config
        """
        _response = self._client_wrapper.httpx_client.request(
            "global/config",
            method="PATCH",
            json={
                "$schema": schema,
                "theme": theme,
                "keybinds": convert_and_respect_annotation_metadata(
                    object_=keybinds, annotation=KeybindsConfig, direction="write"
                ),
                "logLevel": log_level,
                "tui": convert_and_respect_annotation_metadata(object_=tui, annotation=ConfigTui, direction="write"),
                "server": convert_and_respect_annotation_metadata(
                    object_=server, annotation=ServerConfig, direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Dict[str, ConfigCommandValue], direction="write"
                ),
                "skills": convert_and_respect_annotation_metadata(
                    object_=skills, annotation=ConfigSkills, direction="write"
                ),
                "watcher": convert_and_respect_annotation_metadata(
                    object_=watcher, annotation=ConfigWatcher, direction="write"
                ),
                "plugin": plugin,
                "snapshot": snapshot,
                "share": share,
                "autoshare": autoshare,
                "autoupdate": convert_and_respect_annotation_metadata(
                    object_=autoupdate, annotation=ConfigAutoupdate, direction="write"
                ),
                "disabled_providers": disabled_providers,
                "enabled_providers": enabled_providers,
                "model": model,
                "small_model": small_model,
                "default_agent": default_agent,
                "username": username,
                "mode": convert_and_respect_annotation_metadata(object_=mode, annotation=ConfigMode, direction="write"),
                "agent": convert_and_respect_annotation_metadata(
                    object_=agent, annotation=ConfigAgent, direction="write"
                ),
                "provider": convert_and_respect_annotation_metadata(
                    object_=provider, annotation=typing.Dict[str, ProviderConfig], direction="write"
                ),
                "mcp": convert_and_respect_annotation_metadata(
                    object_=mcp, annotation=typing.Dict[str, ConfigMcpValue], direction="write"
                ),
                "formatter": convert_and_respect_annotation_metadata(
                    object_=formatter, annotation=ConfigFormatter, direction="write"
                ),
                "lsp": convert_and_respect_annotation_metadata(object_=lsp, annotation=ConfigLsp, direction="write"),
                "instructions": instructions,
                "layout": layout,
                "permission": convert_and_respect_annotation_metadata(
                    object_=permission, annotation=PermissionConfig, direction="write"
                ),
                "tools": tools,
                "enterprise": convert_and_respect_annotation_metadata(
                    object_=enterprise, annotation=ConfigEnterprise, direction="write"
                ),
                "compaction": convert_and_respect_annotation_metadata(
                    object_=compaction, annotation=ConfigCompaction, direction="write"
                ),
                "experimental": convert_and_respect_annotation_metadata(
                    object_=experimental, annotation=ConfigExperimental, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def global_dispose(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[bool]:
        """
        Clean up and dispose all OpenCode instances, releasing all resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Global disposed
        """
        _response = self._client_wrapper.httpx_client.request(
            "global/dispose",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def auth_set(
        self, provider_id: str, *, request: Auth, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Successfully set authentication credentials
        """
        _response = self._client_wrapper.httpx_client.request(
            f"auth/{encode_path_param(provider_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Auth, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def auth_remove(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Remove authentication credentials

        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Successfully removed authentication credentials
        """
        _response = self._client_wrapper.httpx_client.request(
            f"auth/{encode_path_param(provider_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def project_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Project]]:
        """
        Get a list of projects that have been opened with OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Project]]
            List of projects
        """
        _response = self._client_wrapper.httpx_client.request(
            "project",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Project],
                    parse_obj_as(
                        type_=typing.List[Project],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def project_current(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Project]:
        """
        Retrieve the currently active project that OpenCode is working with.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]
            Current project information
        """
        _response = self._client_wrapper.httpx_client.request(
            "project/current",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def project_update(
        self,
        project_id: str,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[ProjectUpdateRequestIcon] = OMIT,
        commands: typing.Optional[ProjectUpdateRequestCommands] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Project]:
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
        HttpResponse[Project]
            Updated project information
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_id)}",
            method="PATCH",
            params={
                "directory": directory,
            },
            json={
                "name": name,
                "icon": convert_and_respect_annotation_metadata(
                    object_=icon, annotation=ProjectUpdateRequestIcon, direction="write"
                ),
                "commands": convert_and_respect_annotation_metadata(
                    object_=commands, annotation=ProjectUpdateRequestCommands, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pty_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Pty]]:
        """
        Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Pty]]
            List of sessions
        """
        _response = self._client_wrapper.httpx_client.request(
            "pty",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Pty],
                    parse_obj_as(
                        type_=typing.List[Pty],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Pty]:
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
        HttpResponse[Pty]
            Created session
        """
        _response = self._client_wrapper.httpx_client.request(
            "pty",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "command": command,
                "args": args,
                "cwd": cwd,
                "title": title,
                "env": env,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pty,
                    parse_obj_as(
                        type_=Pty,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pty_get(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pty]:
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
        HttpResponse[Pty]
            Session info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pty,
                    parse_obj_as(
                        type_=Pty,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pty_update(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        size: typing.Optional[PtyUpdateRequestSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pty]:
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
        HttpResponse[Pty]
            Updated session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}",
            method="PUT",
            params={
                "directory": directory,
            },
            json={
                "title": title,
                "size": convert_and_respect_annotation_metadata(
                    object_=size, annotation=PtyUpdateRequestSize, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pty,
                    parse_obj_as(
                        type_=Pty,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pty_remove(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Session removed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pty_connect(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Connected session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}/connect",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def config_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Config]:
        """
        Retrieve the current OpenCode configuration settings and preferences.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Config]
            Get config info
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Config]:
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
        HttpResponse[Config]
            Successfully updated config
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="PATCH",
            params={
                "directory": directory,
            },
            json={
                "$schema": schema,
                "theme": theme,
                "keybinds": convert_and_respect_annotation_metadata(
                    object_=keybinds, annotation=KeybindsConfig, direction="write"
                ),
                "logLevel": log_level,
                "tui": convert_and_respect_annotation_metadata(object_=tui, annotation=ConfigTui, direction="write"),
                "server": convert_and_respect_annotation_metadata(
                    object_=server, annotation=ServerConfig, direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Dict[str, ConfigCommandValue], direction="write"
                ),
                "skills": convert_and_respect_annotation_metadata(
                    object_=skills, annotation=ConfigSkills, direction="write"
                ),
                "watcher": convert_and_respect_annotation_metadata(
                    object_=watcher, annotation=ConfigWatcher, direction="write"
                ),
                "plugin": plugin,
                "snapshot": snapshot,
                "share": share,
                "autoshare": autoshare,
                "autoupdate": convert_and_respect_annotation_metadata(
                    object_=autoupdate, annotation=ConfigAutoupdate, direction="write"
                ),
                "disabled_providers": disabled_providers,
                "enabled_providers": enabled_providers,
                "model": model,
                "small_model": small_model,
                "default_agent": default_agent,
                "username": username,
                "mode": convert_and_respect_annotation_metadata(object_=mode, annotation=ConfigMode, direction="write"),
                "agent": convert_and_respect_annotation_metadata(
                    object_=agent, annotation=ConfigAgent, direction="write"
                ),
                "provider": convert_and_respect_annotation_metadata(
                    object_=provider, annotation=typing.Dict[str, ProviderConfig], direction="write"
                ),
                "mcp": convert_and_respect_annotation_metadata(
                    object_=mcp, annotation=typing.Dict[str, ConfigMcpValue], direction="write"
                ),
                "formatter": convert_and_respect_annotation_metadata(
                    object_=formatter, annotation=ConfigFormatter, direction="write"
                ),
                "lsp": convert_and_respect_annotation_metadata(object_=lsp, annotation=ConfigLsp, direction="write"),
                "instructions": instructions,
                "layout": layout,
                "permission": convert_and_respect_annotation_metadata(
                    object_=permission, annotation=PermissionConfig, direction="write"
                ),
                "tools": tools,
                "enterprise": convert_and_respect_annotation_metadata(
                    object_=enterprise, annotation=ConfigEnterprise, direction="write"
                ),
                "compaction": convert_and_respect_annotation_metadata(
                    object_=compaction, annotation=ConfigCompaction, direction="write"
                ),
                "experimental": convert_and_respect_annotation_metadata(
                    object_=experimental, annotation=ConfigExperimental, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def config_providers(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigProvidersResponse]:
        """
        Get a list of all configured AI providers and their default models.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigProvidersResponse]
            List of providers
        """
        _response = self._client_wrapper.httpx_client.request(
            "config/providers",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigProvidersResponse,
                    parse_obj_as(
                        type_=ConfigProvidersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tool_ids(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ToolIDs]:
        """
        Get a list of all available tool IDs, including both built-in tools and dynamically registered tools.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToolIDs]
            Tool IDs
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/tool/ids",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolIDs,
                    parse_obj_as(
                        type_=ToolIDs,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tool_list(
        self,
        *,
        provider: str,
        model: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolList]:
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
        HttpResponse[ToolList]
            Tools
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/tool",
            method="GET",
            params={
                "directory": directory,
                "provider": provider,
                "model": model,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolList,
                    parse_obj_as(
                        type_=ToolList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def worktree_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        List all sandbox worktrees for the current project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            List of worktree directories
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/worktree",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def worktree_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        start_command: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Worktree]:
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
        HttpResponse[Worktree]
            Worktree created
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/worktree",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "name": name,
                "startCommand": start_command,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Worktree,
                    parse_obj_as(
                        type_=Worktree,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def worktree_remove(
        self,
        *,
        worktree_remove_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Worktree removed
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/worktree",
            method="DELETE",
            params={
                "directory": directory,
            },
            json={
                "directory": worktree_remove_input_directory,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def worktree_reset(
        self,
        *,
        worktree_reset_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Worktree reset
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/worktree/reset",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "directory": worktree_reset_input_directory,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def experimental_resource_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, McpResource]]:
        """
        Get all available MCP resources from connected servers. Optionally filter by name.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, McpResource]]
            MCP resources
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/resource",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, McpResource],
                    parse_obj_as(
                        type_=typing.Dict[str, McpResource],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_list(
        self,
        *,
        directory: typing.Optional[str] = None,
        roots: typing.Optional[bool] = None,
        start: typing.Optional[float] = None,
        search: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Session]]:
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
        HttpResponse[typing.List[Session]]
            List of sessions
        """
        _response = self._client_wrapper.httpx_client.request(
            "session",
            method="GET",
            params={
                "directory": directory,
                "roots": roots,
                "start": start,
                "search": search,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Session],
                    parse_obj_as(
                        type_=typing.List[Session],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        permission: typing.Optional[PermissionRuleset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            Successfully created session
        """
        _response = self._client_wrapper.httpx_client.request(
            "session",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "parentID": parent_id,
                "title": title,
                "permission": convert_and_respect_annotation_metadata(
                    object_=permission, annotation=PermissionRuleset, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, SessionStatus]]:
        """
        Retrieve the current status of all sessions, including active, idle, and completed states.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, SessionStatus]]
            Get session status
        """
        _response = self._client_wrapper.httpx_client.request(
            "session/status",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, SessionStatus],
                    parse_obj_as(
                        type_=typing.Dict[str, SessionStatus],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_delete(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Successfully deleted session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_update(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        time: typing.Optional[SessionUpdateRequestTime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            Successfully updated session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}",
            method="PATCH",
            params={
                "directory": directory,
            },
            json={
                "title": title,
                "time": convert_and_respect_annotation_metadata(
                    object_=time, annotation=SessionUpdateRequestTime, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_todo(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Todo]]:
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
        HttpResponse[typing.List[Todo]]
            Todo list
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/todo",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Todo],
                    parse_obj_as(
                        type_=typing.List[Todo],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_init(
        self,
        session_id: str,
        *,
        model_id: str,
        provider_id: str,
        message_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/init",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "modelID": model_id,
                "providerID": provider_id,
                "messageID": message_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_fork(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/fork",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_abort(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Aborted session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/abort",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_share(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            Successfully shared session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/share",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_unshare(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            Successfully unshared session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/share",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_diff(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FileDiff]]:
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
        HttpResponse[typing.List[FileDiff]]
            Successfully retrieved diff
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/diff",
            method="GET",
            params={
                "directory": directory,
                "messageID": message_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileDiff],
                    parse_obj_as(
                        type_=typing.List[FileDiff],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_summarize(
        self,
        session_id: str,
        *,
        provider_id: str,
        model_id: str,
        directory: typing.Optional[str] = None,
        auto: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Summarized session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/summarize",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "providerID": provider_id,
                "modelID": model_id,
                "auto": auto,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_messages(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[SessionMessagesResponseItem]]:
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
        HttpResponse[typing.List[SessionMessagesResponseItem]]
            List of messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message",
            method="GET",
            params={
                "directory": directory,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SessionMessagesResponseItem],
                    parse_obj_as(
                        type_=typing.List[SessionMessagesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[SessionPromptResponse]:
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
        HttpResponse[SessionPromptResponse]
            Created message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=SessionPromptRequestModel, direction="write"
                ),
                "agent": agent,
                "noReply": no_reply,
                "tools": tools,
                "system": system,
                "variant": variant,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[SessionPromptRequestPartsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SessionPromptResponse,
                    parse_obj_as(
                        type_=SessionPromptResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_message(
        self,
        session_id: str,
        message_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SessionMessageResponse]:
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
        HttpResponse[SessionMessageResponse]
            Message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message/{encode_path_param(message_id)}",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SessionMessageResponse,
                    parse_obj_as(
                        type_=SessionMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def part_delete(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Successfully deleted part
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message/{encode_path_param(message_id)}/part/{encode_path_param(part_id)}",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def part_update(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        request: Part,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Part]:
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
        HttpResponse[Part]
            Successfully updated part
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message/{encode_path_param(message_id)}/part/{encode_path_param(part_id)}",
            method="PATCH",
            params={
                "directory": directory,
            },
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Part, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Part,
                    parse_obj_as(
                        type_=Part,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/prompt_async",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=SessionPromptAsyncRequestModel, direction="write"
                ),
                "agent": agent,
                "noReply": no_reply,
                "tools": tools,
                "system": system,
                "variant": variant,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[SessionPromptAsyncRequestPartsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[SessionCommandResponse]:
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
        HttpResponse[SessionCommandResponse]
            Created message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/command",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "agent": agent,
                "model": model,
                "arguments": arguments,
                "command": command,
                "variant": variant,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[SessionCommandRequestPartsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SessionCommandResponse,
                    parse_obj_as(
                        type_=SessionCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_shell(
        self,
        session_id: str,
        *,
        agent: str,
        command: str,
        directory: typing.Optional[str] = None,
        model: typing.Optional[SessionShellRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AssistantMessage]:
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
        HttpResponse[AssistantMessage]
            Created message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/shell",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "agent": agent,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=SessionShellRequestModel, direction="write"
                ),
                "command": command,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssistantMessage,
                    parse_obj_as(
                        type_=AssistantMessage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_revert(
        self,
        session_id: str,
        *,
        message_id: str,
        directory: typing.Optional[str] = None,
        part_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            Updated session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/revert",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "partID": part_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def session_unrevert(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Session]:
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
        HttpResponse[Session]
            Updated session
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/unrevert",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permission_respond(
        self,
        session_id: str,
        permission_id: str,
        *,
        response: PermissionRespondRequestResponse,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Permission processed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/permissions/{encode_path_param(permission_id)}",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "response": response,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permission_reply(
        self,
        request_id: str,
        *,
        reply: PermissionReplyRequestReply,
        directory: typing.Optional[str] = None,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Permission processed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"permission/{encode_path_param(request_id)}/reply",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "reply": reply,
                "message": message,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def permission_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PermissionRequest]]:
        """
        Get all pending permission requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PermissionRequest]]
            List of pending permissions
        """
        _response = self._client_wrapper.httpx_client.request(
            "permission",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PermissionRequest],
                    parse_obj_as(
                        type_=typing.List[PermissionRequest],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def question_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[QuestionRequest]]:
        """
        Get all pending question requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[QuestionRequest]]
            List of pending questions
        """
        _response = self._client_wrapper.httpx_client.request(
            "question",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[QuestionRequest],
                    parse_obj_as(
                        type_=typing.List[QuestionRequest],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def question_reply(
        self,
        request_id: str,
        *,
        answers: typing.Sequence[QuestionAnswer],
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Question answered successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"question/{encode_path_param(request_id)}/reply",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "answers": answers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def question_reject(
        self,
        request_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Question rejected successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"question/{encode_path_param(request_id)}/reject",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProviderListResponse]:
        """
        Get a list of all available AI providers, including both available and connected ones.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderListResponse]
            List of providers
        """
        _response = self._client_wrapper.httpx_client.request(
            "provider",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderListResponse,
                    parse_obj_as(
                        type_=ProviderListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_auth(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.List[ProviderAuthMethod]]]:
        """
        Retrieve available authentication methods for all AI providers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.List[ProviderAuthMethod]]]
            Provider auth methods
        """
        _response = self._client_wrapper.httpx_client.request(
            "provider/auth",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[ProviderAuthMethod]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[ProviderAuthMethod]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_oauth_authorize(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderAuthAuthorization]:
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
        HttpResponse[ProviderAuthAuthorization]
            Authorization URL and method
        """
        _response = self._client_wrapper.httpx_client.request(
            f"provider/{encode_path_param(provider_id)}/oauth/authorize",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "method": method,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderAuthAuthorization,
                    parse_obj_as(
                        type_=ProviderAuthAuthorization,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_oauth_callback(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            OAuth callback processed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"provider/{encode_path_param(provider_id)}/oauth/callback",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "method": method,
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def find_text(
        self,
        *,
        pattern: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FindTextResponseItem]]:
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
        HttpResponse[typing.List[FindTextResponseItem]]
            Matches
        """
        _response = self._client_wrapper.httpx_client.request(
            "find",
            method="GET",
            params={
                "directory": directory,
                "pattern": pattern,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FindTextResponseItem],
                    parse_obj_as(
                        type_=typing.List[FindTextResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def find_files(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        dirs: typing.Optional[FindFilesRequestDirs] = None,
        type: typing.Optional[FindFilesRequestType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
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
        HttpResponse[typing.List[str]]
            File paths
        """
        _response = self._client_wrapper.httpx_client.request(
            "find/file",
            method="GET",
            params={
                "directory": directory,
                "query": query,
                "dirs": dirs,
                "type": type,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def find_symbols(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Symbol]]:
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
        HttpResponse[typing.List[Symbol]]
            Symbols
        """
        _response = self._client_wrapper.httpx_client.request(
            "find/symbol",
            method="GET",
            params={
                "directory": directory,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Symbol],
                    parse_obj_as(
                        type_=typing.List[Symbol],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def file_list(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FileNode]]:
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
        HttpResponse[typing.List[FileNode]]
            Files and directories
        """
        _response = self._client_wrapper.httpx_client.request(
            "file",
            method="GET",
            params={
                "directory": directory,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileNode],
                    parse_obj_as(
                        type_=typing.List[FileNode],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def file_read(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileContent]:
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
        HttpResponse[FileContent]
            File content
        """
        _response = self._client_wrapper.httpx_client.request(
            "file/content",
            method="GET",
            params={
                "directory": directory,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileContent,
                    parse_obj_as(
                        type_=FileContent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def file_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[File]]:
        """
        Get the git status of all files in the project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[File]]
            File status
        """
        _response = self._client_wrapper.httpx_client.request(
            "file/status",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[File],
                    parse_obj_as(
                        type_=typing.List[File],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, McpStatus]]:
        """
        Get the status of all Model Context Protocol (MCP) servers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, McpStatus]]
            MCP server status
        """
        _response = self._client_wrapper.httpx_client.request(
            "mcp",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, McpStatus],
                    parse_obj_as(
                        type_=typing.Dict[str, McpStatus],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_add(
        self,
        *,
        name: str,
        config: McpAddRequestConfig,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, McpStatus]]:
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
        HttpResponse[typing.Dict[str, McpStatus]]
            MCP server added successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "mcp",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=McpAddRequestConfig, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, McpStatus],
                    parse_obj_as(
                        type_=typing.Dict[str, McpStatus],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_auth_start(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[McpAuthStartResponse]:
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
        HttpResponse[McpAuthStartResponse]
            OAuth flow started
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpAuthStartResponse,
                    parse_obj_as(
                        type_=McpAuthStartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_auth_remove(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[McpAuthRemoveResponse]:
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
        HttpResponse[McpAuthRemoveResponse]
            OAuth credentials removed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpAuthRemoveResponse,
                    parse_obj_as(
                        type_=McpAuthRemoveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_auth_callback(
        self,
        name: str,
        *,
        code: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[McpStatus]:
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
        HttpResponse[McpStatus]
            OAuth authentication completed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth/callback",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpStatus,
                    parse_obj_as(
                        type_=McpStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_auth_authenticate(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[McpStatus]:
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
        HttpResponse[McpStatus]
            OAuth authentication completed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth/authenticate",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpStatus,
                    parse_obj_as(
                        type_=McpStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_connect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            MCP server connected successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/connect",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mcp_disconnect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            MCP server disconnected successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/disconnect",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_append_prompt(
        self,
        *,
        text: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Prompt processed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/append-prompt",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_open_help(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Open the help dialog in the TUI to display user assistance information.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Help dialog opened successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/open-help",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_open_sessions(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Open the session dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Session dialog opened successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/open-sessions",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_open_themes(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Open the theme dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Theme dialog opened successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/open-themes",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_open_models(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Open the model dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Model dialog opened successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/open-models",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_submit_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Submit the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Prompt submitted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/submit-prompt",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_clear_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Clear the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Prompt cleared successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/clear-prompt",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_execute_command(
        self,
        *,
        command: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Command executed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/execute-command",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "command": command,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_show_toast(
        self,
        *,
        message: str,
        variant: TuiShowToastRequestVariant,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        duration: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Toast notification shown successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/show-toast",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "title": title,
                "message": message,
                "variant": variant,
                "duration": duration,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_publish(
        self,
        *,
        request: TuiPublishRequestBody,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Event published successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/publish",
            method="POST",
            params={
                "directory": directory,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TuiPublishRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_select_session(
        self,
        *,
        session_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Session selected successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/select-session",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "sessionID": session_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_control_next(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TuiControlNextResponse]:
        """
        Retrieve the next TUI (Terminal User Interface) request from the queue for processing.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TuiControlNextResponse]
            Next TUI request
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/control/next",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TuiControlNextResponse,
                    parse_obj_as(
                        type_=TuiControlNextResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tui_control_response(
        self,
        *,
        request: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Response submitted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "tui/control/response",
            method="POST",
            params={
                "directory": directory,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def instance_dispose(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[bool]:
        """
        Clean up and dispose the current OpenCode instance, releasing all resources.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            Instance disposed
        """
        _response = self._client_wrapper.httpx_client.request(
            "instance/dispose",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def path_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Path]:
        """
        Retrieve the current working directory and related path information for the OpenCode instance.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Path]
            Path
        """
        _response = self._client_wrapper.httpx_client.request(
            "path",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Path,
                    parse_obj_as(
                        type_=Path,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def vcs_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VcsInfo]:
        """
        Retrieve version control system (VCS) information for the current project, such as git branch.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VcsInfo]
            VCS info
        """
        _response = self._client_wrapper.httpx_client.request(
            "vcs",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VcsInfo,
                    parse_obj_as(
                        type_=VcsInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def command_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Command]]:
        """
        Get a list of all available commands in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Command]]
            List of commands
        """
        _response = self._client_wrapper.httpx_client.request(
            "command",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Command],
                    parse_obj_as(
                        type_=typing.List[Command],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def app_log(
        self,
        *,
        service: str,
        level: AppLogRequestLevel,
        message: str,
        directory: typing.Optional[str] = None,
        extra: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
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
        HttpResponse[bool]
            Log entry written successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "log",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "service": service,
                "level": level,
                "message": message,
                "extra": extra,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def app_agents(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Agent]]:
        """
        Get a list of all available AI agents in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Agent]]
            List of agents
        """
        _response = self._client_wrapper.httpx_client.request(
            "agent",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Agent],
                    parse_obj_as(
                        type_=typing.List[Agent],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def app_skills(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AppSkillsResponseItem]]:
        """
        Get a list of all available skills in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AppSkillsResponseItem]]
            List of skills
        """
        _response = self._client_wrapper.httpx_client.request(
            "skill",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AppSkillsResponseItem],
                    parse_obj_as(
                        type_=typing.List[AppSkillsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def lsp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LspStatus]]:
        """
        Get LSP server status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LspStatus]]
            LSP server status
        """
        _response = self._client_wrapper.httpx_client.request(
            "lsp",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LspStatus],
                    parse_obj_as(
                        type_=typing.List[LspStatus],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def formatter_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[FormatterStatus]]:
        """
        Get formatter status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FormatterStatus]]
            Formatter status
        """
        _response = self._client_wrapper.httpx_client.request(
            "formatter",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FormatterStatus],
                    parse_obj_as(
                        type_=typing.List[FormatterStatus],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def event_subscribe(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[Event]]]:
        """
        Get events

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[Event]]]
            Event stream
        """
        with self._client_wrapper.httpx_client.stream(
            "event",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[Event]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        Event,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=Event,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def global_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalHealthResponse]:
        """
        Get health information about the OpenCode server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalHealthResponse]
            Health information
        """
        _response = await self._client_wrapper.httpx_client.request(
            "global/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalHealthResponse,
                    parse_obj_as(
                        type_=GlobalHealthResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def global_event(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[GlobalEvent]]]:
        """
        Subscribe to global events from the OpenCode system using server-sent events.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[GlobalEvent]]]
            Event stream
        """
        async with self._client_wrapper.httpx_client.stream(
            "global/event",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[GlobalEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        GlobalEvent,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=GlobalEvent,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def global_config_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Config]:
        """
        Retrieve the current global OpenCode configuration settings and preferences.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Config]
            Get global config info
        """
        _response = await self._client_wrapper.httpx_client.request(
            "global/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Config]:
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
        AsyncHttpResponse[Config]
            Successfully updated global config
        """
        _response = await self._client_wrapper.httpx_client.request(
            "global/config",
            method="PATCH",
            json={
                "$schema": schema,
                "theme": theme,
                "keybinds": convert_and_respect_annotation_metadata(
                    object_=keybinds, annotation=KeybindsConfig, direction="write"
                ),
                "logLevel": log_level,
                "tui": convert_and_respect_annotation_metadata(object_=tui, annotation=ConfigTui, direction="write"),
                "server": convert_and_respect_annotation_metadata(
                    object_=server, annotation=ServerConfig, direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Dict[str, ConfigCommandValue], direction="write"
                ),
                "skills": convert_and_respect_annotation_metadata(
                    object_=skills, annotation=ConfigSkills, direction="write"
                ),
                "watcher": convert_and_respect_annotation_metadata(
                    object_=watcher, annotation=ConfigWatcher, direction="write"
                ),
                "plugin": plugin,
                "snapshot": snapshot,
                "share": share,
                "autoshare": autoshare,
                "autoupdate": convert_and_respect_annotation_metadata(
                    object_=autoupdate, annotation=ConfigAutoupdate, direction="write"
                ),
                "disabled_providers": disabled_providers,
                "enabled_providers": enabled_providers,
                "model": model,
                "small_model": small_model,
                "default_agent": default_agent,
                "username": username,
                "mode": convert_and_respect_annotation_metadata(object_=mode, annotation=ConfigMode, direction="write"),
                "agent": convert_and_respect_annotation_metadata(
                    object_=agent, annotation=ConfigAgent, direction="write"
                ),
                "provider": convert_and_respect_annotation_metadata(
                    object_=provider, annotation=typing.Dict[str, ProviderConfig], direction="write"
                ),
                "mcp": convert_and_respect_annotation_metadata(
                    object_=mcp, annotation=typing.Dict[str, ConfigMcpValue], direction="write"
                ),
                "formatter": convert_and_respect_annotation_metadata(
                    object_=formatter, annotation=ConfigFormatter, direction="write"
                ),
                "lsp": convert_and_respect_annotation_metadata(object_=lsp, annotation=ConfigLsp, direction="write"),
                "instructions": instructions,
                "layout": layout,
                "permission": convert_and_respect_annotation_metadata(
                    object_=permission, annotation=PermissionConfig, direction="write"
                ),
                "tools": tools,
                "enterprise": convert_and_respect_annotation_metadata(
                    object_=enterprise, annotation=ConfigEnterprise, direction="write"
                ),
                "compaction": convert_and_respect_annotation_metadata(
                    object_=compaction, annotation=ConfigCompaction, direction="write"
                ),
                "experimental": convert_and_respect_annotation_metadata(
                    object_=experimental, annotation=ConfigExperimental, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def global_dispose(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Clean up and dispose all OpenCode instances, releasing all resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Global disposed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "global/dispose",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def auth_set(
        self, provider_id: str, *, request: Auth, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Successfully set authentication credentials
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"auth/{encode_path_param(provider_id)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Auth, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def auth_remove(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Remove authentication credentials

        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Successfully removed authentication credentials
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"auth/{encode_path_param(provider_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def project_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Project]]:
        """
        Get a list of projects that have been opened with OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Project]]
            List of projects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "project",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Project],
                    parse_obj_as(
                        type_=typing.List[Project],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def project_current(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Project]:
        """
        Retrieve the currently active project that OpenCode is working with.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]
            Current project information
        """
        _response = await self._client_wrapper.httpx_client.request(
            "project/current",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def project_update(
        self,
        project_id: str,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        icon: typing.Optional[ProjectUpdateRequestIcon] = OMIT,
        commands: typing.Optional[ProjectUpdateRequestCommands] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Project]:
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
        AsyncHttpResponse[Project]
            Updated project information
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(project_id)}",
            method="PATCH",
            params={
                "directory": directory,
            },
            json={
                "name": name,
                "icon": convert_and_respect_annotation_metadata(
                    object_=icon, annotation=ProjectUpdateRequestIcon, direction="write"
                ),
                "commands": convert_and_respect_annotation_metadata(
                    object_=commands, annotation=ProjectUpdateRequestCommands, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pty_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Pty]]:
        """
        Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Pty]]
            List of sessions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pty",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Pty],
                    parse_obj_as(
                        type_=typing.List[Pty],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Pty]:
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
        AsyncHttpResponse[Pty]
            Created session
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pty",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "command": command,
                "args": args,
                "cwd": cwd,
                "title": title,
                "env": env,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pty,
                    parse_obj_as(
                        type_=Pty,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pty_get(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pty]:
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
        AsyncHttpResponse[Pty]
            Session info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pty,
                    parse_obj_as(
                        type_=Pty,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pty_update(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        size: typing.Optional[PtyUpdateRequestSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pty]:
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
        AsyncHttpResponse[Pty]
            Updated session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}",
            method="PUT",
            params={
                "directory": directory,
            },
            json={
                "title": title,
                "size": convert_and_respect_annotation_metadata(
                    object_=size, annotation=PtyUpdateRequestSize, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pty,
                    parse_obj_as(
                        type_=Pty,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pty_remove(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Session removed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pty_connect(
        self,
        pty_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Connected session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pty/{encode_path_param(pty_id)}/connect",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def config_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Config]:
        """
        Retrieve the current OpenCode configuration settings and preferences.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Config]
            Get config info
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Config]:
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
        AsyncHttpResponse[Config]
            Successfully updated config
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="PATCH",
            params={
                "directory": directory,
            },
            json={
                "$schema": schema,
                "theme": theme,
                "keybinds": convert_and_respect_annotation_metadata(
                    object_=keybinds, annotation=KeybindsConfig, direction="write"
                ),
                "logLevel": log_level,
                "tui": convert_and_respect_annotation_metadata(object_=tui, annotation=ConfigTui, direction="write"),
                "server": convert_and_respect_annotation_metadata(
                    object_=server, annotation=ServerConfig, direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Dict[str, ConfigCommandValue], direction="write"
                ),
                "skills": convert_and_respect_annotation_metadata(
                    object_=skills, annotation=ConfigSkills, direction="write"
                ),
                "watcher": convert_and_respect_annotation_metadata(
                    object_=watcher, annotation=ConfigWatcher, direction="write"
                ),
                "plugin": plugin,
                "snapshot": snapshot,
                "share": share,
                "autoshare": autoshare,
                "autoupdate": convert_and_respect_annotation_metadata(
                    object_=autoupdate, annotation=ConfigAutoupdate, direction="write"
                ),
                "disabled_providers": disabled_providers,
                "enabled_providers": enabled_providers,
                "model": model,
                "small_model": small_model,
                "default_agent": default_agent,
                "username": username,
                "mode": convert_and_respect_annotation_metadata(object_=mode, annotation=ConfigMode, direction="write"),
                "agent": convert_and_respect_annotation_metadata(
                    object_=agent, annotation=ConfigAgent, direction="write"
                ),
                "provider": convert_and_respect_annotation_metadata(
                    object_=provider, annotation=typing.Dict[str, ProviderConfig], direction="write"
                ),
                "mcp": convert_and_respect_annotation_metadata(
                    object_=mcp, annotation=typing.Dict[str, ConfigMcpValue], direction="write"
                ),
                "formatter": convert_and_respect_annotation_metadata(
                    object_=formatter, annotation=ConfigFormatter, direction="write"
                ),
                "lsp": convert_and_respect_annotation_metadata(object_=lsp, annotation=ConfigLsp, direction="write"),
                "instructions": instructions,
                "layout": layout,
                "permission": convert_and_respect_annotation_metadata(
                    object_=permission, annotation=PermissionConfig, direction="write"
                ),
                "tools": tools,
                "enterprise": convert_and_respect_annotation_metadata(
                    object_=enterprise, annotation=ConfigEnterprise, direction="write"
                ),
                "compaction": convert_and_respect_annotation_metadata(
                    object_=compaction, annotation=ConfigCompaction, direction="write"
                ),
                "experimental": convert_and_respect_annotation_metadata(
                    object_=experimental, annotation=ConfigExperimental, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Config,
                    parse_obj_as(
                        type_=Config,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def config_providers(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigProvidersResponse]:
        """
        Get a list of all configured AI providers and their default models.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigProvidersResponse]
            List of providers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config/providers",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigProvidersResponse,
                    parse_obj_as(
                        type_=ConfigProvidersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tool_ids(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ToolIDs]:
        """
        Get a list of all available tool IDs, including both built-in tools and dynamically registered tools.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToolIDs]
            Tool IDs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/tool/ids",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolIDs,
                    parse_obj_as(
                        type_=ToolIDs,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tool_list(
        self,
        *,
        provider: str,
        model: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToolList]:
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
        AsyncHttpResponse[ToolList]
            Tools
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/tool",
            method="GET",
            params={
                "directory": directory,
                "provider": provider,
                "model": model,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolList,
                    parse_obj_as(
                        type_=ToolList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def worktree_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        List all sandbox worktrees for the current project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            List of worktree directories
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/worktree",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def worktree_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        start_command: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Worktree]:
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
        AsyncHttpResponse[Worktree]
            Worktree created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/worktree",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "name": name,
                "startCommand": start_command,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Worktree,
                    parse_obj_as(
                        type_=Worktree,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def worktree_remove(
        self,
        *,
        worktree_remove_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Worktree removed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/worktree",
            method="DELETE",
            params={
                "directory": directory,
            },
            json={
                "directory": worktree_remove_input_directory,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def worktree_reset(
        self,
        *,
        worktree_reset_input_directory: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Worktree reset
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/worktree/reset",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "directory": worktree_reset_input_directory,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def experimental_resource_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, McpResource]]:
        """
        Get all available MCP resources from connected servers. Optionally filter by name.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, McpResource]]
            MCP resources
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/resource",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, McpResource],
                    parse_obj_as(
                        type_=typing.Dict[str, McpResource],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_list(
        self,
        *,
        directory: typing.Optional[str] = None,
        roots: typing.Optional[bool] = None,
        start: typing.Optional[float] = None,
        search: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Session]]:
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
        AsyncHttpResponse[typing.List[Session]]
            List of sessions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "session",
            method="GET",
            params={
                "directory": directory,
                "roots": roots,
                "start": start,
                "search": search,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Session],
                    parse_obj_as(
                        type_=typing.List[Session],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_create(
        self,
        *,
        directory: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        permission: typing.Optional[PermissionRuleset] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            Successfully created session
        """
        _response = await self._client_wrapper.httpx_client.request(
            "session",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "parentID": parent_id,
                "title": title,
                "permission": convert_and_respect_annotation_metadata(
                    object_=permission, annotation=PermissionRuleset, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, SessionStatus]]:
        """
        Retrieve the current status of all sessions, including active, idle, and completed states.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, SessionStatus]]
            Get session status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "session/status",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, SessionStatus],
                    parse_obj_as(
                        type_=typing.Dict[str, SessionStatus],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_delete(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Successfully deleted session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_update(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        time: typing.Optional[SessionUpdateRequestTime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            Successfully updated session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}",
            method="PATCH",
            params={
                "directory": directory,
            },
            json={
                "title": title,
                "time": convert_and_respect_annotation_metadata(
                    object_=time, annotation=SessionUpdateRequestTime, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_todo(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Todo]]:
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
        AsyncHttpResponse[typing.List[Todo]]
            Todo list
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/todo",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Todo],
                    parse_obj_as(
                        type_=typing.List[Todo],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_init(
        self,
        session_id: str,
        *,
        model_id: str,
        provider_id: str,
        message_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/init",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "modelID": model_id,
                "providerID": provider_id,
                "messageID": message_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_fork(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/fork",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_abort(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Aborted session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/abort",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_share(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            Successfully shared session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/share",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_unshare(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            Successfully unshared session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/share",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_diff(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FileDiff]]:
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
        AsyncHttpResponse[typing.List[FileDiff]]
            Successfully retrieved diff
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/diff",
            method="GET",
            params={
                "directory": directory,
                "messageID": message_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileDiff],
                    parse_obj_as(
                        type_=typing.List[FileDiff],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_summarize(
        self,
        session_id: str,
        *,
        provider_id: str,
        model_id: str,
        directory: typing.Optional[str] = None,
        auto: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Summarized session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/summarize",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "providerID": provider_id,
                "modelID": model_id,
                "auto": auto,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_messages(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[SessionMessagesResponseItem]]:
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
        AsyncHttpResponse[typing.List[SessionMessagesResponseItem]]
            List of messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message",
            method="GET",
            params={
                "directory": directory,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SessionMessagesResponseItem],
                    parse_obj_as(
                        type_=typing.List[SessionMessagesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[SessionPromptResponse]:
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
        AsyncHttpResponse[SessionPromptResponse]
            Created message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=SessionPromptRequestModel, direction="write"
                ),
                "agent": agent,
                "noReply": no_reply,
                "tools": tools,
                "system": system,
                "variant": variant,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[SessionPromptRequestPartsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SessionPromptResponse,
                    parse_obj_as(
                        type_=SessionPromptResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_message(
        self,
        session_id: str,
        message_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SessionMessageResponse]:
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
        AsyncHttpResponse[SessionMessageResponse]
            Message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message/{encode_path_param(message_id)}",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SessionMessageResponse,
                    parse_obj_as(
                        type_=SessionMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def part_delete(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Successfully deleted part
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message/{encode_path_param(message_id)}/part/{encode_path_param(part_id)}",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def part_update(
        self,
        session_id: str,
        message_id: str,
        part_id: str,
        *,
        request: Part,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Part]:
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
        AsyncHttpResponse[Part]
            Successfully updated part
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/message/{encode_path_param(message_id)}/part/{encode_path_param(part_id)}",
            method="PATCH",
            params={
                "directory": directory,
            },
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Part, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Part,
                    parse_obj_as(
                        type_=Part,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/prompt_async",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=SessionPromptAsyncRequestModel, direction="write"
                ),
                "agent": agent,
                "noReply": no_reply,
                "tools": tools,
                "system": system,
                "variant": variant,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[SessionPromptAsyncRequestPartsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[SessionCommandResponse]:
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
        AsyncHttpResponse[SessionCommandResponse]
            Created message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/command",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "agent": agent,
                "model": model,
                "arguments": arguments,
                "command": command,
                "variant": variant,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[SessionCommandRequestPartsItem], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SessionCommandResponse,
                    parse_obj_as(
                        type_=SessionCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_shell(
        self,
        session_id: str,
        *,
        agent: str,
        command: str,
        directory: typing.Optional[str] = None,
        model: typing.Optional[SessionShellRequestModel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AssistantMessage]:
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
        AsyncHttpResponse[AssistantMessage]
            Created message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/shell",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "agent": agent,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=SessionShellRequestModel, direction="write"
                ),
                "command": command,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssistantMessage,
                    parse_obj_as(
                        type_=AssistantMessage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_revert(
        self,
        session_id: str,
        *,
        message_id: str,
        directory: typing.Optional[str] = None,
        part_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            Updated session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/revert",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "messageID": message_id,
                "partID": part_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def session_unrevert(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Session]:
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
        AsyncHttpResponse[Session]
            Updated session
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/unrevert",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Session,
                    parse_obj_as(
                        type_=Session,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permission_respond(
        self,
        session_id: str,
        permission_id: str,
        *,
        response: PermissionRespondRequestResponse,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Permission processed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"session/{encode_path_param(session_id)}/permissions/{encode_path_param(permission_id)}",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "response": response,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permission_reply(
        self,
        request_id: str,
        *,
        reply: PermissionReplyRequestReply,
        directory: typing.Optional[str] = None,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Permission processed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"permission/{encode_path_param(request_id)}/reply",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "reply": reply,
                "message": message,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def permission_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PermissionRequest]]:
        """
        Get all pending permission requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PermissionRequest]]
            List of pending permissions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "permission",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PermissionRequest],
                    parse_obj_as(
                        type_=typing.List[PermissionRequest],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def question_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[QuestionRequest]]:
        """
        Get all pending question requests across all sessions.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[QuestionRequest]]
            List of pending questions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "question",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[QuestionRequest],
                    parse_obj_as(
                        type_=typing.List[QuestionRequest],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def question_reply(
        self,
        request_id: str,
        *,
        answers: typing.Sequence[QuestionAnswer],
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Question answered successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"question/{encode_path_param(request_id)}/reply",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "answers": answers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def question_reject(
        self,
        request_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Question rejected successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"question/{encode_path_param(request_id)}/reject",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProviderListResponse]:
        """
        Get a list of all available AI providers, including both available and connected ones.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderListResponse]
            List of providers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "provider",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderListResponse,
                    parse_obj_as(
                        type_=ProviderListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_auth(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.List[ProviderAuthMethod]]]:
        """
        Retrieve available authentication methods for all AI providers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.List[ProviderAuthMethod]]]
            Provider auth methods
        """
        _response = await self._client_wrapper.httpx_client.request(
            "provider/auth",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[ProviderAuthMethod]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[ProviderAuthMethod]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_oauth_authorize(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderAuthAuthorization]:
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
        AsyncHttpResponse[ProviderAuthAuthorization]
            Authorization URL and method
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"provider/{encode_path_param(provider_id)}/oauth/authorize",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "method": method,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderAuthAuthorization,
                    parse_obj_as(
                        type_=ProviderAuthAuthorization,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_oauth_callback(
        self,
        provider_id: str,
        *,
        method: float,
        directory: typing.Optional[str] = None,
        code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            OAuth callback processed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"provider/{encode_path_param(provider_id)}/oauth/callback",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "method": method,
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def find_text(
        self,
        *,
        pattern: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FindTextResponseItem]]:
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
        AsyncHttpResponse[typing.List[FindTextResponseItem]]
            Matches
        """
        _response = await self._client_wrapper.httpx_client.request(
            "find",
            method="GET",
            params={
                "directory": directory,
                "pattern": pattern,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FindTextResponseItem],
                    parse_obj_as(
                        type_=typing.List[FindTextResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def find_files(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        dirs: typing.Optional[FindFilesRequestDirs] = None,
        type: typing.Optional[FindFilesRequestType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
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
        AsyncHttpResponse[typing.List[str]]
            File paths
        """
        _response = await self._client_wrapper.httpx_client.request(
            "find/file",
            method="GET",
            params={
                "directory": directory,
                "query": query,
                "dirs": dirs,
                "type": type,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def find_symbols(
        self,
        *,
        query: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Symbol]]:
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
        AsyncHttpResponse[typing.List[Symbol]]
            Symbols
        """
        _response = await self._client_wrapper.httpx_client.request(
            "find/symbol",
            method="GET",
            params={
                "directory": directory,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Symbol],
                    parse_obj_as(
                        type_=typing.List[Symbol],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def file_list(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FileNode]]:
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
        AsyncHttpResponse[typing.List[FileNode]]
            Files and directories
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file",
            method="GET",
            params={
                "directory": directory,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileNode],
                    parse_obj_as(
                        type_=typing.List[FileNode],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def file_read(
        self,
        *,
        path: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileContent]:
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
        AsyncHttpResponse[FileContent]
            File content
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file/content",
            method="GET",
            params={
                "directory": directory,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileContent,
                    parse_obj_as(
                        type_=FileContent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def file_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[File]]:
        """
        Get the git status of all files in the project.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[File]]
            File status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file/status",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[File],
                    parse_obj_as(
                        type_=typing.List[File],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, McpStatus]]:
        """
        Get the status of all Model Context Protocol (MCP) servers.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, McpStatus]]
            MCP server status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mcp",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, McpStatus],
                    parse_obj_as(
                        type_=typing.Dict[str, McpStatus],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_add(
        self,
        *,
        name: str,
        config: McpAddRequestConfig,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, McpStatus]]:
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
        AsyncHttpResponse[typing.Dict[str, McpStatus]]
            MCP server added successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mcp",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=McpAddRequestConfig, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, McpStatus],
                    parse_obj_as(
                        type_=typing.Dict[str, McpStatus],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_auth_start(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[McpAuthStartResponse]:
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
        AsyncHttpResponse[McpAuthStartResponse]
            OAuth flow started
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpAuthStartResponse,
                    parse_obj_as(
                        type_=McpAuthStartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_auth_remove(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[McpAuthRemoveResponse]:
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
        AsyncHttpResponse[McpAuthRemoveResponse]
            OAuth credentials removed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth",
            method="DELETE",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpAuthRemoveResponse,
                    parse_obj_as(
                        type_=McpAuthRemoveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_auth_callback(
        self,
        name: str,
        *,
        code: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[McpStatus]:
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
        AsyncHttpResponse[McpStatus]
            OAuth authentication completed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth/callback",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "code": code,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpStatus,
                    parse_obj_as(
                        type_=McpStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_auth_authenticate(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[McpStatus]:
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
        AsyncHttpResponse[McpStatus]
            OAuth authentication completed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/auth/authenticate",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpStatus,
                    parse_obj_as(
                        type_=McpStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_connect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            MCP server connected successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/connect",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mcp_disconnect(
        self,
        name: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            MCP server disconnected successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mcp/{encode_path_param(name)}/disconnect",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_append_prompt(
        self,
        *,
        text: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Prompt processed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/append-prompt",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_open_help(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Open the help dialog in the TUI to display user assistance information.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Help dialog opened successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/open-help",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_open_sessions(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Open the session dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Session dialog opened successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/open-sessions",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_open_themes(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Open the theme dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Theme dialog opened successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/open-themes",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_open_models(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Open the model dialog

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Model dialog opened successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/open-models",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_submit_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Submit the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Prompt submitted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/submit-prompt",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_clear_prompt(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Clear the prompt

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Prompt cleared successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/clear-prompt",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_execute_command(
        self,
        *,
        command: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Command executed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/execute-command",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "command": command,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_show_toast(
        self,
        *,
        message: str,
        variant: TuiShowToastRequestVariant,
        directory: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        duration: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Toast notification shown successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/show-toast",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "title": title,
                "message": message,
                "variant": variant,
                "duration": duration,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_publish(
        self,
        *,
        request: TuiPublishRequestBody,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Event published successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/publish",
            method="POST",
            params={
                "directory": directory,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TuiPublishRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_select_session(
        self,
        *,
        session_id: str,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Session selected successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/select-session",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "sessionID": session_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_control_next(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TuiControlNextResponse]:
        """
        Retrieve the next TUI (Terminal User Interface) request from the queue for processing.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TuiControlNextResponse]
            Next TUI request
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/control/next",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TuiControlNextResponse,
                    parse_obj_as(
                        type_=TuiControlNextResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tui_control_response(
        self,
        *,
        request: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Response submitted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tui/control/response",
            method="POST",
            params={
                "directory": directory,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def instance_dispose(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        Clean up and dispose the current OpenCode instance, releasing all resources.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            Instance disposed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "instance/dispose",
            method="POST",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def path_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Path]:
        """
        Retrieve the current working directory and related path information for the OpenCode instance.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Path]
            Path
        """
        _response = await self._client_wrapper.httpx_client.request(
            "path",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Path,
                    parse_obj_as(
                        type_=Path,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def vcs_get(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VcsInfo]:
        """
        Retrieve version control system (VCS) information for the current project, such as git branch.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VcsInfo]
            VCS info
        """
        _response = await self._client_wrapper.httpx_client.request(
            "vcs",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VcsInfo,
                    parse_obj_as(
                        type_=VcsInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def command_list(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Command]]:
        """
        Get a list of all available commands in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Command]]
            List of commands
        """
        _response = await self._client_wrapper.httpx_client.request(
            "command",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Command],
                    parse_obj_as(
                        type_=typing.List[Command],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def app_log(
        self,
        *,
        service: str,
        level: AppLogRequestLevel,
        message: str,
        directory: typing.Optional[str] = None,
        extra: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
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
        AsyncHttpResponse[bool]
            Log entry written successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "log",
            method="POST",
            params={
                "directory": directory,
            },
            json={
                "service": service,
                "level": level,
                "message": message,
                "extra": extra,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def app_agents(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Agent]]:
        """
        Get a list of all available AI agents in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Agent]]
            List of agents
        """
        _response = await self._client_wrapper.httpx_client.request(
            "agent",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Agent],
                    parse_obj_as(
                        type_=typing.List[Agent],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def app_skills(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AppSkillsResponseItem]]:
        """
        Get a list of all available skills in the OpenCode system.

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AppSkillsResponseItem]]
            List of skills
        """
        _response = await self._client_wrapper.httpx_client.request(
            "skill",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AppSkillsResponseItem],
                    parse_obj_as(
                        type_=typing.List[AppSkillsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def lsp_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LspStatus]]:
        """
        Get LSP server status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LspStatus]]
            LSP server status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lsp",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LspStatus],
                    parse_obj_as(
                        type_=typing.List[LspStatus],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def formatter_status(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[FormatterStatus]]:
        """
        Get formatter status

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FormatterStatus]]
            Formatter status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "formatter",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FormatterStatus],
                    parse_obj_as(
                        type_=typing.List[FormatterStatus],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def event_subscribe(
        self, *, directory: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[Event]]]:
        """
        Get events

        Parameters
        ----------
        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[Event]]]
            Event stream
        """
        async with self._client_wrapper.httpx_client.stream(
            "event",
            method="GET",
            params={
                "directory": directory,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[Event]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        Event,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=Event,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
