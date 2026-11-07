

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi

if typing.TYPE_CHECKING:
    from .auth.client import AsyncAuthClient, AuthClient
    from .clusters.client import AsyncClustersClient, ClustersClient
    from .compatibility.client import AsyncCompatibilityClient, CompatibilityClient
    from .dashboard.client import AsyncDashboardClient, DashboardClient
    from .deployments.client import AsyncDeploymentsClient, DeploymentsClient
    from .gateway.client import AsyncGatewayClient, GatewayClient
    from .instances.client import AsyncInstancesClient, InstancesClient
    from .keys.client import AsyncKeysClient, KeysClient
    from .models.client import AsyncModelsClient, ModelsClient
    from .users.client import AsyncUsersClient, UsersClient
    from .workers.client import AsyncWorkersClient, WorkersClient


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
        self._auth: typing.Optional[AuthClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._keys: typing.Optional[KeysClient] = None
        self._clusters: typing.Optional[ClustersClient] = None
        self._workers: typing.Optional[WorkersClient] = None
        self._models: typing.Optional[ModelsClient] = None
        self._instances: typing.Optional[InstancesClient] = None
        self._deployments: typing.Optional[DeploymentsClient] = None
        self._dashboard: typing.Optional[DashboardClient] = None
        self._compatibility: typing.Optional[CompatibilityClient] = None
        self._gateway: typing.Optional[GatewayClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def healthz_healthz_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.healthz_healthz_get()
        """
        _response = self._raw_client.healthz_healthz_get(request_options=request_options)
        return _response.data

    def readyz_readyz_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.readyz_readyz_get()
        """
        _response = self._raw_client.readyz_readyz_get(request_options=request_options)
        return _response.data

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def keys(self):
        if self._keys is None:
            from .keys.client import KeysClient

            self._keys = KeysClient(client_wrapper=self._client_wrapper)
        return self._keys

    @property
    def clusters(self):
        if self._clusters is None:
            from .clusters.client import ClustersClient

            self._clusters = ClustersClient(client_wrapper=self._client_wrapper)
        return self._clusters

    @property
    def workers(self):
        if self._workers is None:
            from .workers.client import WorkersClient

            self._workers = WorkersClient(client_wrapper=self._client_wrapper)
        return self._workers

    @property
    def models(self):
        if self._models is None:
            from .models.client import ModelsClient

            self._models = ModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def instances(self):
        if self._instances is None:
            from .instances.client import InstancesClient

            self._instances = InstancesClient(client_wrapper=self._client_wrapper)
        return self._instances

    @property
    def deployments(self):
        if self._deployments is None:
            from .deployments.client import DeploymentsClient

            self._deployments = DeploymentsClient(client_wrapper=self._client_wrapper)
        return self._deployments

    @property
    def dashboard(self):
        if self._dashboard is None:
            from .dashboard.client import DashboardClient

            self._dashboard = DashboardClient(client_wrapper=self._client_wrapper)
        return self._dashboard

    @property
    def compatibility(self):
        if self._compatibility is None:
            from .compatibility.client import CompatibilityClient

            self._compatibility = CompatibilityClient(client_wrapper=self._client_wrapper)
        return self._compatibility

    @property
    def gateway(self):
        if self._gateway is None:
            from .gateway.client import GatewayClient

            self._gateway = GatewayClient(client_wrapper=self._client_wrapper)
        return self._gateway


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
        self._auth: typing.Optional[AsyncAuthClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._keys: typing.Optional[AsyncKeysClient] = None
        self._clusters: typing.Optional[AsyncClustersClient] = None
        self._workers: typing.Optional[AsyncWorkersClient] = None
        self._models: typing.Optional[AsyncModelsClient] = None
        self._instances: typing.Optional[AsyncInstancesClient] = None
        self._deployments: typing.Optional[AsyncDeploymentsClient] = None
        self._dashboard: typing.Optional[AsyncDashboardClient] = None
        self._compatibility: typing.Optional[AsyncCompatibilityClient] = None
        self._gateway: typing.Optional[AsyncGatewayClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def healthz_healthz_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.healthz_healthz_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.healthz_healthz_get(request_options=request_options)
        return _response.data

    async def readyz_readyz_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.readyz_readyz_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.readyz_readyz_get(request_options=request_options)
        return _response.data

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def keys(self):
        if self._keys is None:
            from .keys.client import AsyncKeysClient

            self._keys = AsyncKeysClient(client_wrapper=self._client_wrapper)
        return self._keys

    @property
    def clusters(self):
        if self._clusters is None:
            from .clusters.client import AsyncClustersClient

            self._clusters = AsyncClustersClient(client_wrapper=self._client_wrapper)
        return self._clusters

    @property
    def workers(self):
        if self._workers is None:
            from .workers.client import AsyncWorkersClient

            self._workers = AsyncWorkersClient(client_wrapper=self._client_wrapper)
        return self._workers

    @property
    def models(self):
        if self._models is None:
            from .models.client import AsyncModelsClient

            self._models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def instances(self):
        if self._instances is None:
            from .instances.client import AsyncInstancesClient

            self._instances = AsyncInstancesClient(client_wrapper=self._client_wrapper)
        return self._instances

    @property
    def deployments(self):
        if self._deployments is None:
            from .deployments.client import AsyncDeploymentsClient

            self._deployments = AsyncDeploymentsClient(client_wrapper=self._client_wrapper)
        return self._deployments

    @property
    def dashboard(self):
        if self._dashboard is None:
            from .dashboard.client import AsyncDashboardClient

            self._dashboard = AsyncDashboardClient(client_wrapper=self._client_wrapper)
        return self._dashboard

    @property
    def compatibility(self):
        if self._compatibility is None:
            from .compatibility.client import AsyncCompatibilityClient

            self._compatibility = AsyncCompatibilityClient(client_wrapper=self._client_wrapper)
        return self._compatibility

    @property
    def gateway(self):
        if self._gateway is None:
            from .gateway.client import AsyncGatewayClient

            self._gateway = AsyncGatewayClient(client_wrapper=self._client_wrapper)
        return self._gateway
