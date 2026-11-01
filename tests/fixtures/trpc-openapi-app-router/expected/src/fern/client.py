

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.echo_response import EchoResponse
from .types.greeting_response import GreetingResponse
from .types.no_input_response import NoInputResponse

if typing.TYPE_CHECKING:
    from .complex_types.client import AsyncComplexTypesClient, ComplexTypesClient
    from .inferred_returns.client import AsyncInferredReturnsClient, InferredReturnsClient
    from .named_types.client import AsyncNamedTypesClient, NamedTypesClient
    from .recursive_types.client import AsyncRecursiveTypesClient, RecursiveTypesClient
    from .simple_cases.client import AsyncSimpleCasesClient, SimpleCasesClient
    from .user.client import AsyncUserClient, UserClient

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
        self._user: typing.Optional[UserClient] = None
        self._complex_types: typing.Optional[ComplexTypesClient] = None
        self._inferred_returns: typing.Optional[InferredReturnsClient] = None
        self._named_types: typing.Optional[NamedTypesClient] = None
        self._recursive_types: typing.Optional[RecursiveTypesClient] = None
        self._simple_cases: typing.Optional[SimpleCasesClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def greeting(self, *, input: str, request_options: typing.Optional[RequestOptions] = None) -> GreetingResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GreetingResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.greeting(
            input="input",
        )
        """
        _response = self._raw_client.greeting(input=input, request_options=request_options)
        return _response.data

    def no_input(self, *, request_options: typing.Optional[RequestOptions] = None) -> NoInputResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoInputResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.no_input()
        """
        _response = self._raw_client.no_input(request_options=request_options)
        return _response.data

    def echo(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> EchoResponse:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EchoResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.echo(
            request="string",
        )
        """
        _response = self._raw_client.echo(request=request, request_options=request_options)
        return _response.data

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def complex_types(self):
        if self._complex_types is None:
            from .complex_types.client import ComplexTypesClient

            self._complex_types = ComplexTypesClient(client_wrapper=self._client_wrapper)
        return self._complex_types

    @property
    def inferred_returns(self):
        if self._inferred_returns is None:
            from .inferred_returns.client import InferredReturnsClient

            self._inferred_returns = InferredReturnsClient(client_wrapper=self._client_wrapper)
        return self._inferred_returns

    @property
    def named_types(self):
        if self._named_types is None:
            from .named_types.client import NamedTypesClient

            self._named_types = NamedTypesClient(client_wrapper=self._client_wrapper)
        return self._named_types

    @property
    def recursive_types(self):
        if self._recursive_types is None:
            from .recursive_types.client import RecursiveTypesClient

            self._recursive_types = RecursiveTypesClient(client_wrapper=self._client_wrapper)
        return self._recursive_types

    @property
    def simple_cases(self):
        if self._simple_cases is None:
            from .simple_cases.client import SimpleCasesClient

            self._simple_cases = SimpleCasesClient(client_wrapper=self._client_wrapper)
        return self._simple_cases


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
        self._user: typing.Optional[AsyncUserClient] = None
        self._complex_types: typing.Optional[AsyncComplexTypesClient] = None
        self._inferred_returns: typing.Optional[AsyncInferredReturnsClient] = None
        self._named_types: typing.Optional[AsyncNamedTypesClient] = None
        self._recursive_types: typing.Optional[AsyncRecursiveTypesClient] = None
        self._simple_cases: typing.Optional[AsyncSimpleCasesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def greeting(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GreetingResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GreetingResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.greeting(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.greeting(input=input, request_options=request_options)
        return _response.data

    async def no_input(self, *, request_options: typing.Optional[RequestOptions] = None) -> NoInputResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NoInputResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.no_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.no_input(request_options=request_options)
        return _response.data

    async def echo(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> EchoResponse:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EchoResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.echo(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.echo(request=request, request_options=request_options)
        return _response.data

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def complex_types(self):
        if self._complex_types is None:
            from .complex_types.client import AsyncComplexTypesClient

            self._complex_types = AsyncComplexTypesClient(client_wrapper=self._client_wrapper)
        return self._complex_types

    @property
    def inferred_returns(self):
        if self._inferred_returns is None:
            from .inferred_returns.client import AsyncInferredReturnsClient

            self._inferred_returns = AsyncInferredReturnsClient(client_wrapper=self._client_wrapper)
        return self._inferred_returns

    @property
    def named_types(self):
        if self._named_types is None:
            from .named_types.client import AsyncNamedTypesClient

            self._named_types = AsyncNamedTypesClient(client_wrapper=self._client_wrapper)
        return self._named_types

    @property
    def recursive_types(self):
        if self._recursive_types is None:
            from .recursive_types.client import AsyncRecursiveTypesClient

            self._recursive_types = AsyncRecursiveTypesClient(client_wrapper=self._client_wrapper)
        return self._recursive_types

    @property
    def simple_cases(self):
        if self._simple_cases is None:
            from .simple_cases.client import AsyncSimpleCasesClient

            self._simple_cases = AsyncSimpleCasesClient(client_wrapper=self._client_wrapper)
        return self._simple_cases
