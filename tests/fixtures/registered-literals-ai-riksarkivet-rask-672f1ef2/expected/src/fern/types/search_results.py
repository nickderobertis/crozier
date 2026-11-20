

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_hit import SearchHit


class SearchResults(UniversalBaseModel):
    """
    Governed search results (P1 Search tier 1 — substring over the discovery estate).
    """

    query: str
    results: typing.List[SearchHit]
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
