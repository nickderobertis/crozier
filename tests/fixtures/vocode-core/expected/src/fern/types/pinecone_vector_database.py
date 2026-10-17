

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pinecone_vector_database_type import PineconeVectorDatabaseType


class PineconeVectorDatabase(UniversalBaseModel):
    id: str
    user_id: str
    type: PineconeVectorDatabaseType
    index: str
    api_key: str
    api_environment: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
