

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.check_asset_for_work_orders_get_response import CheckAssetForWorkOrdersGetResponse
from .types.check_multiple_assets_for_work_orders_get_response import CheckMultipleAssetsForWorkOrdersGetResponse
from .types.create_work_order_get_response import CreateWorkOrderGetResponse
from .types.get_unhealthy_assets_get_response import GetUnhealthyAssetsGetResponse
from .types.login_token_post_response import LoginTokenPostResponse

if typing.TYPE_CHECKING:
    from .hello.client import AsyncHelloClient, HelloClient

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
        self._hello: typing.Optional[HelloClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def login_token_post(
        self,
        *,
        username: str,
        password: str,
        grant_type: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginTokenPostResponse:
        """
        Parameters
        ----------
        username : str
            The username of the user

        password : str
            The password of the user

        grant_type : typing.Optional[str]
            Grant type

        scope : typing.Optional[str]
            The scope of the user

        client_id : typing.Optional[str]
            The client id of the user

        client_secret : typing.Optional[str]
            The client id of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginTokenPostResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.login_token_post(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.login_token_post(
            username=username,
            password=password,
            grant_type=grant_type,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    def read_users_me_users_me_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        )
        client.read_users_me_users_me_get()
        """
        _response = self._raw_client.read_users_me_users_me_get(request_options=request_options)
        return _response.data

    def hello_world_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        )
        client.hello_world_get()
        """
        _response = self._raw_client.hello_world_get(request_options=request_options)
        return _response.data

    def read_items_items_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        )
        client.read_items_items_get()
        """
        _response = self._raw_client.read_items_items_get(request_options=request_options)
        return _response.data

    def get_unhealthy_assets_get(
        self, *, x_access_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUnhealthyAssetsGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUnhealthyAssetsGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_unhealthy_assets_get(
            x_access_token="x_access_token",
        )
        """
        _response = self._raw_client.get_unhealthy_assets_get(
            x_access_token=x_access_token, request_options=request_options
        )
        return _response.data

    def create_work_order_get(
        self,
        *,
        x_access_token: str,
        asset_number: str,
        site_id: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWorkOrderGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        site_id : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWorkOrderGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_work_order_get(
            x_access_token="x_access_token",
            asset_number="asset_number",
            site_id="site_id",
            description="description",
        )
        """
        _response = self._raw_client.create_work_order_get(
            x_access_token=x_access_token,
            asset_number=asset_number,
            site_id=site_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def check_asset_for_work_orders_get(
        self, *, x_access_token: str, asset_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckAssetForWorkOrdersGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAssetForWorkOrdersGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.check_asset_for_work_orders_get(
            x_access_token="x_access_token",
            asset_number="asset_number",
        )
        """
        _response = self._raw_client.check_asset_for_work_orders_get(
            x_access_token=x_access_token, asset_number=asset_number, request_options=request_options
        )
        return _response.data

    def check_multiple_assets_for_work_orders_get(
        self,
        *,
        x_access_token: str,
        comma_separated_asset_list: str,
        comma_separated_asset_uid_list: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckMultipleAssetsForWorkOrdersGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        comma_separated_asset_list : str

        comma_separated_asset_uid_list : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckMultipleAssetsForWorkOrdersGetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.check_multiple_assets_for_work_orders_get(
            x_access_token="x_access_token",
            comma_separated_asset_list="comma_separated_asset_list",
            comma_separated_asset_uid_list="comma_separated_asset_uid_list",
        )
        """
        _response = self._raw_client.check_multiple_assets_for_work_orders_get(
            x_access_token=x_access_token,
            comma_separated_asset_list=comma_separated_asset_list,
            comma_separated_asset_uid_list=comma_separated_asset_uid_list,
            request_options=request_options,
        )
        return _response.data

    @property
    def hello(self):
        if self._hello is None:
            from .hello.client import HelloClient

            self._hello = HelloClient(client_wrapper=self._client_wrapper)
        return self._hello


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
        self._hello: typing.Optional[AsyncHelloClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def login_token_post(
        self,
        *,
        username: str,
        password: str,
        grant_type: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginTokenPostResponse:
        """
        Parameters
        ----------
        username : str
            The username of the user

        password : str
            The password of the user

        grant_type : typing.Optional[str]
            Grant type

        scope : typing.Optional[str]
            The scope of the user

        client_id : typing.Optional[str]
            The client id of the user

        client_secret : typing.Optional[str]
            The client id of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginTokenPostResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.login_token_post(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login_token_post(
            username=username,
            password=password,
            grant_type=grant_type,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    async def read_users_me_users_me_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        )


        async def main() -> None:
            await client.read_users_me_users_me_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_users_me_users_me_get(request_options=request_options)
        return _response.data

    async def hello_world_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        )


        async def main() -> None:
            await client.hello_world_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.hello_world_get(request_options=request_options)
        return _response.data

    async def read_items_items_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        )


        async def main() -> None:
            await client.read_items_items_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_items_items_get(request_options=request_options)
        return _response.data

    async def get_unhealthy_assets_get(
        self, *, x_access_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUnhealthyAssetsGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUnhealthyAssetsGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_unhealthy_assets_get(
                x_access_token="x_access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_unhealthy_assets_get(
            x_access_token=x_access_token, request_options=request_options
        )
        return _response.data

    async def create_work_order_get(
        self,
        *,
        x_access_token: str,
        asset_number: str,
        site_id: str,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWorkOrderGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        site_id : str

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWorkOrderGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_work_order_get(
                x_access_token="x_access_token",
                asset_number="asset_number",
                site_id="site_id",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_work_order_get(
            x_access_token=x_access_token,
            asset_number=asset_number,
            site_id=site_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def check_asset_for_work_orders_get(
        self, *, x_access_token: str, asset_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckAssetForWorkOrdersGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        asset_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAssetForWorkOrdersGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.check_asset_for_work_orders_get(
                x_access_token="x_access_token",
                asset_number="asset_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_asset_for_work_orders_get(
            x_access_token=x_access_token, asset_number=asset_number, request_options=request_options
        )
        return _response.data

    async def check_multiple_assets_for_work_orders_get(
        self,
        *,
        x_access_token: str,
        comma_separated_asset_list: str,
        comma_separated_asset_uid_list: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckMultipleAssetsForWorkOrdersGetResponse:
        """
        Parameters
        ----------
        x_access_token : str

        comma_separated_asset_list : str

        comma_separated_asset_uid_list : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckMultipleAssetsForWorkOrdersGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.check_multiple_assets_for_work_orders_get(
                x_access_token="x_access_token",
                comma_separated_asset_list="comma_separated_asset_list",
                comma_separated_asset_uid_list="comma_separated_asset_uid_list",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_multiple_assets_for_work_orders_get(
            x_access_token=x_access_token,
            comma_separated_asset_list=comma_separated_asset_list,
            comma_separated_asset_uid_list=comma_separated_asset_uid_list,
            request_options=request_options,
        )
        return _response.data

    @property
    def hello(self):
        if self._hello is None:
            from .hello.client import AsyncHelloClient

            self._hello = AsyncHelloClient(client_wrapper=self._client_wrapper)
        return self._hello


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
