

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_rewriting_search_rewrite_search_rewrite import QueryRewritingSearchRewriteSearchRewrite


class QueryRewritingSearchRewrite(UniversalBaseModel):
    """
    Query rewriting enabled, returns query results for spelling corrected or completed query string (=instant search), returns suggestions for corrected or completed query.
    Additional latency for spelling correction and suggestions.
    """

    search_rewrite: typing_extensions.Annotated[
        QueryRewritingSearchRewriteSearchRewrite,
        FieldMetadata(alias="SearchRewrite"),
        pydantic.Field(
            alias="SearchRewrite",
            description="Query rewriting enabled, returns query results for spelling corrected or completed query string (=instant search), returns suggestions for corrected or completed query.\nAdditional latency for spelling correction and suggestions.",
        ),
    ]
    """
    Query rewriting enabled, returns query results for spelling corrected or completed query string (=instant search), returns suggestions for corrected or completed query.
    Additional latency for spelling correction and suggestions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
