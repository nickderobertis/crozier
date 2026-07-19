

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .archival_memory_search_result import ArchivalMemorySearchResult


class ArchivalMemorySearchResponse(UniversalBaseModel):
    results: typing.List[ArchivalMemorySearchResult] = pydantic.Field()
    """
    List of search results matching the query
    """

    count: int = pydantic.Field()
    """
    Total number of results returned
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
