

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .articles.client import ArticlesClient, AsyncArticlesClient
    from .categories.client import AsyncCategoriesClient, CategoriesClient
    from .comparison_shopping_pages.client import AsyncComparisonShoppingPagesClient, ComparisonShoppingPagesClient
    from .conversations.client import AsyncConversationsClient, ConversationsClient
    from .countries.client import AsyncCountriesClient, CountriesClient
    from .csps.client import AsyncCspsClient, CspsClient
    from .curated_sets.client import AsyncCuratedSetsClient, CuratedSetsClient
    from .currencies.client import AsyncCurrenciesClient, CurrenciesClient
    from .feedback.client import AsyncFeedbackClient, FeedbackClient
    from .handpicked.client import AsyncHandpickedClient, HandpickedClient
    from .listing_conditions.client import AsyncListingConditionsClient, ListingConditionsClient
    from .listings.client import AsyncListingsClient, ListingsClient
    from .my.client import AsyncMyClient, MyClient
    from .orders.client import AsyncOrdersClient, OrdersClient
    from .payment_methods.client import AsyncPaymentMethodsClient, PaymentMethodsClient
    from .priceguide.client import AsyncPriceguideClient, PriceguideClient
    from .products.client import AsyncProductsClient, ProductsClient
    from .sales.client import AsyncSalesClient, SalesClient
    from .shipping.client import AsyncShippingClient, ShippingClient
    from .shop.client import AsyncShopClient, ShopClient
    from .shops.client import AsyncShopsClient, ShopsClient
    from .wants.client import AsyncWantsClient, WantsClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient


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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._articles: typing.Optional[ArticlesClient] = None
        self._categories: typing.Optional[CategoriesClient] = None
        self._comparison_shopping_pages: typing.Optional[ComparisonShoppingPagesClient] = None
        self._conversations: typing.Optional[ConversationsClient] = None
        self._countries: typing.Optional[CountriesClient] = None
        self._csps: typing.Optional[CspsClient] = None
        self._curated_sets: typing.Optional[CuratedSetsClient] = None
        self._currencies: typing.Optional[CurrenciesClient] = None
        self._feedback: typing.Optional[FeedbackClient] = None
        self._handpicked: typing.Optional[HandpickedClient] = None
        self._listing_conditions: typing.Optional[ListingConditionsClient] = None
        self._listings: typing.Optional[ListingsClient] = None
        self._my: typing.Optional[MyClient] = None
        self._orders: typing.Optional[OrdersClient] = None
        self._payment_methods: typing.Optional[PaymentMethodsClient] = None
        self._priceguide: typing.Optional[PriceguideClient] = None
        self._products: typing.Optional[ProductsClient] = None
        self._sales: typing.Optional[SalesClient] = None
        self._shipping: typing.Optional[ShippingClient] = None
        self._shop: typing.Optional[ShopClient] = None
        self._shops: typing.Optional[ShopsClient] = None
        self._wants: typing.Optional[WantsClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None

    @property
    def articles(self):
        if self._articles is None:
            from .articles.client import ArticlesClient

            self._articles = ArticlesClient(client_wrapper=self._client_wrapper)
        return self._articles

    @property
    def categories(self):
        if self._categories is None:
            from .categories.client import CategoriesClient

            self._categories = CategoriesClient(client_wrapper=self._client_wrapper)
        return self._categories

    @property
    def comparison_shopping_pages(self):
        if self._comparison_shopping_pages is None:
            from .comparison_shopping_pages.client import ComparisonShoppingPagesClient

            self._comparison_shopping_pages = ComparisonShoppingPagesClient(client_wrapper=self._client_wrapper)
        return self._comparison_shopping_pages

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import ConversationsClient

            self._conversations = ConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def countries(self):
        if self._countries is None:
            from .countries.client import CountriesClient

            self._countries = CountriesClient(client_wrapper=self._client_wrapper)
        return self._countries

    @property
    def csps(self):
        if self._csps is None:
            from .csps.client import CspsClient

            self._csps = CspsClient(client_wrapper=self._client_wrapper)
        return self._csps

    @property
    def curated_sets(self):
        if self._curated_sets is None:
            from .curated_sets.client import CuratedSetsClient

            self._curated_sets = CuratedSetsClient(client_wrapper=self._client_wrapper)
        return self._curated_sets

    @property
    def currencies(self):
        if self._currencies is None:
            from .currencies.client import CurrenciesClient

            self._currencies = CurrenciesClient(client_wrapper=self._client_wrapper)
        return self._currencies

    @property
    def feedback(self):
        if self._feedback is None:
            from .feedback.client import FeedbackClient

            self._feedback = FeedbackClient(client_wrapper=self._client_wrapper)
        return self._feedback

    @property
    def handpicked(self):
        if self._handpicked is None:
            from .handpicked.client import HandpickedClient

            self._handpicked = HandpickedClient(client_wrapper=self._client_wrapper)
        return self._handpicked

    @property
    def listing_conditions(self):
        if self._listing_conditions is None:
            from .listing_conditions.client import ListingConditionsClient

            self._listing_conditions = ListingConditionsClient(client_wrapper=self._client_wrapper)
        return self._listing_conditions

    @property
    def listings(self):
        if self._listings is None:
            from .listings.client import ListingsClient

            self._listings = ListingsClient(client_wrapper=self._client_wrapper)
        return self._listings

    @property
    def my(self):
        if self._my is None:
            from .my.client import MyClient

            self._my = MyClient(client_wrapper=self._client_wrapper)
        return self._my

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import OrdersClient

            self._orders = OrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def payment_methods(self):
        if self._payment_methods is None:
            from .payment_methods.client import PaymentMethodsClient

            self._payment_methods = PaymentMethodsClient(client_wrapper=self._client_wrapper)
        return self._payment_methods

    @property
    def priceguide(self):
        if self._priceguide is None:
            from .priceguide.client import PriceguideClient

            self._priceguide = PriceguideClient(client_wrapper=self._client_wrapper)
        return self._priceguide

    @property
    def products(self):
        if self._products is None:
            from .products.client import ProductsClient

            self._products = ProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def sales(self):
        if self._sales is None:
            from .sales.client import SalesClient

            self._sales = SalesClient(client_wrapper=self._client_wrapper)
        return self._sales

    @property
    def shipping(self):
        if self._shipping is None:
            from .shipping.client import ShippingClient

            self._shipping = ShippingClient(client_wrapper=self._client_wrapper)
        return self._shipping

    @property
    def shop(self):
        if self._shop is None:
            from .shop.client import ShopClient

            self._shop = ShopClient(client_wrapper=self._client_wrapper)
        return self._shop

    @property
    def shops(self):
        if self._shops is None:
            from .shops.client import ShopsClient

            self._shops = ShopsClient(client_wrapper=self._client_wrapper)
        return self._shops

    @property
    def wants(self):
        if self._wants is None:
            from .wants.client import WantsClient

            self._wants = WantsClient(client_wrapper=self._client_wrapper)
        return self._wants

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks


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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._articles: typing.Optional[AsyncArticlesClient] = None
        self._categories: typing.Optional[AsyncCategoriesClient] = None
        self._comparison_shopping_pages: typing.Optional[AsyncComparisonShoppingPagesClient] = None
        self._conversations: typing.Optional[AsyncConversationsClient] = None
        self._countries: typing.Optional[AsyncCountriesClient] = None
        self._csps: typing.Optional[AsyncCspsClient] = None
        self._curated_sets: typing.Optional[AsyncCuratedSetsClient] = None
        self._currencies: typing.Optional[AsyncCurrenciesClient] = None
        self._feedback: typing.Optional[AsyncFeedbackClient] = None
        self._handpicked: typing.Optional[AsyncHandpickedClient] = None
        self._listing_conditions: typing.Optional[AsyncListingConditionsClient] = None
        self._listings: typing.Optional[AsyncListingsClient] = None
        self._my: typing.Optional[AsyncMyClient] = None
        self._orders: typing.Optional[AsyncOrdersClient] = None
        self._payment_methods: typing.Optional[AsyncPaymentMethodsClient] = None
        self._priceguide: typing.Optional[AsyncPriceguideClient] = None
        self._products: typing.Optional[AsyncProductsClient] = None
        self._sales: typing.Optional[AsyncSalesClient] = None
        self._shipping: typing.Optional[AsyncShippingClient] = None
        self._shop: typing.Optional[AsyncShopClient] = None
        self._shops: typing.Optional[AsyncShopsClient] = None
        self._wants: typing.Optional[AsyncWantsClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None

    @property
    def articles(self):
        if self._articles is None:
            from .articles.client import AsyncArticlesClient

            self._articles = AsyncArticlesClient(client_wrapper=self._client_wrapper)
        return self._articles

    @property
    def categories(self):
        if self._categories is None:
            from .categories.client import AsyncCategoriesClient

            self._categories = AsyncCategoriesClient(client_wrapper=self._client_wrapper)
        return self._categories

    @property
    def comparison_shopping_pages(self):
        if self._comparison_shopping_pages is None:
            from .comparison_shopping_pages.client import AsyncComparisonShoppingPagesClient

            self._comparison_shopping_pages = AsyncComparisonShoppingPagesClient(client_wrapper=self._client_wrapper)
        return self._comparison_shopping_pages

    @property
    def conversations(self):
        if self._conversations is None:
            from .conversations.client import AsyncConversationsClient

            self._conversations = AsyncConversationsClient(client_wrapper=self._client_wrapper)
        return self._conversations

    @property
    def countries(self):
        if self._countries is None:
            from .countries.client import AsyncCountriesClient

            self._countries = AsyncCountriesClient(client_wrapper=self._client_wrapper)
        return self._countries

    @property
    def csps(self):
        if self._csps is None:
            from .csps.client import AsyncCspsClient

            self._csps = AsyncCspsClient(client_wrapper=self._client_wrapper)
        return self._csps

    @property
    def curated_sets(self):
        if self._curated_sets is None:
            from .curated_sets.client import AsyncCuratedSetsClient

            self._curated_sets = AsyncCuratedSetsClient(client_wrapper=self._client_wrapper)
        return self._curated_sets

    @property
    def currencies(self):
        if self._currencies is None:
            from .currencies.client import AsyncCurrenciesClient

            self._currencies = AsyncCurrenciesClient(client_wrapper=self._client_wrapper)
        return self._currencies

    @property
    def feedback(self):
        if self._feedback is None:
            from .feedback.client import AsyncFeedbackClient

            self._feedback = AsyncFeedbackClient(client_wrapper=self._client_wrapper)
        return self._feedback

    @property
    def handpicked(self):
        if self._handpicked is None:
            from .handpicked.client import AsyncHandpickedClient

            self._handpicked = AsyncHandpickedClient(client_wrapper=self._client_wrapper)
        return self._handpicked

    @property
    def listing_conditions(self):
        if self._listing_conditions is None:
            from .listing_conditions.client import AsyncListingConditionsClient

            self._listing_conditions = AsyncListingConditionsClient(client_wrapper=self._client_wrapper)
        return self._listing_conditions

    @property
    def listings(self):
        if self._listings is None:
            from .listings.client import AsyncListingsClient

            self._listings = AsyncListingsClient(client_wrapper=self._client_wrapper)
        return self._listings

    @property
    def my(self):
        if self._my is None:
            from .my.client import AsyncMyClient

            self._my = AsyncMyClient(client_wrapper=self._client_wrapper)
        return self._my

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import AsyncOrdersClient

            self._orders = AsyncOrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def payment_methods(self):
        if self._payment_methods is None:
            from .payment_methods.client import AsyncPaymentMethodsClient

            self._payment_methods = AsyncPaymentMethodsClient(client_wrapper=self._client_wrapper)
        return self._payment_methods

    @property
    def priceguide(self):
        if self._priceguide is None:
            from .priceguide.client import AsyncPriceguideClient

            self._priceguide = AsyncPriceguideClient(client_wrapper=self._client_wrapper)
        return self._priceguide

    @property
    def products(self):
        if self._products is None:
            from .products.client import AsyncProductsClient

            self._products = AsyncProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def sales(self):
        if self._sales is None:
            from .sales.client import AsyncSalesClient

            self._sales = AsyncSalesClient(client_wrapper=self._client_wrapper)
        return self._sales

    @property
    def shipping(self):
        if self._shipping is None:
            from .shipping.client import AsyncShippingClient

            self._shipping = AsyncShippingClient(client_wrapper=self._client_wrapper)
        return self._shipping

    @property
    def shop(self):
        if self._shop is None:
            from .shop.client import AsyncShopClient

            self._shop = AsyncShopClient(client_wrapper=self._client_wrapper)
        return self._shop

    @property
    def shops(self):
        if self._shops is None:
            from .shops.client import AsyncShopsClient

            self._shops = AsyncShopsClient(client_wrapper=self._client_wrapper)
        return self._shops

    @property
    def wants(self):
        if self._wants is None:
            from .wants.client import AsyncWantsClient

            self._wants = AsyncWantsClient(client_wrapper=self._client_wrapper)
        return self._wants

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
