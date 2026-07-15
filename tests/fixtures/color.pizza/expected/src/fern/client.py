

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.get_names_response import GetNamesResponse
from .types.possible_lists import PossibleLists


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

    def get_all_colors_of_the_default_color_name_list(
        self,
        *,
        name: str,
        list_: typing.Optional[PossibleLists] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNamesResponse:
        """
        Parameters
        ----------
        name : str
            The name of the color to retrieve (min 3 characters)

        list_ : typing.Optional[PossibleLists]
            The name of the color name list to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNamesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_colors_of_the_default_color_name_list(
            name="name",
        )
        """
        _response = self._raw_client.get_all_colors_of_the_default_color_name_list(
            name=name, list_=list_, request_options=request_options
        )
        return _response.data

    def generate_a_color_swatch_for_any_color(
        self, *, color: str, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        color : str
            The hex value of the color to retrieve without '#'

        name : typing.Optional[str]
            The name of the color

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.generate_a_color_swatch_for_any_color(
            color="color",
        )
        """
        with self._raw_client.generate_a_color_swatch_for_any_color(
            color=color, name=name, request_options=request_options
        ) as r:
            yield from r.data


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

    async def get_all_colors_of_the_default_color_name_list(
        self,
        *,
        name: str,
        list_: typing.Optional[PossibleLists] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNamesResponse:
        """
        Parameters
        ----------
        name : str
            The name of the color to retrieve (min 3 characters)

        list_ : typing.Optional[PossibleLists]
            The name of the color name list to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNamesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_colors_of_the_default_color_name_list(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_colors_of_the_default_color_name_list(
            name=name, list_=list_, request_options=request_options
        )
        return _response.data

    async def generate_a_color_swatch_for_any_color(
        self, *, color: str, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        color : str
            The hex value of the color to retrieve without '#'

        name : typing.Optional[str]
            The name of the color

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.generate_a_color_swatch_for_any_color(
                color="color",
            )


        asyncio.run(main())
        """
        async with self._raw_client.generate_a_color_swatch_for_any_color(
            color=color, name=name, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
