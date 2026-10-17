

import typing

from .pinecone_vector_database_update_params import PineconeVectorDatabaseUpdateParams
from .undefined import Undefined

AgentUpdateParamsVectorDatabase = typing.Union[str, PineconeVectorDatabaseUpdateParams, Undefined]
