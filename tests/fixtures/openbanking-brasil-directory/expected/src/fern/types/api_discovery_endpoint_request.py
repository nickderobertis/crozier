

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_endpoint import ApiEndpoint


class ApiDiscoveryEndpointRequest(UniversalBaseModel):
    api_endpoint: typing_extensions.Annotated[
        typing.Optional[ApiEndpoint], FieldMetadata(alias="ApiEndpoint"), pydantic.Field(alias="ApiEndpoint")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
