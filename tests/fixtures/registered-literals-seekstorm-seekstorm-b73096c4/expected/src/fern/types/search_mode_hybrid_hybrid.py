

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ann_mode import AnnMode


class SearchModeHybridHybrid(UniversalBaseModel):
    """
    Hybrid search mode: Search results are retrieved based on a combination of lexical and vector search.
    The relevance score of search results is calculated based on RRF (Reciprocal Rank Fusion) of the result positions in lexical and vector search.
    """

    similarity_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    optional threshold to filter out low similarity scores
    For dot product similarity, the similarity threshold should be between 0.0 and 1.0, where higher values indicate higher similarity (identical=1.0).
    For Euclidean distance similarity, the similarity threshold should be between 0.0 and infinity, where lower values indicate higher similarity (identical=0.0).
    """

    ann_mode: AnnMode = pydantic.Field()
    """
    Specifies in which clusters to search for ANN results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
