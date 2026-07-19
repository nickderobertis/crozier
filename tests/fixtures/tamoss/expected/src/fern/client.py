

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .flow_delete_requests.client import AsyncFlowDeleteRequestsClient, FlowDeleteRequestsClient
    from .flow_segments.client import AsyncFlowSegmentsClient, FlowSegmentsClient
    from .flows.client import AsyncFlowsClient, FlowsClient
    from .media_storage.client import AsyncMediaStorageClient, MediaStorageClient
    from .objects.client import AsyncObjectsClient, ObjectsClient
    from .service.client import AsyncServiceClient, ServiceClient
    from .sources.client import AsyncSourcesClient, SourcesClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
            username=username,
            password=password,
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
        self._service: typing.Optional[ServiceClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None
        self._sources: typing.Optional[SourcesClient] = None
        self._flows: typing.Optional[FlowsClient] = None
        self._flow_segments: typing.Optional[FlowSegmentsClient] = None
        self._media_storage: typing.Optional[MediaStorageClient] = None
        self._objects: typing.Optional[ObjectsClient] = None
        self._flow_delete_requests: typing.Optional[FlowDeleteRequestsClient] = None

    @property
    def service(self):
        if self._service is None:
            from .service.client import ServiceClient

            self._service = ServiceClient(client_wrapper=self._client_wrapper)
        return self._service

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def sources(self):
        if self._sources is None:
            from .sources.client import SourcesClient

            self._sources = SourcesClient(client_wrapper=self._client_wrapper)
        return self._sources

    @property
    def flows(self):
        if self._flows is None:
            from .flows.client import FlowsClient

            self._flows = FlowsClient(client_wrapper=self._client_wrapper)
        return self._flows

    @property
    def flow_segments(self):
        if self._flow_segments is None:
            from .flow_segments.client import FlowSegmentsClient

            self._flow_segments = FlowSegmentsClient(client_wrapper=self._client_wrapper)
        return self._flow_segments

    @property
    def media_storage(self):
        if self._media_storage is None:
            from .media_storage.client import MediaStorageClient

            self._media_storage = MediaStorageClient(client_wrapper=self._client_wrapper)
        return self._media_storage

    @property
    def objects(self):
        if self._objects is None:
            from .objects.client import ObjectsClient

            self._objects = ObjectsClient(client_wrapper=self._client_wrapper)
        return self._objects

    @property
    def flow_delete_requests(self):
        if self._flow_delete_requests is None:
            from .flow_delete_requests.client import FlowDeleteRequestsClient

            self._flow_delete_requests = FlowDeleteRequestsClient(client_wrapper=self._client_wrapper)
        return self._flow_delete_requests


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
            username=username,
            password=password,
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
        self._service: typing.Optional[AsyncServiceClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None
        self._sources: typing.Optional[AsyncSourcesClient] = None
        self._flows: typing.Optional[AsyncFlowsClient] = None
        self._flow_segments: typing.Optional[AsyncFlowSegmentsClient] = None
        self._media_storage: typing.Optional[AsyncMediaStorageClient] = None
        self._objects: typing.Optional[AsyncObjectsClient] = None
        self._flow_delete_requests: typing.Optional[AsyncFlowDeleteRequestsClient] = None

    @property
    def service(self):
        if self._service is None:
            from .service.client import AsyncServiceClient

            self._service = AsyncServiceClient(client_wrapper=self._client_wrapper)
        return self._service

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def sources(self):
        if self._sources is None:
            from .sources.client import AsyncSourcesClient

            self._sources = AsyncSourcesClient(client_wrapper=self._client_wrapper)
        return self._sources

    @property
    def flows(self):
        if self._flows is None:
            from .flows.client import AsyncFlowsClient

            self._flows = AsyncFlowsClient(client_wrapper=self._client_wrapper)
        return self._flows

    @property
    def flow_segments(self):
        if self._flow_segments is None:
            from .flow_segments.client import AsyncFlowSegmentsClient

            self._flow_segments = AsyncFlowSegmentsClient(client_wrapper=self._client_wrapper)
        return self._flow_segments

    @property
    def media_storage(self):
        if self._media_storage is None:
            from .media_storage.client import AsyncMediaStorageClient

            self._media_storage = AsyncMediaStorageClient(client_wrapper=self._client_wrapper)
        return self._media_storage

    @property
    def objects(self):
        if self._objects is None:
            from .objects.client import AsyncObjectsClient

            self._objects = AsyncObjectsClient(client_wrapper=self._client_wrapper)
        return self._objects

    @property
    def flow_delete_requests(self):
        if self._flow_delete_requests is None:
            from .flow_delete_requests.client import AsyncFlowDeleteRequestsClient

            self._flow_delete_requests = AsyncFlowDeleteRequestsClient(client_wrapper=self._client_wrapper)
        return self._flow_delete_requests


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
