

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .contact_role_enum import ContactRoleEnum
from .status_enum import StatusEnum
from .system_enum import SystemEnum


class AuthorisationDomainUser(UniversalBaseModel):
    authorisation_domain: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomain"),
        pydantic.Field(alias="AuthorisationDomain", description="The authorisation domain for this user"),
    ] = None
    """
    The authorisation domain for this user
    """

    authorisation_domain_role: typing_extensions.Annotated[
        typing.Optional[AuthorisationDomainRoleName],
        FieldMetadata(alias="AuthorisationDomainRole"),
        pydantic.Field(alias="AuthorisationDomainRole"),
    ] = None
    authorisation_domain_user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainUserId"),
        pydantic.Field(alias="AuthorisationDomainUserId", description="Unique record ID"),
    ] = None
    """
    Unique record ID
    """

    contact_role: typing_extensions.Annotated[
        typing.Optional[ContactRoleEnum], FieldMetadata(alias="ContactRole"), pydantic.Field(alias="ContactRole")
    ] = None
    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="The user email address"),
    ] = None
    """
    The user email address
    """

    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    system: typing_extensions.Annotated[
        typing.Optional[SystemEnum], FieldMetadata(alias="System"), pydantic.Field(alias="System")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
