

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embeddings_migrate_post_error500error import EmbeddingsMigratePostError500Error
from .embeddings_migrate_post_error500meta import EmbeddingsMigratePostError500Meta


class EmbeddingsMigratePostError500(UniversalBaseModel):
    success: bool
    error: EmbeddingsMigratePostError500Error
    meta: typing.Optional[EmbeddingsMigratePostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
