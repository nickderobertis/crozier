

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .core_ocs_get_capabilities200response_ocs_data_capabilities_ocm_resource_types_inner import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInner,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcm(UniversalBaseModel):
    enabled: bool
    api_version: typing_extensions.Annotated[str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")]
    end_point: typing_extensions.Annotated[str, FieldMetadata(alias="endPoint"), pydantic.Field(alias="endPoint")]
    resource_types: typing_extensions.Annotated[
        typing.List[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInner],
        FieldMetadata(alias="resourceTypes"),
        pydantic.Field(alias="resourceTypes"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
