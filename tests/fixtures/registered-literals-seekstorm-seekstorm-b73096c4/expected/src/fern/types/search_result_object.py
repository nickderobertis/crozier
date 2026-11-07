

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchResultObject(UniversalBaseModel):
    """
    Search result object
    """

    time: int = pydantic.Field()
    """
    Time taken to execute the search query in nanoseconds
    """

    original_query: str = pydantic.Field()
    """
    Search query string
    """

    query: str = pydantic.Field()
    """
    Search query string after any automatic query correction or completion
    """

    offset: int = pydantic.Field()
    """
    Offset of the returned search results
    """

    length: int = pydantic.Field()
    """
    Number of requested search results
    """

    count: int = pydantic.Field()
    """
    Number of returned search results matching the query
    """

    count_total: int = pydantic.Field()
    """
    Total number of search results matching the query
    """

    query_terms: typing.List[str] = pydantic.Field()
    """
    Vector of search query terms. Can be used e.g. for custom highlighting.
    """

    results: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    Vector of search result documents
    """

    facets: typing.Dict[str, typing.List[typing.List[typing.Any]]] = pydantic.Field()
    """
    Facets with their values and corresponding document counts
    """

    suggestions: typing.List[str] = pydantic.Field()
    """
    Suggestions for query correction or completion
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
