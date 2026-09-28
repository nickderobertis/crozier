

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embeddings_migrate_post_response_data_collections_item import EmbeddingsMigratePostResponseDataCollectionsItem
from .embeddings_migrate_post_response_data_summary import EmbeddingsMigratePostResponseDataSummary


class EmbeddingsMigratePostResponseData(UniversalBaseModel):
    collections: typing.List[EmbeddingsMigratePostResponseDataCollectionsItem] = pydantic.Field()
    """
    Per-collection results
    """

    summary: EmbeddingsMigratePostResponseDataSummary

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
