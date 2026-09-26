

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EmbeddingsMigratePostResponseDataSummary(UniversalBaseModel):
    total_collections: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalCollections"),
        pydantic.Field(alias="totalCollections", description="Total collections processed"),
    ]
    """
    Total collections processed
    """

    migrated: float = pydantic.Field()
    """
    Collections successfully migrated
    """

    skipped: float = pydantic.Field()
    """
    Collections skipped (dimensions already match)
    """

    failed: float = pydantic.Field()
    """
    Collections that failed to migrate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
