

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .addresses.client import AddressesClient, AsyncAddressesClient
    from .cart.client import AsyncCartClient, CartClient
    from .cart_addresses.client import AsyncCartAddressesClient, CartAddressesClient
    from .cart_lines.client import AsyncCartLinesClient, CartLinesClient
    from .collections.client import AsyncCollectionsClient, CollectionsClient
    from .countries.client import AsyncCountriesClient, CountriesClient
    from .customers.client import AsyncCustomersClient, CustomersClient
    from .media.client import AsyncMediaClient, MediaClient
    from .not_supported_yet.client import AsyncNotSupportedYetClient, NotSupportedYetClient
    from .orders.client import AsyncOrdersClient, OrdersClient
    from .products.client import AsyncProductsClient, ProductsClient
    from .shipping_options.client import AsyncShippingOptionsClient, ShippingOptionsClient


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
        self._addresses: typing.Optional[AddressesClient] = None
        self._cart: typing.Optional[CartClient] = None
        self._cart_lines: typing.Optional[CartLinesClient] = None
        self._cart_addresses: typing.Optional[CartAddressesClient] = None
        self._collections: typing.Optional[CollectionsClient] = None
        self._countries: typing.Optional[CountriesClient] = None
        self._customers: typing.Optional[CustomersClient] = None
        self._media: typing.Optional[MediaClient] = None
        self._orders: typing.Optional[OrdersClient] = None
        self._products: typing.Optional[ProductsClient] = None
        self._shipping_options: typing.Optional[ShippingOptionsClient] = None
        self._not_supported_yet: typing.Optional[NotSupportedYetClient] = None

    @property
    def addresses(self):
        if self._addresses is None:
            from .addresses.client import AddressesClient

            self._addresses = AddressesClient(client_wrapper=self._client_wrapper)
        return self._addresses

    @property
    def cart(self):
        if self._cart is None:
            from .cart.client import CartClient

            self._cart = CartClient(client_wrapper=self._client_wrapper)
        return self._cart

    @property
    def cart_lines(self):
        if self._cart_lines is None:
            from .cart_lines.client import CartLinesClient

            self._cart_lines = CartLinesClient(client_wrapper=self._client_wrapper)
        return self._cart_lines

    @property
    def cart_addresses(self):
        if self._cart_addresses is None:
            from .cart_addresses.client import CartAddressesClient

            self._cart_addresses = CartAddressesClient(client_wrapper=self._client_wrapper)
        return self._cart_addresses

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import CollectionsClient

            self._collections = CollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def countries(self):
        if self._countries is None:
            from .countries.client import CountriesClient

            self._countries = CountriesClient(client_wrapper=self._client_wrapper)
        return self._countries

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import CustomersClient

            self._customers = CustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def media(self):
        if self._media is None:
            from .media.client import MediaClient

            self._media = MediaClient(client_wrapper=self._client_wrapper)
        return self._media

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import OrdersClient

            self._orders = OrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def products(self):
        if self._products is None:
            from .products.client import ProductsClient

            self._products = ProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def shipping_options(self):
        if self._shipping_options is None:
            from .shipping_options.client import ShippingOptionsClient

            self._shipping_options = ShippingOptionsClient(client_wrapper=self._client_wrapper)
        return self._shipping_options

    @property
    def not_supported_yet(self):
        if self._not_supported_yet is None:
            from .not_supported_yet.client import NotSupportedYetClient

            self._not_supported_yet = NotSupportedYetClient(client_wrapper=self._client_wrapper)
        return self._not_supported_yet


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
        self._addresses: typing.Optional[AsyncAddressesClient] = None
        self._cart: typing.Optional[AsyncCartClient] = None
        self._cart_lines: typing.Optional[AsyncCartLinesClient] = None
        self._cart_addresses: typing.Optional[AsyncCartAddressesClient] = None
        self._collections: typing.Optional[AsyncCollectionsClient] = None
        self._countries: typing.Optional[AsyncCountriesClient] = None
        self._customers: typing.Optional[AsyncCustomersClient] = None
        self._media: typing.Optional[AsyncMediaClient] = None
        self._orders: typing.Optional[AsyncOrdersClient] = None
        self._products: typing.Optional[AsyncProductsClient] = None
        self._shipping_options: typing.Optional[AsyncShippingOptionsClient] = None
        self._not_supported_yet: typing.Optional[AsyncNotSupportedYetClient] = None

    @property
    def addresses(self):
        if self._addresses is None:
            from .addresses.client import AsyncAddressesClient

            self._addresses = AsyncAddressesClient(client_wrapper=self._client_wrapper)
        return self._addresses

    @property
    def cart(self):
        if self._cart is None:
            from .cart.client import AsyncCartClient

            self._cart = AsyncCartClient(client_wrapper=self._client_wrapper)
        return self._cart

    @property
    def cart_lines(self):
        if self._cart_lines is None:
            from .cart_lines.client import AsyncCartLinesClient

            self._cart_lines = AsyncCartLinesClient(client_wrapper=self._client_wrapper)
        return self._cart_lines

    @property
    def cart_addresses(self):
        if self._cart_addresses is None:
            from .cart_addresses.client import AsyncCartAddressesClient

            self._cart_addresses = AsyncCartAddressesClient(client_wrapper=self._client_wrapper)
        return self._cart_addresses

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import AsyncCollectionsClient

            self._collections = AsyncCollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def countries(self):
        if self._countries is None:
            from .countries.client import AsyncCountriesClient

            self._countries = AsyncCountriesClient(client_wrapper=self._client_wrapper)
        return self._countries

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import AsyncCustomersClient

            self._customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def media(self):
        if self._media is None:
            from .media.client import AsyncMediaClient

            self._media = AsyncMediaClient(client_wrapper=self._client_wrapper)
        return self._media

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import AsyncOrdersClient

            self._orders = AsyncOrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def products(self):
        if self._products is None:
            from .products.client import AsyncProductsClient

            self._products = AsyncProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def shipping_options(self):
        if self._shipping_options is None:
            from .shipping_options.client import AsyncShippingOptionsClient

            self._shipping_options = AsyncShippingOptionsClient(client_wrapper=self._client_wrapper)
        return self._shipping_options

    @property
    def not_supported_yet(self):
        if self._not_supported_yet is None:
            from .not_supported_yet.client import AsyncNotSupportedYetClient

            self._not_supported_yet = AsyncNotSupportedYetClient(client_wrapper=self._client_wrapper)
        return self._not_supported_yet


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
