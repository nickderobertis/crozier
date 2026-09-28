

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .embeddings_migrate_post_response_data_collections_item_status import (
    EmbeddingsMigratePostResponseDataCollectionsItemStatus,
)


class EmbeddingsMigratePostResponseDataCollectionsItem(UniversalBaseModel):
    collection: str = pydantic.Field()
    """
    Collection name
    """

    status: EmbeddingsMigratePostResponseDataCollectionsItemStatus = pydantic.Field()
    """
    Migration outcome
    """

    previous_dimensions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="previousDimensions"),
        pydantic.Field(alias="previousDimensions", description="Vector dimensions before migration"),
    ]
    """
    Vector dimensions before migration
    """

    new_dimensions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="newDimensions"),
        pydantic.Field(alias="newDimensions", description="Vector dimensions after migration"),
    ]
    """
    Vector dimensions after migration
    """

    total: float = pydantic.Field()
    """
    Total points in the collection
    """

    processed: float = pydantic.Field()
    """
    Points successfully re-embedded
    """

    failed: float = pydantic.Field()
    """
    Points that failed to re-embed
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message if migration failed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
