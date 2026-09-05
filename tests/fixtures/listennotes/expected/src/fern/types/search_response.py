

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_response_results_item import SearchResponseResultsItem


class SearchResponse(UniversalBaseModel):
    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of search results in this page.
    """

    next_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Pass this value to the **offset** parameter to do pagination of search results.
    """

    results: typing.Optional[typing.List[SearchResponseResultsItem]] = pydantic.Field(default=None)
    """
    A list of search results.
    """

    took: typing.Optional[float] = pydantic.Field(default=None)
    """
    The time it took to fetch these search results. In seconds.
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of search results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
