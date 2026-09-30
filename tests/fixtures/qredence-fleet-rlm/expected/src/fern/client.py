

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .artifacts.client import ArtifactsClient, AsyncArtifactsClient
    from .attachments.client import AsyncAttachmentsClient, AttachmentsClient
    from .health.client import AsyncHealthClient, HealthClient
    from .runs.client import AsyncRunsClient, RunsClient
    from .sessions.client import AsyncSessionsClient, SessionsClient
    from .settings.client import AsyncSettingsClient, SettingsClient
    from .skills.client import AsyncSkillsClient, SkillsClient
    from .traces.client import AsyncTracesClient, TracesClient
    from .turns.client import AsyncTurnsClient, TurnsClient
    from .volume.client import AsyncVolumeClient, VolumeClient
    from .workspace_files.client import AsyncWorkspaceFilesClient, WorkspaceFilesClient


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
        self._sessions: typing.Optional[SessionsClient] = None
        self._turns: typing.Optional[TurnsClient] = None
        self._traces: typing.Optional[TracesClient] = None
        self._attachments: typing.Optional[AttachmentsClient] = None
        self._artifacts: typing.Optional[ArtifactsClient] = None
        self._skills: typing.Optional[SkillsClient] = None
        self._runs: typing.Optional[RunsClient] = None
        self._settings: typing.Optional[SettingsClient] = None
        self._workspace_files: typing.Optional[WorkspaceFilesClient] = None
        self._volume: typing.Optional[VolumeClient] = None
        self._health: typing.Optional[HealthClient] = None

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import SessionsClient

            self._sessions = SessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def turns(self):
        if self._turns is None:
            from .turns.client import TurnsClient

            self._turns = TurnsClient(client_wrapper=self._client_wrapper)
        return self._turns

    @property
    def traces(self):
        if self._traces is None:
            from .traces.client import TracesClient

            self._traces = TracesClient(client_wrapper=self._client_wrapper)
        return self._traces

    @property
    def attachments(self):
        if self._attachments is None:
            from .attachments.client import AttachmentsClient

            self._attachments = AttachmentsClient(client_wrapper=self._client_wrapper)
        return self._attachments

    @property
    def artifacts(self):
        if self._artifacts is None:
            from .artifacts.client import ArtifactsClient

            self._artifacts = ArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def skills(self):
        if self._skills is None:
            from .skills.client import SkillsClient

            self._skills = SkillsClient(client_wrapper=self._client_wrapper)
        return self._skills

    @property
    def runs(self):
        if self._runs is None:
            from .runs.client import RunsClient

            self._runs = RunsClient(client_wrapper=self._client_wrapper)
        return self._runs

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import SettingsClient

            self._settings = SettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def workspace_files(self):
        if self._workspace_files is None:
            from .workspace_files.client import WorkspaceFilesClient

            self._workspace_files = WorkspaceFilesClient(client_wrapper=self._client_wrapper)
        return self._workspace_files

    @property
    def volume(self):
        if self._volume is None:
            from .volume.client import VolumeClient

            self._volume = VolumeClient(client_wrapper=self._client_wrapper)
        return self._volume

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health


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
        self._sessions: typing.Optional[AsyncSessionsClient] = None
        self._turns: typing.Optional[AsyncTurnsClient] = None
        self._traces: typing.Optional[AsyncTracesClient] = None
        self._attachments: typing.Optional[AsyncAttachmentsClient] = None
        self._artifacts: typing.Optional[AsyncArtifactsClient] = None
        self._skills: typing.Optional[AsyncSkillsClient] = None
        self._runs: typing.Optional[AsyncRunsClient] = None
        self._settings: typing.Optional[AsyncSettingsClient] = None
        self._workspace_files: typing.Optional[AsyncWorkspaceFilesClient] = None
        self._volume: typing.Optional[AsyncVolumeClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import AsyncSessionsClient

            self._sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def turns(self):
        if self._turns is None:
            from .turns.client import AsyncTurnsClient

            self._turns = AsyncTurnsClient(client_wrapper=self._client_wrapper)
        return self._turns

    @property
    def traces(self):
        if self._traces is None:
            from .traces.client import AsyncTracesClient

            self._traces = AsyncTracesClient(client_wrapper=self._client_wrapper)
        return self._traces

    @property
    def attachments(self):
        if self._attachments is None:
            from .attachments.client import AsyncAttachmentsClient

            self._attachments = AsyncAttachmentsClient(client_wrapper=self._client_wrapper)
        return self._attachments

    @property
    def artifacts(self):
        if self._artifacts is None:
            from .artifacts.client import AsyncArtifactsClient

            self._artifacts = AsyncArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def skills(self):
        if self._skills is None:
            from .skills.client import AsyncSkillsClient

            self._skills = AsyncSkillsClient(client_wrapper=self._client_wrapper)
        return self._skills

    @property
    def runs(self):
        if self._runs is None:
            from .runs.client import AsyncRunsClient

            self._runs = AsyncRunsClient(client_wrapper=self._client_wrapper)
        return self._runs

    @property
    def settings(self):
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            self._settings = AsyncSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings

    @property
    def workspace_files(self):
        if self._workspace_files is None:
            from .workspace_files.client import AsyncWorkspaceFilesClient

            self._workspace_files = AsyncWorkspaceFilesClient(client_wrapper=self._client_wrapper)
        return self._workspace_files

    @property
    def volume(self):
        if self._volume is None:
            from .volume.client import AsyncVolumeClient

            self._volume = AsyncVolumeClient(client_wrapper=self._client_wrapper)
        return self._volume

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health
