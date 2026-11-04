

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .annotation_setting_v1alpha_uc.client import (
        AnnotationSettingV1AlphaUcClient,
        AsyncAnnotationSettingV1AlphaUcClient,
    )
    from .attachment_v1alpha1uc.client import AsyncAttachmentV1Alpha1UcClient, AttachmentV1Alpha1UcClient
    from .device_v1alpha1uc.client import AsyncDeviceV1Alpha1UcClient, DeviceV1Alpha1UcClient
    from .notification_v1alpha1uc.client import AsyncNotificationV1Alpha1UcClient, NotificationV1Alpha1UcClient
    from .notifier_v1alpha1uc.client import AsyncNotifierV1Alpha1UcClient, NotifierV1Alpha1UcClient
    from .personal_access_token_v1alpha1uc.client import (
        AsyncPersonalAccessTokenV1Alpha1UcClient,
        PersonalAccessTokenV1Alpha1UcClient,
    )
    from .post_v1alpha1uc.client import AsyncPostV1Alpha1UcClient, PostV1Alpha1UcClient
    from .snapshot_v1alpha1uc.client import AsyncSnapshotV1Alpha1UcClient, SnapshotV1Alpha1UcClient
    from .two_factor_auth_v1alpha1uc.client import AsyncTwoFactorAuthV1Alpha1UcClient, TwoFactorAuthV1Alpha1UcClient
    from .user_connection_v1alpha1uc.client import AsyncUserConnectionV1Alpha1UcClient, UserConnectionV1Alpha1UcClient
    from .user_preference_v1alpha1uc.client import AsyncUserPreferenceV1Alpha1UcClient, UserPreferenceV1Alpha1UcClient
    from .user_v1alpha1uc.client import AsyncUserV1Alpha1UcClient, UserV1Alpha1UcClient


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
            username=username,
            password=password,
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
        self._notifier_v1alpha1uc: typing.Optional[NotifierV1Alpha1UcClient] = None
        self._notification_v1alpha1uc: typing.Optional[NotificationV1Alpha1UcClient] = None
        self._user_connection_v1alpha1uc: typing.Optional[UserConnectionV1Alpha1UcClient] = None
        self._post_v1alpha1uc: typing.Optional[PostV1Alpha1UcClient] = None
        self._snapshot_v1alpha1uc: typing.Optional[SnapshotV1Alpha1UcClient] = None
        self._annotation_setting_v1alpha_uc: typing.Optional[AnnotationSettingV1AlphaUcClient] = None
        self._user_preference_v1alpha1uc: typing.Optional[UserPreferenceV1Alpha1UcClient] = None
        self._user_v1alpha1uc: typing.Optional[UserV1Alpha1UcClient] = None
        self._two_factor_auth_v1alpha1uc: typing.Optional[TwoFactorAuthV1Alpha1UcClient] = None
        self._device_v1alpha1uc: typing.Optional[DeviceV1Alpha1UcClient] = None
        self._personal_access_token_v1alpha1uc: typing.Optional[PersonalAccessTokenV1Alpha1UcClient] = None
        self._attachment_v1alpha1uc: typing.Optional[AttachmentV1Alpha1UcClient] = None

    @property
    def notifier_v1alpha1uc(self):
        if self._notifier_v1alpha1uc is None:
            from .notifier_v1alpha1uc.client import NotifierV1Alpha1UcClient

            self._notifier_v1alpha1uc = NotifierV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._notifier_v1alpha1uc

    @property
    def notification_v1alpha1uc(self):
        if self._notification_v1alpha1uc is None:
            from .notification_v1alpha1uc.client import NotificationV1Alpha1UcClient

            self._notification_v1alpha1uc = NotificationV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._notification_v1alpha1uc

    @property
    def user_connection_v1alpha1uc(self):
        if self._user_connection_v1alpha1uc is None:
            from .user_connection_v1alpha1uc.client import UserConnectionV1Alpha1UcClient

            self._user_connection_v1alpha1uc = UserConnectionV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._user_connection_v1alpha1uc

    @property
    def post_v1alpha1uc(self):
        if self._post_v1alpha1uc is None:
            from .post_v1alpha1uc.client import PostV1Alpha1UcClient

            self._post_v1alpha1uc = PostV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._post_v1alpha1uc

    @property
    def snapshot_v1alpha1uc(self):
        if self._snapshot_v1alpha1uc is None:
            from .snapshot_v1alpha1uc.client import SnapshotV1Alpha1UcClient

            self._snapshot_v1alpha1uc = SnapshotV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._snapshot_v1alpha1uc

    @property
    def annotation_setting_v1alpha_uc(self):
        if self._annotation_setting_v1alpha_uc is None:
            from .annotation_setting_v1alpha_uc.client import AnnotationSettingV1AlphaUcClient

            self._annotation_setting_v1alpha_uc = AnnotationSettingV1AlphaUcClient(client_wrapper=self._client_wrapper)
        return self._annotation_setting_v1alpha_uc

    @property
    def user_preference_v1alpha1uc(self):
        if self._user_preference_v1alpha1uc is None:
            from .user_preference_v1alpha1uc.client import UserPreferenceV1Alpha1UcClient

            self._user_preference_v1alpha1uc = UserPreferenceV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._user_preference_v1alpha1uc

    @property
    def user_v1alpha1uc(self):
        if self._user_v1alpha1uc is None:
            from .user_v1alpha1uc.client import UserV1Alpha1UcClient

            self._user_v1alpha1uc = UserV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._user_v1alpha1uc

    @property
    def two_factor_auth_v1alpha1uc(self):
        if self._two_factor_auth_v1alpha1uc is None:
            from .two_factor_auth_v1alpha1uc.client import TwoFactorAuthV1Alpha1UcClient

            self._two_factor_auth_v1alpha1uc = TwoFactorAuthV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._two_factor_auth_v1alpha1uc

    @property
    def device_v1alpha1uc(self):
        if self._device_v1alpha1uc is None:
            from .device_v1alpha1uc.client import DeviceV1Alpha1UcClient

            self._device_v1alpha1uc = DeviceV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._device_v1alpha1uc

    @property
    def personal_access_token_v1alpha1uc(self):
        if self._personal_access_token_v1alpha1uc is None:
            from .personal_access_token_v1alpha1uc.client import PersonalAccessTokenV1Alpha1UcClient

            self._personal_access_token_v1alpha1uc = PersonalAccessTokenV1Alpha1UcClient(
                client_wrapper=self._client_wrapper
            )
        return self._personal_access_token_v1alpha1uc

    @property
    def attachment_v1alpha1uc(self):
        if self._attachment_v1alpha1uc is None:
            from .attachment_v1alpha1uc.client import AttachmentV1Alpha1UcClient

            self._attachment_v1alpha1uc = AttachmentV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._attachment_v1alpha1uc


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
            username=username,
            password=password,
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
        self._notifier_v1alpha1uc: typing.Optional[AsyncNotifierV1Alpha1UcClient] = None
        self._notification_v1alpha1uc: typing.Optional[AsyncNotificationV1Alpha1UcClient] = None
        self._user_connection_v1alpha1uc: typing.Optional[AsyncUserConnectionV1Alpha1UcClient] = None
        self._post_v1alpha1uc: typing.Optional[AsyncPostV1Alpha1UcClient] = None
        self._snapshot_v1alpha1uc: typing.Optional[AsyncSnapshotV1Alpha1UcClient] = None
        self._annotation_setting_v1alpha_uc: typing.Optional[AsyncAnnotationSettingV1AlphaUcClient] = None
        self._user_preference_v1alpha1uc: typing.Optional[AsyncUserPreferenceV1Alpha1UcClient] = None
        self._user_v1alpha1uc: typing.Optional[AsyncUserV1Alpha1UcClient] = None
        self._two_factor_auth_v1alpha1uc: typing.Optional[AsyncTwoFactorAuthV1Alpha1UcClient] = None
        self._device_v1alpha1uc: typing.Optional[AsyncDeviceV1Alpha1UcClient] = None
        self._personal_access_token_v1alpha1uc: typing.Optional[AsyncPersonalAccessTokenV1Alpha1UcClient] = None
        self._attachment_v1alpha1uc: typing.Optional[AsyncAttachmentV1Alpha1UcClient] = None

    @property
    def notifier_v1alpha1uc(self):
        if self._notifier_v1alpha1uc is None:
            from .notifier_v1alpha1uc.client import AsyncNotifierV1Alpha1UcClient

            self._notifier_v1alpha1uc = AsyncNotifierV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._notifier_v1alpha1uc

    @property
    def notification_v1alpha1uc(self):
        if self._notification_v1alpha1uc is None:
            from .notification_v1alpha1uc.client import AsyncNotificationV1Alpha1UcClient

            self._notification_v1alpha1uc = AsyncNotificationV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._notification_v1alpha1uc

    @property
    def user_connection_v1alpha1uc(self):
        if self._user_connection_v1alpha1uc is None:
            from .user_connection_v1alpha1uc.client import AsyncUserConnectionV1Alpha1UcClient

            self._user_connection_v1alpha1uc = AsyncUserConnectionV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._user_connection_v1alpha1uc

    @property
    def post_v1alpha1uc(self):
        if self._post_v1alpha1uc is None:
            from .post_v1alpha1uc.client import AsyncPostV1Alpha1UcClient

            self._post_v1alpha1uc = AsyncPostV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._post_v1alpha1uc

    @property
    def snapshot_v1alpha1uc(self):
        if self._snapshot_v1alpha1uc is None:
            from .snapshot_v1alpha1uc.client import AsyncSnapshotV1Alpha1UcClient

            self._snapshot_v1alpha1uc = AsyncSnapshotV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._snapshot_v1alpha1uc

    @property
    def annotation_setting_v1alpha_uc(self):
        if self._annotation_setting_v1alpha_uc is None:
            from .annotation_setting_v1alpha_uc.client import AsyncAnnotationSettingV1AlphaUcClient

            self._annotation_setting_v1alpha_uc = AsyncAnnotationSettingV1AlphaUcClient(
                client_wrapper=self._client_wrapper
            )
        return self._annotation_setting_v1alpha_uc

    @property
    def user_preference_v1alpha1uc(self):
        if self._user_preference_v1alpha1uc is None:
            from .user_preference_v1alpha1uc.client import AsyncUserPreferenceV1Alpha1UcClient

            self._user_preference_v1alpha1uc = AsyncUserPreferenceV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._user_preference_v1alpha1uc

    @property
    def user_v1alpha1uc(self):
        if self._user_v1alpha1uc is None:
            from .user_v1alpha1uc.client import AsyncUserV1Alpha1UcClient

            self._user_v1alpha1uc = AsyncUserV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._user_v1alpha1uc

    @property
    def two_factor_auth_v1alpha1uc(self):
        if self._two_factor_auth_v1alpha1uc is None:
            from .two_factor_auth_v1alpha1uc.client import AsyncTwoFactorAuthV1Alpha1UcClient

            self._two_factor_auth_v1alpha1uc = AsyncTwoFactorAuthV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._two_factor_auth_v1alpha1uc

    @property
    def device_v1alpha1uc(self):
        if self._device_v1alpha1uc is None:
            from .device_v1alpha1uc.client import AsyncDeviceV1Alpha1UcClient

            self._device_v1alpha1uc = AsyncDeviceV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._device_v1alpha1uc

    @property
    def personal_access_token_v1alpha1uc(self):
        if self._personal_access_token_v1alpha1uc is None:
            from .personal_access_token_v1alpha1uc.client import AsyncPersonalAccessTokenV1Alpha1UcClient

            self._personal_access_token_v1alpha1uc = AsyncPersonalAccessTokenV1Alpha1UcClient(
                client_wrapper=self._client_wrapper
            )
        return self._personal_access_token_v1alpha1uc

    @property
    def attachment_v1alpha1uc(self):
        if self._attachment_v1alpha1uc is None:
            from .attachment_v1alpha1uc.client import AsyncAttachmentV1Alpha1UcClient

            self._attachment_v1alpha1uc = AsyncAttachmentV1Alpha1UcClient(client_wrapper=self._client_wrapper)
        return self._attachment_v1alpha1uc


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
