

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .escape_hatches.client import AsyncEscapeHatchesClient, EscapeHatchesClient
    from .media_types.client import AsyncMediaTypesClient, MediaTypesClient
    from .query_parameters.client import AsyncQueryParametersClient, QueryParametersClient
    from .request_headers.client import AsyncRequestHeadersClient, RequestHeadersClient
    from .route_matching.client import AsyncRouteMatchingClient, RouteMatchingClient
    from .timeout.client import AsyncTimeoutClient, TimeoutClient
    from .validation.client import AsyncValidationClient, ValidationClient


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



    host : typing.Optional[str]
        Server URL variable for 'host'. Defaults to 'localhost'.

    protocol : typing.Optional[str]
        Server URL variable for 'protocol'. Defaults to 'http'.

    port : typing.Optional[str]
        Server URL variable for 'port'. Defaults to '8080'.

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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        host: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        port: typing.Optional[str] = None,
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
        if host is not None or protocol is not None or port is not None:
            _host = host if host is not None else "localhost"
            _protocol = protocol if protocol is not None else "http"
            _port = port if port is not None else "8080"
            _environment_url_templates = {
                FernApiEnvironment.DEFAULT: "{protocol}://{host}:{port}",
            }
            _url_template = _environment_url_templates.get(environment, "{protocol}://{host}:{port}")
            if base_url is None:
                base_url = _url_template.format(host=_host, protocol=_protocol, port=_port)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._request_headers: typing.Optional[RequestHeadersClient] = None
        self._query_parameters: typing.Optional[QueryParametersClient] = None
        self._validation: typing.Optional[ValidationClient] = None
        self._media_types: typing.Optional[MediaTypesClient] = None
        self._escape_hatches: typing.Optional[EscapeHatchesClient] = None
        self._route_matching: typing.Optional[RouteMatchingClient] = None
        self._timeout: typing.Optional[TimeoutClient] = None

    @property
    def request_headers(self):
        if self._request_headers is None:
            from .request_headers.client import RequestHeadersClient

            self._request_headers = RequestHeadersClient(client_wrapper=self._client_wrapper)
        return self._request_headers

    @property
    def query_parameters(self):
        if self._query_parameters is None:
            from .query_parameters.client import QueryParametersClient

            self._query_parameters = QueryParametersClient(client_wrapper=self._client_wrapper)
        return self._query_parameters

    @property
    def validation(self):
        if self._validation is None:
            from .validation.client import ValidationClient

            self._validation = ValidationClient(client_wrapper=self._client_wrapper)
        return self._validation

    @property
    def media_types(self):
        if self._media_types is None:
            from .media_types.client import MediaTypesClient

            self._media_types = MediaTypesClient(client_wrapper=self._client_wrapper)
        return self._media_types

    @property
    def escape_hatches(self):
        if self._escape_hatches is None:
            from .escape_hatches.client import EscapeHatchesClient

            self._escape_hatches = EscapeHatchesClient(client_wrapper=self._client_wrapper)
        return self._escape_hatches

    @property
    def route_matching(self):
        if self._route_matching is None:
            from .route_matching.client import RouteMatchingClient

            self._route_matching = RouteMatchingClient(client_wrapper=self._client_wrapper)
        return self._route_matching

    @property
    def timeout(self):
        if self._timeout is None:
            from .timeout.client import TimeoutClient

            self._timeout = TimeoutClient(client_wrapper=self._client_wrapper)
        return self._timeout


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



    host : typing.Optional[str]
        Server URL variable for 'host'. Defaults to 'localhost'.

    protocol : typing.Optional[str]
        Server URL variable for 'protocol'. Defaults to 'http'.

    port : typing.Optional[str]
        Server URL variable for 'port'. Defaults to '8080'.

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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        host: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        port: typing.Optional[str] = None,
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
        if host is not None or protocol is not None or port is not None:
            _host = host if host is not None else "localhost"
            _protocol = protocol if protocol is not None else "http"
            _port = port if port is not None else "8080"
            _environment_url_templates = {
                FernApiEnvironment.DEFAULT: "{protocol}://{host}:{port}",
            }
            _url_template = _environment_url_templates.get(environment, "{protocol}://{host}:{port}")
            if base_url is None:
                base_url = _url_template.format(host=_host, protocol=_protocol, port=_port)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._request_headers: typing.Optional[AsyncRequestHeadersClient] = None
        self._query_parameters: typing.Optional[AsyncQueryParametersClient] = None
        self._validation: typing.Optional[AsyncValidationClient] = None
        self._media_types: typing.Optional[AsyncMediaTypesClient] = None
        self._escape_hatches: typing.Optional[AsyncEscapeHatchesClient] = None
        self._route_matching: typing.Optional[AsyncRouteMatchingClient] = None
        self._timeout: typing.Optional[AsyncTimeoutClient] = None

    @property
    def request_headers(self):
        if self._request_headers is None:
            from .request_headers.client import AsyncRequestHeadersClient

            self._request_headers = AsyncRequestHeadersClient(client_wrapper=self._client_wrapper)
        return self._request_headers

    @property
    def query_parameters(self):
        if self._query_parameters is None:
            from .query_parameters.client import AsyncQueryParametersClient

            self._query_parameters = AsyncQueryParametersClient(client_wrapper=self._client_wrapper)
        return self._query_parameters

    @property
    def validation(self):
        if self._validation is None:
            from .validation.client import AsyncValidationClient

            self._validation = AsyncValidationClient(client_wrapper=self._client_wrapper)
        return self._validation

    @property
    def media_types(self):
        if self._media_types is None:
            from .media_types.client import AsyncMediaTypesClient

            self._media_types = AsyncMediaTypesClient(client_wrapper=self._client_wrapper)
        return self._media_types

    @property
    def escape_hatches(self):
        if self._escape_hatches is None:
            from .escape_hatches.client import AsyncEscapeHatchesClient

            self._escape_hatches = AsyncEscapeHatchesClient(client_wrapper=self._client_wrapper)
        return self._escape_hatches

    @property
    def route_matching(self):
        if self._route_matching is None:
            from .route_matching.client import AsyncRouteMatchingClient

            self._route_matching = AsyncRouteMatchingClient(client_wrapper=self._client_wrapper)
        return self._route_matching

    @property
    def timeout(self):
        if self._timeout is None:
            from .timeout.client import AsyncTimeoutClient

            self._timeout = AsyncTimeoutClient(client_wrapper=self._client_wrapper)
        return self._timeout


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
