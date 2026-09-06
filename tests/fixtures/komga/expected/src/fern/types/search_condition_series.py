

from __future__ import annotations

import typing

from .search_condition_age_rating import SearchConditionAgeRating
from .search_condition_author import SearchConditionAuthor
from .search_condition_collection_id import SearchConditionCollectionId
from .search_condition_complete import SearchConditionComplete
from .search_condition_deleted import SearchConditionDeleted
from .search_condition_genre import SearchConditionGenre
from .search_condition_language import SearchConditionLanguage
from .search_condition_library_id import SearchConditionLibraryId
from .search_condition_one_shot import SearchConditionOneShot
from .search_condition_publisher import SearchConditionPublisher
from .search_condition_read_status import SearchConditionReadStatus
from .search_condition_release_date import SearchConditionReleaseDate
from .search_condition_series_status import SearchConditionSeriesStatus
from .search_condition_sharing_label import SearchConditionSharingLabel
from .search_condition_tag import SearchConditionTag
from .search_condition_title import SearchConditionTitle
from .search_condition_title_sort import SearchConditionTitleSort

if typing.TYPE_CHECKING:
    from .search_condition_all_of_series import SearchConditionAllOfSeries
    from .search_condition_any_of_series import SearchConditionAnyOfSeries
SearchConditionSeries = typing.Union[
    "SearchConditionAnyOfSeries",
    "SearchConditionAllOfSeries",
    SearchConditionLibraryId,
    SearchConditionCollectionId,
    SearchConditionDeleted,
    SearchConditionComplete,
    SearchConditionOneShot,
    SearchConditionTitle,
    SearchConditionTitleSort,
    SearchConditionReleaseDate,
    SearchConditionTag,
    SearchConditionSharingLabel,
    SearchConditionPublisher,
    SearchConditionLanguage,
    SearchConditionGenre,
    SearchConditionAgeRating,
    SearchConditionReadStatus,
    SearchConditionSeriesStatus,
    SearchConditionAuthor,
]
