

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.resource import Resource

if typing.TYPE_CHECKING:
    from .config.client import AsyncConfigClient, ConfigClient
    from .job.client import AsyncJobClient, JobClient
    from .metrics.client import AsyncMetricsClient, MetricsClient
    from .mock.client import AsyncMockClient, MockClient
    from .test.client import AsyncTestClient, TestClient


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



    token : typing.Union[str, typing.Callable[[], str]]
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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._job: typing.Optional[JobClient] = None
        self._mock: typing.Optional[MockClient] = None
        self._config: typing.Optional[ConfigClient] = None
        self._metrics: typing.Optional[MetricsClient] = None
        self._test: typing.Optional[TestClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_resources_by_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Resource]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of the Service or API the resources are attached to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Resource]
            List the resources attached to a Service or API

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_resources_by_service(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.get_resources_by_service(service_id, request_options=request_options)
        return _response.data

    def get_resource(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Resource:
        """
        Parameters
        ----------
        name : str
            Unique name/business identifier of the Service or API resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Resource
            Retrieve the resource having this name

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_resource(
            name="name",
        )
        """
        _response = self._raw_client.get_resource(name, request_options=request_options)
        return _response.data

    @property
    def job(self):
        if self._job is None:
            from .job.client import JobClient

            self._job = JobClient(client_wrapper=self._client_wrapper)
        return self._job

    @property
    def mock(self):
        if self._mock is None:
            from .mock.client import MockClient

            self._mock = MockClient(client_wrapper=self._client_wrapper)
        return self._mock

    @property
    def config(self):
        if self._config is None:
            from .config.client import ConfigClient

            self._config = ConfigClient(client_wrapper=self._client_wrapper)
        return self._config

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import MetricsClient

            self._metrics = MetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def test(self):
        if self._test is None:
            from .test.client import TestClient

            self._test = TestClient(client_wrapper=self._client_wrapper)
        return self._test


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



    token : typing.Union[str, typing.Callable[[], str]]
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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._job: typing.Optional[AsyncJobClient] = None
        self._mock: typing.Optional[AsyncMockClient] = None
        self._config: typing.Optional[AsyncConfigClient] = None
        self._metrics: typing.Optional[AsyncMetricsClient] = None
        self._test: typing.Optional[AsyncTestClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_resources_by_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Resource]:
        """
        Parameters
        ----------
        service_id : str
            Unique identifier of the Service or API the resources are attached to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Resource]
            List the resources attached to a Service or API

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_resources_by_service(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_resources_by_service(service_id, request_options=request_options)
        return _response.data

    async def get_resource(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Resource:
        """
        Parameters
        ----------
        name : str
            Unique name/business identifier of the Service or API resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Resource
            Retrieve the resource having this name

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_resource(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_resource(name, request_options=request_options)
        return _response.data

    @property
    def job(self):
        if self._job is None:
            from .job.client import AsyncJobClient

            self._job = AsyncJobClient(client_wrapper=self._client_wrapper)
        return self._job

    @property
    def mock(self):
        if self._mock is None:
            from .mock.client import AsyncMockClient

            self._mock = AsyncMockClient(client_wrapper=self._client_wrapper)
        return self._mock

    @property
    def config(self):
        if self._config is None:
            from .config.client import AsyncConfigClient

            self._config = AsyncConfigClient(client_wrapper=self._client_wrapper)
        return self._config

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import AsyncMetricsClient

            self._metrics = AsyncMetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def test(self):
        if self._test is None:
            from .test.client import AsyncTestClient

            self._test = AsyncTestClient(client_wrapper=self._client_wrapper)
        return self._test


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
