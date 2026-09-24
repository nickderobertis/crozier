

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .calendar_events.client import AsyncCalendarEventsClient, CalendarEventsClient
    from .company.client import AsyncCompanyClient, CompanyClient
    from .contacts.client import AsyncContactsClient, ContactsClient
    from .customer_invoices.client import AsyncCustomerInvoicesClient, CustomerInvoicesClient
    from .customers.client import AsyncCustomersClient, CustomersClient
    from .enquiries.client import AsyncEnquiriesClient, EnquiriesClient
    from .favourites.client import AsyncFavouritesClient, FavouritesClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .jobs_phases.client import AsyncJobsPhasesClient, JobsPhasesClient
    from .jobs_quotes.client import AsyncJobsQuotesClient, JobsQuotesClient
    from .notes.client import AsyncNotesClient, NotesClient
    from .pricebooks.client import AsyncPricebooksClient, PricebooksClient
    from .pricing_tiers.client import AsyncPricingTiersClient, PricingTiersClient
    from .server.client import AsyncServerClient, ServerClient
    from .sites.client import AsyncSitesClient, SitesClient
    from .stock_used.client import AsyncStockUsedClient, StockUsedClient
    from .time_entries.client import AsyncTimeEntriesClient, TimeEntriesClient
    from .users.client import AsyncUsersClient, UsersClient


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
        self._server: typing.Optional[ServerClient] = None
        self._favourites: typing.Optional[FavouritesClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._jobs_quotes: typing.Optional[JobsQuotesClient] = None
        self._customer_invoices: typing.Optional[CustomerInvoicesClient] = None
        self._customers: typing.Optional[CustomersClient] = None
        self._sites: typing.Optional[SitesClient] = None
        self._contacts: typing.Optional[ContactsClient] = None
        self._enquiries: typing.Optional[EnquiriesClient] = None
        self._jobs_phases: typing.Optional[JobsPhasesClient] = None
        self._stock_used: typing.Optional[StockUsedClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._time_entries: typing.Optional[TimeEntriesClient] = None
        self._calendar_events: typing.Optional[CalendarEventsClient] = None
        self._pricing_tiers: typing.Optional[PricingTiersClient] = None
        self._pricebooks: typing.Optional[PricebooksClient] = None
        self._notes: typing.Optional[NotesClient] = None
        self._company: typing.Optional[CompanyClient] = None

    @property
    def server(self):
        if self._server is None:
            from .server.client import ServerClient

            self._server = ServerClient(client_wrapper=self._client_wrapper)
        return self._server

    @property
    def favourites(self):
        if self._favourites is None:
            from .favourites.client import FavouritesClient

            self._favourites = FavouritesClient(client_wrapper=self._client_wrapper)
        return self._favourites

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def jobs_quotes(self):
        if self._jobs_quotes is None:
            from .jobs_quotes.client import JobsQuotesClient

            self._jobs_quotes = JobsQuotesClient(client_wrapper=self._client_wrapper)
        return self._jobs_quotes

    @property
    def customer_invoices(self):
        if self._customer_invoices is None:
            from .customer_invoices.client import CustomerInvoicesClient

            self._customer_invoices = CustomerInvoicesClient(client_wrapper=self._client_wrapper)
        return self._customer_invoices

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import CustomersClient

            self._customers = CustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def sites(self):
        if self._sites is None:
            from .sites.client import SitesClient

            self._sites = SitesClient(client_wrapper=self._client_wrapper)
        return self._sites

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import ContactsClient

            self._contacts = ContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def enquiries(self):
        if self._enquiries is None:
            from .enquiries.client import EnquiriesClient

            self._enquiries = EnquiriesClient(client_wrapper=self._client_wrapper)
        return self._enquiries

    @property
    def jobs_phases(self):
        if self._jobs_phases is None:
            from .jobs_phases.client import JobsPhasesClient

            self._jobs_phases = JobsPhasesClient(client_wrapper=self._client_wrapper)
        return self._jobs_phases

    @property
    def stock_used(self):
        if self._stock_used is None:
            from .stock_used.client import StockUsedClient

            self._stock_used = StockUsedClient(client_wrapper=self._client_wrapper)
        return self._stock_used

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def time_entries(self):
        if self._time_entries is None:
            from .time_entries.client import TimeEntriesClient

            self._time_entries = TimeEntriesClient(client_wrapper=self._client_wrapper)
        return self._time_entries

    @property
    def calendar_events(self):
        if self._calendar_events is None:
            from .calendar_events.client import CalendarEventsClient

            self._calendar_events = CalendarEventsClient(client_wrapper=self._client_wrapper)
        return self._calendar_events

    @property
    def pricing_tiers(self):
        if self._pricing_tiers is None:
            from .pricing_tiers.client import PricingTiersClient

            self._pricing_tiers = PricingTiersClient(client_wrapper=self._client_wrapper)
        return self._pricing_tiers

    @property
    def pricebooks(self):
        if self._pricebooks is None:
            from .pricebooks.client import PricebooksClient

            self._pricebooks = PricebooksClient(client_wrapper=self._client_wrapper)
        return self._pricebooks

    @property
    def notes(self):
        if self._notes is None:
            from .notes.client import NotesClient

            self._notes = NotesClient(client_wrapper=self._client_wrapper)
        return self._notes

    @property
    def company(self):
        if self._company is None:
            from .company.client import CompanyClient

            self._company = CompanyClient(client_wrapper=self._client_wrapper)
        return self._company


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
        self._server: typing.Optional[AsyncServerClient] = None
        self._favourites: typing.Optional[AsyncFavouritesClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._jobs_quotes: typing.Optional[AsyncJobsQuotesClient] = None
        self._customer_invoices: typing.Optional[AsyncCustomerInvoicesClient] = None
        self._customers: typing.Optional[AsyncCustomersClient] = None
        self._sites: typing.Optional[AsyncSitesClient] = None
        self._contacts: typing.Optional[AsyncContactsClient] = None
        self._enquiries: typing.Optional[AsyncEnquiriesClient] = None
        self._jobs_phases: typing.Optional[AsyncJobsPhasesClient] = None
        self._stock_used: typing.Optional[AsyncStockUsedClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._time_entries: typing.Optional[AsyncTimeEntriesClient] = None
        self._calendar_events: typing.Optional[AsyncCalendarEventsClient] = None
        self._pricing_tiers: typing.Optional[AsyncPricingTiersClient] = None
        self._pricebooks: typing.Optional[AsyncPricebooksClient] = None
        self._notes: typing.Optional[AsyncNotesClient] = None
        self._company: typing.Optional[AsyncCompanyClient] = None

    @property
    def server(self):
        if self._server is None:
            from .server.client import AsyncServerClient

            self._server = AsyncServerClient(client_wrapper=self._client_wrapper)
        return self._server

    @property
    def favourites(self):
        if self._favourites is None:
            from .favourites.client import AsyncFavouritesClient

            self._favourites = AsyncFavouritesClient(client_wrapper=self._client_wrapper)
        return self._favourites

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def jobs_quotes(self):
        if self._jobs_quotes is None:
            from .jobs_quotes.client import AsyncJobsQuotesClient

            self._jobs_quotes = AsyncJobsQuotesClient(client_wrapper=self._client_wrapper)
        return self._jobs_quotes

    @property
    def customer_invoices(self):
        if self._customer_invoices is None:
            from .customer_invoices.client import AsyncCustomerInvoicesClient

            self._customer_invoices = AsyncCustomerInvoicesClient(client_wrapper=self._client_wrapper)
        return self._customer_invoices

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import AsyncCustomersClient

            self._customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def sites(self):
        if self._sites is None:
            from .sites.client import AsyncSitesClient

            self._sites = AsyncSitesClient(client_wrapper=self._client_wrapper)
        return self._sites

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import AsyncContactsClient

            self._contacts = AsyncContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def enquiries(self):
        if self._enquiries is None:
            from .enquiries.client import AsyncEnquiriesClient

            self._enquiries = AsyncEnquiriesClient(client_wrapper=self._client_wrapper)
        return self._enquiries

    @property
    def jobs_phases(self):
        if self._jobs_phases is None:
            from .jobs_phases.client import AsyncJobsPhasesClient

            self._jobs_phases = AsyncJobsPhasesClient(client_wrapper=self._client_wrapper)
        return self._jobs_phases

    @property
    def stock_used(self):
        if self._stock_used is None:
            from .stock_used.client import AsyncStockUsedClient

            self._stock_used = AsyncStockUsedClient(client_wrapper=self._client_wrapper)
        return self._stock_used

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def time_entries(self):
        if self._time_entries is None:
            from .time_entries.client import AsyncTimeEntriesClient

            self._time_entries = AsyncTimeEntriesClient(client_wrapper=self._client_wrapper)
        return self._time_entries

    @property
    def calendar_events(self):
        if self._calendar_events is None:
            from .calendar_events.client import AsyncCalendarEventsClient

            self._calendar_events = AsyncCalendarEventsClient(client_wrapper=self._client_wrapper)
        return self._calendar_events

    @property
    def pricing_tiers(self):
        if self._pricing_tiers is None:
            from .pricing_tiers.client import AsyncPricingTiersClient

            self._pricing_tiers = AsyncPricingTiersClient(client_wrapper=self._client_wrapper)
        return self._pricing_tiers

    @property
    def pricebooks(self):
        if self._pricebooks is None:
            from .pricebooks.client import AsyncPricebooksClient

            self._pricebooks = AsyncPricebooksClient(client_wrapper=self._client_wrapper)
        return self._pricebooks

    @property
    def notes(self):
        if self._notes is None:
            from .notes.client import AsyncNotesClient

            self._notes = AsyncNotesClient(client_wrapper=self._client_wrapper)
        return self._notes

    @property
    def company(self):
        if self._company is None:
            from .company.client import AsyncCompanyClient

            self._company = AsyncCompanyClient(client_wrapper=self._client_wrapper)
        return self._company


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
