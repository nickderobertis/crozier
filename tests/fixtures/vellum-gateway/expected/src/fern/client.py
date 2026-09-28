

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .channel_admission_policy.client import AsyncChannelAdmissionPolicyClient, ChannelAdmissionPolicyClient
    from .channel_ingress.client import AsyncChannelIngressClient, ChannelIngressClient
    from .channel_permission_overrides.client import (
        AsyncChannelPermissionOverridesClient,
        ChannelPermissionOverridesClient,
    )
    from .contacts.client import AsyncContactsClient, ContactsClient
    from .credential_requests.client import AsyncCredentialRequestsClient, CredentialRequestsClient
    from .feature_flags.client import AsyncFeatureFlagsClient, FeatureFlagsClient
    from .permissions.client import AsyncPermissionsClient, PermissionsClient
    from .trust_rules.client import AsyncTrustRulesClient, TrustRulesClient


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
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._permissions: typing.Optional[PermissionsClient] = None
        self._channel_admission_policy: typing.Optional[ChannelAdmissionPolicyClient] = None
        self._channel_ingress: typing.Optional[ChannelIngressClient] = None
        self._channel_permission_overrides: typing.Optional[ChannelPermissionOverridesClient] = None
        self._contacts: typing.Optional[ContactsClient] = None
        self._credential_requests: typing.Optional[CredentialRequestsClient] = None
        self._feature_flags: typing.Optional[FeatureFlagsClient] = None
        self._trust_rules: typing.Optional[TrustRulesClient] = None

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import PermissionsClient

            self._permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def channel_admission_policy(self):
        if self._channel_admission_policy is None:
            from .channel_admission_policy.client import ChannelAdmissionPolicyClient

            self._channel_admission_policy = ChannelAdmissionPolicyClient(client_wrapper=self._client_wrapper)
        return self._channel_admission_policy

    @property
    def channel_ingress(self):
        if self._channel_ingress is None:
            from .channel_ingress.client import ChannelIngressClient

            self._channel_ingress = ChannelIngressClient(client_wrapper=self._client_wrapper)
        return self._channel_ingress

    @property
    def channel_permission_overrides(self):
        if self._channel_permission_overrides is None:
            from .channel_permission_overrides.client import ChannelPermissionOverridesClient

            self._channel_permission_overrides = ChannelPermissionOverridesClient(client_wrapper=self._client_wrapper)
        return self._channel_permission_overrides

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import ContactsClient

            self._contacts = ContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def credential_requests(self):
        if self._credential_requests is None:
            from .credential_requests.client import CredentialRequestsClient

            self._credential_requests = CredentialRequestsClient(client_wrapper=self._client_wrapper)
        return self._credential_requests

    @property
    def feature_flags(self):
        if self._feature_flags is None:
            from .feature_flags.client import FeatureFlagsClient

            self._feature_flags = FeatureFlagsClient(client_wrapper=self._client_wrapper)
        return self._feature_flags

    @property
    def trust_rules(self):
        if self._trust_rules is None:
            from .trust_rules.client import TrustRulesClient

            self._trust_rules = TrustRulesClient(client_wrapper=self._client_wrapper)
        return self._trust_rules


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
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._permissions: typing.Optional[AsyncPermissionsClient] = None
        self._channel_admission_policy: typing.Optional[AsyncChannelAdmissionPolicyClient] = None
        self._channel_ingress: typing.Optional[AsyncChannelIngressClient] = None
        self._channel_permission_overrides: typing.Optional[AsyncChannelPermissionOverridesClient] = None
        self._contacts: typing.Optional[AsyncContactsClient] = None
        self._credential_requests: typing.Optional[AsyncCredentialRequestsClient] = None
        self._feature_flags: typing.Optional[AsyncFeatureFlagsClient] = None
        self._trust_rules: typing.Optional[AsyncTrustRulesClient] = None

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import AsyncPermissionsClient

            self._permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def channel_admission_policy(self):
        if self._channel_admission_policy is None:
            from .channel_admission_policy.client import AsyncChannelAdmissionPolicyClient

            self._channel_admission_policy = AsyncChannelAdmissionPolicyClient(client_wrapper=self._client_wrapper)
        return self._channel_admission_policy

    @property
    def channel_ingress(self):
        if self._channel_ingress is None:
            from .channel_ingress.client import AsyncChannelIngressClient

            self._channel_ingress = AsyncChannelIngressClient(client_wrapper=self._client_wrapper)
        return self._channel_ingress

    @property
    def channel_permission_overrides(self):
        if self._channel_permission_overrides is None:
            from .channel_permission_overrides.client import AsyncChannelPermissionOverridesClient

            self._channel_permission_overrides = AsyncChannelPermissionOverridesClient(
                client_wrapper=self._client_wrapper
            )
        return self._channel_permission_overrides

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import AsyncContactsClient

            self._contacts = AsyncContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def credential_requests(self):
        if self._credential_requests is None:
            from .credential_requests.client import AsyncCredentialRequestsClient

            self._credential_requests = AsyncCredentialRequestsClient(client_wrapper=self._client_wrapper)
        return self._credential_requests

    @property
    def feature_flags(self):
        if self._feature_flags is None:
            from .feature_flags.client import AsyncFeatureFlagsClient

            self._feature_flags = AsyncFeatureFlagsClient(client_wrapper=self._client_wrapper)
        return self._feature_flags

    @property
    def trust_rules(self):
        if self._trust_rules is None:
            from .trust_rules.client import AsyncTrustRulesClient

            self._trust_rules = AsyncTrustRulesClient(client_wrapper=self._client_wrapper)
        return self._trust_rules


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
