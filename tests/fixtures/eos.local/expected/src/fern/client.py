

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.connections_response_item import ConnectionsResponseItem
from .types.status_response import StatusResponse


OMIT = typing.cast(typing.Any, ...)


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
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

    def connect(self, *, endpoint: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Initiate a connection to a specified peer.

        Parameters
        ----------
        endpoint : str
            the endpoint to connect to expressed as either IP address or URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connect(
            endpoint="endpoint",
        )
        """
        _response = self._raw_client.connect(endpoint=endpoint, request_options=request_options)
        return _response.data

    def connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConnectionsResponseItem]:
        """
        Returns an array of all peer connection statuses.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConnectionsResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.connections()
        """
        _response = self._raw_client.connections(request_options=request_options)
        return _response.data

    def disconnect(self, *, endpoint: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Initiate disconnection from a specified peer.

        Parameters
        ----------
        endpoint : str
            the endpoint to disconnect from, expressed as either IP address or URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.disconnect(
            endpoint="endpoint",
        )
        """
        _response = self._raw_client.disconnect(endpoint=endpoint, request_options=request_options)
        return _response.data

    def status(self, *, endpoint: str, request_options: typing.Optional[RequestOptions] = None) -> StatusResponse:
        """
        Retrieves the connection status for a specified peer.

        Parameters
        ----------
        endpoint : str
            the endpoint to get the status for, to expressed as either IP address or URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.status(
            endpoint="endpoint",
        )
        """
        _response = self._raw_client.status(endpoint=endpoint, request_options=request_options)
        return _response.data


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
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

    async def connect(self, *, endpoint: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Initiate a connection to a specified peer.

        Parameters
        ----------
        endpoint : str
            the endpoint to connect to expressed as either IP address or URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connect(
                endpoint="endpoint",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect(endpoint=endpoint, request_options=request_options)
        return _response.data

    async def connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConnectionsResponseItem]:
        """
        Returns an array of all peer connection statuses.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConnectionsResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.connections(request_options=request_options)
        return _response.data

    async def disconnect(self, *, endpoint: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Initiate disconnection from a specified peer.

        Parameters
        ----------
        endpoint : str
            the endpoint to disconnect from, expressed as either IP address or URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.disconnect(
                endpoint="endpoint",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disconnect(endpoint=endpoint, request_options=request_options)
        return _response.data

    async def status(self, *, endpoint: str, request_options: typing.Optional[RequestOptions] = None) -> StatusResponse:
        """
        Retrieves the connection status for a specified peer.

        Parameters
        ----------
        endpoint : str
            the endpoint to get the status for, to expressed as either IP address or URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.status(
                endpoint="endpoint",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.status(endpoint=endpoint, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
