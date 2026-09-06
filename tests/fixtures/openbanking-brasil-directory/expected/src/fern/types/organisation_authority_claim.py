

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .authority_id import AuthorityId
from .organisation_authority_claim_authorisations_item import OrganisationAuthorityClaimAuthorisationsItem
from .organisation_authority_claim_id import OrganisationAuthorityClaimId
from .organisation_id import OrganisationId
from .status_enum import StatusEnum


class OrganisationAuthorityClaim(UniversalBaseModel):
    authorisation_domain: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomain"),
        pydantic.Field(alias="AuthorisationDomain", description="Authorisation Domain for the authority"),
    ] = None
    """
    Authorisation Domain for the authority
    """

    authorisations: typing_extensions.Annotated[
        typing.Optional[typing.List[OrganisationAuthorityClaimAuthorisationsItem]],
        FieldMetadata(alias="Authorisations"),
        pydantic.Field(alias="Authorisations"),
    ] = None
    authority_id: typing_extensions.Annotated[
        typing.Optional[AuthorityId], FieldMetadata(alias="AuthorityId"), pydantic.Field(alias="AuthorityId")
    ] = None
    organisation_authority_claim_id: typing_extensions.Annotated[
        typing.Optional[OrganisationAuthorityClaimId],
        FieldMetadata(alias="OrganisationAuthorityClaimId"),
        pydantic.Field(alias="OrganisationAuthorityClaimId"),
    ] = None
    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None
    registration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationId"),
        pydantic.Field(alias="RegistrationId", description="Registration ID for the organisation"),
    ] = None
    """
    Registration ID for the organisation
    """

    role: typing_extensions.Annotated[
        typing.Optional[AuthorisationDomainRoleName], FieldMetadata(alias="Role"), pydantic.Field(alias="Role")
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
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
