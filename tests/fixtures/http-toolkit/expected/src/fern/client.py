

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .authenticated_routes.client import AsyncAuthenticatedRoutesClient, AuthenticatedRoutesClient
    from .base_routes.client import AsyncBaseRoutesClient, BaseRoutesClient
    from .inspect_routes.client import AsyncInspectRoutesClient, InspectRoutesClient
    from .utility_routes.client import AsyncUtilityRoutesClient, UtilityRoutesClient
    from .wildcard_inspection_routes.client import AsyncWildcardInspectionRoutesClient, WildcardInspectionRoutesClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
        self._base_routes: typing.Optional[BaseRoutesClient] = None
        self._wildcard_inspection_routes: typing.Optional[WildcardInspectionRoutesClient] = None
        self._authenticated_routes: typing.Optional[AuthenticatedRoutesClient] = None
        self._utility_routes: typing.Optional[UtilityRoutesClient] = None
        self._inspect_routes: typing.Optional[InspectRoutesClient] = None

    @property
    def base_routes(self):
        if self._base_routes is None:
            from .base_routes.client import BaseRoutesClient

            self._base_routes = BaseRoutesClient(client_wrapper=self._client_wrapper)
        return self._base_routes

    @property
    def wildcard_inspection_routes(self):
        if self._wildcard_inspection_routes is None:
            from .wildcard_inspection_routes.client import WildcardInspectionRoutesClient

            self._wildcard_inspection_routes = WildcardInspectionRoutesClient(client_wrapper=self._client_wrapper)
        return self._wildcard_inspection_routes

    @property
    def authenticated_routes(self):
        if self._authenticated_routes is None:
            from .authenticated_routes.client import AuthenticatedRoutesClient

            self._authenticated_routes = AuthenticatedRoutesClient(client_wrapper=self._client_wrapper)
        return self._authenticated_routes

    @property
    def utility_routes(self):
        if self._utility_routes is None:
            from .utility_routes.client import UtilityRoutesClient

            self._utility_routes = UtilityRoutesClient(client_wrapper=self._client_wrapper)
        return self._utility_routes

    @property
    def inspect_routes(self):
        if self._inspect_routes is None:
            from .inspect_routes.client import InspectRoutesClient

            self._inspect_routes = InspectRoutesClient(client_wrapper=self._client_wrapper)
        return self._inspect_routes


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

    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
        self._base_routes: typing.Optional[AsyncBaseRoutesClient] = None
        self._wildcard_inspection_routes: typing.Optional[AsyncWildcardInspectionRoutesClient] = None
        self._authenticated_routes: typing.Optional[AsyncAuthenticatedRoutesClient] = None
        self._utility_routes: typing.Optional[AsyncUtilityRoutesClient] = None
        self._inspect_routes: typing.Optional[AsyncInspectRoutesClient] = None

    @property
    def base_routes(self):
        if self._base_routes is None:
            from .base_routes.client import AsyncBaseRoutesClient

            self._base_routes = AsyncBaseRoutesClient(client_wrapper=self._client_wrapper)
        return self._base_routes

    @property
    def wildcard_inspection_routes(self):
        if self._wildcard_inspection_routes is None:
            from .wildcard_inspection_routes.client import AsyncWildcardInspectionRoutesClient

            self._wildcard_inspection_routes = AsyncWildcardInspectionRoutesClient(client_wrapper=self._client_wrapper)
        return self._wildcard_inspection_routes

    @property
    def authenticated_routes(self):
        if self._authenticated_routes is None:
            from .authenticated_routes.client import AsyncAuthenticatedRoutesClient

            self._authenticated_routes = AsyncAuthenticatedRoutesClient(client_wrapper=self._client_wrapper)
        return self._authenticated_routes

    @property
    def utility_routes(self):
        if self._utility_routes is None:
            from .utility_routes.client import AsyncUtilityRoutesClient

            self._utility_routes = AsyncUtilityRoutesClient(client_wrapper=self._client_wrapper)
        return self._utility_routes

    @property
    def inspect_routes(self):
        if self._inspect_routes is None:
            from .inspect_routes.client import AsyncInspectRoutesClient

            self._inspect_routes = AsyncInspectRoutesClient(client_wrapper=self._client_wrapper)
        return self._inspect_routes
