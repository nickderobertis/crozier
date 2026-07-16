

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
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

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
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
