

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embeddings_migrate_post_response_data import EmbeddingsMigratePostResponseData
from .embeddings_migrate_post_response_meta import EmbeddingsMigratePostResponseMeta


class EmbeddingsMigratePostResponse(UniversalBaseModel):
    success: bool
    data: EmbeddingsMigratePostResponseData
    meta: typing.Optional[EmbeddingsMigratePostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
