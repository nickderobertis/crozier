

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.fault_simulation_dto import FaultSimulationDto


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

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def list_faults(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Lists all of the faults that the proxy is capable of simulating.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful operation. Returns a list of all fault names.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_faults()
        """
        _response = self._raw_client.list_faults(request_options=request_options)
        return _response.data

    def create_fault_simulation(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FaultSimulationDto:
        """
        A fault simulation implements a specific type of connectivity fault that might occur during the use of the Asset Tracking SDK. In order to simulate a fault, it creates and manipulates a proxy that transparently sits between the client and the Ably Realtime service. The fault simulation returned by this endpoint provides details of how a client can connect to its proxy.

        Faults also specify what state Trackables should enter during a fault and after it has been resolved, so that assertions can be made while testing common use-cases.

        A fault simulation does not have any effect on the connection’s behaviour until it is _enabled_. To enable a fault simulation, use the `POST /fault-simulations/{id}/enable` endpoint.

        At the moment, all created proxies listen on the same port, so it is not possible to have multiple proxies active simultaneously – in order to create a new fault simulation you must first clean up the previous one using the `POST /fault-simulations/{id}/clean-up` endpoint. This is a limitation of the current implementation, which will be resolved in the future.

        Parameters
        ----------
        name : str
            Name of fault to create a simulation for. This must be one of the fault names returned by the `GET /faults` endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FaultSimulationDto
            Successful operation. Returns a representation of the created fault simulation and details of how to connect to its proxy.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.create_fault_simulation(
            name="name",
        )
        """
        _response = self._raw_client.create_fault_simulation(name, request_options=request_options)
        return _response.data

    def enable_fault_simulation(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Breaks the proxy using the fault-specific failure conditions.

        Parameters
        ----------
        id : str
            ID of fault simulation to enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.enable_fault_simulation(
            id="id",
        )
        """
        _response = self._raw_client.enable_fault_simulation(id, request_options=request_options)
        return _response.data

    def resolve_fault_simulation(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Restores the proxy to normal functionality.

        Parameters
        ----------
        id : str
            ID of fault simulation to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resolve_fault_simulation(
            id="id",
        )
        """
        _response = self._raw_client.resolve_fault_simulation(id, request_options=request_options)
        return _response.data

    def clean_up_fault_simulation(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Stops the proxy. This should be called at the end of each test case that creates a fault simulation.

        Parameters
        ----------
        id : str
            ID of fault simulation to clean up

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.clean_up_fault_simulation(
            id="id",
        )
        """
        _response = self._raw_client.clean_up_fault_simulation(id, request_options=request_options)
        return _response.data


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

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def list_faults(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Lists all of the faults that the proxy is capable of simulating.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful operation. Returns a list of all fault names.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_faults()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_faults(request_options=request_options)
        return _response.data

    async def create_fault_simulation(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FaultSimulationDto:
        """
        A fault simulation implements a specific type of connectivity fault that might occur during the use of the Asset Tracking SDK. In order to simulate a fault, it creates and manipulates a proxy that transparently sits between the client and the Ably Realtime service. The fault simulation returned by this endpoint provides details of how a client can connect to its proxy.

        Faults also specify what state Trackables should enter during a fault and after it has been resolved, so that assertions can be made while testing common use-cases.

        A fault simulation does not have any effect on the connection’s behaviour until it is _enabled_. To enable a fault simulation, use the `POST /fault-simulations/{id}/enable` endpoint.

        At the moment, all created proxies listen on the same port, so it is not possible to have multiple proxies active simultaneously – in order to create a new fault simulation you must first clean up the previous one using the `POST /fault-simulations/{id}/clean-up` endpoint. This is a limitation of the current implementation, which will be resolved in the future.

        Parameters
        ----------
        name : str
            Name of fault to create a simulation for. This must be one of the fault names returned by the `GET /faults` endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FaultSimulationDto
            Successful operation. Returns a representation of the created fault simulation and details of how to connect to its proxy.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.create_fault_simulation(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_fault_simulation(name, request_options=request_options)
        return _response.data

    async def enable_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Breaks the proxy using the fault-specific failure conditions.

        Parameters
        ----------
        id : str
            ID of fault simulation to enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.enable_fault_simulation(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_fault_simulation(id, request_options=request_options)
        return _response.data

    async def resolve_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Restores the proxy to normal functionality.

        Parameters
        ----------
        id : str
            ID of fault simulation to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resolve_fault_simulation(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_fault_simulation(id, request_options=request_options)
        return _response.data

    async def clean_up_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stops the proxy. This should be called at the end of each test case that creates a fault simulation.

        Parameters
        ----------
        id : str
            ID of fault simulation to clean up

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.clean_up_fault_simulation(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clean_up_fault_simulation(id, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
