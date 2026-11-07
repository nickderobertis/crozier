

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plan_resource_key_vault_properties import PlanResourceKeyVaultProperties


class PlanResourceEncryptionProperties(UniversalBaseModel):
    key_source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keySource"), pydantic.Field(alias="keySource")
    ] = None
    key_vault_properties: typing_extensions.Annotated[
        typing.Optional[PlanResourceKeyVaultProperties],
        FieldMetadata(alias="keyVaultProperties"),
        pydantic.Field(alias="keyVaultProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
