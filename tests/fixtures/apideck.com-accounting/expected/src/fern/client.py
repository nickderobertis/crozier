

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .balance_sheet.client import AsyncBalanceSheetClient, BalanceSheetClient
    from .bills.client import AsyncBillsClient, BillsClient
    from .company_info.client import AsyncCompanyInfoClient, CompanyInfoClient
    from .credit_notes.client import AsyncCreditNotesClient, CreditNotesClient
    from .customers.client import AsyncCustomersClient, CustomersClient
    from .invoice_items.client import AsyncInvoiceItemsClient, InvoiceItemsClient
    from .invoices.client import AsyncInvoicesClient, InvoicesClient
    from .journal_entries.client import AsyncJournalEntriesClient, JournalEntriesClient
    from .ledger_accounts.client import AsyncLedgerAccountsClient, LedgerAccountsClient
    from .payments.client import AsyncPaymentsClient, PaymentsClient
    from .profit_and_loss.client import AsyncProfitAndLossClient, ProfitAndLossClient
    from .suppliers.client import AsyncSuppliersClient, SuppliersClient
    from .tax_rates.client import AsyncTaxRatesClient, TaxRatesClient


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
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
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
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
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
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
        self._balance_sheet: typing.Optional[BalanceSheetClient] = None
        self._bills: typing.Optional[BillsClient] = None
        self._company_info: typing.Optional[CompanyInfoClient] = None
        self._credit_notes: typing.Optional[CreditNotesClient] = None
        self._customers: typing.Optional[CustomersClient] = None
        self._invoice_items: typing.Optional[InvoiceItemsClient] = None
        self._invoices: typing.Optional[InvoicesClient] = None
        self._journal_entries: typing.Optional[JournalEntriesClient] = None
        self._ledger_accounts: typing.Optional[LedgerAccountsClient] = None
        self._payments: typing.Optional[PaymentsClient] = None
        self._profit_and_loss: typing.Optional[ProfitAndLossClient] = None
        self._suppliers: typing.Optional[SuppliersClient] = None
        self._tax_rates: typing.Optional[TaxRatesClient] = None

    @property
    def balance_sheet(self):
        if self._balance_sheet is None:
            from .balance_sheet.client import BalanceSheetClient

            self._balance_sheet = BalanceSheetClient(client_wrapper=self._client_wrapper)
        return self._balance_sheet

    @property
    def bills(self):
        if self._bills is None:
            from .bills.client import BillsClient

            self._bills = BillsClient(client_wrapper=self._client_wrapper)
        return self._bills

    @property
    def company_info(self):
        if self._company_info is None:
            from .company_info.client import CompanyInfoClient

            self._company_info = CompanyInfoClient(client_wrapper=self._client_wrapper)
        return self._company_info

    @property
    def credit_notes(self):
        if self._credit_notes is None:
            from .credit_notes.client import CreditNotesClient

            self._credit_notes = CreditNotesClient(client_wrapper=self._client_wrapper)
        return self._credit_notes

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import CustomersClient

            self._customers = CustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def invoice_items(self):
        if self._invoice_items is None:
            from .invoice_items.client import InvoiceItemsClient

            self._invoice_items = InvoiceItemsClient(client_wrapper=self._client_wrapper)
        return self._invoice_items

    @property
    def invoices(self):
        if self._invoices is None:
            from .invoices.client import InvoicesClient

            self._invoices = InvoicesClient(client_wrapper=self._client_wrapper)
        return self._invoices

    @property
    def journal_entries(self):
        if self._journal_entries is None:
            from .journal_entries.client import JournalEntriesClient

            self._journal_entries = JournalEntriesClient(client_wrapper=self._client_wrapper)
        return self._journal_entries

    @property
    def ledger_accounts(self):
        if self._ledger_accounts is None:
            from .ledger_accounts.client import LedgerAccountsClient

            self._ledger_accounts = LedgerAccountsClient(client_wrapper=self._client_wrapper)
        return self._ledger_accounts

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import PaymentsClient

            self._payments = PaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def profit_and_loss(self):
        if self._profit_and_loss is None:
            from .profit_and_loss.client import ProfitAndLossClient

            self._profit_and_loss = ProfitAndLossClient(client_wrapper=self._client_wrapper)
        return self._profit_and_loss

    @property
    def suppliers(self):
        if self._suppliers is None:
            from .suppliers.client import SuppliersClient

            self._suppliers = SuppliersClient(client_wrapper=self._client_wrapper)
        return self._suppliers

    @property
    def tax_rates(self):
        if self._tax_rates is None:
            from .tax_rates.client import TaxRatesClient

            self._tax_rates = TaxRatesClient(client_wrapper=self._client_wrapper)
        return self._tax_rates


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
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
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
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
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
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
        self._balance_sheet: typing.Optional[AsyncBalanceSheetClient] = None
        self._bills: typing.Optional[AsyncBillsClient] = None
        self._company_info: typing.Optional[AsyncCompanyInfoClient] = None
        self._credit_notes: typing.Optional[AsyncCreditNotesClient] = None
        self._customers: typing.Optional[AsyncCustomersClient] = None
        self._invoice_items: typing.Optional[AsyncInvoiceItemsClient] = None
        self._invoices: typing.Optional[AsyncInvoicesClient] = None
        self._journal_entries: typing.Optional[AsyncJournalEntriesClient] = None
        self._ledger_accounts: typing.Optional[AsyncLedgerAccountsClient] = None
        self._payments: typing.Optional[AsyncPaymentsClient] = None
        self._profit_and_loss: typing.Optional[AsyncProfitAndLossClient] = None
        self._suppliers: typing.Optional[AsyncSuppliersClient] = None
        self._tax_rates: typing.Optional[AsyncTaxRatesClient] = None

    @property
    def balance_sheet(self):
        if self._balance_sheet is None:
            from .balance_sheet.client import AsyncBalanceSheetClient

            self._balance_sheet = AsyncBalanceSheetClient(client_wrapper=self._client_wrapper)
        return self._balance_sheet

    @property
    def bills(self):
        if self._bills is None:
            from .bills.client import AsyncBillsClient

            self._bills = AsyncBillsClient(client_wrapper=self._client_wrapper)
        return self._bills

    @property
    def company_info(self):
        if self._company_info is None:
            from .company_info.client import AsyncCompanyInfoClient

            self._company_info = AsyncCompanyInfoClient(client_wrapper=self._client_wrapper)
        return self._company_info

    @property
    def credit_notes(self):
        if self._credit_notes is None:
            from .credit_notes.client import AsyncCreditNotesClient

            self._credit_notes = AsyncCreditNotesClient(client_wrapper=self._client_wrapper)
        return self._credit_notes

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import AsyncCustomersClient

            self._customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def invoice_items(self):
        if self._invoice_items is None:
            from .invoice_items.client import AsyncInvoiceItemsClient

            self._invoice_items = AsyncInvoiceItemsClient(client_wrapper=self._client_wrapper)
        return self._invoice_items

    @property
    def invoices(self):
        if self._invoices is None:
            from .invoices.client import AsyncInvoicesClient

            self._invoices = AsyncInvoicesClient(client_wrapper=self._client_wrapper)
        return self._invoices

    @property
    def journal_entries(self):
        if self._journal_entries is None:
            from .journal_entries.client import AsyncJournalEntriesClient

            self._journal_entries = AsyncJournalEntriesClient(client_wrapper=self._client_wrapper)
        return self._journal_entries

    @property
    def ledger_accounts(self):
        if self._ledger_accounts is None:
            from .ledger_accounts.client import AsyncLedgerAccountsClient

            self._ledger_accounts = AsyncLedgerAccountsClient(client_wrapper=self._client_wrapper)
        return self._ledger_accounts

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import AsyncPaymentsClient

            self._payments = AsyncPaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments

    @property
    def profit_and_loss(self):
        if self._profit_and_loss is None:
            from .profit_and_loss.client import AsyncProfitAndLossClient

            self._profit_and_loss = AsyncProfitAndLossClient(client_wrapper=self._client_wrapper)
        return self._profit_and_loss

    @property
    def suppliers(self):
        if self._suppliers is None:
            from .suppliers.client import AsyncSuppliersClient

            self._suppliers = AsyncSuppliersClient(client_wrapper=self._client_wrapper)
        return self._suppliers

    @property
    def tax_rates(self):
        if self._tax_rates is None:
            from .tax_rates.client import AsyncTaxRatesClient

            self._tax_rates = AsyncTaxRatesClient(client_wrapper=self._client_wrapper)
        return self._tax_rates


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
