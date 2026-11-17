

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ranked_document import RankedDocument
from .rerank_result_usage import RerankResultUsage


class RerankResult(UniversalBaseModel):
    """
    The result of a reranking request.
    """

    model: str = pydantic.Field()
    """
    The model used to rerank documents.
    """

    data: typing.List[RankedDocument] = pydantic.Field()
    """
    The reranked documents.
    """

    usage: RerankResultUsage = pydantic.Field()
    """
    Usage statistics for the model inference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
