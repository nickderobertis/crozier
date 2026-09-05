

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_discovery_endpoint import ApiDiscoveryEndpoint


class ApiDiscoveryEndpointFamilyResponse(UniversalBaseModel):
    api_discovery_endpoint: typing_extensions.Annotated[
        typing.Optional[ApiDiscoveryEndpoint],
        FieldMetadata(alias="ApiDiscoveryEndpoint"),
        pydantic.Field(alias="ApiDiscoveryEndpoint"),
    ] = None
    family_complete: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="FamilyComplete"),
        pydantic.Field(alias="FamilyComplete", description="Denotes a completed api family set"),
    ] = None
    """
    Denotes a completed api family set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
