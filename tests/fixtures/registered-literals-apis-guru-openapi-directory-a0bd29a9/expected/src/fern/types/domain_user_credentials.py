

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DomainUserCredentials(UniversalBaseModel):
    domain: str
    organizational_unit: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organizationalUnit"), pydantic.Field(alias="organizationalUnit")
    ] = None
    password_secret_identifier: typing_extensions.Annotated[
        str, FieldMetadata(alias="passwordSecretIdentifier"), pydantic.Field(alias="passwordSecretIdentifier")
    ]
    user_name: typing_extensions.Annotated[str, FieldMetadata(alias="userName"), pydantic.Field(alias="userName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
