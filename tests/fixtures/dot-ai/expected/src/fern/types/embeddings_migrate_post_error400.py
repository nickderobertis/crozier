

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embeddings_migrate_post_error400error import EmbeddingsMigratePostError400Error
from .embeddings_migrate_post_error400meta import EmbeddingsMigratePostError400Meta


class EmbeddingsMigratePostError400(UniversalBaseModel):
    success: bool
    error: EmbeddingsMigratePostError400Error
    meta: typing.Optional[EmbeddingsMigratePostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
