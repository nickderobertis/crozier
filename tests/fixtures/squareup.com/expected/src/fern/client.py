

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .apple_pay.client import ApplePayClient, AsyncApplePayClient
    from .bank_accounts.client import AsyncBankAccountsClient, BankAccountsClient
    from .bookings.client import AsyncBookingsClient, BookingsClient
    from .cards.client import AsyncCardsClient, CardsClient
    from .cash_drawers.client import AsyncCashDrawersClient, CashDrawersClient
    from .catalog.client import AsyncCatalogClient, CatalogClient
    from .checkout.client import AsyncCheckoutClient, CheckoutClient
    from .customer_groups.client import AsyncCustomerGroupsClient, CustomerGroupsClient
    from .customer_segments.client import AsyncCustomerSegmentsClient, CustomerSegmentsClient
    from .customers.client import AsyncCustomersClient, CustomersClient
    from .devices.client import AsyncDevicesClient, DevicesClient
    from .disputes.client import AsyncDisputesClient, DisputesClient
    from .employees.client import AsyncEmployeesClient, EmployeesClient
    from .gift_card_activities.client import AsyncGiftCardActivitiesClient, GiftCardActivitiesClient
    from .gift_cards.client import AsyncGiftCardsClient, GiftCardsClient
    from .inventory.client import AsyncInventoryClient, InventoryClient
    from .invoices.client import AsyncInvoicesClient, InvoicesClient
    from .labor.client import AsyncLaborClient, LaborClient
    from .locations.client import AsyncLocationsClient, LocationsClient
    from .loyalty.client import AsyncLoyaltyClient, LoyaltyClient
    from .merchants.client import AsyncMerchantsClient, MerchantsClient
    from .mobile_authorization.client import AsyncMobileAuthorizationClient, MobileAuthorizationClient
    from .o_auth.client import AsyncOAuthClient, OAuthClient
    from .orders.client import AsyncOrdersClient, OrdersClient
    from .payments.client import AsyncPaymentsClient, PaymentsClient
    from .refunds.client import AsyncRefundsClient, RefundsClient
    from .sites.client import AsyncSitesClient, SitesClient
    from .snippets.client import AsyncSnippetsClient, SnippetsClient
    from .subscriptions.client import AsyncSubscriptionsClient, SubscriptionsClient
    from .team.client import AsyncTeamClient, TeamClient
    from .terminal.client import AsyncTerminalClient, TerminalClient
    from .transactions.client import AsyncTransactionsClient, TransactionsClient
    from .v1employees.client import AsyncV1EmployeesClient, V1EmployeesClient
    from .v1transactions.client import AsyncV1TransactionsClient, V1TransactionsClient


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



    authorization : str
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        authorization="YOUR_AUTHORIZATION",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        authorization: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            authorization=authorization,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._mobile_authorization: typing.Optional[MobileAuthorizationClient] = None
        self._o_auth: typing.Optional[OAuthClient] = None
        self._v1employees: typing.Optional[V1EmployeesClient] = None
        self._v1transactions: typing.Optional[V1TransactionsClient] = None
        self._apple_pay: typing.Optional[ApplePayClient] = None
        self._bank_accounts: typing.Optional[BankAccountsClient] = None
        self._bookings: typing.Optional[BookingsClient] = None
        self._cards: typing.Optional[CardsClient] = None
        self._cash_drawers: typing.Optional[CashDrawersClient] = None
        self._catalog: typing.Optional[CatalogClient] = None
        self._customers: typing.Optional[CustomersClient] = None
        self._customer_groups: typing.Optional[CustomerGroupsClient] = None
        self._customer_segments: typing.Optional[CustomerSegmentsClient] = None
        self._devices: typing.Optional[DevicesClient] = None
        self._disputes: typing.Optional[DisputesClient] = None
        self._employees: typing.Optional[EmployeesClient] = None
        self._gift_cards: typing.Optional[GiftCardsClient] = None
        self._gift_card_activities: typing.Optional[GiftCardActivitiesClient] = None
        self._inventory: typing.Optional[InventoryClient] = None
        self._invoices: typing.Optional[InvoicesClient] = None
        self._labor: typing.Optional[LaborClient] = None
        self._locations: typing.Optional[LocationsClient] = None
        self._checkout: typing.Optional[CheckoutClient] = None
        self._transactions: typing.Optional[TransactionsClient] = None
        self._loyalty: typing.Optional[LoyaltyClient] = None
        self._merchants: typing.Optional[MerchantsClient] = None
        self._orders: typing.Optional[OrdersClient] = None
        self._payments: typing.Optional[PaymentsClient] = None
        self._refunds: typing.Optional[RefundsClient] = None
        self._sites: typing.Optional[SitesClient] = None
        self._snippets: typing.Optional[SnippetsClient] = None
        self._subscriptions: typing.Optional[SubscriptionsClient] = None
        self._team: typing.Optional[TeamClient] = None
        self._terminal: typing.Optional[TerminalClient] = None

    @property
    def mobile_authorization(self):
        if self._mobile_authorization is None:
            from .mobile_authorization.client import MobileAuthorizationClient

            self._mobile_authorization = MobileAuthorizationClient(client_wrapper=self._client_wrapper)
        return self._mobile_authorization

    @property
    def o_auth(self):
        if self._o_auth is None:
            from .o_auth.client import OAuthClient

            self._o_auth = OAuthClient(client_wrapper=self._client_wrapper)
        return self._o_auth

    @property
    def v1employees(self):
        if self._v1employees is None:
            from .v1employees.client import V1EmployeesClient

            self._v1employees = V1EmployeesClient(client_wrapper=self._client_wrapper)
        return self._v1employees

    @property
    def v1transactions(self):
        if self._v1transactions is None:
            from .v1transactions.client import V1TransactionsClient

            self._v1transactions = V1TransactionsClient(client_wrapper=self._client_wrapper)
        return self._v1transactions

    @property
    def apple_pay(self):
        if self._apple_pay is None:
            from .apple_pay.client import ApplePayClient

            self._apple_pay = ApplePayClient(client_wrapper=self._client_wrapper)
        return self._apple_pay

    @property
    def bank_accounts(self):
        if self._bank_accounts is None:
            from .bank_accounts.client import BankAccountsClient

            self._bank_accounts = BankAccountsClient(client_wrapper=self._client_wrapper)
        return self._bank_accounts

    @property
    def bookings(self):
        if self._bookings is None:
            from .bookings.client import BookingsClient

            self._bookings = BookingsClient(client_wrapper=self._client_wrapper)
        return self._bookings

    @property
    def cards(self):
        if self._cards is None:
            from .cards.client import CardsClient

            self._cards = CardsClient(client_wrapper=self._client_wrapper)
        return self._cards

    @property
    def cash_drawers(self):
        if self._cash_drawers is None:
            from .cash_drawers.client import CashDrawersClient

            self._cash_drawers = CashDrawersClient(client_wrapper=self._client_wrapper)
        return self._cash_drawers

    @property
    def catalog(self):
        if self._catalog is None:
            from .catalog.client import CatalogClient

            self._catalog = CatalogClient(client_wrapper=self._client_wrapper)
        return self._catalog

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import CustomersClient

            self._customers = CustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def customer_groups(self):
        if self._customer_groups is None:
            from .customer_groups.client import CustomerGroupsClient

            self._customer_groups = CustomerGroupsClient(client_wrapper=self._client_wrapper)
        return self._customer_groups

    @property
    def customer_segments(self):
        if self._customer_segments is None:
            from .customer_segments.client import CustomerSegmentsClient

            self._customer_segments = CustomerSegmentsClient(client_wrapper=self._client_wrapper)
        return self._customer_segments

    @property
    def devices(self):
        if self._devices is None:
            from .devices.client import DevicesClient

            self._devices = DevicesClient(client_wrapper=self._client_wrapper)
        return self._devices

    @property
    def disputes(self):
        if self._disputes is None:
            from .disputes.client import DisputesClient

            self._disputes = DisputesClient(client_wrapper=self._client_wrapper)
        return self._disputes

    @property
    def employees(self):
        if self._employees is None:
            from .employees.client import EmployeesClient

            self._employees = EmployeesClient(client_wrapper=self._client_wrapper)
        return self._employees

    @property
    def gift_cards(self):
        if self._gift_cards is None:
            from .gift_cards.client import GiftCardsClient

            self._gift_cards = GiftCardsClient(client_wrapper=self._client_wrapper)
        return self._gift_cards

    @property
    def gift_card_activities(self):
        if self._gift_card_activities is None:
            from .gift_card_activities.client import GiftCardActivitiesClient

            self._gift_card_activities = GiftCardActivitiesClient(client_wrapper=self._client_wrapper)
        return self._gift_card_activities

    @property
    def inventory(self):
        if self._inventory is None:
            from .inventory.client import InventoryClient

            self._inventory = InventoryClient(client_wrapper=self._client_wrapper)
        return self._inventory

    @property
    def invoices(self):
        if self._invoices is None:
            from .invoices.client import InvoicesClient

            self._invoices = InvoicesClient(client_wrapper=self._client_wrapper)
        return self._invoices

    @property
    def labor(self):
        if self._labor is None:
            from .labor.client import LaborClient

            self._labor = LaborClient(client_wrapper=self._client_wrapper)
        return self._labor

    @property
    def locations(self):
        if self._locations is None:
            from .locations.client import LocationsClient

            self._locations = LocationsClient(client_wrapper=self._client_wrapper)
        return self._locations

    @property
    def checkout(self):
        if self._checkout is None:
            from .checkout.client import CheckoutClient

            self._checkout = CheckoutClient(client_wrapper=self._client_wrapper)
        return self._checkout

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import TransactionsClient

            self._transactions = TransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions

    @property
    def loyalty(self):
        if self._loyalty is None:
            from .loyalty.client import LoyaltyClient

            self._loyalty = LoyaltyClient(client_wrapper=self._client_wrapper)
        return self._loyalty

    @property
    def merchants(self):
        if self._merchants is None:
            from .merchants.client import MerchantsClient

            self._merchants = MerchantsClient(client_wrapper=self._client_wrapper)
        return self._merchants

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import OrdersClient

            self._orders = OrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import PaymentsClient

            self._payments = PaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def refunds(self):
        if self._refunds is None:
            from .refunds.client import RefundsClient

            self._refunds = RefundsClient(client_wrapper=self._client_wrapper)
        return self._refunds

    @property
    def sites(self):
        if self._sites is None:
            from .sites.client import SitesClient

            self._sites = SitesClient(client_wrapper=self._client_wrapper)
        return self._sites

    @property
    def snippets(self):
        if self._snippets is None:
            from .snippets.client import SnippetsClient

            self._snippets = SnippetsClient(client_wrapper=self._client_wrapper)
        return self._snippets

    @property
    def subscriptions(self):
        if self._subscriptions is None:
            from .subscriptions.client import SubscriptionsClient

            self._subscriptions = SubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._subscriptions

    @property
    def team(self):
        if self._team is None:
            from .team.client import TeamClient

            self._team = TeamClient(client_wrapper=self._client_wrapper)
        return self._team

    @property
    def terminal(self):
        if self._terminal is None:
            from .terminal.client import TerminalClient

            self._terminal = TerminalClient(client_wrapper=self._client_wrapper)
        return self._terminal


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



    authorization : str
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        authorization="YOUR_AUTHORIZATION",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        authorization: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            authorization=authorization,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._mobile_authorization: typing.Optional[AsyncMobileAuthorizationClient] = None
        self._o_auth: typing.Optional[AsyncOAuthClient] = None
        self._v1employees: typing.Optional[AsyncV1EmployeesClient] = None
        self._v1transactions: typing.Optional[AsyncV1TransactionsClient] = None
        self._apple_pay: typing.Optional[AsyncApplePayClient] = None
        self._bank_accounts: typing.Optional[AsyncBankAccountsClient] = None
        self._bookings: typing.Optional[AsyncBookingsClient] = None
        self._cards: typing.Optional[AsyncCardsClient] = None
        self._cash_drawers: typing.Optional[AsyncCashDrawersClient] = None
        self._catalog: typing.Optional[AsyncCatalogClient] = None
        self._customers: typing.Optional[AsyncCustomersClient] = None
        self._customer_groups: typing.Optional[AsyncCustomerGroupsClient] = None
        self._customer_segments: typing.Optional[AsyncCustomerSegmentsClient] = None
        self._devices: typing.Optional[AsyncDevicesClient] = None
        self._disputes: typing.Optional[AsyncDisputesClient] = None
        self._employees: typing.Optional[AsyncEmployeesClient] = None
        self._gift_cards: typing.Optional[AsyncGiftCardsClient] = None
        self._gift_card_activities: typing.Optional[AsyncGiftCardActivitiesClient] = None
        self._inventory: typing.Optional[AsyncInventoryClient] = None
        self._invoices: typing.Optional[AsyncInvoicesClient] = None
        self._labor: typing.Optional[AsyncLaborClient] = None
        self._locations: typing.Optional[AsyncLocationsClient] = None
        self._checkout: typing.Optional[AsyncCheckoutClient] = None
        self._transactions: typing.Optional[AsyncTransactionsClient] = None
        self._loyalty: typing.Optional[AsyncLoyaltyClient] = None
        self._merchants: typing.Optional[AsyncMerchantsClient] = None
        self._orders: typing.Optional[AsyncOrdersClient] = None
        self._payments: typing.Optional[AsyncPaymentsClient] = None
        self._refunds: typing.Optional[AsyncRefundsClient] = None
        self._sites: typing.Optional[AsyncSitesClient] = None
        self._snippets: typing.Optional[AsyncSnippetsClient] = None
        self._subscriptions: typing.Optional[AsyncSubscriptionsClient] = None
        self._team: typing.Optional[AsyncTeamClient] = None
        self._terminal: typing.Optional[AsyncTerminalClient] = None

    @property
    def mobile_authorization(self):
        if self._mobile_authorization is None:
            from .mobile_authorization.client import AsyncMobileAuthorizationClient

            self._mobile_authorization = AsyncMobileAuthorizationClient(client_wrapper=self._client_wrapper)
        return self._mobile_authorization

    @property
    def o_auth(self):
        if self._o_auth is None:
            from .o_auth.client import AsyncOAuthClient

            self._o_auth = AsyncOAuthClient(client_wrapper=self._client_wrapper)
        return self._o_auth

    @property
    def v1employees(self):
        if self._v1employees is None:
            from .v1employees.client import AsyncV1EmployeesClient

            self._v1employees = AsyncV1EmployeesClient(client_wrapper=self._client_wrapper)
        return self._v1employees

    @property
    def v1transactions(self):
        if self._v1transactions is None:
            from .v1transactions.client import AsyncV1TransactionsClient

            self._v1transactions = AsyncV1TransactionsClient(client_wrapper=self._client_wrapper)
        return self._v1transactions

    @property
    def apple_pay(self):
        if self._apple_pay is None:
            from .apple_pay.client import AsyncApplePayClient

            self._apple_pay = AsyncApplePayClient(client_wrapper=self._client_wrapper)
        return self._apple_pay

    @property
    def bank_accounts(self):
        if self._bank_accounts is None:
            from .bank_accounts.client import AsyncBankAccountsClient

            self._bank_accounts = AsyncBankAccountsClient(client_wrapper=self._client_wrapper)
        return self._bank_accounts

    @property
    def bookings(self):
        if self._bookings is None:
            from .bookings.client import AsyncBookingsClient

            self._bookings = AsyncBookingsClient(client_wrapper=self._client_wrapper)
        return self._bookings

    @property
    def cards(self):
        if self._cards is None:
            from .cards.client import AsyncCardsClient

            self._cards = AsyncCardsClient(client_wrapper=self._client_wrapper)
        return self._cards

    @property
    def cash_drawers(self):
        if self._cash_drawers is None:
            from .cash_drawers.client import AsyncCashDrawersClient

            self._cash_drawers = AsyncCashDrawersClient(client_wrapper=self._client_wrapper)
        return self._cash_drawers

    @property
    def catalog(self):
        if self._catalog is None:
            from .catalog.client import AsyncCatalogClient

            self._catalog = AsyncCatalogClient(client_wrapper=self._client_wrapper)
        return self._catalog

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import AsyncCustomersClient

            self._customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def customer_groups(self):
        if self._customer_groups is None:
            from .customer_groups.client import AsyncCustomerGroupsClient

            self._customer_groups = AsyncCustomerGroupsClient(client_wrapper=self._client_wrapper)
        return self._customer_groups

    @property
    def customer_segments(self):
        if self._customer_segments is None:
            from .customer_segments.client import AsyncCustomerSegmentsClient

            self._customer_segments = AsyncCustomerSegmentsClient(client_wrapper=self._client_wrapper)
        return self._customer_segments

    @property
    def devices(self):
        if self._devices is None:
            from .devices.client import AsyncDevicesClient

            self._devices = AsyncDevicesClient(client_wrapper=self._client_wrapper)
        return self._devices

    @property
    def disputes(self):
        if self._disputes is None:
            from .disputes.client import AsyncDisputesClient

            self._disputes = AsyncDisputesClient(client_wrapper=self._client_wrapper)
        return self._disputes

    @property
    def employees(self):
        if self._employees is None:
            from .employees.client import AsyncEmployeesClient

            self._employees = AsyncEmployeesClient(client_wrapper=self._client_wrapper)
        return self._employees

    @property
    def gift_cards(self):
        if self._gift_cards is None:
            from .gift_cards.client import AsyncGiftCardsClient

            self._gift_cards = AsyncGiftCardsClient(client_wrapper=self._client_wrapper)
        return self._gift_cards

    @property
    def gift_card_activities(self):
        if self._gift_card_activities is None:
            from .gift_card_activities.client import AsyncGiftCardActivitiesClient

            self._gift_card_activities = AsyncGiftCardActivitiesClient(client_wrapper=self._client_wrapper)
        return self._gift_card_activities

    @property
    def inventory(self):
        if self._inventory is None:
            from .inventory.client import AsyncInventoryClient

            self._inventory = AsyncInventoryClient(client_wrapper=self._client_wrapper)
        return self._inventory

    @property
    def invoices(self):
        if self._invoices is None:
            from .invoices.client import AsyncInvoicesClient

            self._invoices = AsyncInvoicesClient(client_wrapper=self._client_wrapper)
        return self._invoices

    @property
    def labor(self):
        if self._labor is None:
            from .labor.client import AsyncLaborClient

            self._labor = AsyncLaborClient(client_wrapper=self._client_wrapper)
        return self._labor

    @property
    def locations(self):
        if self._locations is None:
            from .locations.client import AsyncLocationsClient

            self._locations = AsyncLocationsClient(client_wrapper=self._client_wrapper)
        return self._locations

    @property
    def checkout(self):
        if self._checkout is None:
            from .checkout.client import AsyncCheckoutClient

            self._checkout = AsyncCheckoutClient(client_wrapper=self._client_wrapper)
        return self._checkout

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import AsyncTransactionsClient

            self._transactions = AsyncTransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions

    @property
    def loyalty(self):
        if self._loyalty is None:
            from .loyalty.client import AsyncLoyaltyClient

            self._loyalty = AsyncLoyaltyClient(client_wrapper=self._client_wrapper)
        return self._loyalty

    @property
    def merchants(self):
        if self._merchants is None:
            from .merchants.client import AsyncMerchantsClient

            self._merchants = AsyncMerchantsClient(client_wrapper=self._client_wrapper)
        return self._merchants

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import AsyncOrdersClient

            self._orders = AsyncOrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import AsyncPaymentsClient

            self._payments = AsyncPaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def refunds(self):
        if self._refunds is None:
            from .refunds.client import AsyncRefundsClient

            self._refunds = AsyncRefundsClient(client_wrapper=self._client_wrapper)
        return self._refunds

    @property
    def sites(self):
        if self._sites is None:
            from .sites.client import AsyncSitesClient

            self._sites = AsyncSitesClient(client_wrapper=self._client_wrapper)
        return self._sites

    @property
    def snippets(self):
        if self._snippets is None:
            from .snippets.client import AsyncSnippetsClient

            self._snippets = AsyncSnippetsClient(client_wrapper=self._client_wrapper)
        return self._snippets

    @property
    def subscriptions(self):
        if self._subscriptions is None:
            from .subscriptions.client import AsyncSubscriptionsClient

            self._subscriptions = AsyncSubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._subscriptions

    @property
    def team(self):
        if self._team is None:
            from .team.client import AsyncTeamClient

            self._team = AsyncTeamClient(client_wrapper=self._client_wrapper)
        return self._team

    @property
    def terminal(self):
        if self._terminal is None:
            from .terminal.client import AsyncTerminalClient

            self._terminal = AsyncTerminalClient(client_wrapper=self._client_wrapper)
        return self._terminal


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
