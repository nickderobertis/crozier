

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_config_response_output_external_upstream_target import StorageConfigResponseOutputExternalUpstreamTarget


class StorageConfigResponseOutputExternal(UniversalBaseModel):
    upstream_target: typing_extensions.Annotated[
        StorageConfigResponseOutputExternalUpstreamTarget,
        FieldMetadata(alias="upstreamTarget"),
        pydantic.Field(alias="upstreamTarget"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
