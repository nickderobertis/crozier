

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_mode_hybrid_hybrid import SearchModeHybridHybrid


class SearchModeHybrid(UniversalBaseModel):
    """
    Hybrid search mode: Search results are retrieved based on a combination of lexical and vector search.
    The relevance score of search results is calculated based on RRF (Reciprocal Rank Fusion) of the result positions in lexical and vector search.
    """

    hybrid: typing_extensions.Annotated[
        SearchModeHybridHybrid,
        FieldMetadata(alias="Hybrid"),
        pydantic.Field(
            alias="Hybrid",
            description="Hybrid search mode: Search results are retrieved based on a combination of lexical and vector search.\nThe relevance score of search results is calculated based on RRF (Reciprocal Rank Fusion) of the result positions in lexical and vector search.",
        ),
    ]
    """
    Hybrid search mode: Search results are retrieved based on a combination of lexical and vector search.
    The relevance score of search results is calculated based on RRF (Reciprocal Rank Fusion) of the result positions in lexical and vector search.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
