

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .age_verification.client import AgeVerificationClient, AsyncAgeVerificationClient
    from .background_checks.client import AsyncBackgroundChecksClient, BackgroundChecksClient
    from .client_management.client import AsyncClientManagementClient, ClientManagementClient
    from .compliance.client import AsyncComplianceClient, ComplianceClient
    from .consent_management.client import AsyncConsentManagementClient, ConsentManagementClient
    from .customer_data.client import AsyncCustomerDataClient, CustomerDataClient
    from .discovery.client import AsyncDiscoveryClient, DiscoveryClient
    from .health.client import AsyncHealthClient, HealthClient
    from .identification.client import AsyncIdentificationClient, IdentificationClient
    from .o_auth21oidc.client import AsyncOAuth21OidcClient, OAuth21OidcClient
    from .portfolio_services.client import AsyncPortfolioServicesClient, PortfolioServicesClient
    from .referenzprozess.client import AsyncReferenzprozessClient, ReferenzprozessClient
    from .registry.client import AsyncRegistryClient, RegistryClient
    from .signature_services.client import AsyncSignatureServicesClient, SignatureServicesClient


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
        self._o_auth21oidc: typing.Optional[OAuth21OidcClient] = None
        self._client_management: typing.Optional[ClientManagementClient] = None
        self._discovery: typing.Optional[DiscoveryClient] = None
        self._consent_management: typing.Optional[ConsentManagementClient] = None
        self._referenzprozess: typing.Optional[ReferenzprozessClient] = None
        self._customer_data: typing.Optional[CustomerDataClient] = None
        self._portfolio_services: typing.Optional[PortfolioServicesClient] = None
        self._compliance: typing.Optional[ComplianceClient] = None
        self._age_verification: typing.Optional[AgeVerificationClient] = None
        self._identification: typing.Optional[IdentificationClient] = None
        self._background_checks: typing.Optional[BackgroundChecksClient] = None
        self._signature_services: typing.Optional[SignatureServicesClient] = None
        self._registry: typing.Optional[RegistryClient] = None
        self._health: typing.Optional[HealthClient] = None

    @property
    def o_auth21oidc(self):
        if self._o_auth21oidc is None:
            from .o_auth21oidc.client import OAuth21OidcClient

            self._o_auth21oidc = OAuth21OidcClient(client_wrapper=self._client_wrapper)
        return self._o_auth21oidc

    @property
    def client_management(self):
        if self._client_management is None:
            from .client_management.client import ClientManagementClient

            self._client_management = ClientManagementClient(client_wrapper=self._client_wrapper)
        return self._client_management

    @property
    def discovery(self):
        if self._discovery is None:
            from .discovery.client import DiscoveryClient

            self._discovery = DiscoveryClient(client_wrapper=self._client_wrapper)
        return self._discovery

    @property
    def consent_management(self):
        if self._consent_management is None:
            from .consent_management.client import ConsentManagementClient

            self._consent_management = ConsentManagementClient(client_wrapper=self._client_wrapper)
        return self._consent_management

    @property
    def referenzprozess(self):
        if self._referenzprozess is None:
            from .referenzprozess.client import ReferenzprozessClient

            self._referenzprozess = ReferenzprozessClient(client_wrapper=self._client_wrapper)
        return self._referenzprozess

    @property
    def customer_data(self):
        if self._customer_data is None:
            from .customer_data.client import CustomerDataClient

            self._customer_data = CustomerDataClient(client_wrapper=self._client_wrapper)
        return self._customer_data

    @property
    def portfolio_services(self):
        if self._portfolio_services is None:
            from .portfolio_services.client import PortfolioServicesClient

            self._portfolio_services = PortfolioServicesClient(client_wrapper=self._client_wrapper)
        return self._portfolio_services

    @property
    def compliance(self):
        if self._compliance is None:
            from .compliance.client import ComplianceClient

            self._compliance = ComplianceClient(client_wrapper=self._client_wrapper)
        return self._compliance

    @property
    def age_verification(self):
        if self._age_verification is None:
            from .age_verification.client import AgeVerificationClient

            self._age_verification = AgeVerificationClient(client_wrapper=self._client_wrapper)
        return self._age_verification

    @property
    def identification(self):
        if self._identification is None:
            from .identification.client import IdentificationClient

            self._identification = IdentificationClient(client_wrapper=self._client_wrapper)
        return self._identification

    @property
    def background_checks(self):
        if self._background_checks is None:
            from .background_checks.client import BackgroundChecksClient

            self._background_checks = BackgroundChecksClient(client_wrapper=self._client_wrapper)
        return self._background_checks

    @property
    def signature_services(self):
        if self._signature_services is None:
            from .signature_services.client import SignatureServicesClient

            self._signature_services = SignatureServicesClient(client_wrapper=self._client_wrapper)
        return self._signature_services

    @property
    def registry(self):
        if self._registry is None:
            from .registry.client import RegistryClient

            self._registry = RegistryClient(client_wrapper=self._client_wrapper)
        return self._registry

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health


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
        self._o_auth21oidc: typing.Optional[AsyncOAuth21OidcClient] = None
        self._client_management: typing.Optional[AsyncClientManagementClient] = None
        self._discovery: typing.Optional[AsyncDiscoveryClient] = None
        self._consent_management: typing.Optional[AsyncConsentManagementClient] = None
        self._referenzprozess: typing.Optional[AsyncReferenzprozessClient] = None
        self._customer_data: typing.Optional[AsyncCustomerDataClient] = None
        self._portfolio_services: typing.Optional[AsyncPortfolioServicesClient] = None
        self._compliance: typing.Optional[AsyncComplianceClient] = None
        self._age_verification: typing.Optional[AsyncAgeVerificationClient] = None
        self._identification: typing.Optional[AsyncIdentificationClient] = None
        self._background_checks: typing.Optional[AsyncBackgroundChecksClient] = None
        self._signature_services: typing.Optional[AsyncSignatureServicesClient] = None
        self._registry: typing.Optional[AsyncRegistryClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None

    @property
    def o_auth21oidc(self):
        if self._o_auth21oidc is None:
            from .o_auth21oidc.client import AsyncOAuth21OidcClient

            self._o_auth21oidc = AsyncOAuth21OidcClient(client_wrapper=self._client_wrapper)
        return self._o_auth21oidc

    @property
    def client_management(self):
        if self._client_management is None:
            from .client_management.client import AsyncClientManagementClient

            self._client_management = AsyncClientManagementClient(client_wrapper=self._client_wrapper)
        return self._client_management

    @property
    def discovery(self):
        if self._discovery is None:
            from .discovery.client import AsyncDiscoveryClient

            self._discovery = AsyncDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._discovery

    @property
    def consent_management(self):
        if self._consent_management is None:
            from .consent_management.client import AsyncConsentManagementClient

            self._consent_management = AsyncConsentManagementClient(client_wrapper=self._client_wrapper)
        return self._consent_management

    @property
    def referenzprozess(self):
        if self._referenzprozess is None:
            from .referenzprozess.client import AsyncReferenzprozessClient

            self._referenzprozess = AsyncReferenzprozessClient(client_wrapper=self._client_wrapper)
        return self._referenzprozess

    @property
    def customer_data(self):
        if self._customer_data is None:
            from .customer_data.client import AsyncCustomerDataClient

            self._customer_data = AsyncCustomerDataClient(client_wrapper=self._client_wrapper)
        return self._customer_data

    @property
    def portfolio_services(self):
        if self._portfolio_services is None:
            from .portfolio_services.client import AsyncPortfolioServicesClient

            self._portfolio_services = AsyncPortfolioServicesClient(client_wrapper=self._client_wrapper)
        return self._portfolio_services

    @property
    def compliance(self):
        if self._compliance is None:
            from .compliance.client import AsyncComplianceClient

            self._compliance = AsyncComplianceClient(client_wrapper=self._client_wrapper)
        return self._compliance

    @property
    def age_verification(self):
        if self._age_verification is None:
            from .age_verification.client import AsyncAgeVerificationClient

            self._age_verification = AsyncAgeVerificationClient(client_wrapper=self._client_wrapper)
        return self._age_verification

    @property
    def identification(self):
        if self._identification is None:
            from .identification.client import AsyncIdentificationClient

            self._identification = AsyncIdentificationClient(client_wrapper=self._client_wrapper)
        return self._identification

    @property
    def background_checks(self):
        if self._background_checks is None:
            from .background_checks.client import AsyncBackgroundChecksClient

            self._background_checks = AsyncBackgroundChecksClient(client_wrapper=self._client_wrapper)
        return self._background_checks

    @property
    def signature_services(self):
        if self._signature_services is None:
            from .signature_services.client import AsyncSignatureServicesClient

            self._signature_services = AsyncSignatureServicesClient(client_wrapper=self._client_wrapper)
        return self._signature_services

    @property
    def registry(self):
        if self._registry is None:
            from .registry.client import AsyncRegistryClient

            self._registry = AsyncRegistryClient(client_wrapper=self._client_wrapper)
        return self._registry

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
