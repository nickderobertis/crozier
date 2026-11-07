

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .accounting_account.client import AccountingAccountClient, AsyncAccountingAccountClient
    from .accounting_expense.client import AccountingExpenseClient, AsyncAccountingExpenseClient
    from .accounting_proxy.client import AccountingProxyClient, AsyncAccountingProxyClient
    from .accounting_vendor.client import AccountingVendorClient, AsyncAccountingVendorClient
    from .ats_candidate.client import AsyncAtsCandidateClient, AtsCandidateClient
    from .ats_department.client import AsyncAtsDepartmentClient, AtsDepartmentClient
    from .ats_job.client import AsyncAtsJobClient, AtsJobClient
    from .ats_offer.client import AsyncAtsOfferClient, AtsOfferClient
    from .ats_proxy.client import AsyncAtsProxyClient, AtsProxyClient
    from .chat_channels.client import AsyncChatChannelsClient, ChatChannelsClient
    from .chat_messages.client import AsyncChatMessagesClient, ChatMessagesClient
    from .chat_users.client import AsyncChatUsersClient, ChatUsersClient
    from .connection.client import AsyncConnectionClient, ConnectionClient
    from .crm_company.client import AsyncCrmCompanyClient, CrmCompanyClient
    from .crm_contact.client import AsyncCrmContactClient, CrmContactClient
    from .crm_deal.client import AsyncCrmDealClient, CrmDealClient
    from .crm_event.client import AsyncCrmEventClient, CrmEventClient
    from .crm_lead.client import AsyncCrmLeadClient, CrmLeadClient
    from .crm_note.client import AsyncCrmNoteClient, CrmNoteClient
    from .crm_properties.client import AsyncCrmPropertiesClient, CrmPropertiesClient
    from .crm_proxy.client import AsyncCrmProxyClient, CrmProxyClient
    from .crm_task.client import AsyncCrmTaskClient, CrmTaskClient
    from .crm_user.client import AsyncCrmUserClient, CrmUserClient
    from .fieldmapping.client import AsyncFieldmappingClient, FieldmappingClient
    from .internal_account.client import AsyncInternalAccountClient, InternalAccountClient
    from .internal_analytics.client import AsyncInternalAnalyticsClient, InternalAnalyticsClient
    from .internal_app.client import AsyncInternalAppClient, InternalAppClient
    from .internal_telemetry.client import AsyncInternalTelemetryClient, InternalTelemetryClient
    from .metadata.client import AsyncMetadataClient, MetadataClient
    from .sync.client import AsyncSyncClient, SyncClient
    from .ticket_collection.client import AsyncTicketCollectionClient, TicketCollectionClient
    from .ticket_comment.client import AsyncTicketCommentClient, TicketCommentClient
    from .ticket_proxy.client import AsyncTicketProxyClient, TicketProxyClient
    from .ticket_task.client import AsyncTicketTaskClient, TicketTaskClient
    from .ticket_user.client import AsyncTicketUserClient, TicketUserClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._accounting_account: typing.Optional[AccountingAccountClient] = None
        self._accounting_expense: typing.Optional[AccountingExpenseClient] = None
        self._accounting_proxy: typing.Optional[AccountingProxyClient] = None
        self._accounting_vendor: typing.Optional[AccountingVendorClient] = None
        self._ats_candidate: typing.Optional[AtsCandidateClient] = None
        self._ats_department: typing.Optional[AtsDepartmentClient] = None
        self._ats_job: typing.Optional[AtsJobClient] = None
        self._ats_offer: typing.Optional[AtsOfferClient] = None
        self._ats_proxy: typing.Optional[AtsProxyClient] = None
        self._chat_channels: typing.Optional[ChatChannelsClient] = None
        self._chat_messages: typing.Optional[ChatMessagesClient] = None
        self._chat_users: typing.Optional[ChatUsersClient] = None
        self._connection: typing.Optional[ConnectionClient] = None
        self._crm_company: typing.Optional[CrmCompanyClient] = None
        self._crm_contact: typing.Optional[CrmContactClient] = None
        self._crm_deal: typing.Optional[CrmDealClient] = None
        self._crm_event: typing.Optional[CrmEventClient] = None
        self._crm_lead: typing.Optional[CrmLeadClient] = None
        self._crm_note: typing.Optional[CrmNoteClient] = None
        self._crm_properties: typing.Optional[CrmPropertiesClient] = None
        self._crm_proxy: typing.Optional[CrmProxyClient] = None
        self._crm_task: typing.Optional[CrmTaskClient] = None
        self._crm_user: typing.Optional[CrmUserClient] = None
        self._fieldmapping: typing.Optional[FieldmappingClient] = None
        self._internal_account: typing.Optional[InternalAccountClient] = None
        self._internal_analytics: typing.Optional[InternalAnalyticsClient] = None
        self._internal_app: typing.Optional[InternalAppClient] = None
        self._internal_telemetry: typing.Optional[InternalTelemetryClient] = None
        self._metadata: typing.Optional[MetadataClient] = None
        self._sync: typing.Optional[SyncClient] = None
        self._ticket_collection: typing.Optional[TicketCollectionClient] = None
        self._ticket_comment: typing.Optional[TicketCommentClient] = None
        self._ticket_proxy: typing.Optional[TicketProxyClient] = None
        self._ticket_task: typing.Optional[TicketTaskClient] = None
        self._ticket_user: typing.Optional[TicketUserClient] = None

    @property
    def accounting_account(self):
        if self._accounting_account is None:
            from .accounting_account.client import AccountingAccountClient

            self._accounting_account = AccountingAccountClient(client_wrapper=self._client_wrapper)
        return self._accounting_account

    @property
    def accounting_expense(self):
        if self._accounting_expense is None:
            from .accounting_expense.client import AccountingExpenseClient

            self._accounting_expense = AccountingExpenseClient(client_wrapper=self._client_wrapper)
        return self._accounting_expense

    @property
    def accounting_proxy(self):
        if self._accounting_proxy is None:
            from .accounting_proxy.client import AccountingProxyClient

            self._accounting_proxy = AccountingProxyClient(client_wrapper=self._client_wrapper)
        return self._accounting_proxy

    @property
    def accounting_vendor(self):
        if self._accounting_vendor is None:
            from .accounting_vendor.client import AccountingVendorClient

            self._accounting_vendor = AccountingVendorClient(client_wrapper=self._client_wrapper)
        return self._accounting_vendor

    @property
    def ats_candidate(self):
        if self._ats_candidate is None:
            from .ats_candidate.client import AtsCandidateClient

            self._ats_candidate = AtsCandidateClient(client_wrapper=self._client_wrapper)
        return self._ats_candidate

    @property
    def ats_department(self):
        if self._ats_department is None:
            from .ats_department.client import AtsDepartmentClient

            self._ats_department = AtsDepartmentClient(client_wrapper=self._client_wrapper)
        return self._ats_department

    @property
    def ats_job(self):
        if self._ats_job is None:
            from .ats_job.client import AtsJobClient

            self._ats_job = AtsJobClient(client_wrapper=self._client_wrapper)
        return self._ats_job

    @property
    def ats_offer(self):
        if self._ats_offer is None:
            from .ats_offer.client import AtsOfferClient

            self._ats_offer = AtsOfferClient(client_wrapper=self._client_wrapper)
        return self._ats_offer

    @property
    def ats_proxy(self):
        if self._ats_proxy is None:
            from .ats_proxy.client import AtsProxyClient

            self._ats_proxy = AtsProxyClient(client_wrapper=self._client_wrapper)
        return self._ats_proxy

    @property
    def chat_channels(self):
        if self._chat_channels is None:
            from .chat_channels.client import ChatChannelsClient

            self._chat_channels = ChatChannelsClient(client_wrapper=self._client_wrapper)
        return self._chat_channels

    @property
    def chat_messages(self):
        if self._chat_messages is None:
            from .chat_messages.client import ChatMessagesClient

            self._chat_messages = ChatMessagesClient(client_wrapper=self._client_wrapper)
        return self._chat_messages

    @property
    def chat_users(self):
        if self._chat_users is None:
            from .chat_users.client import ChatUsersClient

            self._chat_users = ChatUsersClient(client_wrapper=self._client_wrapper)
        return self._chat_users

    @property
    def connection(self):
        if self._connection is None:
            from .connection.client import ConnectionClient

            self._connection = ConnectionClient(client_wrapper=self._client_wrapper)
        return self._connection

    @property
    def crm_company(self):
        if self._crm_company is None:
            from .crm_company.client import CrmCompanyClient

            self._crm_company = CrmCompanyClient(client_wrapper=self._client_wrapper)
        return self._crm_company

    @property
    def crm_contact(self):
        if self._crm_contact is None:
            from .crm_contact.client import CrmContactClient

            self._crm_contact = CrmContactClient(client_wrapper=self._client_wrapper)
        return self._crm_contact

    @property
    def crm_deal(self):
        if self._crm_deal is None:
            from .crm_deal.client import CrmDealClient

            self._crm_deal = CrmDealClient(client_wrapper=self._client_wrapper)
        return self._crm_deal

    @property
    def crm_event(self):
        if self._crm_event is None:
            from .crm_event.client import CrmEventClient

            self._crm_event = CrmEventClient(client_wrapper=self._client_wrapper)
        return self._crm_event

    @property
    def crm_lead(self):
        if self._crm_lead is None:
            from .crm_lead.client import CrmLeadClient

            self._crm_lead = CrmLeadClient(client_wrapper=self._client_wrapper)
        return self._crm_lead

    @property
    def crm_note(self):
        if self._crm_note is None:
            from .crm_note.client import CrmNoteClient

            self._crm_note = CrmNoteClient(client_wrapper=self._client_wrapper)
        return self._crm_note

    @property
    def crm_properties(self):
        if self._crm_properties is None:
            from .crm_properties.client import CrmPropertiesClient

            self._crm_properties = CrmPropertiesClient(client_wrapper=self._client_wrapper)
        return self._crm_properties

    @property
    def crm_proxy(self):
        if self._crm_proxy is None:
            from .crm_proxy.client import CrmProxyClient

            self._crm_proxy = CrmProxyClient(client_wrapper=self._client_wrapper)
        return self._crm_proxy

    @property
    def crm_task(self):
        if self._crm_task is None:
            from .crm_task.client import CrmTaskClient

            self._crm_task = CrmTaskClient(client_wrapper=self._client_wrapper)
        return self._crm_task

    @property
    def crm_user(self):
        if self._crm_user is None:
            from .crm_user.client import CrmUserClient

            self._crm_user = CrmUserClient(client_wrapper=self._client_wrapper)
        return self._crm_user

    @property
    def fieldmapping(self):
        if self._fieldmapping is None:
            from .fieldmapping.client import FieldmappingClient

            self._fieldmapping = FieldmappingClient(client_wrapper=self._client_wrapper)
        return self._fieldmapping

    @property
    def internal_account(self):
        if self._internal_account is None:
            from .internal_account.client import InternalAccountClient

            self._internal_account = InternalAccountClient(client_wrapper=self._client_wrapper)
        return self._internal_account

    @property
    def internal_analytics(self):
        if self._internal_analytics is None:
            from .internal_analytics.client import InternalAnalyticsClient

            self._internal_analytics = InternalAnalyticsClient(client_wrapper=self._client_wrapper)
        return self._internal_analytics

    @property
    def internal_app(self):
        if self._internal_app is None:
            from .internal_app.client import InternalAppClient

            self._internal_app = InternalAppClient(client_wrapper=self._client_wrapper)
        return self._internal_app

    @property
    def internal_telemetry(self):
        if self._internal_telemetry is None:
            from .internal_telemetry.client import InternalTelemetryClient

            self._internal_telemetry = InternalTelemetryClient(client_wrapper=self._client_wrapper)
        return self._internal_telemetry

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import MetadataClient

            self._metadata = MetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def sync(self):
        if self._sync is None:
            from .sync.client import SyncClient

            self._sync = SyncClient(client_wrapper=self._client_wrapper)
        return self._sync

    @property
    def ticket_collection(self):
        if self._ticket_collection is None:
            from .ticket_collection.client import TicketCollectionClient

            self._ticket_collection = TicketCollectionClient(client_wrapper=self._client_wrapper)
        return self._ticket_collection

    @property
    def ticket_comment(self):
        if self._ticket_comment is None:
            from .ticket_comment.client import TicketCommentClient

            self._ticket_comment = TicketCommentClient(client_wrapper=self._client_wrapper)
        return self._ticket_comment

    @property
    def ticket_proxy(self):
        if self._ticket_proxy is None:
            from .ticket_proxy.client import TicketProxyClient

            self._ticket_proxy = TicketProxyClient(client_wrapper=self._client_wrapper)
        return self._ticket_proxy

    @property
    def ticket_task(self):
        if self._ticket_task is None:
            from .ticket_task.client import TicketTaskClient

            self._ticket_task = TicketTaskClient(client_wrapper=self._client_wrapper)
        return self._ticket_task

    @property
    def ticket_user(self):
        if self._ticket_user is None:
            from .ticket_user.client import TicketUserClient

            self._ticket_user = TicketUserClient(client_wrapper=self._client_wrapper)
        return self._ticket_user


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



        Defaults to FernApiEnvironment.PRODUCTION



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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
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
        self._accounting_account: typing.Optional[AsyncAccountingAccountClient] = None
        self._accounting_expense: typing.Optional[AsyncAccountingExpenseClient] = None
        self._accounting_proxy: typing.Optional[AsyncAccountingProxyClient] = None
        self._accounting_vendor: typing.Optional[AsyncAccountingVendorClient] = None
        self._ats_candidate: typing.Optional[AsyncAtsCandidateClient] = None
        self._ats_department: typing.Optional[AsyncAtsDepartmentClient] = None
        self._ats_job: typing.Optional[AsyncAtsJobClient] = None
        self._ats_offer: typing.Optional[AsyncAtsOfferClient] = None
        self._ats_proxy: typing.Optional[AsyncAtsProxyClient] = None
        self._chat_channels: typing.Optional[AsyncChatChannelsClient] = None
        self._chat_messages: typing.Optional[AsyncChatMessagesClient] = None
        self._chat_users: typing.Optional[AsyncChatUsersClient] = None
        self._connection: typing.Optional[AsyncConnectionClient] = None
        self._crm_company: typing.Optional[AsyncCrmCompanyClient] = None
        self._crm_contact: typing.Optional[AsyncCrmContactClient] = None
        self._crm_deal: typing.Optional[AsyncCrmDealClient] = None
        self._crm_event: typing.Optional[AsyncCrmEventClient] = None
        self._crm_lead: typing.Optional[AsyncCrmLeadClient] = None
        self._crm_note: typing.Optional[AsyncCrmNoteClient] = None
        self._crm_properties: typing.Optional[AsyncCrmPropertiesClient] = None
        self._crm_proxy: typing.Optional[AsyncCrmProxyClient] = None
        self._crm_task: typing.Optional[AsyncCrmTaskClient] = None
        self._crm_user: typing.Optional[AsyncCrmUserClient] = None
        self._fieldmapping: typing.Optional[AsyncFieldmappingClient] = None
        self._internal_account: typing.Optional[AsyncInternalAccountClient] = None
        self._internal_analytics: typing.Optional[AsyncInternalAnalyticsClient] = None
        self._internal_app: typing.Optional[AsyncInternalAppClient] = None
        self._internal_telemetry: typing.Optional[AsyncInternalTelemetryClient] = None
        self._metadata: typing.Optional[AsyncMetadataClient] = None
        self._sync: typing.Optional[AsyncSyncClient] = None
        self._ticket_collection: typing.Optional[AsyncTicketCollectionClient] = None
        self._ticket_comment: typing.Optional[AsyncTicketCommentClient] = None
        self._ticket_proxy: typing.Optional[AsyncTicketProxyClient] = None
        self._ticket_task: typing.Optional[AsyncTicketTaskClient] = None
        self._ticket_user: typing.Optional[AsyncTicketUserClient] = None

    @property
    def accounting_account(self):
        if self._accounting_account is None:
            from .accounting_account.client import AsyncAccountingAccountClient

            self._accounting_account = AsyncAccountingAccountClient(client_wrapper=self._client_wrapper)
        return self._accounting_account

    @property
    def accounting_expense(self):
        if self._accounting_expense is None:
            from .accounting_expense.client import AsyncAccountingExpenseClient

            self._accounting_expense = AsyncAccountingExpenseClient(client_wrapper=self._client_wrapper)
        return self._accounting_expense

    @property
    def accounting_proxy(self):
        if self._accounting_proxy is None:
            from .accounting_proxy.client import AsyncAccountingProxyClient

            self._accounting_proxy = AsyncAccountingProxyClient(client_wrapper=self._client_wrapper)
        return self._accounting_proxy

    @property
    def accounting_vendor(self):
        if self._accounting_vendor is None:
            from .accounting_vendor.client import AsyncAccountingVendorClient

            self._accounting_vendor = AsyncAccountingVendorClient(client_wrapper=self._client_wrapper)
        return self._accounting_vendor

    @property
    def ats_candidate(self):
        if self._ats_candidate is None:
            from .ats_candidate.client import AsyncAtsCandidateClient

            self._ats_candidate = AsyncAtsCandidateClient(client_wrapper=self._client_wrapper)
        return self._ats_candidate

    @property
    def ats_department(self):
        if self._ats_department is None:
            from .ats_department.client import AsyncAtsDepartmentClient

            self._ats_department = AsyncAtsDepartmentClient(client_wrapper=self._client_wrapper)
        return self._ats_department

    @property
    def ats_job(self):
        if self._ats_job is None:
            from .ats_job.client import AsyncAtsJobClient

            self._ats_job = AsyncAtsJobClient(client_wrapper=self._client_wrapper)
        return self._ats_job

    @property
    def ats_offer(self):
        if self._ats_offer is None:
            from .ats_offer.client import AsyncAtsOfferClient

            self._ats_offer = AsyncAtsOfferClient(client_wrapper=self._client_wrapper)
        return self._ats_offer

    @property
    def ats_proxy(self):
        if self._ats_proxy is None:
            from .ats_proxy.client import AsyncAtsProxyClient

            self._ats_proxy = AsyncAtsProxyClient(client_wrapper=self._client_wrapper)
        return self._ats_proxy

    @property
    def chat_channels(self):
        if self._chat_channels is None:
            from .chat_channels.client import AsyncChatChannelsClient

            self._chat_channels = AsyncChatChannelsClient(client_wrapper=self._client_wrapper)
        return self._chat_channels

    @property
    def chat_messages(self):
        if self._chat_messages is None:
            from .chat_messages.client import AsyncChatMessagesClient

            self._chat_messages = AsyncChatMessagesClient(client_wrapper=self._client_wrapper)
        return self._chat_messages

    @property
    def chat_users(self):
        if self._chat_users is None:
            from .chat_users.client import AsyncChatUsersClient

            self._chat_users = AsyncChatUsersClient(client_wrapper=self._client_wrapper)
        return self._chat_users

    @property
    def connection(self):
        if self._connection is None:
            from .connection.client import AsyncConnectionClient

            self._connection = AsyncConnectionClient(client_wrapper=self._client_wrapper)
        return self._connection

    @property
    def crm_company(self):
        if self._crm_company is None:
            from .crm_company.client import AsyncCrmCompanyClient

            self._crm_company = AsyncCrmCompanyClient(client_wrapper=self._client_wrapper)
        return self._crm_company

    @property
    def crm_contact(self):
        if self._crm_contact is None:
            from .crm_contact.client import AsyncCrmContactClient

            self._crm_contact = AsyncCrmContactClient(client_wrapper=self._client_wrapper)
        return self._crm_contact

    @property
    def crm_deal(self):
        if self._crm_deal is None:
            from .crm_deal.client import AsyncCrmDealClient

            self._crm_deal = AsyncCrmDealClient(client_wrapper=self._client_wrapper)
        return self._crm_deal

    @property
    def crm_event(self):
        if self._crm_event is None:
            from .crm_event.client import AsyncCrmEventClient

            self._crm_event = AsyncCrmEventClient(client_wrapper=self._client_wrapper)
        return self._crm_event

    @property
    def crm_lead(self):
        if self._crm_lead is None:
            from .crm_lead.client import AsyncCrmLeadClient

            self._crm_lead = AsyncCrmLeadClient(client_wrapper=self._client_wrapper)
        return self._crm_lead

    @property
    def crm_note(self):
        if self._crm_note is None:
            from .crm_note.client import AsyncCrmNoteClient

            self._crm_note = AsyncCrmNoteClient(client_wrapper=self._client_wrapper)
        return self._crm_note

    @property
    def crm_properties(self):
        if self._crm_properties is None:
            from .crm_properties.client import AsyncCrmPropertiesClient

            self._crm_properties = AsyncCrmPropertiesClient(client_wrapper=self._client_wrapper)
        return self._crm_properties

    @property
    def crm_proxy(self):
        if self._crm_proxy is None:
            from .crm_proxy.client import AsyncCrmProxyClient

            self._crm_proxy = AsyncCrmProxyClient(client_wrapper=self._client_wrapper)
        return self._crm_proxy

    @property
    def crm_task(self):
        if self._crm_task is None:
            from .crm_task.client import AsyncCrmTaskClient

            self._crm_task = AsyncCrmTaskClient(client_wrapper=self._client_wrapper)
        return self._crm_task

    @property
    def crm_user(self):
        if self._crm_user is None:
            from .crm_user.client import AsyncCrmUserClient

            self._crm_user = AsyncCrmUserClient(client_wrapper=self._client_wrapper)
        return self._crm_user

    @property
    def fieldmapping(self):
        if self._fieldmapping is None:
            from .fieldmapping.client import AsyncFieldmappingClient

            self._fieldmapping = AsyncFieldmappingClient(client_wrapper=self._client_wrapper)
        return self._fieldmapping

    @property
    def internal_account(self):
        if self._internal_account is None:
            from .internal_account.client import AsyncInternalAccountClient

            self._internal_account = AsyncInternalAccountClient(client_wrapper=self._client_wrapper)
        return self._internal_account

    @property
    def internal_analytics(self):
        if self._internal_analytics is None:
            from .internal_analytics.client import AsyncInternalAnalyticsClient

            self._internal_analytics = AsyncInternalAnalyticsClient(client_wrapper=self._client_wrapper)
        return self._internal_analytics

    @property
    def internal_app(self):
        if self._internal_app is None:
            from .internal_app.client import AsyncInternalAppClient

            self._internal_app = AsyncInternalAppClient(client_wrapper=self._client_wrapper)
        return self._internal_app

    @property
    def internal_telemetry(self):
        if self._internal_telemetry is None:
            from .internal_telemetry.client import AsyncInternalTelemetryClient

            self._internal_telemetry = AsyncInternalTelemetryClient(client_wrapper=self._client_wrapper)
        return self._internal_telemetry

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import AsyncMetadataClient

            self._metadata = AsyncMetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def sync(self):
        if self._sync is None:
            from .sync.client import AsyncSyncClient

            self._sync = AsyncSyncClient(client_wrapper=self._client_wrapper)
        return self._sync

    @property
    def ticket_collection(self):
        if self._ticket_collection is None:
            from .ticket_collection.client import AsyncTicketCollectionClient

            self._ticket_collection = AsyncTicketCollectionClient(client_wrapper=self._client_wrapper)
        return self._ticket_collection

    @property
    def ticket_comment(self):
        if self._ticket_comment is None:
            from .ticket_comment.client import AsyncTicketCommentClient

            self._ticket_comment = AsyncTicketCommentClient(client_wrapper=self._client_wrapper)
        return self._ticket_comment

    @property
    def ticket_proxy(self):
        if self._ticket_proxy is None:
            from .ticket_proxy.client import AsyncTicketProxyClient

            self._ticket_proxy = AsyncTicketProxyClient(client_wrapper=self._client_wrapper)
        return self._ticket_proxy

    @property
    def ticket_task(self):
        if self._ticket_task is None:
            from .ticket_task.client import AsyncTicketTaskClient

            self._ticket_task = AsyncTicketTaskClient(client_wrapper=self._client_wrapper)
        return self._ticket_task

    @property
    def ticket_user(self):
        if self._ticket_user is None:
            from .ticket_user.client import AsyncTicketUserClient

            self._ticket_user = AsyncTicketUserClient(client_wrapper=self._client_wrapper)
        return self._ticket_user


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
