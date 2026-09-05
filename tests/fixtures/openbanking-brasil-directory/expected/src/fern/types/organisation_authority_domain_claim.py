

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .status_enum import StatusEnum


class OrganisationAuthorityDomainClaim(UniversalBaseModel):
    authorisation_domain_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainName"),
        pydantic.Field(alias="AuthorisationDomainName", description="The authorisation domain name"),
    ] = None
    """
    The authorisation domain name
    """

    authority_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityId"),
        pydantic.Field(alias="AuthorityId", description="The GUID of the Authority"),
    ] = None
    """
    The GUID of the Authority
    """

    authority_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityName"),
        pydantic.Field(alias="AuthorityName", description="The name of the Authority"),
    ] = None
    """
    The name of the Authority
    """

    organisation_authority_domain_claim_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrganisationAuthorityDomainClaimId"),
        pydantic.Field(
            alias="OrganisationAuthorityDomainClaimId", description="The unique org authority domain claim ID"
        ),
    ] = None
    """
    The unique org authority domain claim ID
    """

    registration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationId"),
        pydantic.Field(alias="RegistrationId", description="The registration ID"),
    ] = None
    """
    The registration ID
    """

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
