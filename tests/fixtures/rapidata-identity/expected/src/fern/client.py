

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .bidder.client import AsyncBidderClient, BidderClient
    from .capabilities.client import AsyncCapabilitiesClient, CapabilitiesClient
    from .client.client import AsyncClientClient, ClientClient
    from .customer.client import AsyncCustomerClient, CustomerClient
    from .external_apps.client import AsyncExternalAppsClient, ExternalAppsClient
    from .identity.client import AsyncIdentityClient, IdentityClient
    from .newsletter.client import AsyncNewsletterClient, NewsletterClient
    from .organization.client import AsyncOrganizationClient, OrganizationClient
    from .platform.client import AsyncPlatformClient, PlatformClient
    from .rapidata_identity_api.client import AsyncRapidataIdentityApiClient, RapidataIdentityApiClient
    from .survey.client import AsyncSurveyClient, SurveyClient


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
        self._rapidata_identity_api: typing.Optional[RapidataIdentityApiClient] = None
        self._bidder: typing.Optional[BidderClient] = None
        self._capabilities: typing.Optional[CapabilitiesClient] = None
        self._client: typing.Optional[ClientClient] = None
        self._customer: typing.Optional[CustomerClient] = None
        self._external_apps: typing.Optional[ExternalAppsClient] = None
        self._identity: typing.Optional[IdentityClient] = None
        self._newsletter: typing.Optional[NewsletterClient] = None
        self._organization: typing.Optional[OrganizationClient] = None
        self._platform: typing.Optional[PlatformClient] = None
        self._survey: typing.Optional[SurveyClient] = None

    @property
    def rapidata_identity_api(self):
        if self._rapidata_identity_api is None:
            from .rapidata_identity_api.client import RapidataIdentityApiClient

            self._rapidata_identity_api = RapidataIdentityApiClient(client_wrapper=self._client_wrapper)
        return self._rapidata_identity_api

    @property
    def bidder(self):
        if self._bidder is None:
            from .bidder.client import BidderClient

            self._bidder = BidderClient(client_wrapper=self._client_wrapper)
        return self._bidder

    @property
    def capabilities(self):
        if self._capabilities is None:
            from .capabilities.client import CapabilitiesClient

            self._capabilities = CapabilitiesClient(client_wrapper=self._client_wrapper)
        return self._capabilities

    @property
    def client(self):
        if self._client is None:
            from .client.client import ClientClient

            self._client = ClientClient(client_wrapper=self._client_wrapper)
        return self._client

    @property
    def customer(self):
        if self._customer is None:
            from .customer.client import CustomerClient

            self._customer = CustomerClient(client_wrapper=self._client_wrapper)
        return self._customer

    @property
    def external_apps(self):
        if self._external_apps is None:
            from .external_apps.client import ExternalAppsClient

            self._external_apps = ExternalAppsClient(client_wrapper=self._client_wrapper)
        return self._external_apps

    @property
    def identity(self):
        if self._identity is None:
            from .identity.client import IdentityClient

            self._identity = IdentityClient(client_wrapper=self._client_wrapper)
        return self._identity

    @property
    def newsletter(self):
        if self._newsletter is None:
            from .newsletter.client import NewsletterClient

            self._newsletter = NewsletterClient(client_wrapper=self._client_wrapper)
        return self._newsletter

    @property
    def organization(self):
        if self._organization is None:
            from .organization.client import OrganizationClient

            self._organization = OrganizationClient(client_wrapper=self._client_wrapper)
        return self._organization

    @property
    def platform(self):
        if self._platform is None:
            from .platform.client import PlatformClient

            self._platform = PlatformClient(client_wrapper=self._client_wrapper)
        return self._platform

    @property
    def survey(self):
        if self._survey is None:
            from .survey.client import SurveyClient

            self._survey = SurveyClient(client_wrapper=self._client_wrapper)
        return self._survey


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
        self._rapidata_identity_api: typing.Optional[AsyncRapidataIdentityApiClient] = None
        self._bidder: typing.Optional[AsyncBidderClient] = None
        self._capabilities: typing.Optional[AsyncCapabilitiesClient] = None
        self._client: typing.Optional[AsyncClientClient] = None
        self._customer: typing.Optional[AsyncCustomerClient] = None
        self._external_apps: typing.Optional[AsyncExternalAppsClient] = None
        self._identity: typing.Optional[AsyncIdentityClient] = None
        self._newsletter: typing.Optional[AsyncNewsletterClient] = None
        self._organization: typing.Optional[AsyncOrganizationClient] = None
        self._platform: typing.Optional[AsyncPlatformClient] = None
        self._survey: typing.Optional[AsyncSurveyClient] = None

    @property
    def rapidata_identity_api(self):
        if self._rapidata_identity_api is None:
            from .rapidata_identity_api.client import AsyncRapidataIdentityApiClient

            self._rapidata_identity_api = AsyncRapidataIdentityApiClient(client_wrapper=self._client_wrapper)
        return self._rapidata_identity_api

    @property
    def bidder(self):
        if self._bidder is None:
            from .bidder.client import AsyncBidderClient

            self._bidder = AsyncBidderClient(client_wrapper=self._client_wrapper)
        return self._bidder

    @property
    def capabilities(self):
        if self._capabilities is None:
            from .capabilities.client import AsyncCapabilitiesClient

            self._capabilities = AsyncCapabilitiesClient(client_wrapper=self._client_wrapper)
        return self._capabilities

    @property
    def client(self):
        if self._client is None:
            from .client.client import AsyncClientClient

            self._client = AsyncClientClient(client_wrapper=self._client_wrapper)
        return self._client

    @property
    def customer(self):
        if self._customer is None:
            from .customer.client import AsyncCustomerClient

            self._customer = AsyncCustomerClient(client_wrapper=self._client_wrapper)
        return self._customer

    @property
    def external_apps(self):
        if self._external_apps is None:
            from .external_apps.client import AsyncExternalAppsClient

            self._external_apps = AsyncExternalAppsClient(client_wrapper=self._client_wrapper)
        return self._external_apps

    @property
    def identity(self):
        if self._identity is None:
            from .identity.client import AsyncIdentityClient

            self._identity = AsyncIdentityClient(client_wrapper=self._client_wrapper)
        return self._identity

    @property
    def newsletter(self):
        if self._newsletter is None:
            from .newsletter.client import AsyncNewsletterClient

            self._newsletter = AsyncNewsletterClient(client_wrapper=self._client_wrapper)
        return self._newsletter

    @property
    def organization(self):
        if self._organization is None:
            from .organization.client import AsyncOrganizationClient

            self._organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        return self._organization

    @property
    def platform(self):
        if self._platform is None:
            from .platform.client import AsyncPlatformClient

            self._platform = AsyncPlatformClient(client_wrapper=self._client_wrapper)
        return self._platform

    @property
    def survey(self):
        if self._survey is None:
            from .survey.client import AsyncSurveyClient

            self._survey = AsyncSurveyClient(client_wrapper=self._client_wrapper)
        return self._survey


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
