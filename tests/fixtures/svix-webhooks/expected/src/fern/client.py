

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi

if typing.TYPE_CHECKING:
    from .application.client import ApplicationClient, AsyncApplicationClient
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .endpoint.client import AsyncEndpointClient, EndpointClient
    from .event_type.client import AsyncEventTypeClient, EventTypeClient
    from .health.client import AsyncHealthClient, HealthClient
    from .message.client import AsyncMessageClient, MessageClient
    from .message_attempt.client import AsyncMessageAttemptClient, MessageAttemptClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            token=token,
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
        self._application: typing.Optional[ApplicationClient] = None
        self._message_attempt: typing.Optional[MessageAttemptClient] = None
        self._endpoint: typing.Optional[EndpointClient] = None
        self._message: typing.Optional[MessageClient] = None
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._event_type: typing.Optional[EventTypeClient] = None
        self._health: typing.Optional[HealthClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_api_v1health_ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_api_v1health_ping()
        """
        _response = self._raw_client.get_api_v1health_ping(request_options=request_options)
        return _response.data

    def head_api_v1health_ping(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.head_api_v1health_ping()
        """
        _response = self._raw_client.head_api_v1health_ping(request_options=request_options)
        return _response.headers

    @property
    def application(self):
        if self._application is None:
            from .application.client import ApplicationClient

            self._application = ApplicationClient(client_wrapper=self._client_wrapper)
        return self._application

    @property
    def message_attempt(self):
        if self._message_attempt is None:
            from .message_attempt.client import MessageAttemptClient

            self._message_attempt = MessageAttemptClient(client_wrapper=self._client_wrapper)
        return self._message_attempt

    @property
    def endpoint(self):
        if self._endpoint is None:
            from .endpoint.client import EndpointClient

            self._endpoint = EndpointClient(client_wrapper=self._client_wrapper)
        return self._endpoint

    @property
    def message(self):
        if self._message is None:
            from .message.client import MessageClient

            self._message = MessageClient(client_wrapper=self._client_wrapper)
        return self._message

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def event_type(self):
        if self._event_type is None:
            from .event_type.client import EventTypeClient

            self._event_type = EventTypeClient(client_wrapper=self._client_wrapper)
        return self._event_type

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

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
            token=token,
            headers=headers,
            async_token=async_token,
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
        self._application: typing.Optional[AsyncApplicationClient] = None
        self._message_attempt: typing.Optional[AsyncMessageAttemptClient] = None
        self._endpoint: typing.Optional[AsyncEndpointClient] = None
        self._message: typing.Optional[AsyncMessageClient] = None
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._event_type: typing.Optional[AsyncEventTypeClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_api_v1health_ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_api_v1health_ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1health_ping(request_options=request_options)
        return _response.data

    async def head_api_v1health_ping(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.head_api_v1health_ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_api_v1health_ping(request_options=request_options)
        return _response.headers

    @property
    def application(self):
        if self._application is None:
            from .application.client import AsyncApplicationClient

            self._application = AsyncApplicationClient(client_wrapper=self._client_wrapper)
        return self._application

    @property
    def message_attempt(self):
        if self._message_attempt is None:
            from .message_attempt.client import AsyncMessageAttemptClient

            self._message_attempt = AsyncMessageAttemptClient(client_wrapper=self._client_wrapper)
        return self._message_attempt

    @property
    def endpoint(self):
        if self._endpoint is None:
            from .endpoint.client import AsyncEndpointClient

            self._endpoint = AsyncEndpointClient(client_wrapper=self._client_wrapper)
        return self._endpoint

    @property
    def message(self):
        if self._message is None:
            from .message.client import AsyncMessageClient

            self._message = AsyncMessageClient(client_wrapper=self._client_wrapper)
        return self._message

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def event_type(self):
        if self._event_type is None:
            from .event_type.client import AsyncEventTypeClient

            self._event_type = AsyncEventTypeClient(client_wrapper=self._client_wrapper)
        return self._event_type

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health
