



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .age_restriction_dto import AgeRestrictionDto
    from .age_restriction_dto_restriction import AgeRestrictionDtoRestriction
    from .age_restriction_update_dto import AgeRestrictionUpdateDto
    from .age_restriction_update_dto_restriction import AgeRestrictionUpdateDtoRestriction
    from .alternate_title_dto import AlternateTitleDto
    from .alternate_title_update_dto import AlternateTitleUpdateDto
    from .api_key_dto import ApiKeyDto
    from .authentication_activity_dto import AuthenticationActivityDto
    from .author_dto import AuthorDto
    from .author_update_dto import AuthorUpdateDto
    from .book_dto import BookDto
    from .book_import_dto import BookImportDto
    from .book_metadata_aggregation_dto import BookMetadataAggregationDto
    from .book_metadata_dto import BookMetadataDto
    from .book_metadata_update_dto import BookMetadataUpdateDto
    from .claim_status import ClaimStatus
    from .client_setting_dto import ClientSettingDto
    from .client_setting_global_update_dto import ClientSettingGlobalUpdateDto
    from .client_setting_user_update_dto import ClientSettingUserUpdateDto
    from .collection_dto import CollectionDto
    from .directory_listing_dto import DirectoryListingDto
    from .group_count_dto import GroupCountDto
    from .historical_event_dto import HistoricalEventDto
    from .item_author_dto import ItemAuthorDto
    from .item_dto import ItemDto
    from .json_feed_dto import JsonFeedDto
    from .komga_extension_dto import KomgaExtensionDto
    from .library_dto import LibraryDto
    from .library_dto_scan_interval import LibraryDtoScanInterval
    from .library_dto_series_cover import LibraryDtoSeriesCover
    from .library_update_dto import LibraryUpdateDto
    from .library_update_dto_scan_interval import LibraryUpdateDtoScanInterval
    from .library_update_dto_series_cover import LibraryUpdateDtoSeriesCover
    from .location import Location
    from .media_dto import MediaDto
    from .media_type import MediaType
    from .o_auth2client_dto import OAuth2ClientDto
    from .page_authentication_activity_dto import PageAuthenticationActivityDto
    from .page_author_dto import PageAuthorDto
    from .page_book_dto import PageBookDto
    from .page_collection_dto import PageCollectionDto
    from .page_dto import PageDto
    from .page_hash_known_dto import PageHashKnownDto
    from .page_hash_known_dto_action import PageHashKnownDtoAction
    from .page_hash_match_dto import PageHashMatchDto
    from .page_hash_unknown_dto import PageHashUnknownDto
    from .page_historical_event_dto import PageHistoricalEventDto
    from .page_integer import PageInteger
    from .page_page_hash_known_dto import PagePageHashKnownDto
    from .page_page_hash_match_dto import PagePageHashMatchDto
    from .page_page_hash_unknown_dto import PagePageHashUnknownDto
    from .page_read_list_dto import PageReadListDto
    from .page_series_dto import PageSeriesDto
    from .page_string import PageString
    from .pageable_object import PageableObject
    from .password_update_dto import PasswordUpdateDto
    from .path_dto import PathDto
    from .r2device import R2Device
    from .r2locator import R2Locator
    from .r2positions import R2Positions
    from .r2progression import R2Progression
    from .read_list_dto import ReadListDto
    from .read_list_match_dto import ReadListMatchDto
    from .read_list_request_book_dto import ReadListRequestBookDto
    from .read_list_request_book_match_book_dto import ReadListRequestBookMatchBookDto
    from .read_list_request_book_match_dto import ReadListRequestBookMatchDto
    from .read_list_request_book_match_series_dto import ReadListRequestBookMatchSeriesDto
    from .read_list_request_book_matches_dto import ReadListRequestBookMatchesDto
    from .read_list_request_match_dto import ReadListRequestMatchDto
    from .read_progress_dto import ReadProgressDto
    from .release_dto import ReleaseDto
    from .search_condition_age_rating import SearchConditionAgeRating
    from .search_condition_all_of_book import SearchConditionAllOfBook
    from .search_condition_all_of_series import SearchConditionAllOfSeries
    from .search_condition_any_of_book import SearchConditionAnyOfBook
    from .search_condition_any_of_series import SearchConditionAnyOfSeries
    from .search_condition_author import SearchConditionAuthor
    from .search_condition_book import SearchConditionBook
    from .search_condition_collection_id import SearchConditionCollectionId
    from .search_condition_complete import SearchConditionComplete
    from .search_condition_deleted import SearchConditionDeleted
    from .search_condition_genre import SearchConditionGenre
    from .search_condition_language import SearchConditionLanguage
    from .search_condition_library_id import SearchConditionLibraryId
    from .search_condition_media_profile import SearchConditionMediaProfile
    from .search_condition_media_status import SearchConditionMediaStatus
    from .search_condition_number_sort import SearchConditionNumberSort
    from .search_condition_one_shot import SearchConditionOneShot
    from .search_condition_poster import SearchConditionPoster
    from .search_condition_publisher import SearchConditionPublisher
    from .search_condition_read_list_id import SearchConditionReadListId
    from .search_condition_read_status import SearchConditionReadStatus
    from .search_condition_release_date import SearchConditionReleaseDate
    from .search_condition_series import SearchConditionSeries
    from .search_condition_series_id import SearchConditionSeriesId
    from .search_condition_series_status import SearchConditionSeriesStatus
    from .search_condition_sharing_label import SearchConditionSharingLabel
    from .search_condition_tag import SearchConditionTag
    from .search_condition_title import SearchConditionTitle
    from .search_condition_title_sort import SearchConditionTitleSort
    from .search_operator_after import SearchOperatorAfter
    from .search_operator_before import SearchOperatorBefore
    from .search_operator_begins_with import SearchOperatorBeginsWith
    from .search_operator_boolean import (
        SearchOperatorBoolean,
        SearchOperatorBoolean_IsFalse,
        SearchOperatorBoolean_IsTrue,
    )
    from .search_operator_contains import SearchOperatorContains
    from .search_operator_date import (
        SearchOperatorDate,
        SearchOperatorDate_After,
        SearchOperatorDate_Before,
        SearchOperatorDate_IsInTheLast,
        SearchOperatorDate_IsNotInTheLast,
        SearchOperatorDate_IsNotNull,
        SearchOperatorDate_IsNull,
    )
    from .search_operator_does_not_begin_with import SearchOperatorDoesNotBeginWith
    from .search_operator_does_not_contain import SearchOperatorDoesNotContain
    from .search_operator_does_not_end_with import SearchOperatorDoesNotEndWith
    from .search_operator_ends_with import SearchOperatorEndsWith
    from .search_operator_equality_author_match import (
        SearchOperatorEqualityAuthorMatch,
        SearchOperatorEqualityAuthorMatch_Is,
        SearchOperatorEqualityAuthorMatch_IsNot,
    )
    from .search_operator_equality_media_profile import (
        SearchOperatorEqualityMediaProfile,
        SearchOperatorEqualityMediaProfile_Is,
        SearchOperatorEqualityMediaProfile_IsNot,
    )
    from .search_operator_equality_nullable_string import (
        SearchOperatorEqualityNullableString,
        SearchOperatorEqualityNullableString_Is,
        SearchOperatorEqualityNullableString_IsNot,
        SearchOperatorEqualityNullableString_IsNotNull,
        SearchOperatorEqualityNullableString_IsNull,
    )
    from .search_operator_equality_poster_match import (
        SearchOperatorEqualityPosterMatch,
        SearchOperatorEqualityPosterMatch_Is,
        SearchOperatorEqualityPosterMatch_IsNot,
    )
    from .search_operator_equality_read_status import (
        SearchOperatorEqualityReadStatus,
        SearchOperatorEqualityReadStatus_Is,
        SearchOperatorEqualityReadStatus_IsNot,
    )
    from .search_operator_equality_status import (
        SearchOperatorEqualityStatus,
        SearchOperatorEqualityStatus_Is,
        SearchOperatorEqualityStatus_IsNot,
    )
    from .search_operator_equality_string import (
        SearchOperatorEqualityString,
        SearchOperatorEqualityString_Is,
        SearchOperatorEqualityString_IsNot,
    )
    from .search_operator_greater_than import SearchOperatorGreaterThan
    from .search_operator_is import SearchOperatorIs
    from .search_operator_is_false import SearchOperatorIsFalse
    from .search_operator_is_in_the_last import SearchOperatorIsInTheLast
    from .search_operator_is_not import SearchOperatorIsNot
    from .search_operator_is_not_in_the_last import SearchOperatorIsNotInTheLast
    from .search_operator_is_not_null import SearchOperatorIsNotNull
    from .search_operator_is_not_null_t import SearchOperatorIsNotNullT
    from .search_operator_is_null import SearchOperatorIsNull
    from .search_operator_is_null_t import SearchOperatorIsNullT
    from .search_operator_is_true import SearchOperatorIsTrue
    from .search_operator_less_than import SearchOperatorLessThan
    from .search_operator_numeric_nullable_integer import (
        SearchOperatorNumericNullableInteger,
        SearchOperatorNumericNullableInteger_GreaterThan,
        SearchOperatorNumericNullableInteger_Is,
        SearchOperatorNumericNullableInteger_IsNot,
        SearchOperatorNumericNullableInteger_IsNotNull,
        SearchOperatorNumericNullableInteger_IsNull,
        SearchOperatorNumericNullableInteger_LessThan,
    )
    from .search_operator_numeric_t_float import (
        SearchOperatorNumericTFloat,
        SearchOperatorNumericTFloat_GreaterThan,
        SearchOperatorNumericTFloat_Is,
        SearchOperatorNumericTFloat_IsNot,
        SearchOperatorNumericTFloat_LessThan,
    )
    from .search_operator_string import (
        SearchOperatorString,
        SearchOperatorString_BeginsWith,
        SearchOperatorString_Contains,
        SearchOperatorString_DoesNotBeginWith,
        SearchOperatorString_DoesNotContain,
        SearchOperatorString_DoesNotEndWith,
        SearchOperatorString_EndsWith,
        SearchOperatorString_Is,
        SearchOperatorString_IsNot,
    )
    from .series_dto import SeriesDto
    from .series_metadata_dto import SeriesMetadataDto
    from .series_search import SeriesSearch
    from .setting_multi_source_integer import SettingMultiSourceInteger
    from .setting_multi_source_string import SettingMultiSourceString
    from .settings_dto import SettingsDto
    from .settings_dto_thumbnail_size import SettingsDtoThumbnailSize
    from .shared_libraries_update_dto import SharedLibrariesUpdateDto
    from .sort_object import SortObject
    from .streaming_response_body import StreamingResponseBody
    from .tachiyomi_read_progress_dto import TachiyomiReadProgressDto
    from .tachiyomi_read_progress_v2dto import TachiyomiReadProgressV2Dto
    from .text import Text
    from .thumbnail_book_dto import ThumbnailBookDto
    from .thumbnail_read_list_dto import ThumbnailReadListDto
    from .thumbnail_series_collection_dto import ThumbnailSeriesCollectionDto
    from .thumbnail_series_dto import ThumbnailSeriesDto
    from .transient_book_dto import TransientBookDto
    from .user_dto import UserDto
    from .validation_error_response import ValidationErrorResponse
    from .violation import Violation
    from .web_link_dto import WebLinkDto
    from .web_link_update_dto import WebLinkUpdateDto
    from .wp_belongs_to_dto import WpBelongsToDto
    from .wp_contributor_dto import WpContributorDto
    from .wp_link_dto import WpLinkDto
    from .wp_metadata_dto import WpMetadataDto
    from .wp_metadata_dto_reading_progression import WpMetadataDtoReadingProgression
    from .wp_publication_dto import WpPublicationDto
_dynamic_imports: typing.Dict[str, str] = {
    "AgeRestrictionDto": ".age_restriction_dto",
    "AgeRestrictionDtoRestriction": ".age_restriction_dto_restriction",
    "AgeRestrictionUpdateDto": ".age_restriction_update_dto",
    "AgeRestrictionUpdateDtoRestriction": ".age_restriction_update_dto_restriction",
    "AlternateTitleDto": ".alternate_title_dto",
    "AlternateTitleUpdateDto": ".alternate_title_update_dto",
    "ApiKeyDto": ".api_key_dto",
    "AuthenticationActivityDto": ".authentication_activity_dto",
    "AuthorDto": ".author_dto",
    "AuthorUpdateDto": ".author_update_dto",
    "BookDto": ".book_dto",
    "BookImportDto": ".book_import_dto",
    "BookMetadataAggregationDto": ".book_metadata_aggregation_dto",
    "BookMetadataDto": ".book_metadata_dto",
    "BookMetadataUpdateDto": ".book_metadata_update_dto",
    "ClaimStatus": ".claim_status",
    "ClientSettingDto": ".client_setting_dto",
    "ClientSettingGlobalUpdateDto": ".client_setting_global_update_dto",
    "ClientSettingUserUpdateDto": ".client_setting_user_update_dto",
    "CollectionDto": ".collection_dto",
    "DirectoryListingDto": ".directory_listing_dto",
    "GroupCountDto": ".group_count_dto",
    "HistoricalEventDto": ".historical_event_dto",
    "ItemAuthorDto": ".item_author_dto",
    "ItemDto": ".item_dto",
    "JsonFeedDto": ".json_feed_dto",
    "KomgaExtensionDto": ".komga_extension_dto",
    "LibraryDto": ".library_dto",
    "LibraryDtoScanInterval": ".library_dto_scan_interval",
    "LibraryDtoSeriesCover": ".library_dto_series_cover",
    "LibraryUpdateDto": ".library_update_dto",
    "LibraryUpdateDtoScanInterval": ".library_update_dto_scan_interval",
    "LibraryUpdateDtoSeriesCover": ".library_update_dto_series_cover",
    "Location": ".location",
    "MediaDto": ".media_dto",
    "MediaType": ".media_type",
    "OAuth2ClientDto": ".o_auth2client_dto",
    "PageAuthenticationActivityDto": ".page_authentication_activity_dto",
    "PageAuthorDto": ".page_author_dto",
    "PageBookDto": ".page_book_dto",
    "PageCollectionDto": ".page_collection_dto",
    "PageDto": ".page_dto",
    "PageHashKnownDto": ".page_hash_known_dto",
    "PageHashKnownDtoAction": ".page_hash_known_dto_action",
    "PageHashMatchDto": ".page_hash_match_dto",
    "PageHashUnknownDto": ".page_hash_unknown_dto",
    "PageHistoricalEventDto": ".page_historical_event_dto",
    "PageInteger": ".page_integer",
    "PagePageHashKnownDto": ".page_page_hash_known_dto",
    "PagePageHashMatchDto": ".page_page_hash_match_dto",
    "PagePageHashUnknownDto": ".page_page_hash_unknown_dto",
    "PageReadListDto": ".page_read_list_dto",
    "PageSeriesDto": ".page_series_dto",
    "PageString": ".page_string",
    "PageableObject": ".pageable_object",
    "PasswordUpdateDto": ".password_update_dto",
    "PathDto": ".path_dto",
    "R2Device": ".r2device",
    "R2Locator": ".r2locator",
    "R2Positions": ".r2positions",
    "R2Progression": ".r2progression",
    "ReadListDto": ".read_list_dto",
    "ReadListMatchDto": ".read_list_match_dto",
    "ReadListRequestBookDto": ".read_list_request_book_dto",
    "ReadListRequestBookMatchBookDto": ".read_list_request_book_match_book_dto",
    "ReadListRequestBookMatchDto": ".read_list_request_book_match_dto",
    "ReadListRequestBookMatchSeriesDto": ".read_list_request_book_match_series_dto",
    "ReadListRequestBookMatchesDto": ".read_list_request_book_matches_dto",
    "ReadListRequestMatchDto": ".read_list_request_match_dto",
    "ReadProgressDto": ".read_progress_dto",
    "ReleaseDto": ".release_dto",
    "SearchConditionAgeRating": ".search_condition_age_rating",
    "SearchConditionAllOfBook": ".search_condition_all_of_book",
    "SearchConditionAllOfSeries": ".search_condition_all_of_series",
    "SearchConditionAnyOfBook": ".search_condition_any_of_book",
    "SearchConditionAnyOfSeries": ".search_condition_any_of_series",
    "SearchConditionAuthor": ".search_condition_author",
    "SearchConditionBook": ".search_condition_book",
    "SearchConditionCollectionId": ".search_condition_collection_id",
    "SearchConditionComplete": ".search_condition_complete",
    "SearchConditionDeleted": ".search_condition_deleted",
    "SearchConditionGenre": ".search_condition_genre",
    "SearchConditionLanguage": ".search_condition_language",
    "SearchConditionLibraryId": ".search_condition_library_id",
    "SearchConditionMediaProfile": ".search_condition_media_profile",
    "SearchConditionMediaStatus": ".search_condition_media_status",
    "SearchConditionNumberSort": ".search_condition_number_sort",
    "SearchConditionOneShot": ".search_condition_one_shot",
    "SearchConditionPoster": ".search_condition_poster",
    "SearchConditionPublisher": ".search_condition_publisher",
    "SearchConditionReadListId": ".search_condition_read_list_id",
    "SearchConditionReadStatus": ".search_condition_read_status",
    "SearchConditionReleaseDate": ".search_condition_release_date",
    "SearchConditionSeries": ".search_condition_series",
    "SearchConditionSeriesId": ".search_condition_series_id",
    "SearchConditionSeriesStatus": ".search_condition_series_status",
    "SearchConditionSharingLabel": ".search_condition_sharing_label",
    "SearchConditionTag": ".search_condition_tag",
    "SearchConditionTitle": ".search_condition_title",
    "SearchConditionTitleSort": ".search_condition_title_sort",
    "SearchOperatorAfter": ".search_operator_after",
    "SearchOperatorBefore": ".search_operator_before",
    "SearchOperatorBeginsWith": ".search_operator_begins_with",
    "SearchOperatorBoolean": ".search_operator_boolean",
    "SearchOperatorBoolean_IsFalse": ".search_operator_boolean",
    "SearchOperatorBoolean_IsTrue": ".search_operator_boolean",
    "SearchOperatorContains": ".search_operator_contains",
    "SearchOperatorDate": ".search_operator_date",
    "SearchOperatorDate_After": ".search_operator_date",
    "SearchOperatorDate_Before": ".search_operator_date",
    "SearchOperatorDate_IsInTheLast": ".search_operator_date",
    "SearchOperatorDate_IsNotInTheLast": ".search_operator_date",
    "SearchOperatorDate_IsNotNull": ".search_operator_date",
    "SearchOperatorDate_IsNull": ".search_operator_date",
    "SearchOperatorDoesNotBeginWith": ".search_operator_does_not_begin_with",
    "SearchOperatorDoesNotContain": ".search_operator_does_not_contain",
    "SearchOperatorDoesNotEndWith": ".search_operator_does_not_end_with",
    "SearchOperatorEndsWith": ".search_operator_ends_with",
    "SearchOperatorEqualityAuthorMatch": ".search_operator_equality_author_match",
    "SearchOperatorEqualityAuthorMatch_Is": ".search_operator_equality_author_match",
    "SearchOperatorEqualityAuthorMatch_IsNot": ".search_operator_equality_author_match",
    "SearchOperatorEqualityMediaProfile": ".search_operator_equality_media_profile",
    "SearchOperatorEqualityMediaProfile_Is": ".search_operator_equality_media_profile",
    "SearchOperatorEqualityMediaProfile_IsNot": ".search_operator_equality_media_profile",
    "SearchOperatorEqualityNullableString": ".search_operator_equality_nullable_string",
    "SearchOperatorEqualityNullableString_Is": ".search_operator_equality_nullable_string",
    "SearchOperatorEqualityNullableString_IsNot": ".search_operator_equality_nullable_string",
    "SearchOperatorEqualityNullableString_IsNotNull": ".search_operator_equality_nullable_string",
    "SearchOperatorEqualityNullableString_IsNull": ".search_operator_equality_nullable_string",
    "SearchOperatorEqualityPosterMatch": ".search_operator_equality_poster_match",
    "SearchOperatorEqualityPosterMatch_Is": ".search_operator_equality_poster_match",
    "SearchOperatorEqualityPosterMatch_IsNot": ".search_operator_equality_poster_match",
    "SearchOperatorEqualityReadStatus": ".search_operator_equality_read_status",
    "SearchOperatorEqualityReadStatus_Is": ".search_operator_equality_read_status",
    "SearchOperatorEqualityReadStatus_IsNot": ".search_operator_equality_read_status",
    "SearchOperatorEqualityStatus": ".search_operator_equality_status",
    "SearchOperatorEqualityStatus_Is": ".search_operator_equality_status",
    "SearchOperatorEqualityStatus_IsNot": ".search_operator_equality_status",
    "SearchOperatorEqualityString": ".search_operator_equality_string",
    "SearchOperatorEqualityString_Is": ".search_operator_equality_string",
    "SearchOperatorEqualityString_IsNot": ".search_operator_equality_string",
    "SearchOperatorGreaterThan": ".search_operator_greater_than",
    "SearchOperatorIs": ".search_operator_is",
    "SearchOperatorIsFalse": ".search_operator_is_false",
    "SearchOperatorIsInTheLast": ".search_operator_is_in_the_last",
    "SearchOperatorIsNot": ".search_operator_is_not",
    "SearchOperatorIsNotInTheLast": ".search_operator_is_not_in_the_last",
    "SearchOperatorIsNotNull": ".search_operator_is_not_null",
    "SearchOperatorIsNotNullT": ".search_operator_is_not_null_t",
    "SearchOperatorIsNull": ".search_operator_is_null",
    "SearchOperatorIsNullT": ".search_operator_is_null_t",
    "SearchOperatorIsTrue": ".search_operator_is_true",
    "SearchOperatorLessThan": ".search_operator_less_than",
    "SearchOperatorNumericNullableInteger": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericNullableInteger_GreaterThan": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericNullableInteger_Is": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericNullableInteger_IsNot": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericNullableInteger_IsNotNull": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericNullableInteger_IsNull": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericNullableInteger_LessThan": ".search_operator_numeric_nullable_integer",
    "SearchOperatorNumericTFloat": ".search_operator_numeric_t_float",
    "SearchOperatorNumericTFloat_GreaterThan": ".search_operator_numeric_t_float",
    "SearchOperatorNumericTFloat_Is": ".search_operator_numeric_t_float",
    "SearchOperatorNumericTFloat_IsNot": ".search_operator_numeric_t_float",
    "SearchOperatorNumericTFloat_LessThan": ".search_operator_numeric_t_float",
    "SearchOperatorString": ".search_operator_string",
    "SearchOperatorString_BeginsWith": ".search_operator_string",
    "SearchOperatorString_Contains": ".search_operator_string",
    "SearchOperatorString_DoesNotBeginWith": ".search_operator_string",
    "SearchOperatorString_DoesNotContain": ".search_operator_string",
    "SearchOperatorString_DoesNotEndWith": ".search_operator_string",
    "SearchOperatorString_EndsWith": ".search_operator_string",
    "SearchOperatorString_Is": ".search_operator_string",
    "SearchOperatorString_IsNot": ".search_operator_string",
    "SeriesDto": ".series_dto",
    "SeriesMetadataDto": ".series_metadata_dto",
    "SeriesSearch": ".series_search",
    "SettingMultiSourceInteger": ".setting_multi_source_integer",
    "SettingMultiSourceString": ".setting_multi_source_string",
    "SettingsDto": ".settings_dto",
    "SettingsDtoThumbnailSize": ".settings_dto_thumbnail_size",
    "SharedLibrariesUpdateDto": ".shared_libraries_update_dto",
    "SortObject": ".sort_object",
    "StreamingResponseBody": ".streaming_response_body",
    "TachiyomiReadProgressDto": ".tachiyomi_read_progress_dto",
    "TachiyomiReadProgressV2Dto": ".tachiyomi_read_progress_v2dto",
    "Text": ".text",
    "ThumbnailBookDto": ".thumbnail_book_dto",
    "ThumbnailReadListDto": ".thumbnail_read_list_dto",
    "ThumbnailSeriesCollectionDto": ".thumbnail_series_collection_dto",
    "ThumbnailSeriesDto": ".thumbnail_series_dto",
    "TransientBookDto": ".transient_book_dto",
    "UserDto": ".user_dto",
    "ValidationErrorResponse": ".validation_error_response",
    "Violation": ".violation",
    "WebLinkDto": ".web_link_dto",
    "WebLinkUpdateDto": ".web_link_update_dto",
    "WpBelongsToDto": ".wp_belongs_to_dto",
    "WpContributorDto": ".wp_contributor_dto",
    "WpLinkDto": ".wp_link_dto",
    "WpMetadataDto": ".wp_metadata_dto",
    "WpMetadataDtoReadingProgression": ".wp_metadata_dto_reading_progression",
    "WpPublicationDto": ".wp_publication_dto",
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
    "AgeRestrictionDto",
    "AgeRestrictionDtoRestriction",
    "AgeRestrictionUpdateDto",
    "AgeRestrictionUpdateDtoRestriction",
    "AlternateTitleDto",
    "AlternateTitleUpdateDto",
    "ApiKeyDto",
    "AuthenticationActivityDto",
    "AuthorDto",
    "AuthorUpdateDto",
    "BookDto",
    "BookImportDto",
    "BookMetadataAggregationDto",
    "BookMetadataDto",
    "BookMetadataUpdateDto",
    "ClaimStatus",
    "ClientSettingDto",
    "ClientSettingGlobalUpdateDto",
    "ClientSettingUserUpdateDto",
    "CollectionDto",
    "DirectoryListingDto",
    "GroupCountDto",
    "HistoricalEventDto",
    "ItemAuthorDto",
    "ItemDto",
    "JsonFeedDto",
    "KomgaExtensionDto",
    "LibraryDto",
    "LibraryDtoScanInterval",
    "LibraryDtoSeriesCover",
    "LibraryUpdateDto",
    "LibraryUpdateDtoScanInterval",
    "LibraryUpdateDtoSeriesCover",
    "Location",
    "MediaDto",
    "MediaType",
    "OAuth2ClientDto",
    "PageAuthenticationActivityDto",
    "PageAuthorDto",
    "PageBookDto",
    "PageCollectionDto",
    "PageDto",
    "PageHashKnownDto",
    "PageHashKnownDtoAction",
    "PageHashMatchDto",
    "PageHashUnknownDto",
    "PageHistoricalEventDto",
    "PageInteger",
    "PagePageHashKnownDto",
    "PagePageHashMatchDto",
    "PagePageHashUnknownDto",
    "PageReadListDto",
    "PageSeriesDto",
    "PageString",
    "PageableObject",
    "PasswordUpdateDto",
    "PathDto",
    "R2Device",
    "R2Locator",
    "R2Positions",
    "R2Progression",
    "ReadListDto",
    "ReadListMatchDto",
    "ReadListRequestBookDto",
    "ReadListRequestBookMatchBookDto",
    "ReadListRequestBookMatchDto",
    "ReadListRequestBookMatchSeriesDto",
    "ReadListRequestBookMatchesDto",
    "ReadListRequestMatchDto",
    "ReadProgressDto",
    "ReleaseDto",
    "SearchConditionAgeRating",
    "SearchConditionAllOfBook",
    "SearchConditionAllOfSeries",
    "SearchConditionAnyOfBook",
    "SearchConditionAnyOfSeries",
    "SearchConditionAuthor",
    "SearchConditionBook",
    "SearchConditionCollectionId",
    "SearchConditionComplete",
    "SearchConditionDeleted",
    "SearchConditionGenre",
    "SearchConditionLanguage",
    "SearchConditionLibraryId",
    "SearchConditionMediaProfile",
    "SearchConditionMediaStatus",
    "SearchConditionNumberSort",
    "SearchConditionOneShot",
    "SearchConditionPoster",
    "SearchConditionPublisher",
    "SearchConditionReadListId",
    "SearchConditionReadStatus",
    "SearchConditionReleaseDate",
    "SearchConditionSeries",
    "SearchConditionSeriesId",
    "SearchConditionSeriesStatus",
    "SearchConditionSharingLabel",
    "SearchConditionTag",
    "SearchConditionTitle",
    "SearchConditionTitleSort",
    "SearchOperatorAfter",
    "SearchOperatorBefore",
    "SearchOperatorBeginsWith",
    "SearchOperatorBoolean",
    "SearchOperatorBoolean_IsFalse",
    "SearchOperatorBoolean_IsTrue",
    "SearchOperatorContains",
    "SearchOperatorDate",
    "SearchOperatorDate_After",
    "SearchOperatorDate_Before",
    "SearchOperatorDate_IsInTheLast",
    "SearchOperatorDate_IsNotInTheLast",
    "SearchOperatorDate_IsNotNull",
    "SearchOperatorDate_IsNull",
    "SearchOperatorDoesNotBeginWith",
    "SearchOperatorDoesNotContain",
    "SearchOperatorDoesNotEndWith",
    "SearchOperatorEndsWith",
    "SearchOperatorEqualityAuthorMatch",
    "SearchOperatorEqualityAuthorMatch_Is",
    "SearchOperatorEqualityAuthorMatch_IsNot",
    "SearchOperatorEqualityMediaProfile",
    "SearchOperatorEqualityMediaProfile_Is",
    "SearchOperatorEqualityMediaProfile_IsNot",
    "SearchOperatorEqualityNullableString",
    "SearchOperatorEqualityNullableString_Is",
    "SearchOperatorEqualityNullableString_IsNot",
    "SearchOperatorEqualityNullableString_IsNotNull",
    "SearchOperatorEqualityNullableString_IsNull",
    "SearchOperatorEqualityPosterMatch",
    "SearchOperatorEqualityPosterMatch_Is",
    "SearchOperatorEqualityPosterMatch_IsNot",
    "SearchOperatorEqualityReadStatus",
    "SearchOperatorEqualityReadStatus_Is",
    "SearchOperatorEqualityReadStatus_IsNot",
    "SearchOperatorEqualityStatus",
    "SearchOperatorEqualityStatus_Is",
    "SearchOperatorEqualityStatus_IsNot",
    "SearchOperatorEqualityString",
    "SearchOperatorEqualityString_Is",
    "SearchOperatorEqualityString_IsNot",
    "SearchOperatorGreaterThan",
    "SearchOperatorIs",
    "SearchOperatorIsFalse",
    "SearchOperatorIsInTheLast",
    "SearchOperatorIsNot",
    "SearchOperatorIsNotInTheLast",
    "SearchOperatorIsNotNull",
    "SearchOperatorIsNotNullT",
    "SearchOperatorIsNull",
    "SearchOperatorIsNullT",
    "SearchOperatorIsTrue",
    "SearchOperatorLessThan",
    "SearchOperatorNumericNullableInteger",
    "SearchOperatorNumericNullableInteger_GreaterThan",
    "SearchOperatorNumericNullableInteger_Is",
    "SearchOperatorNumericNullableInteger_IsNot",
    "SearchOperatorNumericNullableInteger_IsNotNull",
    "SearchOperatorNumericNullableInteger_IsNull",
    "SearchOperatorNumericNullableInteger_LessThan",
    "SearchOperatorNumericTFloat",
    "SearchOperatorNumericTFloat_GreaterThan",
    "SearchOperatorNumericTFloat_Is",
    "SearchOperatorNumericTFloat_IsNot",
    "SearchOperatorNumericTFloat_LessThan",
    "SearchOperatorString",
    "SearchOperatorString_BeginsWith",
    "SearchOperatorString_Contains",
    "SearchOperatorString_DoesNotBeginWith",
    "SearchOperatorString_DoesNotContain",
    "SearchOperatorString_DoesNotEndWith",
    "SearchOperatorString_EndsWith",
    "SearchOperatorString_Is",
    "SearchOperatorString_IsNot",
    "SeriesDto",
    "SeriesMetadataDto",
    "SeriesSearch",
    "SettingMultiSourceInteger",
    "SettingMultiSourceString",
    "SettingsDto",
    "SettingsDtoThumbnailSize",
    "SharedLibrariesUpdateDto",
    "SortObject",
    "StreamingResponseBody",
    "TachiyomiReadProgressDto",
    "TachiyomiReadProgressV2Dto",
    "Text",
    "ThumbnailBookDto",
    "ThumbnailReadListDto",
    "ThumbnailSeriesCollectionDto",
    "ThumbnailSeriesDto",
    "TransientBookDto",
    "UserDto",
    "ValidationErrorResponse",
    "Violation",
    "WebLinkDto",
    "WebLinkUpdateDto",
    "WpBelongsToDto",
    "WpContributorDto",
    "WpLinkDto",
    "WpMetadataDto",
    "WpMetadataDtoReadingProgression",
    "WpPublicationDto",
]
