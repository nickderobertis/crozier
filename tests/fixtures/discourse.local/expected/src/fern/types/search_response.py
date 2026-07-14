

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_response_grouped_search_result import SearchResponseGroupedSearchResult


class SearchResponse(UniversalBaseModel):
    categories: typing.List[typing.Optional[typing.Any]]
    grouped_search_result: SearchResponseGroupedSearchResult
    groups: typing.List[typing.Optional[typing.Any]]
    posts: typing.List[typing.Optional[typing.Any]]
    tags: typing.List[typing.Optional[typing.Any]]
    users: typing.List[typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
