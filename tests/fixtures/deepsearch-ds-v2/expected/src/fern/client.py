

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .content_manager.client import AsyncContentManagerClient, ContentManagerClient
    from .data_indices.client import AsyncDataIndicesClient, DataIndicesClient
    from .data_indices_upload.client import AsyncDataIndicesUploadClient, DataIndicesUploadClient
    from .knowledge_graphs.client import AsyncKnowledgeGraphsClient, KnowledgeGraphsClient
    from .project.client import AsyncProjectClient, ProjectClient
    from .semantic.client import AsyncSemanticClient, SemanticClient
    from .system.client import AsyncSystemClient, SystemClient
    from .system_flavours.client import AsyncSystemFlavoursClient, SystemFlavoursClient
    from .system_quotas.client import AsyncSystemQuotasClient, SystemQuotasClient
    from .system_summary.client import AsyncSystemSummaryClient, SystemSummaryClient
    from .tasks.client import AsyncTasksClient, TasksClient
    from .upload.client import AsyncUploadClient, UploadClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
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
        self._content_manager: typing.Optional[ContentManagerClient] = None
        self._data_indices: typing.Optional[DataIndicesClient] = None
        self._data_indices_upload: typing.Optional[DataIndicesUploadClient] = None
        self._knowledge_graphs: typing.Optional[KnowledgeGraphsClient] = None
        self._project: typing.Optional[ProjectClient] = None
        self._semantic: typing.Optional[SemanticClient] = None
        self._system: typing.Optional[SystemClient] = None
        self._system_flavours: typing.Optional[SystemFlavoursClient] = None
        self._system_summary: typing.Optional[SystemSummaryClient] = None
        self._system_quotas: typing.Optional[SystemQuotasClient] = None
        self._tasks: typing.Optional[TasksClient] = None
        self._upload: typing.Optional[UploadClient] = None

    @property
    def content_manager(self):
        if self._content_manager is None:
            from .content_manager.client import ContentManagerClient

            self._content_manager = ContentManagerClient(client_wrapper=self._client_wrapper)
        return self._content_manager

    @property
    def data_indices(self):
        if self._data_indices is None:
            from .data_indices.client import DataIndicesClient

            self._data_indices = DataIndicesClient(client_wrapper=self._client_wrapper)
        return self._data_indices

    @property
    def data_indices_upload(self):
        if self._data_indices_upload is None:
            from .data_indices_upload.client import DataIndicesUploadClient

            self._data_indices_upload = DataIndicesUploadClient(client_wrapper=self._client_wrapper)
        return self._data_indices_upload

    @property
    def knowledge_graphs(self):
        if self._knowledge_graphs is None:
            from .knowledge_graphs.client import KnowledgeGraphsClient

            self._knowledge_graphs = KnowledgeGraphsClient(client_wrapper=self._client_wrapper)
        return self._knowledge_graphs

    @property
    def project(self):
        if self._project is None:
            from .project.client import ProjectClient

            self._project = ProjectClient(client_wrapper=self._client_wrapper)
        return self._project

    @property
    def semantic(self):
        if self._semantic is None:
            from .semantic.client import SemanticClient

            self._semantic = SemanticClient(client_wrapper=self._client_wrapper)
        return self._semantic

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def system_flavours(self):
        if self._system_flavours is None:
            from .system_flavours.client import SystemFlavoursClient

            self._system_flavours = SystemFlavoursClient(client_wrapper=self._client_wrapper)
        return self._system_flavours

    @property
    def system_summary(self):
        if self._system_summary is None:
            from .system_summary.client import SystemSummaryClient

            self._system_summary = SystemSummaryClient(client_wrapper=self._client_wrapper)
        return self._system_summary

    @property
    def system_quotas(self):
        if self._system_quotas is None:
            from .system_quotas.client import SystemQuotasClient

            self._system_quotas = SystemQuotasClient(client_wrapper=self._client_wrapper)
        return self._system_quotas

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import TasksClient

            self._tasks = TasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def upload(self):
        if self._upload is None:
            from .upload.client import UploadClient

            self._upload = UploadClient(client_wrapper=self._client_wrapper)
        return self._upload


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
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
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
        self._content_manager: typing.Optional[AsyncContentManagerClient] = None
        self._data_indices: typing.Optional[AsyncDataIndicesClient] = None
        self._data_indices_upload: typing.Optional[AsyncDataIndicesUploadClient] = None
        self._knowledge_graphs: typing.Optional[AsyncKnowledgeGraphsClient] = None
        self._project: typing.Optional[AsyncProjectClient] = None
        self._semantic: typing.Optional[AsyncSemanticClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None
        self._system_flavours: typing.Optional[AsyncSystemFlavoursClient] = None
        self._system_summary: typing.Optional[AsyncSystemSummaryClient] = None
        self._system_quotas: typing.Optional[AsyncSystemQuotasClient] = None
        self._tasks: typing.Optional[AsyncTasksClient] = None
        self._upload: typing.Optional[AsyncUploadClient] = None

    @property
    def content_manager(self):
        if self._content_manager is None:
            from .content_manager.client import AsyncContentManagerClient

            self._content_manager = AsyncContentManagerClient(client_wrapper=self._client_wrapper)
        return self._content_manager

    @property
    def data_indices(self):
        if self._data_indices is None:
            from .data_indices.client import AsyncDataIndicesClient

            self._data_indices = AsyncDataIndicesClient(client_wrapper=self._client_wrapper)
        return self._data_indices

    @property
    def data_indices_upload(self):
        if self._data_indices_upload is None:
            from .data_indices_upload.client import AsyncDataIndicesUploadClient

            self._data_indices_upload = AsyncDataIndicesUploadClient(client_wrapper=self._client_wrapper)
        return self._data_indices_upload

    @property
    def knowledge_graphs(self):
        if self._knowledge_graphs is None:
            from .knowledge_graphs.client import AsyncKnowledgeGraphsClient

            self._knowledge_graphs = AsyncKnowledgeGraphsClient(client_wrapper=self._client_wrapper)
        return self._knowledge_graphs

    @property
    def project(self):
        if self._project is None:
            from .project.client import AsyncProjectClient

            self._project = AsyncProjectClient(client_wrapper=self._client_wrapper)
        return self._project

    @property
    def semantic(self):
        if self._semantic is None:
            from .semantic.client import AsyncSemanticClient

            self._semantic = AsyncSemanticClient(client_wrapper=self._client_wrapper)
        return self._semantic

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def system_flavours(self):
        if self._system_flavours is None:
            from .system_flavours.client import AsyncSystemFlavoursClient

            self._system_flavours = AsyncSystemFlavoursClient(client_wrapper=self._client_wrapper)
        return self._system_flavours

    @property
    def system_summary(self):
        if self._system_summary is None:
            from .system_summary.client import AsyncSystemSummaryClient

            self._system_summary = AsyncSystemSummaryClient(client_wrapper=self._client_wrapper)
        return self._system_summary

    @property
    def system_quotas(self):
        if self._system_quotas is None:
            from .system_quotas.client import AsyncSystemQuotasClient

            self._system_quotas = AsyncSystemQuotasClient(client_wrapper=self._client_wrapper)
        return self._system_quotas

    @property
    def tasks(self):
        if self._tasks is None:
            from .tasks.client import AsyncTasksClient

            self._tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        return self._tasks

    @property
    def upload(self):
        if self._upload is None:
            from .upload.client import AsyncUploadClient

            self._upload = AsyncUploadClient(client_wrapper=self._client_wrapper)
        return self._upload


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
