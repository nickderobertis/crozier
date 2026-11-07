

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vector_store_item import VectorStoreItem


class VectorStoreSearchResult(UniversalBaseModel):
    """
    Result of a vector store search operation containing full item data and similarity score.
    """

    item: VectorStoreItem
    score: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
