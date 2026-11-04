

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_rewriting_search_suggest_search_suggest import QueryRewritingSearchSuggestSearchSuggest


class QueryRewritingSearchSuggest(UniversalBaseModel):
    """
    Query rewriting disabled, returns query results for original query string, returns suggestions for corrected or completed query.
    Additional latency for spelling suggestions.
    """

    search_suggest: typing_extensions.Annotated[
        QueryRewritingSearchSuggestSearchSuggest,
        FieldMetadata(alias="SearchSuggest"),
        pydantic.Field(
            alias="SearchSuggest",
            description="Query rewriting disabled, returns query results for original query string, returns suggestions for corrected or completed query.\nAdditional latency for spelling suggestions.",
        ),
    ]
    """
    Query rewriting disabled, returns query results for original query string, returns suggestions for corrected or completed query.
    Additional latency for spelling suggestions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
