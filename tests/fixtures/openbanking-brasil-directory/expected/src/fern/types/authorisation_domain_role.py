

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .status_enum import StatusEnum


class AuthorisationDomainRole(UniversalBaseModel):
    authorisation_domain_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainName"),
        pydantic.Field(alias="AuthorisationDomainName", description="The authorisation domain name"),
    ] = None
    """
    The authorisation domain name
    """

    authorisation_domain_role_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainRoleDescription"),
        pydantic.Field(
            alias="AuthorisationDomainRoleDescription", description="The authorisation domain role description"
        ),
    ] = None
    """
    The authorisation domain role description
    """

    authorisation_domain_role_name: typing_extensions.Annotated[
        typing.Optional[AuthorisationDomainRoleName],
        FieldMetadata(alias="AuthorisationDomainRoleName"),
        pydantic.Field(alias="AuthorisationDomainRoleName"),
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
