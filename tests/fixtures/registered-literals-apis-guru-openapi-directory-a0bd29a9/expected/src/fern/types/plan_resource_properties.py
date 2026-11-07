

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plan_resource_encryption_properties import PlanResourceEncryptionProperties
from .vnet_properties import VnetProperties


class PlanResourceProperties(UniversalBaseModel):
    default_codespace_sku: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="defaultCodespaceSku"), pydantic.Field(alias="defaultCodespaceSku")
    ] = None
    default_environment_sku: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="defaultEnvironmentSku"),
        pydantic.Field(alias="defaultEnvironmentSku"),
    ] = None
    encryption: typing.Optional[PlanResourceEncryptionProperties] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    vnet_properties: typing_extensions.Annotated[
        typing.Optional[VnetProperties], FieldMetadata(alias="vnetProperties"), pydantic.Field(alias="vnetProperties")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
