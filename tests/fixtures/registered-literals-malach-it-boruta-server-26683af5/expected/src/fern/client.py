

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .assets.client import AssetsClient, AsyncAssetsClient
    from .did_and_verifiable_credentials.client import (
        AsyncDidAndVerifiableCredentialsClient,
        DidAndVerifiableCredentialsClient,
    )
    from .discovery.client import AsyncDiscoveryClient, DiscoveryClient
    from .federated_identity.client import AsyncFederatedIdentityClient, FederatedIdentityClient
    from .identity_confirmation.client import AsyncIdentityConfirmationClient, IdentityConfirmationClient
    from .identity_consent.client import AsyncIdentityConsentClient, IdentityConsentClient
    from .identity_mfa.client import AsyncIdentityMfaClient, IdentityMfaClient
    from .identity_password_recovery.client import AsyncIdentityPasswordRecoveryClient, IdentityPasswordRecoveryClient
    from .identity_registration.client import AsyncIdentityRegistrationClient, IdentityRegistrationClient
    from .identity_sessions.client import AsyncIdentitySessionsClient, IdentitySessionsClient
    from .identity_settings.client import AsyncIdentitySettingsClient, IdentitySettingsClient
    from .identity_wallet.client import AsyncIdentityWalletClient, IdentityWalletClient
    from .infrastructure.client import AsyncInfrastructureClient, InfrastructureClient
    from .o_auth20.client import AsyncOAuth20Client, OAuth20Client
    from .open_id_connect.client import AsyncOpenIdConnectClient, OpenIdConnectClient
    from .open_id_for_verifiable_credentials.client import (
        AsyncOpenIdForVerifiableCredentialsClient,
        OpenIdForVerifiableCredentialsClient,
    )
    from .open_id_for_verifiable_presentations.client import (
        AsyncOpenIdForVerifiablePresentationsClient,
        OpenIdForVerifiablePresentationsClient,
    )


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
        self._discovery: typing.Optional[DiscoveryClient] = None
        self._infrastructure: typing.Optional[InfrastructureClient] = None
        self._assets: typing.Optional[AssetsClient] = None
        self._o_auth20: typing.Optional[OAuth20Client] = None
        self._open_id_connect: typing.Optional[OpenIdConnectClient] = None
        self._open_id_for_verifiable_credentials: typing.Optional[OpenIdForVerifiableCredentialsClient] = None
        self._open_id_for_verifiable_presentations: typing.Optional[OpenIdForVerifiablePresentationsClient] = None
        self._did_and_verifiable_credentials: typing.Optional[DidAndVerifiableCredentialsClient] = None
        self._identity_registration: typing.Optional[IdentityRegistrationClient] = None
        self._identity_sessions: typing.Optional[IdentitySessionsClient] = None
        self._identity_password_recovery: typing.Optional[IdentityPasswordRecoveryClient] = None
        self._identity_confirmation: typing.Optional[IdentityConfirmationClient] = None
        self._identity_mfa: typing.Optional[IdentityMfaClient] = None
        self._identity_consent: typing.Optional[IdentityConsentClient] = None
        self._identity_settings: typing.Optional[IdentitySettingsClient] = None
        self._federated_identity: typing.Optional[FederatedIdentityClient] = None
        self._identity_wallet: typing.Optional[IdentityWalletClient] = None

    @property
    def discovery(self):
        if self._discovery is None:
            from .discovery.client import DiscoveryClient

            self._discovery = DiscoveryClient(client_wrapper=self._client_wrapper)
        return self._discovery

    @property
    def infrastructure(self):
        if self._infrastructure is None:
            from .infrastructure.client import InfrastructureClient

            self._infrastructure = InfrastructureClient(client_wrapper=self._client_wrapper)
        return self._infrastructure

    @property
    def assets(self):
        if self._assets is None:
            from .assets.client import AssetsClient

            self._assets = AssetsClient(client_wrapper=self._client_wrapper)
        return self._assets

    @property
    def o_auth20(self):
        if self._o_auth20 is None:
            from .o_auth20.client import OAuth20Client

            self._o_auth20 = OAuth20Client(client_wrapper=self._client_wrapper)
        return self._o_auth20

    @property
    def open_id_connect(self):
        if self._open_id_connect is None:
            from .open_id_connect.client import OpenIdConnectClient

            self._open_id_connect = OpenIdConnectClient(client_wrapper=self._client_wrapper)
        return self._open_id_connect

    @property
    def open_id_for_verifiable_credentials(self):
        if self._open_id_for_verifiable_credentials is None:
            from .open_id_for_verifiable_credentials.client import OpenIdForVerifiableCredentialsClient

            self._open_id_for_verifiable_credentials = OpenIdForVerifiableCredentialsClient(
                client_wrapper=self._client_wrapper
            )
        return self._open_id_for_verifiable_credentials

    @property
    def open_id_for_verifiable_presentations(self):
        if self._open_id_for_verifiable_presentations is None:
            from .open_id_for_verifiable_presentations.client import (
                OpenIdForVerifiablePresentationsClient,
            )

            self._open_id_for_verifiable_presentations = OpenIdForVerifiablePresentationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._open_id_for_verifiable_presentations

    @property
    def did_and_verifiable_credentials(self):
        if self._did_and_verifiable_credentials is None:
            from .did_and_verifiable_credentials.client import DidAndVerifiableCredentialsClient

            self._did_and_verifiable_credentials = DidAndVerifiableCredentialsClient(
                client_wrapper=self._client_wrapper
            )
        return self._did_and_verifiable_credentials

    @property
    def identity_registration(self):
        if self._identity_registration is None:
            from .identity_registration.client import IdentityRegistrationClient

            self._identity_registration = IdentityRegistrationClient(client_wrapper=self._client_wrapper)
        return self._identity_registration

    @property
    def identity_sessions(self):
        if self._identity_sessions is None:
            from .identity_sessions.client import IdentitySessionsClient

            self._identity_sessions = IdentitySessionsClient(client_wrapper=self._client_wrapper)
        return self._identity_sessions

    @property
    def identity_password_recovery(self):
        if self._identity_password_recovery is None:
            from .identity_password_recovery.client import IdentityPasswordRecoveryClient

            self._identity_password_recovery = IdentityPasswordRecoveryClient(client_wrapper=self._client_wrapper)
        return self._identity_password_recovery

    @property
    def identity_confirmation(self):
        if self._identity_confirmation is None:
            from .identity_confirmation.client import IdentityConfirmationClient

            self._identity_confirmation = IdentityConfirmationClient(client_wrapper=self._client_wrapper)
        return self._identity_confirmation

    @property
    def identity_mfa(self):
        if self._identity_mfa is None:
            from .identity_mfa.client import IdentityMfaClient

            self._identity_mfa = IdentityMfaClient(client_wrapper=self._client_wrapper)
        return self._identity_mfa

    @property
    def identity_consent(self):
        if self._identity_consent is None:
            from .identity_consent.client import IdentityConsentClient

            self._identity_consent = IdentityConsentClient(client_wrapper=self._client_wrapper)
        return self._identity_consent

    @property
    def identity_settings(self):
        if self._identity_settings is None:
            from .identity_settings.client import IdentitySettingsClient

            self._identity_settings = IdentitySettingsClient(client_wrapper=self._client_wrapper)
        return self._identity_settings

    @property
    def federated_identity(self):
        if self._federated_identity is None:
            from .federated_identity.client import FederatedIdentityClient

            self._federated_identity = FederatedIdentityClient(client_wrapper=self._client_wrapper)
        return self._federated_identity

    @property
    def identity_wallet(self):
        if self._identity_wallet is None:
            from .identity_wallet.client import IdentityWalletClient

            self._identity_wallet = IdentityWalletClient(client_wrapper=self._client_wrapper)
        return self._identity_wallet


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
        self._discovery: typing.Optional[AsyncDiscoveryClient] = None
        self._infrastructure: typing.Optional[AsyncInfrastructureClient] = None
        self._assets: typing.Optional[AsyncAssetsClient] = None
        self._o_auth20: typing.Optional[AsyncOAuth20Client] = None
        self._open_id_connect: typing.Optional[AsyncOpenIdConnectClient] = None
        self._open_id_for_verifiable_credentials: typing.Optional[AsyncOpenIdForVerifiableCredentialsClient] = None
        self._open_id_for_verifiable_presentations: typing.Optional[AsyncOpenIdForVerifiablePresentationsClient] = None
        self._did_and_verifiable_credentials: typing.Optional[AsyncDidAndVerifiableCredentialsClient] = None
        self._identity_registration: typing.Optional[AsyncIdentityRegistrationClient] = None
        self._identity_sessions: typing.Optional[AsyncIdentitySessionsClient] = None
        self._identity_password_recovery: typing.Optional[AsyncIdentityPasswordRecoveryClient] = None
        self._identity_confirmation: typing.Optional[AsyncIdentityConfirmationClient] = None
        self._identity_mfa: typing.Optional[AsyncIdentityMfaClient] = None
        self._identity_consent: typing.Optional[AsyncIdentityConsentClient] = None
        self._identity_settings: typing.Optional[AsyncIdentitySettingsClient] = None
        self._federated_identity: typing.Optional[AsyncFederatedIdentityClient] = None
        self._identity_wallet: typing.Optional[AsyncIdentityWalletClient] = None

    @property
    def discovery(self):
        if self._discovery is None:
            from .discovery.client import AsyncDiscoveryClient

            self._discovery = AsyncDiscoveryClient(client_wrapper=self._client_wrapper)
        return self._discovery

    @property
    def infrastructure(self):
        if self._infrastructure is None:
            from .infrastructure.client import AsyncInfrastructureClient

            self._infrastructure = AsyncInfrastructureClient(client_wrapper=self._client_wrapper)
        return self._infrastructure

    @property
    def assets(self):
        if self._assets is None:
            from .assets.client import AsyncAssetsClient

            self._assets = AsyncAssetsClient(client_wrapper=self._client_wrapper)
        return self._assets

    @property
    def o_auth20(self):
        if self._o_auth20 is None:
            from .o_auth20.client import AsyncOAuth20Client

            self._o_auth20 = AsyncOAuth20Client(client_wrapper=self._client_wrapper)
        return self._o_auth20

    @property
    def open_id_connect(self):
        if self._open_id_connect is None:
            from .open_id_connect.client import AsyncOpenIdConnectClient

            self._open_id_connect = AsyncOpenIdConnectClient(client_wrapper=self._client_wrapper)
        return self._open_id_connect

    @property
    def open_id_for_verifiable_credentials(self):
        if self._open_id_for_verifiable_credentials is None:
            from .open_id_for_verifiable_credentials.client import (
                AsyncOpenIdForVerifiableCredentialsClient,
            )

            self._open_id_for_verifiable_credentials = AsyncOpenIdForVerifiableCredentialsClient(
                client_wrapper=self._client_wrapper
            )
        return self._open_id_for_verifiable_credentials

    @property
    def open_id_for_verifiable_presentations(self):
        if self._open_id_for_verifiable_presentations is None:
            from .open_id_for_verifiable_presentations.client import (
                AsyncOpenIdForVerifiablePresentationsClient,
            )

            self._open_id_for_verifiable_presentations = AsyncOpenIdForVerifiablePresentationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._open_id_for_verifiable_presentations

    @property
    def did_and_verifiable_credentials(self):
        if self._did_and_verifiable_credentials is None:
            from .did_and_verifiable_credentials.client import AsyncDidAndVerifiableCredentialsClient

            self._did_and_verifiable_credentials = AsyncDidAndVerifiableCredentialsClient(
                client_wrapper=self._client_wrapper
            )
        return self._did_and_verifiable_credentials

    @property
    def identity_registration(self):
        if self._identity_registration is None:
            from .identity_registration.client import AsyncIdentityRegistrationClient

            self._identity_registration = AsyncIdentityRegistrationClient(client_wrapper=self._client_wrapper)
        return self._identity_registration

    @property
    def identity_sessions(self):
        if self._identity_sessions is None:
            from .identity_sessions.client import AsyncIdentitySessionsClient

            self._identity_sessions = AsyncIdentitySessionsClient(client_wrapper=self._client_wrapper)
        return self._identity_sessions

    @property
    def identity_password_recovery(self):
        if self._identity_password_recovery is None:
            from .identity_password_recovery.client import AsyncIdentityPasswordRecoveryClient

            self._identity_password_recovery = AsyncIdentityPasswordRecoveryClient(client_wrapper=self._client_wrapper)
        return self._identity_password_recovery

    @property
    def identity_confirmation(self):
        if self._identity_confirmation is None:
            from .identity_confirmation.client import AsyncIdentityConfirmationClient

            self._identity_confirmation = AsyncIdentityConfirmationClient(client_wrapper=self._client_wrapper)
        return self._identity_confirmation

    @property
    def identity_mfa(self):
        if self._identity_mfa is None:
            from .identity_mfa.client import AsyncIdentityMfaClient

            self._identity_mfa = AsyncIdentityMfaClient(client_wrapper=self._client_wrapper)
        return self._identity_mfa

    @property
    def identity_consent(self):
        if self._identity_consent is None:
            from .identity_consent.client import AsyncIdentityConsentClient

            self._identity_consent = AsyncIdentityConsentClient(client_wrapper=self._client_wrapper)
        return self._identity_consent

    @property
    def identity_settings(self):
        if self._identity_settings is None:
            from .identity_settings.client import AsyncIdentitySettingsClient

            self._identity_settings = AsyncIdentitySettingsClient(client_wrapper=self._client_wrapper)
        return self._identity_settings

    @property
    def federated_identity(self):
        if self._federated_identity is None:
            from .federated_identity.client import AsyncFederatedIdentityClient

            self._federated_identity = AsyncFederatedIdentityClient(client_wrapper=self._client_wrapper)
        return self._federated_identity

    @property
    def identity_wallet(self):
        if self._identity_wallet is None:
            from .identity_wallet.client import AsyncIdentityWalletClient

            self._identity_wallet = AsyncIdentityWalletClient(client_wrapper=self._client_wrapper)
        return self._identity_wallet


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
