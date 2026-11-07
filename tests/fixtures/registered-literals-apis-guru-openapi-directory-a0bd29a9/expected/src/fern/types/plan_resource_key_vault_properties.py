

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PlanResourceKeyVaultProperties(UniversalBaseModel):
    key_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keyName"), pydantic.Field(alias="keyName")
    ] = None
    key_vault_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keyVaultUri"), pydantic.Field(alias="keyVaultUri")
    ] = None
    key_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="keyVersion"), pydantic.Field(alias="keyVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
