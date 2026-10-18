

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_storage_config_body_external_upstream_target import UpdateStorageConfigBodyExternalUpstreamTarget


class UpdateStorageConfigBodyExternal(UniversalBaseModel):
    upstream_target: typing_extensions.Annotated[
        UpdateStorageConfigBodyExternalUpstreamTarget,
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
