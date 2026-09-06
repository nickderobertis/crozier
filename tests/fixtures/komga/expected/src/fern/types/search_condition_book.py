

from __future__ import annotations

import typing

from .search_condition_author import SearchConditionAuthor
from .search_condition_deleted import SearchConditionDeleted
from .search_condition_library_id import SearchConditionLibraryId
from .search_condition_media_profile import SearchConditionMediaProfile
from .search_condition_media_status import SearchConditionMediaStatus
from .search_condition_number_sort import SearchConditionNumberSort
from .search_condition_one_shot import SearchConditionOneShot
from .search_condition_poster import SearchConditionPoster
from .search_condition_read_list_id import SearchConditionReadListId
from .search_condition_read_status import SearchConditionReadStatus
from .search_condition_release_date import SearchConditionReleaseDate
from .search_condition_series_id import SearchConditionSeriesId
from .search_condition_tag import SearchConditionTag
from .search_condition_title import SearchConditionTitle

if typing.TYPE_CHECKING:
    from .search_condition_all_of_book import SearchConditionAllOfBook
    from .search_condition_any_of_book import SearchConditionAnyOfBook
SearchConditionBook = typing.Union[
    "SearchConditionAnyOfBook",
    "SearchConditionAllOfBook",
    SearchConditionLibraryId,
    SearchConditionReadListId,
    SearchConditionSeriesId,
    SearchConditionDeleted,
    SearchConditionOneShot,
    SearchConditionTitle,
    SearchConditionReleaseDate,
    SearchConditionTag,
    SearchConditionNumberSort,
    SearchConditionReadStatus,
    SearchConditionMediaStatus,
    SearchConditionMediaProfile,
    SearchConditionAuthor,
    SearchConditionPoster,
]
