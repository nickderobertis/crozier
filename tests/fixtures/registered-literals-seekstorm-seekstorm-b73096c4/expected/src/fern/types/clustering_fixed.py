

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClusteringFixed(UniversalBaseModel):
    """
    Set the number of clusters to a fixed value per level and shard.
    """

    fixed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Fixed"),
        pydantic.Field(alias="Fixed", description="Set the number of clusters to a fixed value per level and shard."),
    ]
    """
    Set the number of clusters to a fixed value per level and shard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
