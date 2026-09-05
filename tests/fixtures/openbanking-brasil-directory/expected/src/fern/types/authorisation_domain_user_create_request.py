

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .contact_role_enum import ContactRoleEnum
from .system_enum import SystemEnum


class AuthorisationDomainUserCreateRequest(UniversalBaseModel):
    authorisation_domain_role: typing_extensions.Annotated[
        AuthorisationDomainRoleName,
        FieldMetadata(alias="AuthorisationDomainRole"),
        pydantic.Field(alias="AuthorisationDomainRole"),
    ]
    contact_role: typing_extensions.Annotated[
        ContactRoleEnum, FieldMetadata(alias="ContactRole"), pydantic.Field(alias="ContactRole")
    ]
    email: typing_extensions.Annotated[
        str, FieldMetadata(alias="Email"), pydantic.Field(alias="Email", description="The user email address")
    ]
    """
    The user email address
    """

    system: typing_extensions.Annotated[SystemEnum, FieldMetadata(alias="System"), pydantic.Field(alias="System")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
