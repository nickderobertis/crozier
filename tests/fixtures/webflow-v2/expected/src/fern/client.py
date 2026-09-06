

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .analyze.client import AnalyzeClient, AsyncAnalyzeClient
    from .assets.client import AssetsClient, AsyncAssetsClient
    from .collections.client import AsyncCollectionsClient, CollectionsClient
    from .components.client import AsyncComponentsClient, ComponentsClient
    from .custom_fonts.client import AsyncCustomFontsClient, CustomFontsClient
    from .ecommerce.client import AsyncEcommerceClient, EcommerceClient
    from .forms.client import AsyncFormsClient, FormsClient
    from .inventory.client import AsyncInventoryClient, InventoryClient
    from .orders.client import AsyncOrdersClient, OrdersClient
    from .pages.client import AsyncPagesClient, PagesClient
    from .products.client import AsyncProductsClient, ProductsClient
    from .scripts.client import AsyncScriptsClient, ScriptsClient
    from .sites.client import AsyncSitesClient, SitesClient
    from .token.client import AsyncTokenClient, TokenClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient
    from .workspaces.client import AsyncWorkspacesClient, WorkspacesClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DATA_API



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
        environment: FernApiEnvironment = FernApiEnvironment.DATA_API,
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
            environment=environment,
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
        self._token: typing.Optional[TokenClient] = None
        self._sites: typing.Optional[SitesClient] = None
        self._collections: typing.Optional[CollectionsClient] = None
        self._pages: typing.Optional[PagesClient] = None
        self._components: typing.Optional[ComponentsClient] = None
        self._scripts: typing.Optional[ScriptsClient] = None
        self._assets: typing.Optional[AssetsClient] = None
        self._custom_fonts: typing.Optional[CustomFontsClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None
        self._forms: typing.Optional[FormsClient] = None
        self._products: typing.Optional[ProductsClient] = None
        self._orders: typing.Optional[OrdersClient] = None
        self._inventory: typing.Optional[InventoryClient] = None
        self._ecommerce: typing.Optional[EcommerceClient] = None
        self._analyze: typing.Optional[AnalyzeClient] = None
        self._workspaces: typing.Optional[WorkspacesClient] = None

    @property
    def token(self):
        if self._token is None:
            from .token.client import TokenClient

            self._token = TokenClient(client_wrapper=self._client_wrapper)
        return self._token

    @property
    def sites(self):
        if self._sites is None:
            from .sites.client import SitesClient

            self._sites = SitesClient(client_wrapper=self._client_wrapper)
        return self._sites

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import CollectionsClient

            self._collections = CollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def pages(self):
        if self._pages is None:
            from .pages.client import PagesClient

            self._pages = PagesClient(client_wrapper=self._client_wrapper)
        return self._pages

    @property
    def components(self):
        if self._components is None:
            from .components.client import ComponentsClient

            self._components = ComponentsClient(client_wrapper=self._client_wrapper)
        return self._components

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import ScriptsClient

            self._scripts = ScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def assets(self):
        if self._assets is None:
            from .assets.client import AssetsClient

            self._assets = AssetsClient(client_wrapper=self._client_wrapper)
        return self._assets

    @property
    def custom_fonts(self):
        if self._custom_fonts is None:
            from .custom_fonts.client import CustomFontsClient

            self._custom_fonts = CustomFontsClient(client_wrapper=self._client_wrapper)
        return self._custom_fonts

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import FormsClient

            self._forms = FormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def products(self):
        if self._products is None:
            from .products.client import ProductsClient

            self._products = ProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import OrdersClient

            self._orders = OrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def inventory(self):
        if self._inventory is None:
            from .inventory.client import InventoryClient

            self._inventory = InventoryClient(client_wrapper=self._client_wrapper)
        return self._inventory

    @property
    def ecommerce(self):
        if self._ecommerce is None:
            from .ecommerce.client import EcommerceClient

            self._ecommerce = EcommerceClient(client_wrapper=self._client_wrapper)
        return self._ecommerce

    @property
    def analyze(self):
        if self._analyze is None:
            from .analyze.client import AnalyzeClient

            self._analyze = AnalyzeClient(client_wrapper=self._client_wrapper)
        return self._analyze

    @property
    def workspaces(self):
        if self._workspaces is None:
            from .workspaces.client import WorkspacesClient

            self._workspaces = WorkspacesClient(client_wrapper=self._client_wrapper)
        return self._workspaces


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
    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DATA_API



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
        environment: FernApiEnvironment = FernApiEnvironment.DATA_API,
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
            environment=environment,
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
        self._token: typing.Optional[AsyncTokenClient] = None
        self._sites: typing.Optional[AsyncSitesClient] = None
        self._collections: typing.Optional[AsyncCollectionsClient] = None
        self._pages: typing.Optional[AsyncPagesClient] = None
        self._components: typing.Optional[AsyncComponentsClient] = None
        self._scripts: typing.Optional[AsyncScriptsClient] = None
        self._assets: typing.Optional[AsyncAssetsClient] = None
        self._custom_fonts: typing.Optional[AsyncCustomFontsClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None
        self._forms: typing.Optional[AsyncFormsClient] = None
        self._products: typing.Optional[AsyncProductsClient] = None
        self._orders: typing.Optional[AsyncOrdersClient] = None
        self._inventory: typing.Optional[AsyncInventoryClient] = None
        self._ecommerce: typing.Optional[AsyncEcommerceClient] = None
        self._analyze: typing.Optional[AsyncAnalyzeClient] = None
        self._workspaces: typing.Optional[AsyncWorkspacesClient] = None

    @property
    def token(self):
        if self._token is None:
            from .token.client import AsyncTokenClient

            self._token = AsyncTokenClient(client_wrapper=self._client_wrapper)
        return self._token

    @property
    def sites(self):
        if self._sites is None:
            from .sites.client import AsyncSitesClient

            self._sites = AsyncSitesClient(client_wrapper=self._client_wrapper)
        return self._sites

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import AsyncCollectionsClient

            self._collections = AsyncCollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def pages(self):
        if self._pages is None:
            from .pages.client import AsyncPagesClient

            self._pages = AsyncPagesClient(client_wrapper=self._client_wrapper)
        return self._pages

    @property
    def components(self):
        if self._components is None:
            from .components.client import AsyncComponentsClient

            self._components = AsyncComponentsClient(client_wrapper=self._client_wrapper)
        return self._components

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import AsyncScriptsClient

            self._scripts = AsyncScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def assets(self):
        if self._assets is None:
            from .assets.client import AsyncAssetsClient

            self._assets = AsyncAssetsClient(client_wrapper=self._client_wrapper)
        return self._assets

    @property
    def custom_fonts(self):
        if self._custom_fonts is None:
            from .custom_fonts.client import AsyncCustomFontsClient

            self._custom_fonts = AsyncCustomFontsClient(client_wrapper=self._client_wrapper)
        return self._custom_fonts

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import AsyncFormsClient

            self._forms = AsyncFormsClient(client_wrapper=self._client_wrapper)
        return self._forms

    @property
    def products(self):
        if self._products is None:
            from .products.client import AsyncProductsClient

            self._products = AsyncProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import AsyncOrdersClient

            self._orders = AsyncOrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def inventory(self):
        if self._inventory is None:
            from .inventory.client import AsyncInventoryClient

            self._inventory = AsyncInventoryClient(client_wrapper=self._client_wrapper)
        return self._inventory

    @property
    def ecommerce(self):
        if self._ecommerce is None:
            from .ecommerce.client import AsyncEcommerceClient

            self._ecommerce = AsyncEcommerceClient(client_wrapper=self._client_wrapper)
        return self._ecommerce

    @property
    def analyze(self):
        if self._analyze is None:
            from .analyze.client import AsyncAnalyzeClient

            self._analyze = AsyncAnalyzeClient(client_wrapper=self._client_wrapper)
        return self._analyze

    @property
    def workspaces(self):
        if self._workspaces is None:
            from .workspaces.client import AsyncWorkspacesClient

            self._workspaces = AsyncWorkspacesClient(client_wrapper=self._client_wrapper)
        return self._workspaces
