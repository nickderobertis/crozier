

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateStorageConfigBodyFeaturesVectorBuckets(UniversalBaseModel):
    enabled: bool
    max_buckets: typing_extensions.Annotated[int, FieldMetadata(alias="maxBuckets"), pydantic.Field(alias="maxBuckets")]
    max_indexes: typing_extensions.Annotated[int, FieldMetadata(alias="maxIndexes"), pydantic.Field(alias="maxIndexes")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
