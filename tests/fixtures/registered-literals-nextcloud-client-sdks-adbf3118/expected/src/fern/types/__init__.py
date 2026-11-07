



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cloud_federation_api_add_share import CloudFederationApiAddShare
    from .cloud_federation_api_capabilities import CloudFederationApiCapabilities
    from .cloud_federation_api_error import CloudFederationApiError
    from .cloud_federation_api_validation_error import CloudFederationApiValidationError
    from .cloud_federation_api_validation_error_all_of import CloudFederationApiValidationErrorAllOf
    from .cloud_federation_api_validation_error_all_of_validation_errors import (
        CloudFederationApiValidationErrorAllOfValidationErrors,
    )
    from .core_app_password_get_app_password200response import CoreAppPasswordGetAppPassword200Response
    from .core_app_password_get_app_password200response_ocs import CoreAppPasswordGetAppPassword200ResponseOcs
    from .core_app_password_get_app_password200response_ocs_data import CoreAppPasswordGetAppPassword200ResponseOcsData
    from .core_auto_complete_get200response import CoreAutoCompleteGet200Response
    from .core_auto_complete_get200response_ocs import CoreAutoCompleteGet200ResponseOcs
    from .core_autocomplete_result import CoreAutocompleteResult
    from .core_collaboration_resources_list_collection200response import (
        CoreCollaborationResourcesListCollection200Response,
    )
    from .core_collaboration_resources_list_collection200response_ocs import (
        CoreCollaborationResourcesListCollection200ResponseOcs,
    )
    from .core_collaboration_resources_search_collections200response import (
        CoreCollaborationResourcesSearchCollections200Response,
    )
    from .core_collaboration_resources_search_collections200response_ocs import (
        CoreCollaborationResourcesSearchCollections200ResponseOcs,
    )
    from .core_collection import CoreCollection
    from .core_contacts_action import CoreContactsAction
    from .core_hover_card_get_user200response import CoreHoverCardGetUser200Response
    from .core_hover_card_get_user200response_ocs import CoreHoverCardGetUser200ResponseOcs
    from .core_hover_card_get_user200response_ocs_data import CoreHoverCardGetUser200ResponseOcsData
    from .core_login_flow_v2 import CoreLoginFlowV2
    from .core_login_flow_v2credentials import CoreLoginFlowV2Credentials
    from .core_login_flow_v2poll import CoreLoginFlowV2Poll
    from .core_navigation_entry import CoreNavigationEntry
    from .core_navigation_entry_order import CoreNavigationEntryOrder
    from .core_navigation_get_apps_navigation200response import CoreNavigationGetAppsNavigation200Response
    from .core_navigation_get_apps_navigation200response_ocs import CoreNavigationGetAppsNavigation200ResponseOcs
    from .core_ocs_get_capabilities200response import CoreOcsGetCapabilities200Response
    from .core_ocs_get_capabilities200response_ocs import CoreOcsGetCapabilities200ResponseOcs
    from .core_ocs_get_capabilities200response_ocs_data import CoreOcsGetCapabilities200ResponseOcsData
    from .core_ocs_get_capabilities200response_ocs_data_capabilities import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilities,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_dav import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesDav,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharing,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_federation import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingFederation,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_group import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingGroup,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublic,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public_expire_date import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public_password import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicPassword,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_sharee import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingSharee,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUser,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user_expire_date import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_ocm import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcm,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_ocm_resource_types_inner import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInner,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_ocm_resource_types_inner_protocols import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInnerProtocols,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_provisioning_api import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_theming import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesTheming,
    )
    from .core_ocs_get_capabilities200response_ocs_data_capabilities_user_status import (
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesUserStatus,
    )
    from .core_ocs_get_capabilities200response_ocs_data_version import CoreOcsGetCapabilities200ResponseOcsDataVersion
    from .core_reference import CoreReference
    from .core_reference_api_get_providers_info200response import CoreReferenceApiGetProvidersInfo200Response
    from .core_reference_api_get_providers_info200response_ocs import CoreReferenceApiGetProvidersInfo200ResponseOcs
    from .core_reference_api_resolve_one200response import CoreReferenceApiResolveOne200Response
    from .core_reference_api_resolve_one200response_ocs import CoreReferenceApiResolveOne200ResponseOcs
    from .core_reference_api_resolve_one200response_ocs_data import CoreReferenceApiResolveOne200ResponseOcsData
    from .core_reference_api_touch_provider200response import CoreReferenceApiTouchProvider200Response
    from .core_reference_api_touch_provider200response_ocs import CoreReferenceApiTouchProvider200ResponseOcs
    from .core_reference_api_touch_provider200response_ocs_data import CoreReferenceApiTouchProvider200ResponseOcsData
    from .core_reference_open_graph_object import CoreReferenceOpenGraphObject
    from .core_reference_provider import CoreReferenceProvider
    from .core_status import CoreStatus
    from .core_translation_api_languages200response import CoreTranslationApiLanguages200Response
    from .core_translation_api_languages200response_ocs import CoreTranslationApiLanguages200ResponseOcs
    from .core_translation_api_languages200response_ocs_data import CoreTranslationApiLanguages200ResponseOcsData
    from .core_translation_api_languages200response_ocs_data_languages_inner import (
        CoreTranslationApiLanguages200ResponseOcsDataLanguagesInner,
    )
    from .core_translation_api_translate200response import CoreTranslationApiTranslate200Response
    from .core_translation_api_translate200response_ocs import CoreTranslationApiTranslate200ResponseOcs
    from .core_translation_api_translate200response_ocs_data import CoreTranslationApiTranslate200ResponseOcsData
    from .core_unified_search_get_providers200response import CoreUnifiedSearchGetProviders200Response
    from .core_unified_search_get_providers200response_ocs import CoreUnifiedSearchGetProviders200ResponseOcs
    from .core_unified_search_provider import CoreUnifiedSearchProvider
    from .core_unified_search_result import CoreUnifiedSearchResult
    from .core_unified_search_result_cursor import CoreUnifiedSearchResultCursor
    from .core_unified_search_result_entry import CoreUnifiedSearchResultEntry
    from .core_unified_search_search200response import CoreUnifiedSearchSearch200Response
    from .core_unified_search_search200response_ocs import CoreUnifiedSearchSearch200ResponseOcs
    from .core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
    from .core_whats_new_dismiss200response_ocs import CoreWhatsNewDismiss200ResponseOcs
    from .core_whats_new_get200response import CoreWhatsNewGet200Response
    from .core_whats_new_get200response_ocs import CoreWhatsNewGet200ResponseOcs
    from .core_whats_new_get200response_ocs_data import CoreWhatsNewGet200ResponseOcsData
    from .core_whats_new_get200response_ocs_data_whats_new import CoreWhatsNewGet200ResponseOcsDataWhatsNew
    from .core_wipe_check_wipe200response import CoreWipeCheckWipe200Response
    from .dashboard_dashboard_api_get_widget_items200response import DashboardDashboardApiGetWidgetItems200Response
    from .dashboard_dashboard_api_get_widget_items200response_ocs import (
        DashboardDashboardApiGetWidgetItems200ResponseOcs,
    )
    from .dashboard_dashboard_api_get_widgets200response import DashboardDashboardApiGetWidgets200Response
    from .dashboard_dashboard_api_get_widgets200response_ocs import DashboardDashboardApiGetWidgets200ResponseOcs
    from .dashboard_widget import DashboardWidget
    from .dashboard_widget_buttons_inner import DashboardWidgetButtonsInner
    from .dashboard_widget_item import DashboardWidgetItem
    from .dav_capabilities import DavCapabilities
    from .dav_direct_get_url200response import DavDirectGetUrl200Response
    from .dav_direct_get_url200response_ocs import DavDirectGetUrl200ResponseOcs
    from .dav_direct_get_url200response_ocs_data import DavDirectGetUrl200ResponseOcsData
    from .files_sharing_capabilities import FilesSharingCapabilities
    from .files_sharing_deleted_share import FilesSharingDeletedShare
    from .files_sharing_deleted_shareapi_list200response import FilesSharingDeletedShareapiList200Response
    from .files_sharing_deleted_shareapi_list200response_ocs import FilesSharingDeletedShareapiList200ResponseOcs
    from .files_sharing_lookup import FilesSharingLookup
    from .files_sharing_remote_get_share200response import FilesSharingRemoteGetShare200Response
    from .files_sharing_remote_get_share200response_ocs import FilesSharingRemoteGetShare200ResponseOcs
    from .files_sharing_remote_get_shares200response import FilesSharingRemoteGetShares200Response
    from .files_sharing_remote_get_shares200response_ocs import FilesSharingRemoteGetShares200ResponseOcs
    from .files_sharing_remote_share import FilesSharingRemoteShare
    from .files_sharing_share import FilesSharingShare
    from .files_sharing_share_info import FilesSharingShareInfo
    from .files_sharing_share_status import FilesSharingShareStatus
    from .files_sharing_share_status_one_of import FilesSharingShareStatusOneOf
    from .files_sharing_shareapi_create_share200response import FilesSharingShareapiCreateShare200Response
    from .files_sharing_shareapi_create_share200response_ocs import FilesSharingShareapiCreateShare200ResponseOcs
    from .files_sharing_shareapi_get_shares200response import FilesSharingShareapiGetShares200Response
    from .files_sharing_shareapi_get_shares200response_ocs import FilesSharingShareapiGetShares200ResponseOcs
    from .files_sharing_sharee import FilesSharingSharee
    from .files_sharing_sharee_circle import FilesSharingShareeCircle
    from .files_sharing_sharee_circle_all_of import FilesSharingShareeCircleAllOf
    from .files_sharing_sharee_circle_all_of_value import FilesSharingShareeCircleAllOfValue
    from .files_sharing_sharee_circle_all_of_value_all_of import FilesSharingShareeCircleAllOfValueAllOf
    from .files_sharing_sharee_email import FilesSharingShareeEmail
    from .files_sharing_sharee_email_all_of import FilesSharingShareeEmailAllOf
    from .files_sharing_sharee_lookup import FilesSharingShareeLookup
    from .files_sharing_sharee_lookup_all_of import FilesSharingShareeLookupAllOf
    from .files_sharing_sharee_lookup_all_of_extra import FilesSharingShareeLookupAllOfExtra
    from .files_sharing_sharee_lookup_all_of_value import FilesSharingShareeLookupAllOfValue
    from .files_sharing_sharee_lookup_all_of_value_all_of import FilesSharingShareeLookupAllOfValueAllOf
    from .files_sharing_sharee_remote import FilesSharingShareeRemote
    from .files_sharing_sharee_remote_all_of import FilesSharingShareeRemoteAllOf
    from .files_sharing_sharee_remote_all_of_value import FilesSharingShareeRemoteAllOfValue
    from .files_sharing_sharee_remote_all_of_value_all_of import FilesSharingShareeRemoteAllOfValueAllOf
    from .files_sharing_sharee_remote_group import FilesSharingShareeRemoteGroup
    from .files_sharing_sharee_remote_group_all_of import FilesSharingShareeRemoteGroupAllOf
    from .files_sharing_sharee_user import FilesSharingShareeUser
    from .files_sharing_sharee_user_all_of import FilesSharingShareeUserAllOf
    from .files_sharing_sharee_user_all_of_status import FilesSharingShareeUserAllOfStatus
    from .files_sharing_sharee_value import FilesSharingShareeValue
    from .files_sharing_sharees_recommended_result import FilesSharingShareesRecommendedResult
    from .files_sharing_sharees_recommended_result_exact import FilesSharingShareesRecommendedResultExact
    from .files_sharing_sharees_search_result import FilesSharingShareesSearchResult
    from .files_sharing_sharees_search_result_exact import FilesSharingShareesSearchResultExact
    from .files_sharing_shareesapi_find_recommended200response import FilesSharingShareesapiFindRecommended200Response
    from .files_sharing_shareesapi_find_recommended200response_ocs import (
        FilesSharingShareesapiFindRecommended200ResponseOcs,
    )
    from .files_sharing_shareesapi_search200response import FilesSharingShareesapiSearch200Response
    from .files_sharing_shareesapi_search200response_ocs import FilesSharingShareesapiSearch200ResponseOcs
    from .oauth2oauth_api_get_token200response import Oauth2OauthApiGetToken200Response
    from .ocs_meta import OcsMeta
    from .provisioning_api_app_config_get_apps200response import ProvisioningApiAppConfigGetApps200Response
    from .provisioning_api_app_config_get_apps200response_ocs import ProvisioningApiAppConfigGetApps200ResponseOcs
    from .provisioning_api_app_config_get_apps200response_ocs_data import (
        ProvisioningApiAppConfigGetApps200ResponseOcsData,
    )
    from .provisioning_api_app_config_get_value200response import ProvisioningApiAppConfigGetValue200Response
    from .provisioning_api_app_config_get_value200response_ocs import ProvisioningApiAppConfigGetValue200ResponseOcs
    from .provisioning_api_app_config_get_value200response_ocs_data import (
        ProvisioningApiAppConfigGetValue200ResponseOcsData,
    )
    from .provisioning_api_app_info import ProvisioningApiAppInfo
    from .provisioning_api_apps_get_app_info200response import ProvisioningApiAppsGetAppInfo200Response
    from .provisioning_api_apps_get_app_info200response_ocs import ProvisioningApiAppsGetAppInfo200ResponseOcs
    from .provisioning_api_apps_get_apps200response import ProvisioningApiAppsGetApps200Response
    from .provisioning_api_apps_get_apps200response_ocs import ProvisioningApiAppsGetApps200ResponseOcs
    from .provisioning_api_apps_get_apps200response_ocs_data import ProvisioningApiAppsGetApps200ResponseOcsData
    from .provisioning_api_capabilities import ProvisioningApiCapabilities
    from .provisioning_api_group_details import ProvisioningApiGroupDetails
    from .provisioning_api_group_details_usercount import ProvisioningApiGroupDetailsUsercount
    from .provisioning_api_groups_get_group_users200response import ProvisioningApiGroupsGetGroupUsers200Response
    from .provisioning_api_groups_get_group_users200response_ocs import ProvisioningApiGroupsGetGroupUsers200ResponseOcs
    from .provisioning_api_groups_get_group_users200response_ocs_data import (
        ProvisioningApiGroupsGetGroupUsers200ResponseOcsData,
    )
    from .provisioning_api_groups_get_group_users_details200response import (
        ProvisioningApiGroupsGetGroupUsersDetails200Response,
    )
    from .provisioning_api_groups_get_group_users_details200response_ocs import (
        ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcs,
    )
    from .provisioning_api_groups_get_group_users_details200response_ocs_data import (
        ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsData,
    )
    from .provisioning_api_groups_get_group_users_details200response_ocs_data_users_value import (
        ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValue,
    )
    from .provisioning_api_groups_get_group_users_details200response_ocs_data_users_value_one_of import (
        ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValueOneOf,
    )
    from .provisioning_api_groups_get_groups200response import ProvisioningApiGroupsGetGroups200Response
    from .provisioning_api_groups_get_groups200response_ocs import ProvisioningApiGroupsGetGroups200ResponseOcs
    from .provisioning_api_groups_get_groups200response_ocs_data import ProvisioningApiGroupsGetGroups200ResponseOcsData
    from .provisioning_api_groups_get_groups_details200response import ProvisioningApiGroupsGetGroupsDetails200Response
    from .provisioning_api_groups_get_groups_details200response_ocs import (
        ProvisioningApiGroupsGetGroupsDetails200ResponseOcs,
    )
    from .provisioning_api_groups_get_groups_details200response_ocs_data import (
        ProvisioningApiGroupsGetGroupsDetails200ResponseOcsData,
    )
    from .provisioning_api_groups_get_sub_admins_of_group200response import (
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
    )
    from .provisioning_api_groups_get_sub_admins_of_group200response_ocs import (
        ProvisioningApiGroupsGetSubAdminsOfGroup200ResponseOcs,
    )
    from .provisioning_api_user_details import ProvisioningApiUserDetails
    from .provisioning_api_user_details_backend_capabilities import ProvisioningApiUserDetailsBackendCapabilities
    from .provisioning_api_user_details_quota import ProvisioningApiUserDetailsQuota
    from .provisioning_api_user_details_quota_quota import ProvisioningApiUserDetailsQuotaQuota
    from .provisioning_api_users_add_user200response import ProvisioningApiUsersAddUser200Response
    from .provisioning_api_users_add_user200response_ocs import ProvisioningApiUsersAddUser200ResponseOcs
    from .provisioning_api_users_get_user200response import ProvisioningApiUsersGetUser200Response
    from .provisioning_api_users_get_user200response_ocs import ProvisioningApiUsersGetUser200ResponseOcs
    from .provisioning_api_users_search_by_phone_numbers200response import (
        ProvisioningApiUsersSearchByPhoneNumbers200Response,
    )
    from .provisioning_api_users_search_by_phone_numbers200response_ocs import (
        ProvisioningApiUsersSearchByPhoneNumbers200ResponseOcs,
    )
    from .theming_background import ThemingBackground
    from .theming_public_capabilities import ThemingPublicCapabilities
    from .theming_theming_get_manifest200response import ThemingThemingGetManifest200Response
    from .theming_theming_get_manifest200response_icons_inner import ThemingThemingGetManifest200ResponseIconsInner
    from .user_status_capabilities import UserStatusCapabilities
    from .user_status_clear_at import UserStatusClearAt
    from .user_status_clear_at_time import UserStatusClearAtTime
    from .user_status_clear_at_time_type import UserStatusClearAtTimeType
    from .user_status_clear_at_type import UserStatusClearAtType
    from .user_status_predefined import UserStatusPredefined
    from .user_status_predefined_status_find_all200response import UserStatusPredefinedStatusFindAll200Response
    from .user_status_predefined_status_find_all200response_ocs import UserStatusPredefinedStatusFindAll200ResponseOcs
    from .user_status_private import UserStatusPrivate
    from .user_status_private_all_of import UserStatusPrivateAllOf
    from .user_status_public import UserStatusPublic
    from .user_status_statuses_find200response import UserStatusStatusesFind200Response
    from .user_status_statuses_find200response_ocs import UserStatusStatusesFind200ResponseOcs
    from .user_status_statuses_find_all200response import UserStatusStatusesFindAll200Response
    from .user_status_statuses_find_all200response_ocs import UserStatusStatusesFindAll200ResponseOcs
    from .user_status_user_status_get_status200response import UserStatusUserStatusGetStatus200Response
    from .user_status_user_status_get_status200response_ocs import UserStatusUserStatusGetStatus200ResponseOcs
    from .weather_status_capabilities import WeatherStatusCapabilities
    from .weather_status_forecast import WeatherStatusForecast
    from .weather_status_forecast_data import WeatherStatusForecastData
    from .weather_status_forecast_data_instant import WeatherStatusForecastDataInstant
    from .weather_status_forecast_data_instant_details import WeatherStatusForecastDataInstantDetails
    from .weather_status_forecast_data_next12hours import WeatherStatusForecastDataNext12Hours
    from .weather_status_forecast_data_next12hours_details import WeatherStatusForecastDataNext12HoursDetails
    from .weather_status_forecast_data_next12hours_summary import WeatherStatusForecastDataNext12HoursSummary
    from .weather_status_forecast_data_next1hours import WeatherStatusForecastDataNext1Hours
    from .weather_status_forecast_data_next1hours_details import WeatherStatusForecastDataNext1HoursDetails
    from .weather_status_forecast_data_next6hours import WeatherStatusForecastDataNext6Hours
    from .weather_status_forecast_data_next6hours_details import WeatherStatusForecastDataNext6HoursDetails
    from .weather_status_weather_status_get_forecast200response import WeatherStatusWeatherStatusGetForecast200Response
    from .weather_status_weather_status_get_forecast200response_ocs import (
        WeatherStatusWeatherStatusGetForecast200ResponseOcs,
    )
    from .weather_status_weather_status_get_location200response import WeatherStatusWeatherStatusGetLocation200Response
    from .weather_status_weather_status_get_location200response_ocs import (
        WeatherStatusWeatherStatusGetLocation200ResponseOcs,
    )
    from .weather_status_weather_status_get_location200response_ocs_data import (
        WeatherStatusWeatherStatusGetLocation200ResponseOcsData,
    )
    from .weather_status_weather_status_use_personal_address200response import (
        WeatherStatusWeatherStatusUsePersonalAddress200Response,
    )
    from .weather_status_weather_status_use_personal_address200response_ocs import (
        WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcs,
    )
    from .weather_status_weather_status_use_personal_address200response_ocs_data import (
        WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcsData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CloudFederationApiAddShare": ".cloud_federation_api_add_share",
    "CloudFederationApiCapabilities": ".cloud_federation_api_capabilities",
    "CloudFederationApiError": ".cloud_federation_api_error",
    "CloudFederationApiValidationError": ".cloud_federation_api_validation_error",
    "CloudFederationApiValidationErrorAllOf": ".cloud_federation_api_validation_error_all_of",
    "CloudFederationApiValidationErrorAllOfValidationErrors": ".cloud_federation_api_validation_error_all_of_validation_errors",
    "CoreAppPasswordGetAppPassword200Response": ".core_app_password_get_app_password200response",
    "CoreAppPasswordGetAppPassword200ResponseOcs": ".core_app_password_get_app_password200response_ocs",
    "CoreAppPasswordGetAppPassword200ResponseOcsData": ".core_app_password_get_app_password200response_ocs_data",
    "CoreAutoCompleteGet200Response": ".core_auto_complete_get200response",
    "CoreAutoCompleteGet200ResponseOcs": ".core_auto_complete_get200response_ocs",
    "CoreAutocompleteResult": ".core_autocomplete_result",
    "CoreCollaborationResourcesListCollection200Response": ".core_collaboration_resources_list_collection200response",
    "CoreCollaborationResourcesListCollection200ResponseOcs": ".core_collaboration_resources_list_collection200response_ocs",
    "CoreCollaborationResourcesSearchCollections200Response": ".core_collaboration_resources_search_collections200response",
    "CoreCollaborationResourcesSearchCollections200ResponseOcs": ".core_collaboration_resources_search_collections200response_ocs",
    "CoreCollection": ".core_collection",
    "CoreContactsAction": ".core_contacts_action",
    "CoreHoverCardGetUser200Response": ".core_hover_card_get_user200response",
    "CoreHoverCardGetUser200ResponseOcs": ".core_hover_card_get_user200response_ocs",
    "CoreHoverCardGetUser200ResponseOcsData": ".core_hover_card_get_user200response_ocs_data",
    "CoreLoginFlowV2": ".core_login_flow_v2",
    "CoreLoginFlowV2Credentials": ".core_login_flow_v2credentials",
    "CoreLoginFlowV2Poll": ".core_login_flow_v2poll",
    "CoreNavigationEntry": ".core_navigation_entry",
    "CoreNavigationEntryOrder": ".core_navigation_entry_order",
    "CoreNavigationGetAppsNavigation200Response": ".core_navigation_get_apps_navigation200response",
    "CoreNavigationGetAppsNavigation200ResponseOcs": ".core_navigation_get_apps_navigation200response_ocs",
    "CoreOcsGetCapabilities200Response": ".core_ocs_get_capabilities200response",
    "CoreOcsGetCapabilities200ResponseOcs": ".core_ocs_get_capabilities200response_ocs",
    "CoreOcsGetCapabilities200ResponseOcsData": ".core_ocs_get_capabilities200response_ocs_data",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilities": ".core_ocs_get_capabilities200response_ocs_data_capabilities",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesDav": ".core_ocs_get_capabilities200response_ocs_data_capabilities_dav",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharing": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingFederation": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_federation",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingGroup": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_group",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublic": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public_expire_date",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicPassword": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public_password",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingSharee": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_sharee",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUser": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate": ".core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user_expire_date",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcm": ".core_ocs_get_capabilities200response_ocs_data_capabilities_ocm",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInner": ".core_ocs_get_capabilities200response_ocs_data_capabilities_ocm_resource_types_inner",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInnerProtocols": ".core_ocs_get_capabilities200response_ocs_data_capabilities_ocm_resource_types_inner_protocols",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi": ".core_ocs_get_capabilities200response_ocs_data_capabilities_provisioning_api",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesTheming": ".core_ocs_get_capabilities200response_ocs_data_capabilities_theming",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesUserStatus": ".core_ocs_get_capabilities200response_ocs_data_capabilities_user_status",
    "CoreOcsGetCapabilities200ResponseOcsDataVersion": ".core_ocs_get_capabilities200response_ocs_data_version",
    "CoreReference": ".core_reference",
    "CoreReferenceApiGetProvidersInfo200Response": ".core_reference_api_get_providers_info200response",
    "CoreReferenceApiGetProvidersInfo200ResponseOcs": ".core_reference_api_get_providers_info200response_ocs",
    "CoreReferenceApiResolveOne200Response": ".core_reference_api_resolve_one200response",
    "CoreReferenceApiResolveOne200ResponseOcs": ".core_reference_api_resolve_one200response_ocs",
    "CoreReferenceApiResolveOne200ResponseOcsData": ".core_reference_api_resolve_one200response_ocs_data",
    "CoreReferenceApiTouchProvider200Response": ".core_reference_api_touch_provider200response",
    "CoreReferenceApiTouchProvider200ResponseOcs": ".core_reference_api_touch_provider200response_ocs",
    "CoreReferenceApiTouchProvider200ResponseOcsData": ".core_reference_api_touch_provider200response_ocs_data",
    "CoreReferenceOpenGraphObject": ".core_reference_open_graph_object",
    "CoreReferenceProvider": ".core_reference_provider",
    "CoreStatus": ".core_status",
    "CoreTranslationApiLanguages200Response": ".core_translation_api_languages200response",
    "CoreTranslationApiLanguages200ResponseOcs": ".core_translation_api_languages200response_ocs",
    "CoreTranslationApiLanguages200ResponseOcsData": ".core_translation_api_languages200response_ocs_data",
    "CoreTranslationApiLanguages200ResponseOcsDataLanguagesInner": ".core_translation_api_languages200response_ocs_data_languages_inner",
    "CoreTranslationApiTranslate200Response": ".core_translation_api_translate200response",
    "CoreTranslationApiTranslate200ResponseOcs": ".core_translation_api_translate200response_ocs",
    "CoreTranslationApiTranslate200ResponseOcsData": ".core_translation_api_translate200response_ocs_data",
    "CoreUnifiedSearchGetProviders200Response": ".core_unified_search_get_providers200response",
    "CoreUnifiedSearchGetProviders200ResponseOcs": ".core_unified_search_get_providers200response_ocs",
    "CoreUnifiedSearchProvider": ".core_unified_search_provider",
    "CoreUnifiedSearchResult": ".core_unified_search_result",
    "CoreUnifiedSearchResultCursor": ".core_unified_search_result_cursor",
    "CoreUnifiedSearchResultEntry": ".core_unified_search_result_entry",
    "CoreUnifiedSearchSearch200Response": ".core_unified_search_search200response",
    "CoreUnifiedSearchSearch200ResponseOcs": ".core_unified_search_search200response_ocs",
    "CoreWhatsNewDismiss200Response": ".core_whats_new_dismiss200response",
    "CoreWhatsNewDismiss200ResponseOcs": ".core_whats_new_dismiss200response_ocs",
    "CoreWhatsNewGet200Response": ".core_whats_new_get200response",
    "CoreWhatsNewGet200ResponseOcs": ".core_whats_new_get200response_ocs",
    "CoreWhatsNewGet200ResponseOcsData": ".core_whats_new_get200response_ocs_data",
    "CoreWhatsNewGet200ResponseOcsDataWhatsNew": ".core_whats_new_get200response_ocs_data_whats_new",
    "CoreWipeCheckWipe200Response": ".core_wipe_check_wipe200response",
    "DashboardDashboardApiGetWidgetItems200Response": ".dashboard_dashboard_api_get_widget_items200response",
    "DashboardDashboardApiGetWidgetItems200ResponseOcs": ".dashboard_dashboard_api_get_widget_items200response_ocs",
    "DashboardDashboardApiGetWidgets200Response": ".dashboard_dashboard_api_get_widgets200response",
    "DashboardDashboardApiGetWidgets200ResponseOcs": ".dashboard_dashboard_api_get_widgets200response_ocs",
    "DashboardWidget": ".dashboard_widget",
    "DashboardWidgetButtonsInner": ".dashboard_widget_buttons_inner",
    "DashboardWidgetItem": ".dashboard_widget_item",
    "DavCapabilities": ".dav_capabilities",
    "DavDirectGetUrl200Response": ".dav_direct_get_url200response",
    "DavDirectGetUrl200ResponseOcs": ".dav_direct_get_url200response_ocs",
    "DavDirectGetUrl200ResponseOcsData": ".dav_direct_get_url200response_ocs_data",
    "FilesSharingCapabilities": ".files_sharing_capabilities",
    "FilesSharingDeletedShare": ".files_sharing_deleted_share",
    "FilesSharingDeletedShareapiList200Response": ".files_sharing_deleted_shareapi_list200response",
    "FilesSharingDeletedShareapiList200ResponseOcs": ".files_sharing_deleted_shareapi_list200response_ocs",
    "FilesSharingLookup": ".files_sharing_lookup",
    "FilesSharingRemoteGetShare200Response": ".files_sharing_remote_get_share200response",
    "FilesSharingRemoteGetShare200ResponseOcs": ".files_sharing_remote_get_share200response_ocs",
    "FilesSharingRemoteGetShares200Response": ".files_sharing_remote_get_shares200response",
    "FilesSharingRemoteGetShares200ResponseOcs": ".files_sharing_remote_get_shares200response_ocs",
    "FilesSharingRemoteShare": ".files_sharing_remote_share",
    "FilesSharingShare": ".files_sharing_share",
    "FilesSharingShareInfo": ".files_sharing_share_info",
    "FilesSharingShareStatus": ".files_sharing_share_status",
    "FilesSharingShareStatusOneOf": ".files_sharing_share_status_one_of",
    "FilesSharingShareapiCreateShare200Response": ".files_sharing_shareapi_create_share200response",
    "FilesSharingShareapiCreateShare200ResponseOcs": ".files_sharing_shareapi_create_share200response_ocs",
    "FilesSharingShareapiGetShares200Response": ".files_sharing_shareapi_get_shares200response",
    "FilesSharingShareapiGetShares200ResponseOcs": ".files_sharing_shareapi_get_shares200response_ocs",
    "FilesSharingSharee": ".files_sharing_sharee",
    "FilesSharingShareeCircle": ".files_sharing_sharee_circle",
    "FilesSharingShareeCircleAllOf": ".files_sharing_sharee_circle_all_of",
    "FilesSharingShareeCircleAllOfValue": ".files_sharing_sharee_circle_all_of_value",
    "FilesSharingShareeCircleAllOfValueAllOf": ".files_sharing_sharee_circle_all_of_value_all_of",
    "FilesSharingShareeEmail": ".files_sharing_sharee_email",
    "FilesSharingShareeEmailAllOf": ".files_sharing_sharee_email_all_of",
    "FilesSharingShareeLookup": ".files_sharing_sharee_lookup",
    "FilesSharingShareeLookupAllOf": ".files_sharing_sharee_lookup_all_of",
    "FilesSharingShareeLookupAllOfExtra": ".files_sharing_sharee_lookup_all_of_extra",
    "FilesSharingShareeLookupAllOfValue": ".files_sharing_sharee_lookup_all_of_value",
    "FilesSharingShareeLookupAllOfValueAllOf": ".files_sharing_sharee_lookup_all_of_value_all_of",
    "FilesSharingShareeRemote": ".files_sharing_sharee_remote",
    "FilesSharingShareeRemoteAllOf": ".files_sharing_sharee_remote_all_of",
    "FilesSharingShareeRemoteAllOfValue": ".files_sharing_sharee_remote_all_of_value",
    "FilesSharingShareeRemoteAllOfValueAllOf": ".files_sharing_sharee_remote_all_of_value_all_of",
    "FilesSharingShareeRemoteGroup": ".files_sharing_sharee_remote_group",
    "FilesSharingShareeRemoteGroupAllOf": ".files_sharing_sharee_remote_group_all_of",
    "FilesSharingShareeUser": ".files_sharing_sharee_user",
    "FilesSharingShareeUserAllOf": ".files_sharing_sharee_user_all_of",
    "FilesSharingShareeUserAllOfStatus": ".files_sharing_sharee_user_all_of_status",
    "FilesSharingShareeValue": ".files_sharing_sharee_value",
    "FilesSharingShareesRecommendedResult": ".files_sharing_sharees_recommended_result",
    "FilesSharingShareesRecommendedResultExact": ".files_sharing_sharees_recommended_result_exact",
    "FilesSharingShareesSearchResult": ".files_sharing_sharees_search_result",
    "FilesSharingShareesSearchResultExact": ".files_sharing_sharees_search_result_exact",
    "FilesSharingShareesapiFindRecommended200Response": ".files_sharing_shareesapi_find_recommended200response",
    "FilesSharingShareesapiFindRecommended200ResponseOcs": ".files_sharing_shareesapi_find_recommended200response_ocs",
    "FilesSharingShareesapiSearch200Response": ".files_sharing_shareesapi_search200response",
    "FilesSharingShareesapiSearch200ResponseOcs": ".files_sharing_shareesapi_search200response_ocs",
    "Oauth2OauthApiGetToken200Response": ".oauth2oauth_api_get_token200response",
    "OcsMeta": ".ocs_meta",
    "ProvisioningApiAppConfigGetApps200Response": ".provisioning_api_app_config_get_apps200response",
    "ProvisioningApiAppConfigGetApps200ResponseOcs": ".provisioning_api_app_config_get_apps200response_ocs",
    "ProvisioningApiAppConfigGetApps200ResponseOcsData": ".provisioning_api_app_config_get_apps200response_ocs_data",
    "ProvisioningApiAppConfigGetValue200Response": ".provisioning_api_app_config_get_value200response",
    "ProvisioningApiAppConfigGetValue200ResponseOcs": ".provisioning_api_app_config_get_value200response_ocs",
    "ProvisioningApiAppConfigGetValue200ResponseOcsData": ".provisioning_api_app_config_get_value200response_ocs_data",
    "ProvisioningApiAppInfo": ".provisioning_api_app_info",
    "ProvisioningApiAppsGetAppInfo200Response": ".provisioning_api_apps_get_app_info200response",
    "ProvisioningApiAppsGetAppInfo200ResponseOcs": ".provisioning_api_apps_get_app_info200response_ocs",
    "ProvisioningApiAppsGetApps200Response": ".provisioning_api_apps_get_apps200response",
    "ProvisioningApiAppsGetApps200ResponseOcs": ".provisioning_api_apps_get_apps200response_ocs",
    "ProvisioningApiAppsGetApps200ResponseOcsData": ".provisioning_api_apps_get_apps200response_ocs_data",
    "ProvisioningApiCapabilities": ".provisioning_api_capabilities",
    "ProvisioningApiGroupDetails": ".provisioning_api_group_details",
    "ProvisioningApiGroupDetailsUsercount": ".provisioning_api_group_details_usercount",
    "ProvisioningApiGroupsGetGroupUsers200Response": ".provisioning_api_groups_get_group_users200response",
    "ProvisioningApiGroupsGetGroupUsers200ResponseOcs": ".provisioning_api_groups_get_group_users200response_ocs",
    "ProvisioningApiGroupsGetGroupUsers200ResponseOcsData": ".provisioning_api_groups_get_group_users200response_ocs_data",
    "ProvisioningApiGroupsGetGroupUsersDetails200Response": ".provisioning_api_groups_get_group_users_details200response",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcs": ".provisioning_api_groups_get_group_users_details200response_ocs",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsData": ".provisioning_api_groups_get_group_users_details200response_ocs_data",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValue": ".provisioning_api_groups_get_group_users_details200response_ocs_data_users_value",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValueOneOf": ".provisioning_api_groups_get_group_users_details200response_ocs_data_users_value_one_of",
    "ProvisioningApiGroupsGetGroups200Response": ".provisioning_api_groups_get_groups200response",
    "ProvisioningApiGroupsGetGroups200ResponseOcs": ".provisioning_api_groups_get_groups200response_ocs",
    "ProvisioningApiGroupsGetGroups200ResponseOcsData": ".provisioning_api_groups_get_groups200response_ocs_data",
    "ProvisioningApiGroupsGetGroupsDetails200Response": ".provisioning_api_groups_get_groups_details200response",
    "ProvisioningApiGroupsGetGroupsDetails200ResponseOcs": ".provisioning_api_groups_get_groups_details200response_ocs",
    "ProvisioningApiGroupsGetGroupsDetails200ResponseOcsData": ".provisioning_api_groups_get_groups_details200response_ocs_data",
    "ProvisioningApiGroupsGetSubAdminsOfGroup200Response": ".provisioning_api_groups_get_sub_admins_of_group200response",
    "ProvisioningApiGroupsGetSubAdminsOfGroup200ResponseOcs": ".provisioning_api_groups_get_sub_admins_of_group200response_ocs",
    "ProvisioningApiUserDetails": ".provisioning_api_user_details",
    "ProvisioningApiUserDetailsBackendCapabilities": ".provisioning_api_user_details_backend_capabilities",
    "ProvisioningApiUserDetailsQuota": ".provisioning_api_user_details_quota",
    "ProvisioningApiUserDetailsQuotaQuota": ".provisioning_api_user_details_quota_quota",
    "ProvisioningApiUsersAddUser200Response": ".provisioning_api_users_add_user200response",
    "ProvisioningApiUsersAddUser200ResponseOcs": ".provisioning_api_users_add_user200response_ocs",
    "ProvisioningApiUsersGetUser200Response": ".provisioning_api_users_get_user200response",
    "ProvisioningApiUsersGetUser200ResponseOcs": ".provisioning_api_users_get_user200response_ocs",
    "ProvisioningApiUsersSearchByPhoneNumbers200Response": ".provisioning_api_users_search_by_phone_numbers200response",
    "ProvisioningApiUsersSearchByPhoneNumbers200ResponseOcs": ".provisioning_api_users_search_by_phone_numbers200response_ocs",
    "ThemingBackground": ".theming_background",
    "ThemingPublicCapabilities": ".theming_public_capabilities",
    "ThemingThemingGetManifest200Response": ".theming_theming_get_manifest200response",
    "ThemingThemingGetManifest200ResponseIconsInner": ".theming_theming_get_manifest200response_icons_inner",
    "UserStatusCapabilities": ".user_status_capabilities",
    "UserStatusClearAt": ".user_status_clear_at",
    "UserStatusClearAtTime": ".user_status_clear_at_time",
    "UserStatusClearAtTimeType": ".user_status_clear_at_time_type",
    "UserStatusClearAtType": ".user_status_clear_at_type",
    "UserStatusPredefined": ".user_status_predefined",
    "UserStatusPredefinedStatusFindAll200Response": ".user_status_predefined_status_find_all200response",
    "UserStatusPredefinedStatusFindAll200ResponseOcs": ".user_status_predefined_status_find_all200response_ocs",
    "UserStatusPrivate": ".user_status_private",
    "UserStatusPrivateAllOf": ".user_status_private_all_of",
    "UserStatusPublic": ".user_status_public",
    "UserStatusStatusesFind200Response": ".user_status_statuses_find200response",
    "UserStatusStatusesFind200ResponseOcs": ".user_status_statuses_find200response_ocs",
    "UserStatusStatusesFindAll200Response": ".user_status_statuses_find_all200response",
    "UserStatusStatusesFindAll200ResponseOcs": ".user_status_statuses_find_all200response_ocs",
    "UserStatusUserStatusGetStatus200Response": ".user_status_user_status_get_status200response",
    "UserStatusUserStatusGetStatus200ResponseOcs": ".user_status_user_status_get_status200response_ocs",
    "WeatherStatusCapabilities": ".weather_status_capabilities",
    "WeatherStatusForecast": ".weather_status_forecast",
    "WeatherStatusForecastData": ".weather_status_forecast_data",
    "WeatherStatusForecastDataInstant": ".weather_status_forecast_data_instant",
    "WeatherStatusForecastDataInstantDetails": ".weather_status_forecast_data_instant_details",
    "WeatherStatusForecastDataNext12Hours": ".weather_status_forecast_data_next12hours",
    "WeatherStatusForecastDataNext12HoursDetails": ".weather_status_forecast_data_next12hours_details",
    "WeatherStatusForecastDataNext12HoursSummary": ".weather_status_forecast_data_next12hours_summary",
    "WeatherStatusForecastDataNext1Hours": ".weather_status_forecast_data_next1hours",
    "WeatherStatusForecastDataNext1HoursDetails": ".weather_status_forecast_data_next1hours_details",
    "WeatherStatusForecastDataNext6Hours": ".weather_status_forecast_data_next6hours",
    "WeatherStatusForecastDataNext6HoursDetails": ".weather_status_forecast_data_next6hours_details",
    "WeatherStatusWeatherStatusGetForecast200Response": ".weather_status_weather_status_get_forecast200response",
    "WeatherStatusWeatherStatusGetForecast200ResponseOcs": ".weather_status_weather_status_get_forecast200response_ocs",
    "WeatherStatusWeatherStatusGetLocation200Response": ".weather_status_weather_status_get_location200response",
    "WeatherStatusWeatherStatusGetLocation200ResponseOcs": ".weather_status_weather_status_get_location200response_ocs",
    "WeatherStatusWeatherStatusGetLocation200ResponseOcsData": ".weather_status_weather_status_get_location200response_ocs_data",
    "WeatherStatusWeatherStatusUsePersonalAddress200Response": ".weather_status_weather_status_use_personal_address200response",
    "WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcs": ".weather_status_weather_status_use_personal_address200response_ocs",
    "WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcsData": ".weather_status_weather_status_use_personal_address200response_ocs_data",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CloudFederationApiAddShare",
    "CloudFederationApiCapabilities",
    "CloudFederationApiError",
    "CloudFederationApiValidationError",
    "CloudFederationApiValidationErrorAllOf",
    "CloudFederationApiValidationErrorAllOfValidationErrors",
    "CoreAppPasswordGetAppPassword200Response",
    "CoreAppPasswordGetAppPassword200ResponseOcs",
    "CoreAppPasswordGetAppPassword200ResponseOcsData",
    "CoreAutoCompleteGet200Response",
    "CoreAutoCompleteGet200ResponseOcs",
    "CoreAutocompleteResult",
    "CoreCollaborationResourcesListCollection200Response",
    "CoreCollaborationResourcesListCollection200ResponseOcs",
    "CoreCollaborationResourcesSearchCollections200Response",
    "CoreCollaborationResourcesSearchCollections200ResponseOcs",
    "CoreCollection",
    "CoreContactsAction",
    "CoreHoverCardGetUser200Response",
    "CoreHoverCardGetUser200ResponseOcs",
    "CoreHoverCardGetUser200ResponseOcsData",
    "CoreLoginFlowV2",
    "CoreLoginFlowV2Credentials",
    "CoreLoginFlowV2Poll",
    "CoreNavigationEntry",
    "CoreNavigationEntryOrder",
    "CoreNavigationGetAppsNavigation200Response",
    "CoreNavigationGetAppsNavigation200ResponseOcs",
    "CoreOcsGetCapabilities200Response",
    "CoreOcsGetCapabilities200ResponseOcs",
    "CoreOcsGetCapabilities200ResponseOcsData",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilities",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesDav",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharing",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingFederation",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingGroup",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublic",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicPassword",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingSharee",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUser",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcm",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInner",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInnerProtocols",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesTheming",
    "CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesUserStatus",
    "CoreOcsGetCapabilities200ResponseOcsDataVersion",
    "CoreReference",
    "CoreReferenceApiGetProvidersInfo200Response",
    "CoreReferenceApiGetProvidersInfo200ResponseOcs",
    "CoreReferenceApiResolveOne200Response",
    "CoreReferenceApiResolveOne200ResponseOcs",
    "CoreReferenceApiResolveOne200ResponseOcsData",
    "CoreReferenceApiTouchProvider200Response",
    "CoreReferenceApiTouchProvider200ResponseOcs",
    "CoreReferenceApiTouchProvider200ResponseOcsData",
    "CoreReferenceOpenGraphObject",
    "CoreReferenceProvider",
    "CoreStatus",
    "CoreTranslationApiLanguages200Response",
    "CoreTranslationApiLanguages200ResponseOcs",
    "CoreTranslationApiLanguages200ResponseOcsData",
    "CoreTranslationApiLanguages200ResponseOcsDataLanguagesInner",
    "CoreTranslationApiTranslate200Response",
    "CoreTranslationApiTranslate200ResponseOcs",
    "CoreTranslationApiTranslate200ResponseOcsData",
    "CoreUnifiedSearchGetProviders200Response",
    "CoreUnifiedSearchGetProviders200ResponseOcs",
    "CoreUnifiedSearchProvider",
    "CoreUnifiedSearchResult",
    "CoreUnifiedSearchResultCursor",
    "CoreUnifiedSearchResultEntry",
    "CoreUnifiedSearchSearch200Response",
    "CoreUnifiedSearchSearch200ResponseOcs",
    "CoreWhatsNewDismiss200Response",
    "CoreWhatsNewDismiss200ResponseOcs",
    "CoreWhatsNewGet200Response",
    "CoreWhatsNewGet200ResponseOcs",
    "CoreWhatsNewGet200ResponseOcsData",
    "CoreWhatsNewGet200ResponseOcsDataWhatsNew",
    "CoreWipeCheckWipe200Response",
    "DashboardDashboardApiGetWidgetItems200Response",
    "DashboardDashboardApiGetWidgetItems200ResponseOcs",
    "DashboardDashboardApiGetWidgets200Response",
    "DashboardDashboardApiGetWidgets200ResponseOcs",
    "DashboardWidget",
    "DashboardWidgetButtonsInner",
    "DashboardWidgetItem",
    "DavCapabilities",
    "DavDirectGetUrl200Response",
    "DavDirectGetUrl200ResponseOcs",
    "DavDirectGetUrl200ResponseOcsData",
    "FilesSharingCapabilities",
    "FilesSharingDeletedShare",
    "FilesSharingDeletedShareapiList200Response",
    "FilesSharingDeletedShareapiList200ResponseOcs",
    "FilesSharingLookup",
    "FilesSharingRemoteGetShare200Response",
    "FilesSharingRemoteGetShare200ResponseOcs",
    "FilesSharingRemoteGetShares200Response",
    "FilesSharingRemoteGetShares200ResponseOcs",
    "FilesSharingRemoteShare",
    "FilesSharingShare",
    "FilesSharingShareInfo",
    "FilesSharingShareStatus",
    "FilesSharingShareStatusOneOf",
    "FilesSharingShareapiCreateShare200Response",
    "FilesSharingShareapiCreateShare200ResponseOcs",
    "FilesSharingShareapiGetShares200Response",
    "FilesSharingShareapiGetShares200ResponseOcs",
    "FilesSharingSharee",
    "FilesSharingShareeCircle",
    "FilesSharingShareeCircleAllOf",
    "FilesSharingShareeCircleAllOfValue",
    "FilesSharingShareeCircleAllOfValueAllOf",
    "FilesSharingShareeEmail",
    "FilesSharingShareeEmailAllOf",
    "FilesSharingShareeLookup",
    "FilesSharingShareeLookupAllOf",
    "FilesSharingShareeLookupAllOfExtra",
    "FilesSharingShareeLookupAllOfValue",
    "FilesSharingShareeLookupAllOfValueAllOf",
    "FilesSharingShareeRemote",
    "FilesSharingShareeRemoteAllOf",
    "FilesSharingShareeRemoteAllOfValue",
    "FilesSharingShareeRemoteAllOfValueAllOf",
    "FilesSharingShareeRemoteGroup",
    "FilesSharingShareeRemoteGroupAllOf",
    "FilesSharingShareeUser",
    "FilesSharingShareeUserAllOf",
    "FilesSharingShareeUserAllOfStatus",
    "FilesSharingShareeValue",
    "FilesSharingShareesRecommendedResult",
    "FilesSharingShareesRecommendedResultExact",
    "FilesSharingShareesSearchResult",
    "FilesSharingShareesSearchResultExact",
    "FilesSharingShareesapiFindRecommended200Response",
    "FilesSharingShareesapiFindRecommended200ResponseOcs",
    "FilesSharingShareesapiSearch200Response",
    "FilesSharingShareesapiSearch200ResponseOcs",
    "Oauth2OauthApiGetToken200Response",
    "OcsMeta",
    "ProvisioningApiAppConfigGetApps200Response",
    "ProvisioningApiAppConfigGetApps200ResponseOcs",
    "ProvisioningApiAppConfigGetApps200ResponseOcsData",
    "ProvisioningApiAppConfigGetValue200Response",
    "ProvisioningApiAppConfigGetValue200ResponseOcs",
    "ProvisioningApiAppConfigGetValue200ResponseOcsData",
    "ProvisioningApiAppInfo",
    "ProvisioningApiAppsGetAppInfo200Response",
    "ProvisioningApiAppsGetAppInfo200ResponseOcs",
    "ProvisioningApiAppsGetApps200Response",
    "ProvisioningApiAppsGetApps200ResponseOcs",
    "ProvisioningApiAppsGetApps200ResponseOcsData",
    "ProvisioningApiCapabilities",
    "ProvisioningApiGroupDetails",
    "ProvisioningApiGroupDetailsUsercount",
    "ProvisioningApiGroupsGetGroupUsers200Response",
    "ProvisioningApiGroupsGetGroupUsers200ResponseOcs",
    "ProvisioningApiGroupsGetGroupUsers200ResponseOcsData",
    "ProvisioningApiGroupsGetGroupUsersDetails200Response",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcs",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsData",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValue",
    "ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValueOneOf",
    "ProvisioningApiGroupsGetGroups200Response",
    "ProvisioningApiGroupsGetGroups200ResponseOcs",
    "ProvisioningApiGroupsGetGroups200ResponseOcsData",
    "ProvisioningApiGroupsGetGroupsDetails200Response",
    "ProvisioningApiGroupsGetGroupsDetails200ResponseOcs",
    "ProvisioningApiGroupsGetGroupsDetails200ResponseOcsData",
    "ProvisioningApiGroupsGetSubAdminsOfGroup200Response",
    "ProvisioningApiGroupsGetSubAdminsOfGroup200ResponseOcs",
    "ProvisioningApiUserDetails",
    "ProvisioningApiUserDetailsBackendCapabilities",
    "ProvisioningApiUserDetailsQuota",
    "ProvisioningApiUserDetailsQuotaQuota",
    "ProvisioningApiUsersAddUser200Response",
    "ProvisioningApiUsersAddUser200ResponseOcs",
    "ProvisioningApiUsersGetUser200Response",
    "ProvisioningApiUsersGetUser200ResponseOcs",
    "ProvisioningApiUsersSearchByPhoneNumbers200Response",
    "ProvisioningApiUsersSearchByPhoneNumbers200ResponseOcs",
    "ThemingBackground",
    "ThemingPublicCapabilities",
    "ThemingThemingGetManifest200Response",
    "ThemingThemingGetManifest200ResponseIconsInner",
    "UserStatusCapabilities",
    "UserStatusClearAt",
    "UserStatusClearAtTime",
    "UserStatusClearAtTimeType",
    "UserStatusClearAtType",
    "UserStatusPredefined",
    "UserStatusPredefinedStatusFindAll200Response",
    "UserStatusPredefinedStatusFindAll200ResponseOcs",
    "UserStatusPrivate",
    "UserStatusPrivateAllOf",
    "UserStatusPublic",
    "UserStatusStatusesFind200Response",
    "UserStatusStatusesFind200ResponseOcs",
    "UserStatusStatusesFindAll200Response",
    "UserStatusStatusesFindAll200ResponseOcs",
    "UserStatusUserStatusGetStatus200Response",
    "UserStatusUserStatusGetStatus200ResponseOcs",
    "WeatherStatusCapabilities",
    "WeatherStatusForecast",
    "WeatherStatusForecastData",
    "WeatherStatusForecastDataInstant",
    "WeatherStatusForecastDataInstantDetails",
    "WeatherStatusForecastDataNext12Hours",
    "WeatherStatusForecastDataNext12HoursDetails",
    "WeatherStatusForecastDataNext12HoursSummary",
    "WeatherStatusForecastDataNext1Hours",
    "WeatherStatusForecastDataNext1HoursDetails",
    "WeatherStatusForecastDataNext6Hours",
    "WeatherStatusForecastDataNext6HoursDetails",
    "WeatherStatusWeatherStatusGetForecast200Response",
    "WeatherStatusWeatherStatusGetForecast200ResponseOcs",
    "WeatherStatusWeatherStatusGetLocation200Response",
    "WeatherStatusWeatherStatusGetLocation200ResponseOcs",
    "WeatherStatusWeatherStatusGetLocation200ResponseOcsData",
    "WeatherStatusWeatherStatusUsePersonalAddress200Response",
    "WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcs",
    "WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcsData",
]
