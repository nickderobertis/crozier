

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_config_response_output_features_iceberg_catalog import StorageConfigResponseOutputFeaturesIcebergCatalog
from .storage_config_response_output_features_image_transformation import (
    StorageConfigResponseOutputFeaturesImageTransformation,
)
from .storage_config_response_output_features_purge_cache import StorageConfigResponseOutputFeaturesPurgeCache
from .storage_config_response_output_features_s3protocol import StorageConfigResponseOutputFeaturesS3Protocol
from .storage_config_response_output_features_vector_buckets import StorageConfigResponseOutputFeaturesVectorBuckets


class StorageConfigResponseOutputFeatures(UniversalBaseModel):
    image_transformation: typing_extensions.Annotated[
        StorageConfigResponseOutputFeaturesImageTransformation,
        FieldMetadata(alias="imageTransformation"),
        pydantic.Field(alias="imageTransformation"),
    ]
    s3protocol: typing_extensions.Annotated[
        StorageConfigResponseOutputFeaturesS3Protocol,
        FieldMetadata(alias="s3Protocol"),
        pydantic.Field(alias="s3Protocol"),
    ]
    purge_cache: typing_extensions.Annotated[
        StorageConfigResponseOutputFeaturesPurgeCache,
        FieldMetadata(alias="purgeCache"),
        pydantic.Field(alias="purgeCache"),
    ]
    iceberg_catalog: typing_extensions.Annotated[
        StorageConfigResponseOutputFeaturesIcebergCatalog,
        FieldMetadata(alias="icebergCatalog"),
        pydantic.Field(alias="icebergCatalog"),
    ]
    vector_buckets: typing_extensions.Annotated[
        StorageConfigResponseOutputFeaturesVectorBuckets,
        FieldMetadata(alias="vectorBuckets"),
        pydantic.Field(alias="vectorBuckets"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
