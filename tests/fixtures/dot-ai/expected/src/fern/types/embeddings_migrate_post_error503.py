

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embeddings_migrate_post_error503error import EmbeddingsMigratePostError503Error
from .embeddings_migrate_post_error503meta import EmbeddingsMigratePostError503Meta


class EmbeddingsMigratePostError503(UniversalBaseModel):
    success: bool
    error: EmbeddingsMigratePostError503Error
    meta: typing.Optional[EmbeddingsMigratePostError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
