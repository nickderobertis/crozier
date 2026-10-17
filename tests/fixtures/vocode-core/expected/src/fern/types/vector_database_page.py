

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pinecone_vector_database import PineconeVectorDatabase


class VectorDatabasePage(UniversalBaseModel):
    items: typing.List[PineconeVectorDatabase]
    page: int
    size: int
    has_more: bool
    total: int
    total_is_estimated: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
