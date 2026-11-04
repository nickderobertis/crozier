

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .cloud_federation_api_request_handler.client import (
        AsyncCloudFederationApiRequestHandlerClient,
        CloudFederationApiRequestHandlerClient,
    )
    from .core.client import AsyncCoreClient, CoreClient
    from .core_app_password.client import AsyncCoreAppPasswordClient, CoreAppPasswordClient
    from .core_auto_complete.client import AsyncCoreAutoCompleteClient, CoreAutoCompleteClient
    from .core_avatar.client import AsyncCoreAvatarClient, CoreAvatarClient
    from .core_client_flow_login_v2.client import AsyncCoreClientFlowLoginV2Client, CoreClientFlowLoginV2Client
    from .core_collaboration_resources.client import (
        AsyncCoreCollaborationResourcesClient,
        CoreCollaborationResourcesClient,
    )
    from .core_guest_avatar.client import AsyncCoreGuestAvatarClient, CoreGuestAvatarClient
    from .core_hover_card.client import AsyncCoreHoverCardClient, CoreHoverCardClient
    from .core_navigation.client import AsyncCoreNavigationClient, CoreNavigationClient
    from .core_ocs.client import AsyncCoreOcsClient, CoreOcsClient
    from .core_preview.client import AsyncCorePreviewClient, CorePreviewClient
    from .core_profile_api.client import AsyncCoreProfileApiClient, CoreProfileApiClient
    from .core_reference.client import AsyncCoreReferenceClient, CoreReferenceClient
    from .core_reference_api.client import AsyncCoreReferenceApiClient, CoreReferenceApiClient
    from .core_translation_api.client import AsyncCoreTranslationApiClient, CoreTranslationApiClient
    from .core_unified_search.client import AsyncCoreUnifiedSearchClient, CoreUnifiedSearchClient
    from .core_whats_new.client import AsyncCoreWhatsNewClient, CoreWhatsNewClient
    from .core_wipe.client import AsyncCoreWipeClient, CoreWipeClient
    from .dashboard_dashboard_api.client import AsyncDashboardDashboardApiClient, DashboardDashboardApiClient
    from .dav_direct.client import AsyncDavDirectClient, DavDirectClient
    from .files_sharing_deleted_shareapi.client import (
        AsyncFilesSharingDeletedShareapiClient,
        FilesSharingDeletedShareapiClient,
    )
    from .files_sharing_remote.client import AsyncFilesSharingRemoteClient, FilesSharingRemoteClient
    from .files_sharing_share_info.client import AsyncFilesSharingShareInfoClient, FilesSharingShareInfoClient
    from .files_sharing_shareapi.client import AsyncFilesSharingShareapiClient, FilesSharingShareapiClient
    from .files_sharing_shareesapi.client import AsyncFilesSharingShareesapiClient, FilesSharingShareesapiClient
    from .oauth2login_redirector.client import AsyncOauth2LoginRedirectorClient, Oauth2LoginRedirectorClient
    from .oauth2oauth_api.client import AsyncOauth2OauthApiClient, Oauth2OauthApiClient
    from .provisioning_api_app_config.client import AsyncProvisioningApiAppConfigClient, ProvisioningApiAppConfigClient
    from .provisioning_api_apps.client import AsyncProvisioningApiAppsClient, ProvisioningApiAppsClient
    from .provisioning_api_groups.client import AsyncProvisioningApiGroupsClient, ProvisioningApiGroupsClient
    from .provisioning_api_preferences.client import (
        AsyncProvisioningApiPreferencesClient,
        ProvisioningApiPreferencesClient,
    )
    from .provisioning_api_users.client import AsyncProvisioningApiUsersClient, ProvisioningApiUsersClient
    from .settings_log_settings.client import AsyncSettingsLogSettingsClient, SettingsLogSettingsClient
    from .theming_icon.client import AsyncThemingIconClient, ThemingIconClient
    from .theming_theming.client import AsyncThemingThemingClient, ThemingThemingClient
    from .theming_user_theme.client import AsyncThemingUserThemeClient, ThemingUserThemeClient
    from .user_status_heartbeat.client import AsyncUserStatusHeartbeatClient, UserStatusHeartbeatClient
    from .user_status_predefined_status.client import (
        AsyncUserStatusPredefinedStatusClient,
        UserStatusPredefinedStatusClient,
    )
    from .user_status_statuses.client import AsyncUserStatusStatusesClient, UserStatusStatusesClient
    from .user_status_user_status.client import AsyncUserStatusUserStatusClient, UserStatusUserStatusClient
    from .weather_status_weather_status.client import (
        AsyncWeatherStatusWeatherStatusClient,
        WeatherStatusWeatherStatusClient,
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



    ocs_api_request : typing.Optional[typing.Literal["true"]]
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
        ocs_api_request="YOUR_OCS_API_REQUEST",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        ocs_api_request: typing.Optional[typing.Literal["true"]] = None,
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
            ocs_api_request=ocs_api_request,
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
        self._core_avatar: typing.Optional[CoreAvatarClient] = None
        self._core_guest_avatar: typing.Optional[CoreGuestAvatarClient] = None
        self._core_client_flow_login_v2: typing.Optional[CoreClientFlowLoginV2Client] = None
        self._core_preview: typing.Optional[CorePreviewClient] = None
        self._core_reference: typing.Optional[CoreReferenceClient] = None
        self._core_wipe: typing.Optional[CoreWipeClient] = None
        self._core_ocs: typing.Optional[CoreOcsClient] = None
        self._core_navigation: typing.Optional[CoreNavigationClient] = None
        self._core_auto_complete: typing.Optional[CoreAutoCompleteClient] = None
        self._core_whats_new: typing.Optional[CoreWhatsNewClient] = None
        self._core_app_password: typing.Optional[CoreAppPasswordClient] = None
        self._core_hover_card: typing.Optional[CoreHoverCardClient] = None
        self._core_collaboration_resources: typing.Optional[CoreCollaborationResourcesClient] = None
        self._core_reference_api: typing.Optional[CoreReferenceApiClient] = None
        self._core_profile_api: typing.Optional[CoreProfileApiClient] = None
        self._core_unified_search: typing.Optional[CoreUnifiedSearchClient] = None
        self._core_translation_api: typing.Optional[CoreTranslationApiClient] = None
        self._core: typing.Optional[CoreClient] = None
        self._cloud_federation_api_request_handler: typing.Optional[CloudFederationApiRequestHandlerClient] = None
        self._dashboard_dashboard_api: typing.Optional[DashboardDashboardApiClient] = None
        self._dav_direct: typing.Optional[DavDirectClient] = None
        self._files_sharing_share_info: typing.Optional[FilesSharingShareInfoClient] = None
        self._files_sharing_shareapi: typing.Optional[FilesSharingShareapiClient] = None
        self._files_sharing_deleted_shareapi: typing.Optional[FilesSharingDeletedShareapiClient] = None
        self._files_sharing_shareesapi: typing.Optional[FilesSharingShareesapiClient] = None
        self._files_sharing_remote: typing.Optional[FilesSharingRemoteClient] = None
        self._oauth2login_redirector: typing.Optional[Oauth2LoginRedirectorClient] = None
        self._oauth2oauth_api: typing.Optional[Oauth2OauthApiClient] = None
        self._provisioning_api_apps: typing.Optional[ProvisioningApiAppsClient] = None
        self._provisioning_api_groups: typing.Optional[ProvisioningApiGroupsClient] = None
        self._provisioning_api_users: typing.Optional[ProvisioningApiUsersClient] = None
        self._provisioning_api_app_config: typing.Optional[ProvisioningApiAppConfigClient] = None
        self._provisioning_api_preferences: typing.Optional[ProvisioningApiPreferencesClient] = None
        self._settings_log_settings: typing.Optional[SettingsLogSettingsClient] = None
        self._theming_theming: typing.Optional[ThemingThemingClient] = None
        self._theming_icon: typing.Optional[ThemingIconClient] = None
        self._theming_user_theme: typing.Optional[ThemingUserThemeClient] = None
        self._user_status_statuses: typing.Optional[UserStatusStatusesClient] = None
        self._user_status_user_status: typing.Optional[UserStatusUserStatusClient] = None
        self._user_status_predefined_status: typing.Optional[UserStatusPredefinedStatusClient] = None
        self._user_status_heartbeat: typing.Optional[UserStatusHeartbeatClient] = None
        self._weather_status_weather_status: typing.Optional[WeatherStatusWeatherStatusClient] = None

    @property
    def core_avatar(self):
        if self._core_avatar is None:
            from .core_avatar.client import CoreAvatarClient

            self._core_avatar = CoreAvatarClient(client_wrapper=self._client_wrapper)
        return self._core_avatar

    @property
    def core_guest_avatar(self):
        if self._core_guest_avatar is None:
            from .core_guest_avatar.client import CoreGuestAvatarClient

            self._core_guest_avatar = CoreGuestAvatarClient(client_wrapper=self._client_wrapper)
        return self._core_guest_avatar

    @property
    def core_client_flow_login_v2(self):
        if self._core_client_flow_login_v2 is None:
            from .core_client_flow_login_v2.client import CoreClientFlowLoginV2Client

            self._core_client_flow_login_v2 = CoreClientFlowLoginV2Client(client_wrapper=self._client_wrapper)
        return self._core_client_flow_login_v2

    @property
    def core_preview(self):
        if self._core_preview is None:
            from .core_preview.client import CorePreviewClient

            self._core_preview = CorePreviewClient(client_wrapper=self._client_wrapper)
        return self._core_preview

    @property
    def core_reference(self):
        if self._core_reference is None:
            from .core_reference.client import CoreReferenceClient

            self._core_reference = CoreReferenceClient(client_wrapper=self._client_wrapper)
        return self._core_reference

    @property
    def core_wipe(self):
        if self._core_wipe is None:
            from .core_wipe.client import CoreWipeClient

            self._core_wipe = CoreWipeClient(client_wrapper=self._client_wrapper)
        return self._core_wipe

    @property
    def core_ocs(self):
        if self._core_ocs is None:
            from .core_ocs.client import CoreOcsClient

            self._core_ocs = CoreOcsClient(client_wrapper=self._client_wrapper)
        return self._core_ocs

    @property
    def core_navigation(self):
        if self._core_navigation is None:
            from .core_navigation.client import CoreNavigationClient

            self._core_navigation = CoreNavigationClient(client_wrapper=self._client_wrapper)
        return self._core_navigation

    @property
    def core_auto_complete(self):
        if self._core_auto_complete is None:
            from .core_auto_complete.client import CoreAutoCompleteClient

            self._core_auto_complete = CoreAutoCompleteClient(client_wrapper=self._client_wrapper)
        return self._core_auto_complete

    @property
    def core_whats_new(self):
        if self._core_whats_new is None:
            from .core_whats_new.client import CoreWhatsNewClient

            self._core_whats_new = CoreWhatsNewClient(client_wrapper=self._client_wrapper)
        return self._core_whats_new

    @property
    def core_app_password(self):
        if self._core_app_password is None:
            from .core_app_password.client import CoreAppPasswordClient

            self._core_app_password = CoreAppPasswordClient(client_wrapper=self._client_wrapper)
        return self._core_app_password

    @property
    def core_hover_card(self):
        if self._core_hover_card is None:
            from .core_hover_card.client import CoreHoverCardClient

            self._core_hover_card = CoreHoverCardClient(client_wrapper=self._client_wrapper)
        return self._core_hover_card

    @property
    def core_collaboration_resources(self):
        if self._core_collaboration_resources is None:
            from .core_collaboration_resources.client import CoreCollaborationResourcesClient

            self._core_collaboration_resources = CoreCollaborationResourcesClient(client_wrapper=self._client_wrapper)
        return self._core_collaboration_resources

    @property
    def core_reference_api(self):
        if self._core_reference_api is None:
            from .core_reference_api.client import CoreReferenceApiClient

            self._core_reference_api = CoreReferenceApiClient(client_wrapper=self._client_wrapper)
        return self._core_reference_api

    @property
    def core_profile_api(self):
        if self._core_profile_api is None:
            from .core_profile_api.client import CoreProfileApiClient

            self._core_profile_api = CoreProfileApiClient(client_wrapper=self._client_wrapper)
        return self._core_profile_api

    @property
    def core_unified_search(self):
        if self._core_unified_search is None:
            from .core_unified_search.client import CoreUnifiedSearchClient

            self._core_unified_search = CoreUnifiedSearchClient(client_wrapper=self._client_wrapper)
        return self._core_unified_search

    @property
    def core_translation_api(self):
        if self._core_translation_api is None:
            from .core_translation_api.client import CoreTranslationApiClient

            self._core_translation_api = CoreTranslationApiClient(client_wrapper=self._client_wrapper)
        return self._core_translation_api

    @property
    def core(self):
        if self._core is None:
            from .core.client import CoreClient

            self._core = CoreClient(client_wrapper=self._client_wrapper)
        return self._core

    @property
    def cloud_federation_api_request_handler(self):
        if self._cloud_federation_api_request_handler is None:
            from .cloud_federation_api_request_handler.client import (
                CloudFederationApiRequestHandlerClient,
            )

            self._cloud_federation_api_request_handler = CloudFederationApiRequestHandlerClient(
                client_wrapper=self._client_wrapper
            )
        return self._cloud_federation_api_request_handler

    @property
    def dashboard_dashboard_api(self):
        if self._dashboard_dashboard_api is None:
            from .dashboard_dashboard_api.client import DashboardDashboardApiClient

            self._dashboard_dashboard_api = DashboardDashboardApiClient(client_wrapper=self._client_wrapper)
        return self._dashboard_dashboard_api

    @property
    def dav_direct(self):
        if self._dav_direct is None:
            from .dav_direct.client import DavDirectClient

            self._dav_direct = DavDirectClient(client_wrapper=self._client_wrapper)
        return self._dav_direct

    @property
    def files_sharing_share_info(self):
        if self._files_sharing_share_info is None:
            from .files_sharing_share_info.client import FilesSharingShareInfoClient

            self._files_sharing_share_info = FilesSharingShareInfoClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_share_info

    @property
    def files_sharing_shareapi(self):
        if self._files_sharing_shareapi is None:
            from .files_sharing_shareapi.client import FilesSharingShareapiClient

            self._files_sharing_shareapi = FilesSharingShareapiClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_shareapi

    @property
    def files_sharing_deleted_shareapi(self):
        if self._files_sharing_deleted_shareapi is None:
            from .files_sharing_deleted_shareapi.client import FilesSharingDeletedShareapiClient

            self._files_sharing_deleted_shareapi = FilesSharingDeletedShareapiClient(
                client_wrapper=self._client_wrapper
            )
        return self._files_sharing_deleted_shareapi

    @property
    def files_sharing_shareesapi(self):
        if self._files_sharing_shareesapi is None:
            from .files_sharing_shareesapi.client import FilesSharingShareesapiClient

            self._files_sharing_shareesapi = FilesSharingShareesapiClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_shareesapi

    @property
    def files_sharing_remote(self):
        if self._files_sharing_remote is None:
            from .files_sharing_remote.client import FilesSharingRemoteClient

            self._files_sharing_remote = FilesSharingRemoteClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_remote

    @property
    def oauth2login_redirector(self):
        if self._oauth2login_redirector is None:
            from .oauth2login_redirector.client import Oauth2LoginRedirectorClient

            self._oauth2login_redirector = Oauth2LoginRedirectorClient(client_wrapper=self._client_wrapper)
        return self._oauth2login_redirector

    @property
    def oauth2oauth_api(self):
        if self._oauth2oauth_api is None:
            from .oauth2oauth_api.client import Oauth2OauthApiClient

            self._oauth2oauth_api = Oauth2OauthApiClient(client_wrapper=self._client_wrapper)
        return self._oauth2oauth_api

    @property
    def provisioning_api_apps(self):
        if self._provisioning_api_apps is None:
            from .provisioning_api_apps.client import ProvisioningApiAppsClient

            self._provisioning_api_apps = ProvisioningApiAppsClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_apps

    @property
    def provisioning_api_groups(self):
        if self._provisioning_api_groups is None:
            from .provisioning_api_groups.client import ProvisioningApiGroupsClient

            self._provisioning_api_groups = ProvisioningApiGroupsClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_groups

    @property
    def provisioning_api_users(self):
        if self._provisioning_api_users is None:
            from .provisioning_api_users.client import ProvisioningApiUsersClient

            self._provisioning_api_users = ProvisioningApiUsersClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_users

    @property
    def provisioning_api_app_config(self):
        if self._provisioning_api_app_config is None:
            from .provisioning_api_app_config.client import ProvisioningApiAppConfigClient

            self._provisioning_api_app_config = ProvisioningApiAppConfigClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_app_config

    @property
    def provisioning_api_preferences(self):
        if self._provisioning_api_preferences is None:
            from .provisioning_api_preferences.client import ProvisioningApiPreferencesClient

            self._provisioning_api_preferences = ProvisioningApiPreferencesClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_preferences

    @property
    def settings_log_settings(self):
        if self._settings_log_settings is None:
            from .settings_log_settings.client import SettingsLogSettingsClient

            self._settings_log_settings = SettingsLogSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings_log_settings

    @property
    def theming_theming(self):
        if self._theming_theming is None:
            from .theming_theming.client import ThemingThemingClient

            self._theming_theming = ThemingThemingClient(client_wrapper=self._client_wrapper)
        return self._theming_theming

    @property
    def theming_icon(self):
        if self._theming_icon is None:
            from .theming_icon.client import ThemingIconClient

            self._theming_icon = ThemingIconClient(client_wrapper=self._client_wrapper)
        return self._theming_icon

    @property
    def theming_user_theme(self):
        if self._theming_user_theme is None:
            from .theming_user_theme.client import ThemingUserThemeClient

            self._theming_user_theme = ThemingUserThemeClient(client_wrapper=self._client_wrapper)
        return self._theming_user_theme

    @property
    def user_status_statuses(self):
        if self._user_status_statuses is None:
            from .user_status_statuses.client import UserStatusStatusesClient

            self._user_status_statuses = UserStatusStatusesClient(client_wrapper=self._client_wrapper)
        return self._user_status_statuses

    @property
    def user_status_user_status(self):
        if self._user_status_user_status is None:
            from .user_status_user_status.client import UserStatusUserStatusClient

            self._user_status_user_status = UserStatusUserStatusClient(client_wrapper=self._client_wrapper)
        return self._user_status_user_status

    @property
    def user_status_predefined_status(self):
        if self._user_status_predefined_status is None:
            from .user_status_predefined_status.client import UserStatusPredefinedStatusClient

            self._user_status_predefined_status = UserStatusPredefinedStatusClient(client_wrapper=self._client_wrapper)
        return self._user_status_predefined_status

    @property
    def user_status_heartbeat(self):
        if self._user_status_heartbeat is None:
            from .user_status_heartbeat.client import UserStatusHeartbeatClient

            self._user_status_heartbeat = UserStatusHeartbeatClient(client_wrapper=self._client_wrapper)
        return self._user_status_heartbeat

    @property
    def weather_status_weather_status(self):
        if self._weather_status_weather_status is None:
            from .weather_status_weather_status.client import WeatherStatusWeatherStatusClient

            self._weather_status_weather_status = WeatherStatusWeatherStatusClient(client_wrapper=self._client_wrapper)
        return self._weather_status_weather_status


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



    ocs_api_request : typing.Optional[typing.Literal["true"]]
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
        ocs_api_request="YOUR_OCS_API_REQUEST",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        ocs_api_request: typing.Optional[typing.Literal["true"]] = None,
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
            ocs_api_request=ocs_api_request,
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
        self._core_avatar: typing.Optional[AsyncCoreAvatarClient] = None
        self._core_guest_avatar: typing.Optional[AsyncCoreGuestAvatarClient] = None
        self._core_client_flow_login_v2: typing.Optional[AsyncCoreClientFlowLoginV2Client] = None
        self._core_preview: typing.Optional[AsyncCorePreviewClient] = None
        self._core_reference: typing.Optional[AsyncCoreReferenceClient] = None
        self._core_wipe: typing.Optional[AsyncCoreWipeClient] = None
        self._core_ocs: typing.Optional[AsyncCoreOcsClient] = None
        self._core_navigation: typing.Optional[AsyncCoreNavigationClient] = None
        self._core_auto_complete: typing.Optional[AsyncCoreAutoCompleteClient] = None
        self._core_whats_new: typing.Optional[AsyncCoreWhatsNewClient] = None
        self._core_app_password: typing.Optional[AsyncCoreAppPasswordClient] = None
        self._core_hover_card: typing.Optional[AsyncCoreHoverCardClient] = None
        self._core_collaboration_resources: typing.Optional[AsyncCoreCollaborationResourcesClient] = None
        self._core_reference_api: typing.Optional[AsyncCoreReferenceApiClient] = None
        self._core_profile_api: typing.Optional[AsyncCoreProfileApiClient] = None
        self._core_unified_search: typing.Optional[AsyncCoreUnifiedSearchClient] = None
        self._core_translation_api: typing.Optional[AsyncCoreTranslationApiClient] = None
        self._core: typing.Optional[AsyncCoreClient] = None
        self._cloud_federation_api_request_handler: typing.Optional[AsyncCloudFederationApiRequestHandlerClient] = None
        self._dashboard_dashboard_api: typing.Optional[AsyncDashboardDashboardApiClient] = None
        self._dav_direct: typing.Optional[AsyncDavDirectClient] = None
        self._files_sharing_share_info: typing.Optional[AsyncFilesSharingShareInfoClient] = None
        self._files_sharing_shareapi: typing.Optional[AsyncFilesSharingShareapiClient] = None
        self._files_sharing_deleted_shareapi: typing.Optional[AsyncFilesSharingDeletedShareapiClient] = None
        self._files_sharing_shareesapi: typing.Optional[AsyncFilesSharingShareesapiClient] = None
        self._files_sharing_remote: typing.Optional[AsyncFilesSharingRemoteClient] = None
        self._oauth2login_redirector: typing.Optional[AsyncOauth2LoginRedirectorClient] = None
        self._oauth2oauth_api: typing.Optional[AsyncOauth2OauthApiClient] = None
        self._provisioning_api_apps: typing.Optional[AsyncProvisioningApiAppsClient] = None
        self._provisioning_api_groups: typing.Optional[AsyncProvisioningApiGroupsClient] = None
        self._provisioning_api_users: typing.Optional[AsyncProvisioningApiUsersClient] = None
        self._provisioning_api_app_config: typing.Optional[AsyncProvisioningApiAppConfigClient] = None
        self._provisioning_api_preferences: typing.Optional[AsyncProvisioningApiPreferencesClient] = None
        self._settings_log_settings: typing.Optional[AsyncSettingsLogSettingsClient] = None
        self._theming_theming: typing.Optional[AsyncThemingThemingClient] = None
        self._theming_icon: typing.Optional[AsyncThemingIconClient] = None
        self._theming_user_theme: typing.Optional[AsyncThemingUserThemeClient] = None
        self._user_status_statuses: typing.Optional[AsyncUserStatusStatusesClient] = None
        self._user_status_user_status: typing.Optional[AsyncUserStatusUserStatusClient] = None
        self._user_status_predefined_status: typing.Optional[AsyncUserStatusPredefinedStatusClient] = None
        self._user_status_heartbeat: typing.Optional[AsyncUserStatusHeartbeatClient] = None
        self._weather_status_weather_status: typing.Optional[AsyncWeatherStatusWeatherStatusClient] = None

    @property
    def core_avatar(self):
        if self._core_avatar is None:
            from .core_avatar.client import AsyncCoreAvatarClient

            self._core_avatar = AsyncCoreAvatarClient(client_wrapper=self._client_wrapper)
        return self._core_avatar

    @property
    def core_guest_avatar(self):
        if self._core_guest_avatar is None:
            from .core_guest_avatar.client import AsyncCoreGuestAvatarClient

            self._core_guest_avatar = AsyncCoreGuestAvatarClient(client_wrapper=self._client_wrapper)
        return self._core_guest_avatar

    @property
    def core_client_flow_login_v2(self):
        if self._core_client_flow_login_v2 is None:
            from .core_client_flow_login_v2.client import AsyncCoreClientFlowLoginV2Client

            self._core_client_flow_login_v2 = AsyncCoreClientFlowLoginV2Client(client_wrapper=self._client_wrapper)
        return self._core_client_flow_login_v2

    @property
    def core_preview(self):
        if self._core_preview is None:
            from .core_preview.client import AsyncCorePreviewClient

            self._core_preview = AsyncCorePreviewClient(client_wrapper=self._client_wrapper)
        return self._core_preview

    @property
    def core_reference(self):
        if self._core_reference is None:
            from .core_reference.client import AsyncCoreReferenceClient

            self._core_reference = AsyncCoreReferenceClient(client_wrapper=self._client_wrapper)
        return self._core_reference

    @property
    def core_wipe(self):
        if self._core_wipe is None:
            from .core_wipe.client import AsyncCoreWipeClient

            self._core_wipe = AsyncCoreWipeClient(client_wrapper=self._client_wrapper)
        return self._core_wipe

    @property
    def core_ocs(self):
        if self._core_ocs is None:
            from .core_ocs.client import AsyncCoreOcsClient

            self._core_ocs = AsyncCoreOcsClient(client_wrapper=self._client_wrapper)
        return self._core_ocs

    @property
    def core_navigation(self):
        if self._core_navigation is None:
            from .core_navigation.client import AsyncCoreNavigationClient

            self._core_navigation = AsyncCoreNavigationClient(client_wrapper=self._client_wrapper)
        return self._core_navigation

    @property
    def core_auto_complete(self):
        if self._core_auto_complete is None:
            from .core_auto_complete.client import AsyncCoreAutoCompleteClient

            self._core_auto_complete = AsyncCoreAutoCompleteClient(client_wrapper=self._client_wrapper)
        return self._core_auto_complete

    @property
    def core_whats_new(self):
        if self._core_whats_new is None:
            from .core_whats_new.client import AsyncCoreWhatsNewClient

            self._core_whats_new = AsyncCoreWhatsNewClient(client_wrapper=self._client_wrapper)
        return self._core_whats_new

    @property
    def core_app_password(self):
        if self._core_app_password is None:
            from .core_app_password.client import AsyncCoreAppPasswordClient

            self._core_app_password = AsyncCoreAppPasswordClient(client_wrapper=self._client_wrapper)
        return self._core_app_password

    @property
    def core_hover_card(self):
        if self._core_hover_card is None:
            from .core_hover_card.client import AsyncCoreHoverCardClient

            self._core_hover_card = AsyncCoreHoverCardClient(client_wrapper=self._client_wrapper)
        return self._core_hover_card

    @property
    def core_collaboration_resources(self):
        if self._core_collaboration_resources is None:
            from .core_collaboration_resources.client import AsyncCoreCollaborationResourcesClient

            self._core_collaboration_resources = AsyncCoreCollaborationResourcesClient(
                client_wrapper=self._client_wrapper
            )
        return self._core_collaboration_resources

    @property
    def core_reference_api(self):
        if self._core_reference_api is None:
            from .core_reference_api.client import AsyncCoreReferenceApiClient

            self._core_reference_api = AsyncCoreReferenceApiClient(client_wrapper=self._client_wrapper)
        return self._core_reference_api

    @property
    def core_profile_api(self):
        if self._core_profile_api is None:
            from .core_profile_api.client import AsyncCoreProfileApiClient

            self._core_profile_api = AsyncCoreProfileApiClient(client_wrapper=self._client_wrapper)
        return self._core_profile_api

    @property
    def core_unified_search(self):
        if self._core_unified_search is None:
            from .core_unified_search.client import AsyncCoreUnifiedSearchClient

            self._core_unified_search = AsyncCoreUnifiedSearchClient(client_wrapper=self._client_wrapper)
        return self._core_unified_search

    @property
    def core_translation_api(self):
        if self._core_translation_api is None:
            from .core_translation_api.client import AsyncCoreTranslationApiClient

            self._core_translation_api = AsyncCoreTranslationApiClient(client_wrapper=self._client_wrapper)
        return self._core_translation_api

    @property
    def core(self):
        if self._core is None:
            from .core.client import AsyncCoreClient

            self._core = AsyncCoreClient(client_wrapper=self._client_wrapper)
        return self._core

    @property
    def cloud_federation_api_request_handler(self):
        if self._cloud_federation_api_request_handler is None:
            from .cloud_federation_api_request_handler.client import (
                AsyncCloudFederationApiRequestHandlerClient,
            )

            self._cloud_federation_api_request_handler = AsyncCloudFederationApiRequestHandlerClient(
                client_wrapper=self._client_wrapper
            )
        return self._cloud_federation_api_request_handler

    @property
    def dashboard_dashboard_api(self):
        if self._dashboard_dashboard_api is None:
            from .dashboard_dashboard_api.client import AsyncDashboardDashboardApiClient

            self._dashboard_dashboard_api = AsyncDashboardDashboardApiClient(client_wrapper=self._client_wrapper)
        return self._dashboard_dashboard_api

    @property
    def dav_direct(self):
        if self._dav_direct is None:
            from .dav_direct.client import AsyncDavDirectClient

            self._dav_direct = AsyncDavDirectClient(client_wrapper=self._client_wrapper)
        return self._dav_direct

    @property
    def files_sharing_share_info(self):
        if self._files_sharing_share_info is None:
            from .files_sharing_share_info.client import AsyncFilesSharingShareInfoClient

            self._files_sharing_share_info = AsyncFilesSharingShareInfoClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_share_info

    @property
    def files_sharing_shareapi(self):
        if self._files_sharing_shareapi is None:
            from .files_sharing_shareapi.client import AsyncFilesSharingShareapiClient

            self._files_sharing_shareapi = AsyncFilesSharingShareapiClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_shareapi

    @property
    def files_sharing_deleted_shareapi(self):
        if self._files_sharing_deleted_shareapi is None:
            from .files_sharing_deleted_shareapi.client import AsyncFilesSharingDeletedShareapiClient

            self._files_sharing_deleted_shareapi = AsyncFilesSharingDeletedShareapiClient(
                client_wrapper=self._client_wrapper
            )
        return self._files_sharing_deleted_shareapi

    @property
    def files_sharing_shareesapi(self):
        if self._files_sharing_shareesapi is None:
            from .files_sharing_shareesapi.client import AsyncFilesSharingShareesapiClient

            self._files_sharing_shareesapi = AsyncFilesSharingShareesapiClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_shareesapi

    @property
    def files_sharing_remote(self):
        if self._files_sharing_remote is None:
            from .files_sharing_remote.client import AsyncFilesSharingRemoteClient

            self._files_sharing_remote = AsyncFilesSharingRemoteClient(client_wrapper=self._client_wrapper)
        return self._files_sharing_remote

    @property
    def oauth2login_redirector(self):
        if self._oauth2login_redirector is None:
            from .oauth2login_redirector.client import AsyncOauth2LoginRedirectorClient

            self._oauth2login_redirector = AsyncOauth2LoginRedirectorClient(client_wrapper=self._client_wrapper)
        return self._oauth2login_redirector

    @property
    def oauth2oauth_api(self):
        if self._oauth2oauth_api is None:
            from .oauth2oauth_api.client import AsyncOauth2OauthApiClient

            self._oauth2oauth_api = AsyncOauth2OauthApiClient(client_wrapper=self._client_wrapper)
        return self._oauth2oauth_api

    @property
    def provisioning_api_apps(self):
        if self._provisioning_api_apps is None:
            from .provisioning_api_apps.client import AsyncProvisioningApiAppsClient

            self._provisioning_api_apps = AsyncProvisioningApiAppsClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_apps

    @property
    def provisioning_api_groups(self):
        if self._provisioning_api_groups is None:
            from .provisioning_api_groups.client import AsyncProvisioningApiGroupsClient

            self._provisioning_api_groups = AsyncProvisioningApiGroupsClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_groups

    @property
    def provisioning_api_users(self):
        if self._provisioning_api_users is None:
            from .provisioning_api_users.client import AsyncProvisioningApiUsersClient

            self._provisioning_api_users = AsyncProvisioningApiUsersClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_users

    @property
    def provisioning_api_app_config(self):
        if self._provisioning_api_app_config is None:
            from .provisioning_api_app_config.client import AsyncProvisioningApiAppConfigClient

            self._provisioning_api_app_config = AsyncProvisioningApiAppConfigClient(client_wrapper=self._client_wrapper)
        return self._provisioning_api_app_config

    @property
    def provisioning_api_preferences(self):
        if self._provisioning_api_preferences is None:
            from .provisioning_api_preferences.client import AsyncProvisioningApiPreferencesClient

            self._provisioning_api_preferences = AsyncProvisioningApiPreferencesClient(
                client_wrapper=self._client_wrapper
            )
        return self._provisioning_api_preferences

    @property
    def settings_log_settings(self):
        if self._settings_log_settings is None:
            from .settings_log_settings.client import AsyncSettingsLogSettingsClient

            self._settings_log_settings = AsyncSettingsLogSettingsClient(client_wrapper=self._client_wrapper)
        return self._settings_log_settings

    @property
    def theming_theming(self):
        if self._theming_theming is None:
            from .theming_theming.client import AsyncThemingThemingClient

            self._theming_theming = AsyncThemingThemingClient(client_wrapper=self._client_wrapper)
        return self._theming_theming

    @property
    def theming_icon(self):
        if self._theming_icon is None:
            from .theming_icon.client import AsyncThemingIconClient

            self._theming_icon = AsyncThemingIconClient(client_wrapper=self._client_wrapper)
        return self._theming_icon

    @property
    def theming_user_theme(self):
        if self._theming_user_theme is None:
            from .theming_user_theme.client import AsyncThemingUserThemeClient

            self._theming_user_theme = AsyncThemingUserThemeClient(client_wrapper=self._client_wrapper)
        return self._theming_user_theme

    @property
    def user_status_statuses(self):
        if self._user_status_statuses is None:
            from .user_status_statuses.client import AsyncUserStatusStatusesClient

            self._user_status_statuses = AsyncUserStatusStatusesClient(client_wrapper=self._client_wrapper)
        return self._user_status_statuses

    @property
    def user_status_user_status(self):
        if self._user_status_user_status is None:
            from .user_status_user_status.client import AsyncUserStatusUserStatusClient

            self._user_status_user_status = AsyncUserStatusUserStatusClient(client_wrapper=self._client_wrapper)
        return self._user_status_user_status

    @property
    def user_status_predefined_status(self):
        if self._user_status_predefined_status is None:
            from .user_status_predefined_status.client import AsyncUserStatusPredefinedStatusClient

            self._user_status_predefined_status = AsyncUserStatusPredefinedStatusClient(
                client_wrapper=self._client_wrapper
            )
        return self._user_status_predefined_status

    @property
    def user_status_heartbeat(self):
        if self._user_status_heartbeat is None:
            from .user_status_heartbeat.client import AsyncUserStatusHeartbeatClient

            self._user_status_heartbeat = AsyncUserStatusHeartbeatClient(client_wrapper=self._client_wrapper)
        return self._user_status_heartbeat

    @property
    def weather_status_weather_status(self):
        if self._weather_status_weather_status is None:
            from .weather_status_weather_status.client import AsyncWeatherStatusWeatherStatusClient

            self._weather_status_weather_status = AsyncWeatherStatusWeatherStatusClient(
                client_wrapper=self._client_wrapper
            )
        return self._weather_status_weather_status


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
