

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.search_result import SearchResult
from .inlined_search_response_neighbor import InlinedSearchResponseNeighbor


class InlinedSearchResponse(UniversalBaseModel):
    results: typing.List[SearchResult]
    neighbor: typing.Optional[InlinedSearchResponseNeighbor] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
