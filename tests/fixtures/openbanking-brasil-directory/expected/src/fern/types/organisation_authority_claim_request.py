

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .authority_id import AuthorityId
from .status_enum import StatusEnum


class OrganisationAuthorityClaimRequest(UniversalBaseModel):
    authorisation_domain: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorisationDomain"),
        pydantic.Field(alias="AuthorisationDomain", description="Authorisation domain for the authority"),
    ]
    """
    Authorisation domain for the authority
    """

    authority_id: typing_extensions.Annotated[
        AuthorityId, FieldMetadata(alias="AuthorityId"), pydantic.Field(alias="AuthorityId")
    ]
    registration_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="RegistrationId"),
        pydantic.Field(alias="RegistrationId", description="Registration ID for the organisation"),
    ]
    """
    Registration ID for the organisation
    """

    role: typing_extensions.Annotated[
        AuthorisationDomainRoleName, FieldMetadata(alias="Role"), pydantic.Field(alias="Role")
    ]
    status: typing_extensions.Annotated[StatusEnum, FieldMetadata(alias="Status"), pydantic.Field(alias="Status")]
    unique_technical_idenifier: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="UniqueTechnicalIdenifier"),
        pydantic.Field(alias="UniqueTechnicalIdenifier"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
