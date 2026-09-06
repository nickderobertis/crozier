

import typing

from ...types.apps_response import AppsResponse
from ...types.c_store_query_search_suggestions_response import CStoreQuerySearchSuggestionsResponse

PostV1SearchGamesResponse = typing.Union[AppsResponse, CStoreQuerySearchSuggestionsResponse]
