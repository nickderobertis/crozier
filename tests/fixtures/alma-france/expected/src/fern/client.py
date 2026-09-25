

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .addresses.client import AddressesClient, AsyncAddressesClient
    from .balance_transactions.client import AsyncBalanceTransactionsClient, BalanceTransactionsClient
    from .customers.client import AsyncCustomersClient, CustomersClient
    from .data_exports.client import AsyncDataExportsClient, DataExportsClient
    from .eligibility.client import AsyncEligibilityClient, EligibilityClient
    from .orders.client import AsyncOrdersClient, OrdersClient
    from .payments.client import AsyncPaymentsClient, PaymentsClient
    from .refunds.client import AsyncRefundsClient, RefundsClient
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



    api_key : str
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._payments: typing.Optional[PaymentsClient] = None
        self._orders: typing.Optional[OrdersClient] = None
        self._refunds: typing.Optional[RefundsClient] = None
        self._eligibility: typing.Optional[EligibilityClient] = None
        self._addresses: typing.Optional[AddressesClient] = None
        self._balance_transactions: typing.Optional[BalanceTransactionsClient] = None
        self._data_exports: typing.Optional[DataExportsClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None
        self._customers: typing.Optional[CustomersClient] = None

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import PaymentsClient

            self._payments = PaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import OrdersClient

            self._orders = OrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def refunds(self):
        if self._refunds is None:
            from .refunds.client import RefundsClient

            self._refunds = RefundsClient(client_wrapper=self._client_wrapper)
        return self._refunds

    @property
    def eligibility(self):
        if self._eligibility is None:
            from .eligibility.client import EligibilityClient

            self._eligibility = EligibilityClient(client_wrapper=self._client_wrapper)
        return self._eligibility

    @property
    def addresses(self):
        if self._addresses is None:
            from .addresses.client import AddressesClient

            self._addresses = AddressesClient(client_wrapper=self._client_wrapper)
        return self._addresses

    @property
    def balance_transactions(self):
        if self._balance_transactions is None:
            from .balance_transactions.client import BalanceTransactionsClient

            self._balance_transactions = BalanceTransactionsClient(client_wrapper=self._client_wrapper)
        return self._balance_transactions

    @property
    def data_exports(self):
        if self._data_exports is None:
            from .data_exports.client import DataExportsClient

            self._data_exports = DataExportsClient(client_wrapper=self._client_wrapper)
        return self._data_exports

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import CustomersClient

            self._customers = CustomersClient(client_wrapper=self._client_wrapper)
        return self._customers


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



    api_key : str
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

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
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
            api_key=api_key,
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
        self._payments: typing.Optional[AsyncPaymentsClient] = None
        self._orders: typing.Optional[AsyncOrdersClient] = None
        self._refunds: typing.Optional[AsyncRefundsClient] = None
        self._eligibility: typing.Optional[AsyncEligibilityClient] = None
        self._addresses: typing.Optional[AsyncAddressesClient] = None
        self._balance_transactions: typing.Optional[AsyncBalanceTransactionsClient] = None
        self._data_exports: typing.Optional[AsyncDataExportsClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None
        self._customers: typing.Optional[AsyncCustomersClient] = None

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import AsyncPaymentsClient

            self._payments = AsyncPaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import AsyncOrdersClient

            self._orders = AsyncOrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def refunds(self):
        if self._refunds is None:
            from .refunds.client import AsyncRefundsClient

            self._refunds = AsyncRefundsClient(client_wrapper=self._client_wrapper)
        return self._refunds

    @property
    def eligibility(self):
        if self._eligibility is None:
            from .eligibility.client import AsyncEligibilityClient

            self._eligibility = AsyncEligibilityClient(client_wrapper=self._client_wrapper)
        return self._eligibility

    @property
    def addresses(self):
        if self._addresses is None:
            from .addresses.client import AsyncAddressesClient

            self._addresses = AsyncAddressesClient(client_wrapper=self._client_wrapper)
        return self._addresses

    @property
    def balance_transactions(self):
        if self._balance_transactions is None:
            from .balance_transactions.client import AsyncBalanceTransactionsClient

            self._balance_transactions = AsyncBalanceTransactionsClient(client_wrapper=self._client_wrapper)
        return self._balance_transactions

    @property
    def data_exports(self):
        if self._data_exports is None:
            from .data_exports.client import AsyncDataExportsClient

            self._data_exports = AsyncDataExportsClient(client_wrapper=self._client_wrapper)
        return self._data_exports

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import AsyncCustomersClient

            self._customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        return self._customers


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
