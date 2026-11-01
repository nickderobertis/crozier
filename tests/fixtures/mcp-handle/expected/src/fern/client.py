

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .airtable_oauth.client import AirtableOauthClient, AsyncAirtableOauthClient
    from .asana_oauth.client import AsanaOauthClient, AsyncAsanaOauthClient
    from .attio_oauth.client import AsyncAttioOauthClient, AttioOauthClient
    from .box_oauth.client import AsyncBoxOauthClient, BoxOauthClient
    from .calcom_oauth.client import AsyncCalcomOauthClient, CalcomOauthClient
    from .canva_oauth.client import AsyncCanvaOauthClient, CanvaOauthClient
    from .clickup_oauth.client import AsyncClickupOauthClient, ClickupOauthClient
    from .close_oauth.client import AsyncCloseOauthClient, CloseOauthClient
    from .confluence_oauth.client import AsyncConfluenceOauthClient, ConfluenceOauthClient
    from .dialpad_oauth.client import AsyncDialpadOauthClient, DialpadOauthClient
    from .docusign_oauth.client import AsyncDocusignOauthClient, DocusignOauthClient
    from .dropbox_oauth.client import AsyncDropboxOauthClient, DropboxOauthClient
    from .fathom_oauth.client import AsyncFathomOauthClient, FathomOauthClient
    from .figma_oauth.client import AsyncFigmaOauthClient, FigmaOauthClient
    from .gcalendar_oauth.client import AsyncGcalendarOauthClient, GcalendarOauthClient
    from .gdocs_oauth.client import AsyncGdocsOauthClient, GdocsOauthClient
    from .gdrive_oauth.client import AsyncGdriveOauthClient, GdriveOauthClient
    from .github_oauth.client import AsyncGithubOauthClient, GithubOauthClient
    from .gitlab_oauth.client import AsyncGitlabOauthClient, GitlabOauthClient
    from .gmail_oauth.client import AsyncGmailOauthClient, GmailOauthClient
    from .gsheets_oauth.client import AsyncGsheetsOauthClient, GsheetsOauthClient
    from .hubspot_oauth.client import AsyncHubspotOauthClient, HubspotOauthClient
    from .jira_oauth.client import AsyncJiraOauthClient, JiraOauthClient
    from .klaviyo_oauth.client import AsyncKlaviyoOauthClient, KlaviyoOauthClient
    from .linear_oauth.client import AsyncLinearOauthClient, LinearOauthClient
    from .linkedin_oauth.client import AsyncLinkedinOauthClient, LinkedinOauthClient
    from .mcp_server.client import AsyncMcpServerClient, McpServerClient
    from .monday_oauth.client import AsyncMondayOauthClient, MondayOauthClient
    from .notion_oauth.client import AsyncNotionOauthClient, NotionOauthClient
    from .onedrive_oauth.client import AsyncOnedriveOauthClient, OnedriveOauthClient
    from .outlook_oauth.client import AsyncOutlookOauthClient, OutlookOauthClient
    from .pagerduty_oauth.client import AsyncPagerdutyOauthClient, PagerdutyOauthClient
    from .pipedrive_oauth.client import AsyncPipedriveOauthClient, PipedriveOauthClient
    from .quickbooks_oauth.client import AsyncQuickbooksOauthClient, QuickbooksOauthClient
    from .salesforce_oauth.client import AsyncSalesforceOauthClient, SalesforceOauthClient
    from .shopify_oauth.client import AsyncShopifyOauthClient, ShopifyOauthClient
    from .slack_oauth.client import AsyncSlackOauthClient, SlackOauthClient
    from .stripe_connect_oauth.client import AsyncStripeConnectOauthClient, StripeConnectOauthClient
    from .supabase_oauth.client import AsyncSupabaseOauthClient, SupabaseOauthClient
    from .teams_oauth.client import AsyncTeamsOauthClient, TeamsOauthClient
    from .user.client import AsyncUserClient, UserClient
    from .vercel_oauth.client import AsyncVercelOauthClient, VercelOauthClient
    from .white_labeling.client import AsyncWhiteLabelingClient, WhiteLabelingClient
    from .wordpress_oauth.client import AsyncWordpressOauthClient, WordpressOauthClient
    from .xero_oauth.client import AsyncXeroOauthClient, XeroOauthClient
    from .zendesk_oauth.client import AsyncZendeskOauthClient, ZendeskOauthClient


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



    api_key : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
        self._mcp_server: typing.Optional[McpServerClient] = None
        self._white_labeling: typing.Optional[WhiteLabelingClient] = None
        self._user: typing.Optional[UserClient] = None
        self._slack_oauth: typing.Optional[SlackOauthClient] = None
        self._github_oauth: typing.Optional[GithubOauthClient] = None
        self._gitlab_oauth: typing.Optional[GitlabOauthClient] = None
        self._supabase_oauth: typing.Optional[SupabaseOauthClient] = None
        self._notion_oauth: typing.Optional[NotionOauthClient] = None
        self._jira_oauth: typing.Optional[JiraOauthClient] = None
        self._confluence_oauth: typing.Optional[ConfluenceOauthClient] = None
        self._wordpress_oauth: typing.Optional[WordpressOauthClient] = None
        self._gmail_oauth: typing.Optional[GmailOauthClient] = None
        self._gdrive_oauth: typing.Optional[GdriveOauthClient] = None
        self._gcalendar_oauth: typing.Optional[GcalendarOauthClient] = None
        self._gsheets_oauth: typing.Optional[GsheetsOauthClient] = None
        self._gdocs_oauth: typing.Optional[GdocsOauthClient] = None
        self._attio_oauth: typing.Optional[AttioOauthClient] = None
        self._salesforce_oauth: typing.Optional[SalesforceOauthClient] = None
        self._asana_oauth: typing.Optional[AsanaOauthClient] = None
        self._linear_oauth: typing.Optional[LinearOauthClient] = None
        self._close_oauth: typing.Optional[CloseOauthClient] = None
        self._clickup_oauth: typing.Optional[ClickupOauthClient] = None
        self._airtable_oauth: typing.Optional[AirtableOauthClient] = None
        self._hubspot_oauth: typing.Optional[HubspotOauthClient] = None
        self._linkedin_oauth: typing.Optional[LinkedinOauthClient] = None
        self._canva_oauth: typing.Optional[CanvaOauthClient] = None
        self._xero_oauth: typing.Optional[XeroOauthClient] = None
        self._dropbox_oauth: typing.Optional[DropboxOauthClient] = None
        self._box_oauth: typing.Optional[BoxOauthClient] = None
        self._quickbooks_oauth: typing.Optional[QuickbooksOauthClient] = None
        self._zendesk_oauth: typing.Optional[ZendeskOauthClient] = None
        self._stripe_connect_oauth: typing.Optional[StripeConnectOauthClient] = None
        self._calcom_oauth: typing.Optional[CalcomOauthClient] = None
        self._vercel_oauth: typing.Optional[VercelOauthClient] = None
        self._pipedrive_oauth: typing.Optional[PipedriveOauthClient] = None
        self._figma_oauth: typing.Optional[FigmaOauthClient] = None
        self._klaviyo_oauth: typing.Optional[KlaviyoOauthClient] = None
        self._pagerduty_oauth: typing.Optional[PagerdutyOauthClient] = None
        self._docusign_oauth: typing.Optional[DocusignOauthClient] = None
        self._dialpad_oauth: typing.Optional[DialpadOauthClient] = None
        self._shopify_oauth: typing.Optional[ShopifyOauthClient] = None
        self._onedrive_oauth: typing.Optional[OnedriveOauthClient] = None
        self._outlook_oauth: typing.Optional[OutlookOauthClient] = None
        self._teams_oauth: typing.Optional[TeamsOauthClient] = None
        self._fathom_oauth: typing.Optional[FathomOauthClient] = None
        self._monday_oauth: typing.Optional[MondayOauthClient] = None

    @property
    def mcp_server(self):
        if self._mcp_server is None:
            from .mcp_server.client import McpServerClient

            self._mcp_server = McpServerClient(client_wrapper=self._client_wrapper)
        return self._mcp_server

    @property
    def white_labeling(self):
        if self._white_labeling is None:
            from .white_labeling.client import WhiteLabelingClient

            self._white_labeling = WhiteLabelingClient(client_wrapper=self._client_wrapper)
        return self._white_labeling

    @property
    def user(self):
        if self._user is None:
            from .user.client import UserClient

            self._user = UserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def slack_oauth(self):
        if self._slack_oauth is None:
            from .slack_oauth.client import SlackOauthClient

            self._slack_oauth = SlackOauthClient(client_wrapper=self._client_wrapper)
        return self._slack_oauth

    @property
    def github_oauth(self):
        if self._github_oauth is None:
            from .github_oauth.client import GithubOauthClient

            self._github_oauth = GithubOauthClient(client_wrapper=self._client_wrapper)
        return self._github_oauth

    @property
    def gitlab_oauth(self):
        if self._gitlab_oauth is None:
            from .gitlab_oauth.client import GitlabOauthClient

            self._gitlab_oauth = GitlabOauthClient(client_wrapper=self._client_wrapper)
        return self._gitlab_oauth

    @property
    def supabase_oauth(self):
        if self._supabase_oauth is None:
            from .supabase_oauth.client import SupabaseOauthClient

            self._supabase_oauth = SupabaseOauthClient(client_wrapper=self._client_wrapper)
        return self._supabase_oauth

    @property
    def notion_oauth(self):
        if self._notion_oauth is None:
            from .notion_oauth.client import NotionOauthClient

            self._notion_oauth = NotionOauthClient(client_wrapper=self._client_wrapper)
        return self._notion_oauth

    @property
    def jira_oauth(self):
        if self._jira_oauth is None:
            from .jira_oauth.client import JiraOauthClient

            self._jira_oauth = JiraOauthClient(client_wrapper=self._client_wrapper)
        return self._jira_oauth

    @property
    def confluence_oauth(self):
        if self._confluence_oauth is None:
            from .confluence_oauth.client import ConfluenceOauthClient

            self._confluence_oauth = ConfluenceOauthClient(client_wrapper=self._client_wrapper)
        return self._confluence_oauth

    @property
    def wordpress_oauth(self):
        if self._wordpress_oauth is None:
            from .wordpress_oauth.client import WordpressOauthClient

            self._wordpress_oauth = WordpressOauthClient(client_wrapper=self._client_wrapper)
        return self._wordpress_oauth

    @property
    def gmail_oauth(self):
        if self._gmail_oauth is None:
            from .gmail_oauth.client import GmailOauthClient

            self._gmail_oauth = GmailOauthClient(client_wrapper=self._client_wrapper)
        return self._gmail_oauth

    @property
    def gdrive_oauth(self):
        if self._gdrive_oauth is None:
            from .gdrive_oauth.client import GdriveOauthClient

            self._gdrive_oauth = GdriveOauthClient(client_wrapper=self._client_wrapper)
        return self._gdrive_oauth

    @property
    def gcalendar_oauth(self):
        if self._gcalendar_oauth is None:
            from .gcalendar_oauth.client import GcalendarOauthClient

            self._gcalendar_oauth = GcalendarOauthClient(client_wrapper=self._client_wrapper)
        return self._gcalendar_oauth

    @property
    def gsheets_oauth(self):
        if self._gsheets_oauth is None:
            from .gsheets_oauth.client import GsheetsOauthClient

            self._gsheets_oauth = GsheetsOauthClient(client_wrapper=self._client_wrapper)
        return self._gsheets_oauth

    @property
    def gdocs_oauth(self):
        if self._gdocs_oauth is None:
            from .gdocs_oauth.client import GdocsOauthClient

            self._gdocs_oauth = GdocsOauthClient(client_wrapper=self._client_wrapper)
        return self._gdocs_oauth

    @property
    def attio_oauth(self):
        if self._attio_oauth is None:
            from .attio_oauth.client import AttioOauthClient

            self._attio_oauth = AttioOauthClient(client_wrapper=self._client_wrapper)
        return self._attio_oauth

    @property
    def salesforce_oauth(self):
        if self._salesforce_oauth is None:
            from .salesforce_oauth.client import SalesforceOauthClient

            self._salesforce_oauth = SalesforceOauthClient(client_wrapper=self._client_wrapper)
        return self._salesforce_oauth

    @property
    def asana_oauth(self):
        if self._asana_oauth is None:
            from .asana_oauth.client import AsanaOauthClient

            self._asana_oauth = AsanaOauthClient(client_wrapper=self._client_wrapper)
        return self._asana_oauth

    @property
    def linear_oauth(self):
        if self._linear_oauth is None:
            from .linear_oauth.client import LinearOauthClient

            self._linear_oauth = LinearOauthClient(client_wrapper=self._client_wrapper)
        return self._linear_oauth

    @property
    def close_oauth(self):
        if self._close_oauth is None:
            from .close_oauth.client import CloseOauthClient

            self._close_oauth = CloseOauthClient(client_wrapper=self._client_wrapper)
        return self._close_oauth

    @property
    def clickup_oauth(self):
        if self._clickup_oauth is None:
            from .clickup_oauth.client import ClickupOauthClient

            self._clickup_oauth = ClickupOauthClient(client_wrapper=self._client_wrapper)
        return self._clickup_oauth

    @property
    def airtable_oauth(self):
        if self._airtable_oauth is None:
            from .airtable_oauth.client import AirtableOauthClient

            self._airtable_oauth = AirtableOauthClient(client_wrapper=self._client_wrapper)
        return self._airtable_oauth

    @property
    def hubspot_oauth(self):
        if self._hubspot_oauth is None:
            from .hubspot_oauth.client import HubspotOauthClient

            self._hubspot_oauth = HubspotOauthClient(client_wrapper=self._client_wrapper)
        return self._hubspot_oauth

    @property
    def linkedin_oauth(self):
        if self._linkedin_oauth is None:
            from .linkedin_oauth.client import LinkedinOauthClient

            self._linkedin_oauth = LinkedinOauthClient(client_wrapper=self._client_wrapper)
        return self._linkedin_oauth

    @property
    def canva_oauth(self):
        if self._canva_oauth is None:
            from .canva_oauth.client import CanvaOauthClient

            self._canva_oauth = CanvaOauthClient(client_wrapper=self._client_wrapper)
        return self._canva_oauth

    @property
    def xero_oauth(self):
        if self._xero_oauth is None:
            from .xero_oauth.client import XeroOauthClient

            self._xero_oauth = XeroOauthClient(client_wrapper=self._client_wrapper)
        return self._xero_oauth

    @property
    def dropbox_oauth(self):
        if self._dropbox_oauth is None:
            from .dropbox_oauth.client import DropboxOauthClient

            self._dropbox_oauth = DropboxOauthClient(client_wrapper=self._client_wrapper)
        return self._dropbox_oauth

    @property
    def box_oauth(self):
        if self._box_oauth is None:
            from .box_oauth.client import BoxOauthClient

            self._box_oauth = BoxOauthClient(client_wrapper=self._client_wrapper)
        return self._box_oauth

    @property
    def quickbooks_oauth(self):
        if self._quickbooks_oauth is None:
            from .quickbooks_oauth.client import QuickbooksOauthClient

            self._quickbooks_oauth = QuickbooksOauthClient(client_wrapper=self._client_wrapper)
        return self._quickbooks_oauth

    @property
    def zendesk_oauth(self):
        if self._zendesk_oauth is None:
            from .zendesk_oauth.client import ZendeskOauthClient

            self._zendesk_oauth = ZendeskOauthClient(client_wrapper=self._client_wrapper)
        return self._zendesk_oauth

    @property
    def stripe_connect_oauth(self):
        if self._stripe_connect_oauth is None:
            from .stripe_connect_oauth.client import StripeConnectOauthClient

            self._stripe_connect_oauth = StripeConnectOauthClient(client_wrapper=self._client_wrapper)
        return self._stripe_connect_oauth

    @property
    def calcom_oauth(self):
        if self._calcom_oauth is None:
            from .calcom_oauth.client import CalcomOauthClient

            self._calcom_oauth = CalcomOauthClient(client_wrapper=self._client_wrapper)
        return self._calcom_oauth

    @property
    def vercel_oauth(self):
        if self._vercel_oauth is None:
            from .vercel_oauth.client import VercelOauthClient

            self._vercel_oauth = VercelOauthClient(client_wrapper=self._client_wrapper)
        return self._vercel_oauth

    @property
    def pipedrive_oauth(self):
        if self._pipedrive_oauth is None:
            from .pipedrive_oauth.client import PipedriveOauthClient

            self._pipedrive_oauth = PipedriveOauthClient(client_wrapper=self._client_wrapper)
        return self._pipedrive_oauth

    @property
    def figma_oauth(self):
        if self._figma_oauth is None:
            from .figma_oauth.client import FigmaOauthClient

            self._figma_oauth = FigmaOauthClient(client_wrapper=self._client_wrapper)
        return self._figma_oauth

    @property
    def klaviyo_oauth(self):
        if self._klaviyo_oauth is None:
            from .klaviyo_oauth.client import KlaviyoOauthClient

            self._klaviyo_oauth = KlaviyoOauthClient(client_wrapper=self._client_wrapper)
        return self._klaviyo_oauth

    @property
    def pagerduty_oauth(self):
        if self._pagerduty_oauth is None:
            from .pagerduty_oauth.client import PagerdutyOauthClient

            self._pagerduty_oauth = PagerdutyOauthClient(client_wrapper=self._client_wrapper)
        return self._pagerduty_oauth

    @property
    def docusign_oauth(self):
        if self._docusign_oauth is None:
            from .docusign_oauth.client import DocusignOauthClient

            self._docusign_oauth = DocusignOauthClient(client_wrapper=self._client_wrapper)
        return self._docusign_oauth

    @property
    def dialpad_oauth(self):
        if self._dialpad_oauth is None:
            from .dialpad_oauth.client import DialpadOauthClient

            self._dialpad_oauth = DialpadOauthClient(client_wrapper=self._client_wrapper)
        return self._dialpad_oauth

    @property
    def shopify_oauth(self):
        if self._shopify_oauth is None:
            from .shopify_oauth.client import ShopifyOauthClient

            self._shopify_oauth = ShopifyOauthClient(client_wrapper=self._client_wrapper)
        return self._shopify_oauth

    @property
    def onedrive_oauth(self):
        if self._onedrive_oauth is None:
            from .onedrive_oauth.client import OnedriveOauthClient

            self._onedrive_oauth = OnedriveOauthClient(client_wrapper=self._client_wrapper)
        return self._onedrive_oauth

    @property
    def outlook_oauth(self):
        if self._outlook_oauth is None:
            from .outlook_oauth.client import OutlookOauthClient

            self._outlook_oauth = OutlookOauthClient(client_wrapper=self._client_wrapper)
        return self._outlook_oauth

    @property
    def teams_oauth(self):
        if self._teams_oauth is None:
            from .teams_oauth.client import TeamsOauthClient

            self._teams_oauth = TeamsOauthClient(client_wrapper=self._client_wrapper)
        return self._teams_oauth

    @property
    def fathom_oauth(self):
        if self._fathom_oauth is None:
            from .fathom_oauth.client import FathomOauthClient

            self._fathom_oauth = FathomOauthClient(client_wrapper=self._client_wrapper)
        return self._fathom_oauth

    @property
    def monday_oauth(self):
        if self._monday_oauth is None:
            from .monday_oauth.client import MondayOauthClient

            self._monday_oauth = MondayOauthClient(client_wrapper=self._client_wrapper)
        return self._monday_oauth


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



    api_key : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            api_key=api_key,
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
        self._mcp_server: typing.Optional[AsyncMcpServerClient] = None
        self._white_labeling: typing.Optional[AsyncWhiteLabelingClient] = None
        self._user: typing.Optional[AsyncUserClient] = None
        self._slack_oauth: typing.Optional[AsyncSlackOauthClient] = None
        self._github_oauth: typing.Optional[AsyncGithubOauthClient] = None
        self._gitlab_oauth: typing.Optional[AsyncGitlabOauthClient] = None
        self._supabase_oauth: typing.Optional[AsyncSupabaseOauthClient] = None
        self._notion_oauth: typing.Optional[AsyncNotionOauthClient] = None
        self._jira_oauth: typing.Optional[AsyncJiraOauthClient] = None
        self._confluence_oauth: typing.Optional[AsyncConfluenceOauthClient] = None
        self._wordpress_oauth: typing.Optional[AsyncWordpressOauthClient] = None
        self._gmail_oauth: typing.Optional[AsyncGmailOauthClient] = None
        self._gdrive_oauth: typing.Optional[AsyncGdriveOauthClient] = None
        self._gcalendar_oauth: typing.Optional[AsyncGcalendarOauthClient] = None
        self._gsheets_oauth: typing.Optional[AsyncGsheetsOauthClient] = None
        self._gdocs_oauth: typing.Optional[AsyncGdocsOauthClient] = None
        self._attio_oauth: typing.Optional[AsyncAttioOauthClient] = None
        self._salesforce_oauth: typing.Optional[AsyncSalesforceOauthClient] = None
        self._asana_oauth: typing.Optional[AsyncAsanaOauthClient] = None
        self._linear_oauth: typing.Optional[AsyncLinearOauthClient] = None
        self._close_oauth: typing.Optional[AsyncCloseOauthClient] = None
        self._clickup_oauth: typing.Optional[AsyncClickupOauthClient] = None
        self._airtable_oauth: typing.Optional[AsyncAirtableOauthClient] = None
        self._hubspot_oauth: typing.Optional[AsyncHubspotOauthClient] = None
        self._linkedin_oauth: typing.Optional[AsyncLinkedinOauthClient] = None
        self._canva_oauth: typing.Optional[AsyncCanvaOauthClient] = None
        self._xero_oauth: typing.Optional[AsyncXeroOauthClient] = None
        self._dropbox_oauth: typing.Optional[AsyncDropboxOauthClient] = None
        self._box_oauth: typing.Optional[AsyncBoxOauthClient] = None
        self._quickbooks_oauth: typing.Optional[AsyncQuickbooksOauthClient] = None
        self._zendesk_oauth: typing.Optional[AsyncZendeskOauthClient] = None
        self._stripe_connect_oauth: typing.Optional[AsyncStripeConnectOauthClient] = None
        self._calcom_oauth: typing.Optional[AsyncCalcomOauthClient] = None
        self._vercel_oauth: typing.Optional[AsyncVercelOauthClient] = None
        self._pipedrive_oauth: typing.Optional[AsyncPipedriveOauthClient] = None
        self._figma_oauth: typing.Optional[AsyncFigmaOauthClient] = None
        self._klaviyo_oauth: typing.Optional[AsyncKlaviyoOauthClient] = None
        self._pagerduty_oauth: typing.Optional[AsyncPagerdutyOauthClient] = None
        self._docusign_oauth: typing.Optional[AsyncDocusignOauthClient] = None
        self._dialpad_oauth: typing.Optional[AsyncDialpadOauthClient] = None
        self._shopify_oauth: typing.Optional[AsyncShopifyOauthClient] = None
        self._onedrive_oauth: typing.Optional[AsyncOnedriveOauthClient] = None
        self._outlook_oauth: typing.Optional[AsyncOutlookOauthClient] = None
        self._teams_oauth: typing.Optional[AsyncTeamsOauthClient] = None
        self._fathom_oauth: typing.Optional[AsyncFathomOauthClient] = None
        self._monday_oauth: typing.Optional[AsyncMondayOauthClient] = None

    @property
    def mcp_server(self):
        if self._mcp_server is None:
            from .mcp_server.client import AsyncMcpServerClient

            self._mcp_server = AsyncMcpServerClient(client_wrapper=self._client_wrapper)
        return self._mcp_server

    @property
    def white_labeling(self):
        if self._white_labeling is None:
            from .white_labeling.client import AsyncWhiteLabelingClient

            self._white_labeling = AsyncWhiteLabelingClient(client_wrapper=self._client_wrapper)
        return self._white_labeling

    @property
    def user(self):
        if self._user is None:
            from .user.client import AsyncUserClient

            self._user = AsyncUserClient(client_wrapper=self._client_wrapper)
        return self._user

    @property
    def slack_oauth(self):
        if self._slack_oauth is None:
            from .slack_oauth.client import AsyncSlackOauthClient

            self._slack_oauth = AsyncSlackOauthClient(client_wrapper=self._client_wrapper)
        return self._slack_oauth

    @property
    def github_oauth(self):
        if self._github_oauth is None:
            from .github_oauth.client import AsyncGithubOauthClient

            self._github_oauth = AsyncGithubOauthClient(client_wrapper=self._client_wrapper)
        return self._github_oauth

    @property
    def gitlab_oauth(self):
        if self._gitlab_oauth is None:
            from .gitlab_oauth.client import AsyncGitlabOauthClient

            self._gitlab_oauth = AsyncGitlabOauthClient(client_wrapper=self._client_wrapper)
        return self._gitlab_oauth

    @property
    def supabase_oauth(self):
        if self._supabase_oauth is None:
            from .supabase_oauth.client import AsyncSupabaseOauthClient

            self._supabase_oauth = AsyncSupabaseOauthClient(client_wrapper=self._client_wrapper)
        return self._supabase_oauth

    @property
    def notion_oauth(self):
        if self._notion_oauth is None:
            from .notion_oauth.client import AsyncNotionOauthClient

            self._notion_oauth = AsyncNotionOauthClient(client_wrapper=self._client_wrapper)
        return self._notion_oauth

    @property
    def jira_oauth(self):
        if self._jira_oauth is None:
            from .jira_oauth.client import AsyncJiraOauthClient

            self._jira_oauth = AsyncJiraOauthClient(client_wrapper=self._client_wrapper)
        return self._jira_oauth

    @property
    def confluence_oauth(self):
        if self._confluence_oauth is None:
            from .confluence_oauth.client import AsyncConfluenceOauthClient

            self._confluence_oauth = AsyncConfluenceOauthClient(client_wrapper=self._client_wrapper)
        return self._confluence_oauth

    @property
    def wordpress_oauth(self):
        if self._wordpress_oauth is None:
            from .wordpress_oauth.client import AsyncWordpressOauthClient

            self._wordpress_oauth = AsyncWordpressOauthClient(client_wrapper=self._client_wrapper)
        return self._wordpress_oauth

    @property
    def gmail_oauth(self):
        if self._gmail_oauth is None:
            from .gmail_oauth.client import AsyncGmailOauthClient

            self._gmail_oauth = AsyncGmailOauthClient(client_wrapper=self._client_wrapper)
        return self._gmail_oauth

    @property
    def gdrive_oauth(self):
        if self._gdrive_oauth is None:
            from .gdrive_oauth.client import AsyncGdriveOauthClient

            self._gdrive_oauth = AsyncGdriveOauthClient(client_wrapper=self._client_wrapper)
        return self._gdrive_oauth

    @property
    def gcalendar_oauth(self):
        if self._gcalendar_oauth is None:
            from .gcalendar_oauth.client import AsyncGcalendarOauthClient

            self._gcalendar_oauth = AsyncGcalendarOauthClient(client_wrapper=self._client_wrapper)
        return self._gcalendar_oauth

    @property
    def gsheets_oauth(self):
        if self._gsheets_oauth is None:
            from .gsheets_oauth.client import AsyncGsheetsOauthClient

            self._gsheets_oauth = AsyncGsheetsOauthClient(client_wrapper=self._client_wrapper)
        return self._gsheets_oauth

    @property
    def gdocs_oauth(self):
        if self._gdocs_oauth is None:
            from .gdocs_oauth.client import AsyncGdocsOauthClient

            self._gdocs_oauth = AsyncGdocsOauthClient(client_wrapper=self._client_wrapper)
        return self._gdocs_oauth

    @property
    def attio_oauth(self):
        if self._attio_oauth is None:
            from .attio_oauth.client import AsyncAttioOauthClient

            self._attio_oauth = AsyncAttioOauthClient(client_wrapper=self._client_wrapper)
        return self._attio_oauth

    @property
    def salesforce_oauth(self):
        if self._salesforce_oauth is None:
            from .salesforce_oauth.client import AsyncSalesforceOauthClient

            self._salesforce_oauth = AsyncSalesforceOauthClient(client_wrapper=self._client_wrapper)
        return self._salesforce_oauth

    @property
    def asana_oauth(self):
        if self._asana_oauth is None:
            from .asana_oauth.client import AsyncAsanaOauthClient

            self._asana_oauth = AsyncAsanaOauthClient(client_wrapper=self._client_wrapper)
        return self._asana_oauth

    @property
    def linear_oauth(self):
        if self._linear_oauth is None:
            from .linear_oauth.client import AsyncLinearOauthClient

            self._linear_oauth = AsyncLinearOauthClient(client_wrapper=self._client_wrapper)
        return self._linear_oauth

    @property
    def close_oauth(self):
        if self._close_oauth is None:
            from .close_oauth.client import AsyncCloseOauthClient

            self._close_oauth = AsyncCloseOauthClient(client_wrapper=self._client_wrapper)
        return self._close_oauth

    @property
    def clickup_oauth(self):
        if self._clickup_oauth is None:
            from .clickup_oauth.client import AsyncClickupOauthClient

            self._clickup_oauth = AsyncClickupOauthClient(client_wrapper=self._client_wrapper)
        return self._clickup_oauth

    @property
    def airtable_oauth(self):
        if self._airtable_oauth is None:
            from .airtable_oauth.client import AsyncAirtableOauthClient

            self._airtable_oauth = AsyncAirtableOauthClient(client_wrapper=self._client_wrapper)
        return self._airtable_oauth

    @property
    def hubspot_oauth(self):
        if self._hubspot_oauth is None:
            from .hubspot_oauth.client import AsyncHubspotOauthClient

            self._hubspot_oauth = AsyncHubspotOauthClient(client_wrapper=self._client_wrapper)
        return self._hubspot_oauth

    @property
    def linkedin_oauth(self):
        if self._linkedin_oauth is None:
            from .linkedin_oauth.client import AsyncLinkedinOauthClient

            self._linkedin_oauth = AsyncLinkedinOauthClient(client_wrapper=self._client_wrapper)
        return self._linkedin_oauth

    @property
    def canva_oauth(self):
        if self._canva_oauth is None:
            from .canva_oauth.client import AsyncCanvaOauthClient

            self._canva_oauth = AsyncCanvaOauthClient(client_wrapper=self._client_wrapper)
        return self._canva_oauth

    @property
    def xero_oauth(self):
        if self._xero_oauth is None:
            from .xero_oauth.client import AsyncXeroOauthClient

            self._xero_oauth = AsyncXeroOauthClient(client_wrapper=self._client_wrapper)
        return self._xero_oauth

    @property
    def dropbox_oauth(self):
        if self._dropbox_oauth is None:
            from .dropbox_oauth.client import AsyncDropboxOauthClient

            self._dropbox_oauth = AsyncDropboxOauthClient(client_wrapper=self._client_wrapper)
        return self._dropbox_oauth

    @property
    def box_oauth(self):
        if self._box_oauth is None:
            from .box_oauth.client import AsyncBoxOauthClient

            self._box_oauth = AsyncBoxOauthClient(client_wrapper=self._client_wrapper)
        return self._box_oauth

    @property
    def quickbooks_oauth(self):
        if self._quickbooks_oauth is None:
            from .quickbooks_oauth.client import AsyncQuickbooksOauthClient

            self._quickbooks_oauth = AsyncQuickbooksOauthClient(client_wrapper=self._client_wrapper)
        return self._quickbooks_oauth

    @property
    def zendesk_oauth(self):
        if self._zendesk_oauth is None:
            from .zendesk_oauth.client import AsyncZendeskOauthClient

            self._zendesk_oauth = AsyncZendeskOauthClient(client_wrapper=self._client_wrapper)
        return self._zendesk_oauth

    @property
    def stripe_connect_oauth(self):
        if self._stripe_connect_oauth is None:
            from .stripe_connect_oauth.client import AsyncStripeConnectOauthClient

            self._stripe_connect_oauth = AsyncStripeConnectOauthClient(client_wrapper=self._client_wrapper)
        return self._stripe_connect_oauth

    @property
    def calcom_oauth(self):
        if self._calcom_oauth is None:
            from .calcom_oauth.client import AsyncCalcomOauthClient

            self._calcom_oauth = AsyncCalcomOauthClient(client_wrapper=self._client_wrapper)
        return self._calcom_oauth

    @property
    def vercel_oauth(self):
        if self._vercel_oauth is None:
            from .vercel_oauth.client import AsyncVercelOauthClient

            self._vercel_oauth = AsyncVercelOauthClient(client_wrapper=self._client_wrapper)
        return self._vercel_oauth

    @property
    def pipedrive_oauth(self):
        if self._pipedrive_oauth is None:
            from .pipedrive_oauth.client import AsyncPipedriveOauthClient

            self._pipedrive_oauth = AsyncPipedriveOauthClient(client_wrapper=self._client_wrapper)
        return self._pipedrive_oauth

    @property
    def figma_oauth(self):
        if self._figma_oauth is None:
            from .figma_oauth.client import AsyncFigmaOauthClient

            self._figma_oauth = AsyncFigmaOauthClient(client_wrapper=self._client_wrapper)
        return self._figma_oauth

    @property
    def klaviyo_oauth(self):
        if self._klaviyo_oauth is None:
            from .klaviyo_oauth.client import AsyncKlaviyoOauthClient

            self._klaviyo_oauth = AsyncKlaviyoOauthClient(client_wrapper=self._client_wrapper)
        return self._klaviyo_oauth

    @property
    def pagerduty_oauth(self):
        if self._pagerduty_oauth is None:
            from .pagerduty_oauth.client import AsyncPagerdutyOauthClient

            self._pagerduty_oauth = AsyncPagerdutyOauthClient(client_wrapper=self._client_wrapper)
        return self._pagerduty_oauth

    @property
    def docusign_oauth(self):
        if self._docusign_oauth is None:
            from .docusign_oauth.client import AsyncDocusignOauthClient

            self._docusign_oauth = AsyncDocusignOauthClient(client_wrapper=self._client_wrapper)
        return self._docusign_oauth

    @property
    def dialpad_oauth(self):
        if self._dialpad_oauth is None:
            from .dialpad_oauth.client import AsyncDialpadOauthClient

            self._dialpad_oauth = AsyncDialpadOauthClient(client_wrapper=self._client_wrapper)
        return self._dialpad_oauth

    @property
    def shopify_oauth(self):
        if self._shopify_oauth is None:
            from .shopify_oauth.client import AsyncShopifyOauthClient

            self._shopify_oauth = AsyncShopifyOauthClient(client_wrapper=self._client_wrapper)
        return self._shopify_oauth

    @property
    def onedrive_oauth(self):
        if self._onedrive_oauth is None:
            from .onedrive_oauth.client import AsyncOnedriveOauthClient

            self._onedrive_oauth = AsyncOnedriveOauthClient(client_wrapper=self._client_wrapper)
        return self._onedrive_oauth

    @property
    def outlook_oauth(self):
        if self._outlook_oauth is None:
            from .outlook_oauth.client import AsyncOutlookOauthClient

            self._outlook_oauth = AsyncOutlookOauthClient(client_wrapper=self._client_wrapper)
        return self._outlook_oauth

    @property
    def teams_oauth(self):
        if self._teams_oauth is None:
            from .teams_oauth.client import AsyncTeamsOauthClient

            self._teams_oauth = AsyncTeamsOauthClient(client_wrapper=self._client_wrapper)
        return self._teams_oauth

    @property
    def fathom_oauth(self):
        if self._fathom_oauth is None:
            from .fathom_oauth.client import AsyncFathomOauthClient

            self._fathom_oauth = AsyncFathomOauthClient(client_wrapper=self._client_wrapper)
        return self._fathom_oauth

    @property
    def monday_oauth(self):
        if self._monday_oauth is None:
            from .monday_oauth.client import AsyncMondayOauthClient

            self._monday_oauth = AsyncMondayOauthClient(client_wrapper=self._client_wrapper)
        return self._monday_oauth


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
