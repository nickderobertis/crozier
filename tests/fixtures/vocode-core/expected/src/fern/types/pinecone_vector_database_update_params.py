

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pinecone_vector_database_update_params_api_environment import PineconeVectorDatabaseUpdateParamsApiEnvironment
from .pinecone_vector_database_update_params_api_key import PineconeVectorDatabaseUpdateParamsApiKey
from .pinecone_vector_database_update_params_index import PineconeVectorDatabaseUpdateParamsIndex
from .pinecone_vector_database_update_params_type import PineconeVectorDatabaseUpdateParamsType


class PineconeVectorDatabaseUpdateParams(UniversalBaseModel):
    type: PineconeVectorDatabaseUpdateParamsType
    index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = None
    api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = None
    api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
