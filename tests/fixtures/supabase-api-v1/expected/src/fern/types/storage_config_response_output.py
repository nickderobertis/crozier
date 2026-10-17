

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_config_response_output_capabilities import StorageConfigResponseOutputCapabilities
from .storage_config_response_output_external import StorageConfigResponseOutputExternal
from .storage_config_response_output_features import StorageConfigResponseOutputFeatures


class StorageConfigResponseOutput(UniversalBaseModel):
    file_size_limit: typing_extensions.Annotated[
        int, FieldMetadata(alias="fileSizeLimit"), pydantic.Field(alias="fileSizeLimit")
    ]
    features: StorageConfigResponseOutputFeatures
    capabilities: StorageConfigResponseOutputCapabilities
    external: StorageConfigResponseOutputExternal
    migration_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="migrationVersion"), pydantic.Field(alias="migrationVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
