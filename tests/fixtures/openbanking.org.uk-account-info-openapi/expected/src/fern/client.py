

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .account_access.client import AccountAccessClient, AsyncAccountAccessClient
    from .accounts.client import AccountsClient, AsyncAccountsClient
    from .balances.client import AsyncBalancesClient, BalancesClient
    from .beneficiaries.client import AsyncBeneficiariesClient, BeneficiariesClient
    from .direct_debits.client import AsyncDirectDebitsClient, DirectDebitsClient
    from .offers.client import AsyncOffersClient, OffersClient
    from .parties.client import AsyncPartiesClient, PartiesClient
    from .products.client import AsyncProductsClient, ProductsClient
    from .scheduled_payments.client import AsyncScheduledPaymentsClient, ScheduledPaymentsClient
    from .standing_orders.client import AsyncStandingOrdersClient, StandingOrdersClient
    from .statements.client import AsyncStatementsClient, StatementsClient
    from .transactions.client import AsyncTransactionsClient, TransactionsClient


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



    fapi_auth_date : typing.Optional[str]
    fapi_customer_ip_address : typing.Optional[str]
    fapi_interaction_id : typing.Optional[str]
    customer_user_agent : typing.Optional[str]
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
        fapi_auth_date="YOUR_FAPI_AUTH_DATE",
        fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
        fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
        customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        fapi_auth_date: typing.Optional[str] = None,
        fapi_customer_ip_address: typing.Optional[str] = None,
        fapi_interaction_id: typing.Optional[str] = None,
        customer_user_agent: typing.Optional[str] = None,
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
            fapi_auth_date=fapi_auth_date,
            fapi_customer_ip_address=fapi_customer_ip_address,
            fapi_interaction_id=fapi_interaction_id,
            customer_user_agent=customer_user_agent,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._account_access: typing.Optional[AccountAccessClient] = None
        self._accounts: typing.Optional[AccountsClient] = None
        self._balances: typing.Optional[BalancesClient] = None
        self._beneficiaries: typing.Optional[BeneficiariesClient] = None
        self._direct_debits: typing.Optional[DirectDebitsClient] = None
        self._offers: typing.Optional[OffersClient] = None
        self._parties: typing.Optional[PartiesClient] = None
        self._products: typing.Optional[ProductsClient] = None
        self._scheduled_payments: typing.Optional[ScheduledPaymentsClient] = None
        self._standing_orders: typing.Optional[StandingOrdersClient] = None
        self._statements: typing.Optional[StatementsClient] = None
        self._transactions: typing.Optional[TransactionsClient] = None

    @property
    def account_access(self):
        if self._account_access is None:
            from .account_access.client import AccountAccessClient

            self._account_access = AccountAccessClient(client_wrapper=self._client_wrapper)
        return self._account_access

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AccountsClient

            self._accounts = AccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def balances(self):
        if self._balances is None:
            from .balances.client import BalancesClient

            self._balances = BalancesClient(client_wrapper=self._client_wrapper)
        return self._balances

    @property
    def beneficiaries(self):
        if self._beneficiaries is None:
            from .beneficiaries.client import BeneficiariesClient

            self._beneficiaries = BeneficiariesClient(client_wrapper=self._client_wrapper)
        return self._beneficiaries

    @property
    def direct_debits(self):
        if self._direct_debits is None:
            from .direct_debits.client import DirectDebitsClient

            self._direct_debits = DirectDebitsClient(client_wrapper=self._client_wrapper)
        return self._direct_debits

    @property
    def offers(self):
        if self._offers is None:
            from .offers.client import OffersClient

            self._offers = OffersClient(client_wrapper=self._client_wrapper)
        return self._offers

    @property
    def parties(self):
        if self._parties is None:
            from .parties.client import PartiesClient

            self._parties = PartiesClient(client_wrapper=self._client_wrapper)
        return self._parties

    @property
    def products(self):
        if self._products is None:
            from .products.client import ProductsClient

            self._products = ProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def scheduled_payments(self):
        if self._scheduled_payments is None:
            from .scheduled_payments.client import ScheduledPaymentsClient

            self._scheduled_payments = ScheduledPaymentsClient(client_wrapper=self._client_wrapper)
        return self._scheduled_payments

    @property
    def standing_orders(self):
        if self._standing_orders is None:
            from .standing_orders.client import StandingOrdersClient

            self._standing_orders = StandingOrdersClient(client_wrapper=self._client_wrapper)
        return self._standing_orders

    @property
    def statements(self):
        if self._statements is None:
            from .statements.client import StatementsClient

            self._statements = StatementsClient(client_wrapper=self._client_wrapper)
        return self._statements

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import TransactionsClient

            self._transactions = TransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions


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



    fapi_auth_date : typing.Optional[str]
    fapi_customer_ip_address : typing.Optional[str]
    fapi_interaction_id : typing.Optional[str]
    customer_user_agent : typing.Optional[str]
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
        fapi_auth_date="YOUR_FAPI_AUTH_DATE",
        fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
        fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
        customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        fapi_auth_date: typing.Optional[str] = None,
        fapi_customer_ip_address: typing.Optional[str] = None,
        fapi_interaction_id: typing.Optional[str] = None,
        customer_user_agent: typing.Optional[str] = None,
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
            fapi_auth_date=fapi_auth_date,
            fapi_customer_ip_address=fapi_customer_ip_address,
            fapi_interaction_id=fapi_interaction_id,
            customer_user_agent=customer_user_agent,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._account_access: typing.Optional[AsyncAccountAccessClient] = None
        self._accounts: typing.Optional[AsyncAccountsClient] = None
        self._balances: typing.Optional[AsyncBalancesClient] = None
        self._beneficiaries: typing.Optional[AsyncBeneficiariesClient] = None
        self._direct_debits: typing.Optional[AsyncDirectDebitsClient] = None
        self._offers: typing.Optional[AsyncOffersClient] = None
        self._parties: typing.Optional[AsyncPartiesClient] = None
        self._products: typing.Optional[AsyncProductsClient] = None
        self._scheduled_payments: typing.Optional[AsyncScheduledPaymentsClient] = None
        self._standing_orders: typing.Optional[AsyncStandingOrdersClient] = None
        self._statements: typing.Optional[AsyncStatementsClient] = None
        self._transactions: typing.Optional[AsyncTransactionsClient] = None

    @property
    def account_access(self):
        if self._account_access is None:
            from .account_access.client import AsyncAccountAccessClient

            self._account_access = AsyncAccountAccessClient(client_wrapper=self._client_wrapper)
        return self._account_access

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AsyncAccountsClient

            self._accounts = AsyncAccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def balances(self):
        if self._balances is None:
            from .balances.client import AsyncBalancesClient

            self._balances = AsyncBalancesClient(client_wrapper=self._client_wrapper)
        return self._balances

    @property
    def beneficiaries(self):
        if self._beneficiaries is None:
            from .beneficiaries.client import AsyncBeneficiariesClient

            self._beneficiaries = AsyncBeneficiariesClient(client_wrapper=self._client_wrapper)
        return self._beneficiaries

    @property
    def direct_debits(self):
        if self._direct_debits is None:
            from .direct_debits.client import AsyncDirectDebitsClient

            self._direct_debits = AsyncDirectDebitsClient(client_wrapper=self._client_wrapper)
        return self._direct_debits

    @property
    def offers(self):
        if self._offers is None:
            from .offers.client import AsyncOffersClient

            self._offers = AsyncOffersClient(client_wrapper=self._client_wrapper)
        return self._offers

    @property
    def parties(self):
        if self._parties is None:
            from .parties.client import AsyncPartiesClient

            self._parties = AsyncPartiesClient(client_wrapper=self._client_wrapper)
        return self._parties

    @property
    def products(self):
        if self._products is None:
            from .products.client import AsyncProductsClient

            self._products = AsyncProductsClient(client_wrapper=self._client_wrapper)
        return self._products

    @property
    def scheduled_payments(self):
        if self._scheduled_payments is None:
            from .scheduled_payments.client import AsyncScheduledPaymentsClient

            self._scheduled_payments = AsyncScheduledPaymentsClient(client_wrapper=self._client_wrapper)
        return self._scheduled_payments

    @property
    def standing_orders(self):
        if self._standing_orders is None:
            from .standing_orders.client import AsyncStandingOrdersClient

            self._standing_orders = AsyncStandingOrdersClient(client_wrapper=self._client_wrapper)
        return self._standing_orders

    @property
    def statements(self):
        if self._statements is None:
            from .statements.client import AsyncStatementsClient

            self._statements = AsyncStatementsClient(client_wrapper=self._client_wrapper)
        return self._statements

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import AsyncTransactionsClient

            self._transactions = AsyncTransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
