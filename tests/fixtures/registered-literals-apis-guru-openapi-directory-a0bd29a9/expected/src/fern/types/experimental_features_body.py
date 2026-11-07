

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExperimentalFeaturesBody(UniversalBaseModel):
    enable_dynamic_https_detection: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="enableDynamicHttpsDetection"),
        pydantic.Field(alias="enableDynamicHttpsDetection"),
    ] = None
    queue_resource_allocation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="queueResourceAllocation"),
        pydantic.Field(alias="queueResourceAllocation"),
    ] = None
    use_prebuild_fast_path_if_available: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="usePrebuildFastPathIfAvailable"),
        pydantic.Field(alias="usePrebuildFastPathIfAvailable"),
    ] = None
    use_prebuilt_images: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="usePrebuiltImages"), pydantic.Field(alias="usePrebuiltImages")
    ] = None
    use_storage_v2: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="useStorageV2"), pydantic.Field(alias="useStorageV2")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
