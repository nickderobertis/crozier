

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .azure_location import AzureLocation


class VsoPlanInfo(UniversalBaseModel):
    location: typing.Optional[AzureLocation] = None
    name: typing.Optional[str] = None
    provider_namespace: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="providerNamespace"), pydantic.Field(alias="providerNamespace")
    ] = None
    resource_group: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceGroup"), pydantic.Field(alias="resourceGroup")
    ] = None
    resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    subscription: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
