

import typing

from .curated_list_search_result import CuratedListSearchResult
from .episode_search_result import EpisodeSearchResult
from .podcast_search_result import PodcastSearchResult

SearchResponseResultsItem = typing.Union[EpisodeSearchResult, PodcastSearchResult, CuratedListSearchResult]
