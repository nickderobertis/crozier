

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organisation_id import OrganisationId
from .organisation_roles_org_domain_claims_item import OrganisationRolesOrgDomainClaimsItem
from .organisation_roles_org_domain_role_claims_item import OrganisationRolesOrgDomainRoleClaimsItem
from .organisation_roles_status import OrganisationRolesStatus


class OrganisationRoles(UniversalBaseModel):
    org_domain_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[OrganisationRolesOrgDomainClaimsItem]],
        FieldMetadata(alias="OrgDomainClaims"),
        pydantic.Field(alias="OrgDomainClaims"),
    ] = None
    org_domain_role_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[OrganisationRolesOrgDomainRoleClaimsItem]],
        FieldMetadata(alias="OrgDomainRoleClaims"),
        pydantic.Field(alias="OrgDomainRoleClaims"),
    ] = None
    organisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationId], FieldMetadata(alias="OrganisationId"), pydantic.Field(alias="OrganisationId")
    ] = None
    parent_organisation_reference: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ParentOrganisationReference"),
        pydantic.Field(alias="ParentOrganisationReference", description="Parent Organisation Reference"),
    ] = None
    """
    Parent Organisation Reference
    """

    registered_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="RegisteredName"), pydantic.Field(alias="RegisteredName")
    ] = None
    registration_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationNumber"),
        pydantic.Field(
            alias="RegistrationNumber",
            description="Company registration number from company register i.e. Companies House registration number",
        ),
    ] = None
    """
    Company registration number from company register i.e. Companies House registration number
    """

    status: typing_extensions.Annotated[
        typing.Optional[OrganisationRolesStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="Status of the directory registration of an organisation"),
    ] = None
    """
    Status of the directory registration of an organisation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
