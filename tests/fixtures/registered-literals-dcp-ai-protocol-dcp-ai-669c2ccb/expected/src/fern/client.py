

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .advisory.client import AdvisoryClient, AsyncAdvisoryClient
    from .anchoring.client import AnchoringClient, AsyncAnchoringClient
    from .audit.client import AsyncAuditClient, AuditClient
    from .discovery.client import AsyncDiscoveryClient, DiscoveryClient
    from .emergency.client import AsyncEmergencyClient, EmergencyClient
    from .governance.client import AsyncGovernanceClient, GovernanceClient
    from .health.client import AsyncHealthClient, HealthClient
    from .intent.client import AsyncIntentClient, IntentClient
    from .keys.client import AsyncKeysClient, KeysClient
    from .multi_party.client import AsyncMultiPartyClient, MultiPartyClient
    from .passport.client import AsyncPassportClient, PassportClient
    from .policy.client import AsyncPolicyClient, PolicyClient
    from .revocation.client import AsyncRevocationClient, RevocationClient
    from .transparency.client import AsyncTransparencyClient, TransparencyClient
    from .verification.client import AsyncVerificationClient, VerificationClient


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



    dcp_api_key : str
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
        dcp_api_key="YOUR_DCP_API_KEY",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        dcp_api_key: str,
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
            dcp_api_key=dcp_api_key,
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
        self._health: typing.Optional[HealthClient] = None
        self._discovery: typing.Optional[DiscoveryClient] = None
        self._advisory: typing.Optional[AdvisoryClient] = None
        self._governance: typing.Optional[GovernanceClient] = None
        self._verification: typing.Optional[VerificationClient] = None
        self._anchoring: typing.Optional[AnchoringClient] = None
        self._revocation: typing.Optional[RevocationClient] = None
        self._transparency: typing.Optional[TransparencyClient] = None
        self._passport: typing.Optional[PassportClient] = None
        self._intent: typing.Optional[IntentClient] = None
        self._audit: typing.Optional[AuditClient] = None
        self._keys: typing.Optional[KeysClient] = None
        self._emergency: typing.Optional[EmergencyClient] = None
        self._multi_party: typing.Optional[MultiPartyClient] = None
        self._policy: typing.Optional[PolicyClient] = None

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def discovery(self):
        if self._discovery is None:
            from .discovery.client import DiscoveryClient

            self._discovery = DiscoveryClient(client_wrapper=self._client_wrapper)
        return self._discovery

    @property
    def advisory(self):
        if self._advisory is None:
            from .advisory.client import AdvisoryClient

            self._advisory = AdvisoryClient(client_wrapper=self._client_wrapper)
        return self._advisory

    @property
    def governance(self):
        if self._governance is None:
            from .governance.client import GovernanceClient

            self._governance = GovernanceClient(client_wrapper=self._client_wrapper)
        return self._governance

    @property
    def verification(self):
        if self._verification is None:
            from .verification.client import VerificationClient

            self._verification = VerificationClient(client_wrapper=self._client_wrapper)
        return self._verification

    @property
    def anchoring(self):
        if self._anchoring is None:
            from .anchoring.client import AnchoringClient

            self._anchoring = AnchoringClient(client_wrapper=self._client_wrapper)
        return self._anchoring

    @property
    def revocation(self):
        if self._revocation is None:
            from .revocation.client import RevocationClient

            self._revocation = RevocationClient(client_wrapper=self._client_wrapper)
        return self._revocation

    @property
    def transparency(self):
        if self._transparency is None:
            from .transparency.client import TransparencyClient

            self._transparency = TransparencyClient(client_wrapper=self._client_wrapper)
        return self._transparency

    @property
    def passport(self):
        if self._passport is None:
            from .passport.client import PassportClient

            self._passport = PassportClient(client_wrapper=self._client_wrapper)
        return self._passport

    @property
    def intent(self):
        if self._intent is None:
            from .intent.client import IntentClient

            self._intent = IntentClient(client_wrapper=self._client_wrapper)
        return self._intent

    @property
    def audit(self):
        if self._audit is None:
            from .audit.client import AuditClient

            self._audit = AuditClient(client_wrapper=self._client_wrapper)
        return self._audit

    @property
    def keys(self):
        if self._keys is None:
            from .keys.client import KeysClient

            self._keys = KeysClient(client_wrapper=self._client_wrapper)
        return self._keys

    @property
    def emergency(self):
        if self._emergency is None:
            from .emergency.client import EmergencyClient

            self._emergency = EmergencyClient(client_wrapper=self._client_wrapper)
        return self._emergency

    @property
    def multi_party(self):
        if self._multi_party is None:
            from .multi_party.client import MultiPartyClient

            self._multi_party = MultiPartyClient(client_wrapper=self._client_wrapper)
        return self._multi_party

    @property
    def policy(self):
        if self._policy is None:
            from .policy.client import PolicyClient

            self._policy = PolicyClient(client_wrapper=self._client_wrapper)
        return self._policy


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



    dcp_api_key : str
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
        dcp_api_key="YOUR_DCP_API_KEY",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        dcp_api_key: str,
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
            dcp_api_key=dcp_api_key,
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
        self._health: typing.Optional[AsyncHealthClient] = None
        self._discovery: typing.Optional[AsyncDiscoveryClient] = None
        self._advisory: typing.Optional[AsyncAdvisoryClient] = None
        self._governance: typing.Optional[AsyncGovernanceClient] = None
        self._verification: typing.Optional[AsyncVerificationClient] = None
        self._anchoring: typing.Optional[AsyncAnchoringClient] = None
        self._revocation: typing.Optional[AsyncRevocationClient] = None
        self._transparency: typing.Optional[AsyncTransparencyClient] = None
        self._passport: typing.Optional[AsyncPassportClient] = None
        self._intent: typing.Optional[AsyncIntentClient] = None
        self._audit: typing.Optional[AsyncAuditClient] = None
        self._keys: typing.Optional[AsyncKeysClient] = None
        self._emergency: typing.Optional[AsyncEmergencyClient] = None
        self._multi_party: typing.Optional[AsyncMultiPartyClient] = None
        self._policy: typing.Optional[AsyncPolicyClient] = None

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def discovery(self):
        if self._discovery is None:
            from .discovery.client import AsyncDiscoveryClient

            self._discovery = AsyncDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._discovery

    @property
    def advisory(self):
        if self._advisory is None:
            from .advisory.client import AsyncAdvisoryClient

            self._advisory = AsyncAdvisoryClient(client_wrapper=self._client_wrapper)
        return self._advisory

    @property
    def governance(self):
        if self._governance is None:
            from .governance.client import AsyncGovernanceClient

            self._governance = AsyncGovernanceClient(client_wrapper=self._client_wrapper)
        return self._governance

    @property
    def verification(self):
        if self._verification is None:
            from .verification.client import AsyncVerificationClient

            self._verification = AsyncVerificationClient(client_wrapper=self._client_wrapper)
        return self._verification

    @property
    def anchoring(self):
        if self._anchoring is None:
            from .anchoring.client import AsyncAnchoringClient

            self._anchoring = AsyncAnchoringClient(client_wrapper=self._client_wrapper)
        return self._anchoring

    @property
    def revocation(self):
        if self._revocation is None:
            from .revocation.client import AsyncRevocationClient

            self._revocation = AsyncRevocationClient(client_wrapper=self._client_wrapper)
        return self._revocation

    @property
    def transparency(self):
        if self._transparency is None:
            from .transparency.client import AsyncTransparencyClient

            self._transparency = AsyncTransparencyClient(client_wrapper=self._client_wrapper)
        return self._transparency

    @property
    def passport(self):
        if self._passport is None:
            from .passport.client import AsyncPassportClient

            self._passport = AsyncPassportClient(client_wrapper=self._client_wrapper)
        return self._passport

    @property
    def intent(self):
        if self._intent is None:
            from .intent.client import AsyncIntentClient

            self._intent = AsyncIntentClient(client_wrapper=self._client_wrapper)
        return self._intent

    @property
    def audit(self):
        if self._audit is None:
            from .audit.client import AsyncAuditClient

            self._audit = AsyncAuditClient(client_wrapper=self._client_wrapper)
        return self._audit

    @property
    def keys(self):
        if self._keys is None:
            from .keys.client import AsyncKeysClient

            self._keys = AsyncKeysClient(client_wrapper=self._client_wrapper)
        return self._keys

    @property
    def emergency(self):
        if self._emergency is None:
            from .emergency.client import AsyncEmergencyClient

            self._emergency = AsyncEmergencyClient(client_wrapper=self._client_wrapper)
        return self._emergency

    @property
    def multi_party(self):
        if self._multi_party is None:
            from .multi_party.client import AsyncMultiPartyClient

            self._multi_party = AsyncMultiPartyClient(client_wrapper=self._client_wrapper)
        return self._multi_party

    @property
    def policy(self):
        if self._policy is None:
            from .policy.client import AsyncPolicyClient

            self._policy = AsyncPolicyClient(client_wrapper=self._client_wrapper)
        return self._policy


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
