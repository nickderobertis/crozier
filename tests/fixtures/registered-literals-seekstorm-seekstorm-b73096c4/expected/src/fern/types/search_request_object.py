

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .distance_field import DistanceField
from .facet_filter import FacetFilter
from .highlight import Highlight
from .query_facet import QueryFacet
from .query_rewriting import QueryRewriting
from .query_type import QueryType
from .result_sort import ResultSort
from .result_type import ResultType
from .search_mode import SearchMode


class SearchRequestObject(UniversalBaseModel):
    """
    Search request object
    """

    query: str = pydantic.Field()
    """
    Query string, search operators + - "" are recognized.
    """

    query_vector: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Optional query vector: If None, then the query vector is derived from the query string using the specified model. If Some, then the query vector is used for semantic search and the query string is only used for lexical search and highlighting.
    """

    enable_empty_query: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable empty query: if true, an empty query string iterates through all indexed documents, supporting the query parameters: offset, length, query_facets, facet_filter, result_sort,
    otherwise an empty query string returns no results.
    Typical use cases include index browsing, index export, conversion, analytics, audits, and inspection.
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Offset of search results to return.
    """

    length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of search results to return.
    """

    result_type: typing.Optional[ResultType] = pydantic.Field(default=None)
    """
    Specify the type of search result.
    """

    realtime: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True realtime search: include indexed, but uncommitted documents into search results.
    """

    highlights: typing.Optional[typing.List[Highlight]] = pydantic.Field(default=None)
    """
    Specify field names where to create keyword-in-context fragments and highlight query terms.
    """

    field_filter: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Specify field names where to search at querytime, whereas SchemaField.indexed is set at indextime. If empty then all indexed fields are searched.
    """

    fields: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Specify names of fields to return in the search results, where SchemaField.store is set at indextime. If empty then all stored fields are returned.
    """

    distance_fields: typing.Optional[typing.List[DistanceField]] = pydantic.Field(default=None)
    """
    Specify distance fields to derive at query time and return in the search results.
    """

    query_facets: typing.Optional[typing.List[QueryFacet]] = pydantic.Field(default=None)
    """
    Facets to return with search results: if empty then no facets are returned. Facets are only enabled on facet fields that are defined in schema at create_index!
    """

    facet_filter: typing.Optional[typing.List[FacetFilter]] = pydantic.Field(default=None)
    """
    Facet filters to filter search results by facet values: if empty then no facet filters are applied. Facet filters are only enabled on facet fields that are defined in schema at create_index!
    """

    result_sort: typing.Optional[typing.List[ResultSort]] = pydantic.Field(default=None)
    """
    Sort field and order:
    Search results are sorted by the specified facet field, either in ascending or descending order.
    If no sort field is specified, then the search results are sorted by rank in descending order per default.
    Multiple sort fields are combined by a "sort by, then sort by"-method ("tie-breaking"-algorithm).
    The results are sorted by the first field, and only for those results where the first field value is identical (tie) the results are sub-sorted by the second field,
    until the n-th field value is either not equal or the last field is reached.
    A special _score field (BM25x), reflecting how relevant the result is for a given search query (phrase match, match in title etc.) can be combined with any of the other sort fields as primary, secondary or n-th search criterium.
    Sort is only enabled on facet fields that are defined in schema at create_index!
    Examples:
    - result_sort = vec![ResultSort {field: "price".into(), order: SortOrder::Descending, base: FacetValue::None},ResultSort {field: "language".into(), order: SortOrder::Ascending, base: FacetValue::None}];
    - result_sort = vec![ResultSort {field: "location".into(),order: SortOrder::Ascending, base: FacetValue::Point(vec![38.8951, -77.0364])}];
    """

    query_type_default: typing.Optional[QueryType] = pydantic.Field(default=None)
    """
    Specify default query type: (default=Intersection). This can be overwritten by search operator within the query string (+-"").
    """

    query_rewriting: typing.Optional[QueryRewriting] = pydantic.Field(default=None)
    """
    Specify query rewriting method for search query correction and completion: (default=SearchOnly).
    """

    search_mode: typing.Optional[SearchMode] = pydantic.Field(default=None)
    """
    Specify search mode: (default=Lexical).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
