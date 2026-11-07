

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .core_ocs_get_capabilities200response_ocs_data_capabilities_ocm_resource_types_inner_protocols import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInnerProtocols,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInner(UniversalBaseModel):
    name: str
    share_types: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="shareTypes"), pydantic.Field(alias="shareTypes")
    ]
    protocols: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcmResourceTypesInnerProtocols

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
