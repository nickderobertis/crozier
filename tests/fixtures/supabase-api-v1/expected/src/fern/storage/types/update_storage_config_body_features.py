

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_storage_config_body_features_iceberg_catalog import UpdateStorageConfigBodyFeaturesIcebergCatalog
from .update_storage_config_body_features_image_transformation import UpdateStorageConfigBodyFeaturesImageTransformation
from .update_storage_config_body_features_purge_cache import UpdateStorageConfigBodyFeaturesPurgeCache
from .update_storage_config_body_features_s3protocol import UpdateStorageConfigBodyFeaturesS3Protocol
from .update_storage_config_body_features_vector_buckets import UpdateStorageConfigBodyFeaturesVectorBuckets


class UpdateStorageConfigBodyFeatures(UniversalBaseModel):
    image_transformation: typing_extensions.Annotated[
        typing.Optional[UpdateStorageConfigBodyFeaturesImageTransformation],
        FieldMetadata(alias="imageTransformation"),
        pydantic.Field(alias="imageTransformation"),
    ] = None
    s3protocol: typing_extensions.Annotated[
        typing.Optional[UpdateStorageConfigBodyFeaturesS3Protocol],
        FieldMetadata(alias="s3Protocol"),
        pydantic.Field(alias="s3Protocol"),
    ] = None
    purge_cache: typing_extensions.Annotated[
        typing.Optional[UpdateStorageConfigBodyFeaturesPurgeCache],
        FieldMetadata(alias="purgeCache"),
        pydantic.Field(alias="purgeCache"),
    ] = None
    iceberg_catalog: typing_extensions.Annotated[
        typing.Optional[UpdateStorageConfigBodyFeaturesIcebergCatalog],
        FieldMetadata(alias="icebergCatalog"),
        pydantic.Field(alias="icebergCatalog"),
    ] = None
    vector_buckets: typing_extensions.Annotated[
        typing.Optional[UpdateStorageConfigBodyFeaturesVectorBuckets],
        FieldMetadata(alias="vectorBuckets"),
        pydantic.Field(alias="vectorBuckets"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
