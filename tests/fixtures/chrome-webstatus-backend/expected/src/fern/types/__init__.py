



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .baseline_info import BaselineInfo
    from .baseline_info_status import BaselineInfoStatus
    from .baseline_status_metric import BaselineStatusMetric
    from .baseline_status_metrics_page import BaselineStatusMetricsPage
    from .basic_error_model import BasicErrorModel
    from .browser_implementation import BrowserImplementation
    from .browser_implementation_status import BrowserImplementationStatus
    from .browser_release_feature_metric import BrowserReleaseFeatureMetric
    from .browser_release_feature_metrics_page import BrowserReleaseFeatureMetricsPage
    from .browser_usage import BrowserUsage
    from .can_i_use_info import CanIUseInfo
    from .can_i_use_item import CanIUseItem
    from .chrome_daily_stats_page import ChromeDailyStatsPage
    from .chrome_usage_info import ChromeUsageInfo
    from .chrome_usage_stat import ChromeUsageStat
    from .code_subscription_page import CodeSubscriptionPage
    from .code_subscription_response import CodeSubscriptionResponse
    from .code_subscription_response_status import CodeSubscriptionResponseStatus
    from .create_notification_channel_request_config import (
        CreateNotificationChannelRequestConfig,
        CreateNotificationChannelRequestConfig_Rss,
        CreateNotificationChannelRequestConfig_Webhook,
    )
    from .email_config import EmailConfig
    from .enum_unknown import EnumUnknown
    from .extended_error_model import ExtendedErrorModel
    from .feature import Feature
    from .feature_developer_signals import FeatureDeveloperSignals
    from .feature_discouraged_according_to import FeatureDiscouragedAccordingTo
    from .feature_discouraged_alternative import FeatureDiscouragedAlternative
    from .feature_discouraged_info import FeatureDiscouragedInfo
    from .feature_evolution_split import FeatureEvolutionSplit
    from .feature_gone_error import FeatureGoneError
    from .feature_gone_split import FeatureGoneSplit
    from .feature_gone_split_type import FeatureGoneSplitType
    from .feature_metadata import FeatureMetadata
    from .feature_page import FeaturePage
    from .feature_spec_info import FeatureSpecInfo
    from .feature_split_info import FeatureSplitInfo
    from .feature_wpt_snapshots import FeatureWptSnapshots
    from .generic_updatable_unique_model import GenericUpdatableUniqueModel
    from .global_saved_search import GlobalSavedSearch
    from .global_saved_search_page import GlobalSavedSearchPage
    from .handle_vcs_webhook_request_provider import HandleVcsWebhookRequestProvider
    from .healthcheck_response import HealthcheckResponse
    from .list_aggregated_wpt_metrics_request_channel import ListAggregatedWptMetricsRequestChannel
    from .list_code_subscriptions_request_provider import ListCodeSubscriptionsRequestProvider
    from .list_feature_wpt_metrics_request_channel import ListFeatureWptMetricsRequestChannel
    from .list_features_request_sort import ListFeaturesRequestSort
    from .missing_one_impl_feature import MissingOneImplFeature
    from .missing_one_impl_features_page import MissingOneImplFeaturesPage
    from .notification_channel import NotificationChannel
    from .notification_channel_config import (
        NotificationChannelConfig,
        NotificationChannelConfig_Email,
        NotificationChannelConfig_Rss,
        NotificationChannelConfig_Webhook,
    )
    from .notification_channel_page import NotificationChannelPage
    from .notification_channel_response import NotificationChannelResponse
    from .notification_channel_response_status import NotificationChannelResponseStatus
    from .notification_channel_type import NotificationChannelType
    from .page_metadata import PageMetadata
    from .page_metadata_with_total import PageMetadataWithTotal
    from .rss_config import RssConfig
    from .saved_search import SavedSearch
    from .saved_search_info import SavedSearchInfo
    from .saved_search_response import SavedSearchResponse
    from .saved_search_update_request_update_mask_item import SavedSearchUpdateRequestUpdateMaskItem
    from .spec_link import SpecLink
    from .subscription_channel_type import SubscriptionChannelType
    from .subscription_frequency import SubscriptionFrequency
    from .subscription_occurrence import SubscriptionOccurrence
    from .subscription_page import SubscriptionPage
    from .subscription_response import SubscriptionResponse
    from .subscription_response_channel_type import SubscriptionResponseChannelType
    from .subscription_trigger_response_item import SubscriptionTriggerResponseItem
    from .subscription_trigger_response_value import SubscriptionTriggerResponseValue
    from .subscription_trigger_writable import SubscriptionTriggerWritable
    from .supported_browsers import SupportedBrowsers
    from .update_notification_channel_request_config import (
        UpdateNotificationChannelRequestConfig,
        UpdateNotificationChannelRequestConfig_Rss,
        UpdateNotificationChannelRequestConfig_Webhook,
    )
    from .update_notification_channel_request_update_mask_item import UpdateNotificationChannelRequestUpdateMaskItem
    from .update_subscription_request_update_mask_item import UpdateSubscriptionRequestUpdateMaskItem
    from .user_saved_search_bookmark import UserSavedSearchBookmark
    from .user_saved_search_bookmark_status import UserSavedSearchBookmarkStatus
    from .user_saved_search_page import UserSavedSearchPage
    from .user_saved_search_permissions import UserSavedSearchPermissions
    from .user_saved_search_role import UserSavedSearchRole
    from .vendor_position import VendorPosition
    from .webhook_config import WebhookConfig
    from .wpt_feature_data import WptFeatureData
    from .wpt_metric_view import WptMetricView
    from .wpt_run_metric import WptRunMetric
    from .wpt_run_metrics_page import WptRunMetricsPage
_dynamic_imports: typing.Dict[str, str] = {
    "BaselineInfo": ".baseline_info",
    "BaselineInfoStatus": ".baseline_info_status",
    "BaselineStatusMetric": ".baseline_status_metric",
    "BaselineStatusMetricsPage": ".baseline_status_metrics_page",
    "BasicErrorModel": ".basic_error_model",
    "BrowserImplementation": ".browser_implementation",
    "BrowserImplementationStatus": ".browser_implementation_status",
    "BrowserReleaseFeatureMetric": ".browser_release_feature_metric",
    "BrowserReleaseFeatureMetricsPage": ".browser_release_feature_metrics_page",
    "BrowserUsage": ".browser_usage",
    "CanIUseInfo": ".can_i_use_info",
    "CanIUseItem": ".can_i_use_item",
    "ChromeDailyStatsPage": ".chrome_daily_stats_page",
    "ChromeUsageInfo": ".chrome_usage_info",
    "ChromeUsageStat": ".chrome_usage_stat",
    "CodeSubscriptionPage": ".code_subscription_page",
    "CodeSubscriptionResponse": ".code_subscription_response",
    "CodeSubscriptionResponseStatus": ".code_subscription_response_status",
    "CreateNotificationChannelRequestConfig": ".create_notification_channel_request_config",
    "CreateNotificationChannelRequestConfig_Rss": ".create_notification_channel_request_config",
    "CreateNotificationChannelRequestConfig_Webhook": ".create_notification_channel_request_config",
    "EmailConfig": ".email_config",
    "EnumUnknown": ".enum_unknown",
    "ExtendedErrorModel": ".extended_error_model",
    "Feature": ".feature",
    "FeatureDeveloperSignals": ".feature_developer_signals",
    "FeatureDiscouragedAccordingTo": ".feature_discouraged_according_to",
    "FeatureDiscouragedAlternative": ".feature_discouraged_alternative",
    "FeatureDiscouragedInfo": ".feature_discouraged_info",
    "FeatureEvolutionSplit": ".feature_evolution_split",
    "FeatureGoneError": ".feature_gone_error",
    "FeatureGoneSplit": ".feature_gone_split",
    "FeatureGoneSplitType": ".feature_gone_split_type",
    "FeatureMetadata": ".feature_metadata",
    "FeaturePage": ".feature_page",
    "FeatureSpecInfo": ".feature_spec_info",
    "FeatureSplitInfo": ".feature_split_info",
    "FeatureWptSnapshots": ".feature_wpt_snapshots",
    "GenericUpdatableUniqueModel": ".generic_updatable_unique_model",
    "GlobalSavedSearch": ".global_saved_search",
    "GlobalSavedSearchPage": ".global_saved_search_page",
    "HandleVcsWebhookRequestProvider": ".handle_vcs_webhook_request_provider",
    "HealthcheckResponse": ".healthcheck_response",
    "ListAggregatedWptMetricsRequestChannel": ".list_aggregated_wpt_metrics_request_channel",
    "ListCodeSubscriptionsRequestProvider": ".list_code_subscriptions_request_provider",
    "ListFeatureWptMetricsRequestChannel": ".list_feature_wpt_metrics_request_channel",
    "ListFeaturesRequestSort": ".list_features_request_sort",
    "MissingOneImplFeature": ".missing_one_impl_feature",
    "MissingOneImplFeaturesPage": ".missing_one_impl_features_page",
    "NotificationChannel": ".notification_channel",
    "NotificationChannelConfig": ".notification_channel_config",
    "NotificationChannelConfig_Email": ".notification_channel_config",
    "NotificationChannelConfig_Rss": ".notification_channel_config",
    "NotificationChannelConfig_Webhook": ".notification_channel_config",
    "NotificationChannelPage": ".notification_channel_page",
    "NotificationChannelResponse": ".notification_channel_response",
    "NotificationChannelResponseStatus": ".notification_channel_response_status",
    "NotificationChannelType": ".notification_channel_type",
    "PageMetadata": ".page_metadata",
    "PageMetadataWithTotal": ".page_metadata_with_total",
    "RssConfig": ".rss_config",
    "SavedSearch": ".saved_search",
    "SavedSearchInfo": ".saved_search_info",
    "SavedSearchResponse": ".saved_search_response",
    "SavedSearchUpdateRequestUpdateMaskItem": ".saved_search_update_request_update_mask_item",
    "SpecLink": ".spec_link",
    "SubscriptionChannelType": ".subscription_channel_type",
    "SubscriptionFrequency": ".subscription_frequency",
    "SubscriptionOccurrence": ".subscription_occurrence",
    "SubscriptionPage": ".subscription_page",
    "SubscriptionResponse": ".subscription_response",
    "SubscriptionResponseChannelType": ".subscription_response_channel_type",
    "SubscriptionTriggerResponseItem": ".subscription_trigger_response_item",
    "SubscriptionTriggerResponseValue": ".subscription_trigger_response_value",
    "SubscriptionTriggerWritable": ".subscription_trigger_writable",
    "SupportedBrowsers": ".supported_browsers",
    "UpdateNotificationChannelRequestConfig": ".update_notification_channel_request_config",
    "UpdateNotificationChannelRequestConfig_Rss": ".update_notification_channel_request_config",
    "UpdateNotificationChannelRequestConfig_Webhook": ".update_notification_channel_request_config",
    "UpdateNotificationChannelRequestUpdateMaskItem": ".update_notification_channel_request_update_mask_item",
    "UpdateSubscriptionRequestUpdateMaskItem": ".update_subscription_request_update_mask_item",
    "UserSavedSearchBookmark": ".user_saved_search_bookmark",
    "UserSavedSearchBookmarkStatus": ".user_saved_search_bookmark_status",
    "UserSavedSearchPage": ".user_saved_search_page",
    "UserSavedSearchPermissions": ".user_saved_search_permissions",
    "UserSavedSearchRole": ".user_saved_search_role",
    "VendorPosition": ".vendor_position",
    "WebhookConfig": ".webhook_config",
    "WptFeatureData": ".wpt_feature_data",
    "WptMetricView": ".wpt_metric_view",
    "WptRunMetric": ".wpt_run_metric",
    "WptRunMetricsPage": ".wpt_run_metrics_page",
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
    "BaselineInfo",
    "BaselineInfoStatus",
    "BaselineStatusMetric",
    "BaselineStatusMetricsPage",
    "BasicErrorModel",
    "BrowserImplementation",
    "BrowserImplementationStatus",
    "BrowserReleaseFeatureMetric",
    "BrowserReleaseFeatureMetricsPage",
    "BrowserUsage",
    "CanIUseInfo",
    "CanIUseItem",
    "ChromeDailyStatsPage",
    "ChromeUsageInfo",
    "ChromeUsageStat",
    "CodeSubscriptionPage",
    "CodeSubscriptionResponse",
    "CodeSubscriptionResponseStatus",
    "CreateNotificationChannelRequestConfig",
    "CreateNotificationChannelRequestConfig_Rss",
    "CreateNotificationChannelRequestConfig_Webhook",
    "EmailConfig",
    "EnumUnknown",
    "ExtendedErrorModel",
    "Feature",
    "FeatureDeveloperSignals",
    "FeatureDiscouragedAccordingTo",
    "FeatureDiscouragedAlternative",
    "FeatureDiscouragedInfo",
    "FeatureEvolutionSplit",
    "FeatureGoneError",
    "FeatureGoneSplit",
    "FeatureGoneSplitType",
    "FeatureMetadata",
    "FeaturePage",
    "FeatureSpecInfo",
    "FeatureSplitInfo",
    "FeatureWptSnapshots",
    "GenericUpdatableUniqueModel",
    "GlobalSavedSearch",
    "GlobalSavedSearchPage",
    "HandleVcsWebhookRequestProvider",
    "HealthcheckResponse",
    "ListAggregatedWptMetricsRequestChannel",
    "ListCodeSubscriptionsRequestProvider",
    "ListFeatureWptMetricsRequestChannel",
    "ListFeaturesRequestSort",
    "MissingOneImplFeature",
    "MissingOneImplFeaturesPage",
    "NotificationChannel",
    "NotificationChannelConfig",
    "NotificationChannelConfig_Email",
    "NotificationChannelConfig_Rss",
    "NotificationChannelConfig_Webhook",
    "NotificationChannelPage",
    "NotificationChannelResponse",
    "NotificationChannelResponseStatus",
    "NotificationChannelType",
    "PageMetadata",
    "PageMetadataWithTotal",
    "RssConfig",
    "SavedSearch",
    "SavedSearchInfo",
    "SavedSearchResponse",
    "SavedSearchUpdateRequestUpdateMaskItem",
    "SpecLink",
    "SubscriptionChannelType",
    "SubscriptionFrequency",
    "SubscriptionOccurrence",
    "SubscriptionPage",
    "SubscriptionResponse",
    "SubscriptionResponseChannelType",
    "SubscriptionTriggerResponseItem",
    "SubscriptionTriggerResponseValue",
    "SubscriptionTriggerWritable",
    "SupportedBrowsers",
    "UpdateNotificationChannelRequestConfig",
    "UpdateNotificationChannelRequestConfig_Rss",
    "UpdateNotificationChannelRequestConfig_Webhook",
    "UpdateNotificationChannelRequestUpdateMaskItem",
    "UpdateSubscriptionRequestUpdateMaskItem",
    "UserSavedSearchBookmark",
    "UserSavedSearchBookmarkStatus",
    "UserSavedSearchPage",
    "UserSavedSearchPermissions",
    "UserSavedSearchRole",
    "VendorPosition",
    "WebhookConfig",
    "WptFeatureData",
    "WptMetricView",
    "WptRunMetric",
    "WptRunMetricsPage",
]
