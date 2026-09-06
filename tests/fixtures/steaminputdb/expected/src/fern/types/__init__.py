



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .app_filter import AppFilter
    from .app_info_item import AppInfoItem
    from .app_info_item_type import AppInfoItemType
    from .app_item import AppItem
    from .app_item_type import AppItemType
    from .apps_include import AppsInclude
    from .apps_platforms import AppsPlatforms
    from .apps_release import AppsRelease
    from .apps_response import AppsResponse
    from .avatar_frame import AvatarFrame
    from .c_published_file_get_details_response import CPublishedFileGetDetailsResponse
    from .c_published_file_query_files_response import CPublishedFileQueryFilesResponse
    from .c_store_query_per_result_metadata import CStoreQueryPerResultMetadata
    from .c_store_query_result_metadata import CStoreQueryResultMetadata
    from .c_store_query_search_suggestions_response import CStoreQuerySearchSuggestionsResponse
    from .config_detail_response import ConfigDetailResponse
    from .config_detail_response_votes_struct import ConfigDetailResponseVotesStruct
    from .config_filter import ConfigFilter
    from .config_include import ConfigInclude
    from .config_item import ConfigItem
    from .config_item_votes_struct import ConfigItemVotesStruct
    from .config_rank import ConfigRank
    from .config_rank_by import ConfigRankBy
    from .configs_response import ConfigsResponse
    from .controller_support import ControllerSupport
    from .error_detail import ErrorDetail
    from .error_model import ErrorModel
    from .login_response import LoginResponse
    from .mini_profile_background import MiniProfileBackground
    from .ping import Ping
    from .published_file_author_snapshot import PublishedFileAuthorSnapshot
    from .published_file_details import PublishedFileDetails
    from .published_file_details_child import PublishedFileDetailsChild
    from .published_file_details_for_sale_data import PublishedFileDetailsForSaleData
    from .published_file_details_kv_tag import PublishedFileDetailsKvTag
    from .published_file_details_playtime_stats import PublishedFileDetailsPlaytimeStats
    from .published_file_details_preview import PublishedFileDetailsPreview
    from .published_file_details_reaction import PublishedFileDetailsReaction
    from .published_file_details_tag import PublishedFileDetailsTag
    from .published_file_details_vote_data import PublishedFileDetailsVoteData
    from .search_response_body import SearchResponseBody
    from .steam_input_db_info import SteamInputDbInfo
    from .store_browse_filter_failure import StoreBrowseFilterFailure
    from .store_game_rating import StoreGameRating
    from .store_item import StoreItem
    from .store_item_assets import StoreItemAssets
    from .store_item_basic_info import StoreItemBasicInfo
    from .store_item_basic_info_creator_home_link import StoreItemBasicInfoCreatorHomeLink
    from .store_item_categories import StoreItemCategories
    from .store_item_free_weekend import StoreItemFreeWeekend
    from .store_item_id import StoreItemId
    from .store_item_included_items import StoreItemIncludedItems
    from .store_item_link import StoreItemLink
    from .store_item_platforms import StoreItemPlatforms
    from .store_item_platforms_vr_support import StoreItemPlatformsVrSupport
    from .store_item_purchase_option import StoreItemPurchaseOption
    from .store_item_purchase_option_discount import StoreItemPurchaseOptionDiscount
    from .store_item_purchase_option_recurrence_info import StoreItemPurchaseOptionRecurrenceInfo
    from .store_item_related_items import StoreItemRelatedItems
    from .store_item_release_info import StoreItemReleaseInfo
    from .store_item_reviews import StoreItemReviews
    from .store_item_reviews_store_review_summary import StoreItemReviewsStoreReviewSummary
    from .store_item_screenshots import StoreItemScreenshots
    from .store_item_screenshots_screenshot import StoreItemScreenshotsScreenshot
    from .store_item_supported_language import StoreItemSupportedLanguage
    from .store_item_tag import StoreItemTag
    from .store_item_trailers import StoreItemTrailers
    from .store_item_trailers_adaptive_trailer import StoreItemTrailersAdaptiveTrailer
    from .store_item_trailers_trailer import StoreItemTrailersTrailer
    from .store_item_trailers_video_source import StoreItemTrailersVideoSource
    from .user_info_response import UserInfoResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AppFilter": ".app_filter",
    "AppInfoItem": ".app_info_item",
    "AppInfoItemType": ".app_info_item_type",
    "AppItem": ".app_item",
    "AppItemType": ".app_item_type",
    "AppsInclude": ".apps_include",
    "AppsPlatforms": ".apps_platforms",
    "AppsRelease": ".apps_release",
    "AppsResponse": ".apps_response",
    "AvatarFrame": ".avatar_frame",
    "CPublishedFileGetDetailsResponse": ".c_published_file_get_details_response",
    "CPublishedFileQueryFilesResponse": ".c_published_file_query_files_response",
    "CStoreQueryPerResultMetadata": ".c_store_query_per_result_metadata",
    "CStoreQueryResultMetadata": ".c_store_query_result_metadata",
    "CStoreQuerySearchSuggestionsResponse": ".c_store_query_search_suggestions_response",
    "ConfigDetailResponse": ".config_detail_response",
    "ConfigDetailResponseVotesStruct": ".config_detail_response_votes_struct",
    "ConfigFilter": ".config_filter",
    "ConfigInclude": ".config_include",
    "ConfigItem": ".config_item",
    "ConfigItemVotesStruct": ".config_item_votes_struct",
    "ConfigRank": ".config_rank",
    "ConfigRankBy": ".config_rank_by",
    "ConfigsResponse": ".configs_response",
    "ControllerSupport": ".controller_support",
    "ErrorDetail": ".error_detail",
    "ErrorModel": ".error_model",
    "LoginResponse": ".login_response",
    "MiniProfileBackground": ".mini_profile_background",
    "Ping": ".ping",
    "PublishedFileAuthorSnapshot": ".published_file_author_snapshot",
    "PublishedFileDetails": ".published_file_details",
    "PublishedFileDetailsChild": ".published_file_details_child",
    "PublishedFileDetailsForSaleData": ".published_file_details_for_sale_data",
    "PublishedFileDetailsKvTag": ".published_file_details_kv_tag",
    "PublishedFileDetailsPlaytimeStats": ".published_file_details_playtime_stats",
    "PublishedFileDetailsPreview": ".published_file_details_preview",
    "PublishedFileDetailsReaction": ".published_file_details_reaction",
    "PublishedFileDetailsTag": ".published_file_details_tag",
    "PublishedFileDetailsVoteData": ".published_file_details_vote_data",
    "SearchResponseBody": ".search_response_body",
    "SteamInputDbInfo": ".steam_input_db_info",
    "StoreBrowseFilterFailure": ".store_browse_filter_failure",
    "StoreGameRating": ".store_game_rating",
    "StoreItem": ".store_item",
    "StoreItemAssets": ".store_item_assets",
    "StoreItemBasicInfo": ".store_item_basic_info",
    "StoreItemBasicInfoCreatorHomeLink": ".store_item_basic_info_creator_home_link",
    "StoreItemCategories": ".store_item_categories",
    "StoreItemFreeWeekend": ".store_item_free_weekend",
    "StoreItemId": ".store_item_id",
    "StoreItemIncludedItems": ".store_item_included_items",
    "StoreItemLink": ".store_item_link",
    "StoreItemPlatforms": ".store_item_platforms",
    "StoreItemPlatformsVrSupport": ".store_item_platforms_vr_support",
    "StoreItemPurchaseOption": ".store_item_purchase_option",
    "StoreItemPurchaseOptionDiscount": ".store_item_purchase_option_discount",
    "StoreItemPurchaseOptionRecurrenceInfo": ".store_item_purchase_option_recurrence_info",
    "StoreItemRelatedItems": ".store_item_related_items",
    "StoreItemReleaseInfo": ".store_item_release_info",
    "StoreItemReviews": ".store_item_reviews",
    "StoreItemReviewsStoreReviewSummary": ".store_item_reviews_store_review_summary",
    "StoreItemScreenshots": ".store_item_screenshots",
    "StoreItemScreenshotsScreenshot": ".store_item_screenshots_screenshot",
    "StoreItemSupportedLanguage": ".store_item_supported_language",
    "StoreItemTag": ".store_item_tag",
    "StoreItemTrailers": ".store_item_trailers",
    "StoreItemTrailersAdaptiveTrailer": ".store_item_trailers_adaptive_trailer",
    "StoreItemTrailersTrailer": ".store_item_trailers_trailer",
    "StoreItemTrailersVideoSource": ".store_item_trailers_video_source",
    "UserInfoResponse": ".user_info_response",
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
    "AppFilter",
    "AppInfoItem",
    "AppInfoItemType",
    "AppItem",
    "AppItemType",
    "AppsInclude",
    "AppsPlatforms",
    "AppsRelease",
    "AppsResponse",
    "AvatarFrame",
    "CPublishedFileGetDetailsResponse",
    "CPublishedFileQueryFilesResponse",
    "CStoreQueryPerResultMetadata",
    "CStoreQueryResultMetadata",
    "CStoreQuerySearchSuggestionsResponse",
    "ConfigDetailResponse",
    "ConfigDetailResponseVotesStruct",
    "ConfigFilter",
    "ConfigInclude",
    "ConfigItem",
    "ConfigItemVotesStruct",
    "ConfigRank",
    "ConfigRankBy",
    "ConfigsResponse",
    "ControllerSupport",
    "ErrorDetail",
    "ErrorModel",
    "LoginResponse",
    "MiniProfileBackground",
    "Ping",
    "PublishedFileAuthorSnapshot",
    "PublishedFileDetails",
    "PublishedFileDetailsChild",
    "PublishedFileDetailsForSaleData",
    "PublishedFileDetailsKvTag",
    "PublishedFileDetailsPlaytimeStats",
    "PublishedFileDetailsPreview",
    "PublishedFileDetailsReaction",
    "PublishedFileDetailsTag",
    "PublishedFileDetailsVoteData",
    "SearchResponseBody",
    "SteamInputDbInfo",
    "StoreBrowseFilterFailure",
    "StoreGameRating",
    "StoreItem",
    "StoreItemAssets",
    "StoreItemBasicInfo",
    "StoreItemBasicInfoCreatorHomeLink",
    "StoreItemCategories",
    "StoreItemFreeWeekend",
    "StoreItemId",
    "StoreItemIncludedItems",
    "StoreItemLink",
    "StoreItemPlatforms",
    "StoreItemPlatformsVrSupport",
    "StoreItemPurchaseOption",
    "StoreItemPurchaseOptionDiscount",
    "StoreItemPurchaseOptionRecurrenceInfo",
    "StoreItemRelatedItems",
    "StoreItemReleaseInfo",
    "StoreItemReviews",
    "StoreItemReviewsStoreReviewSummary",
    "StoreItemScreenshots",
    "StoreItemScreenshotsScreenshot",
    "StoreItemSupportedLanguage",
    "StoreItemTag",
    "StoreItemTrailers",
    "StoreItemTrailersAdaptiveTrailer",
    "StoreItemTrailersTrailer",
    "StoreItemTrailersVideoSource",
    "UserInfoResponse",
]
