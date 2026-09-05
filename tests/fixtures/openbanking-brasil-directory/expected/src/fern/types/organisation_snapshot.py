

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_servers import AuthorisationServers
from .certificates_or_keys import CertificatesOrKeys
from .contacts import Contacts
from .organisation import Organisation
from .organisation_authority_claims import OrganisationAuthorityClaims
from .organisation_authority_domain_claims import OrganisationAuthorityDomainClaims
from .organisation_snapshot_software_statements_value import OrganisationSnapshotSoftwareStatementsValue


class OrganisationSnapshot(UniversalBaseModel):
    authorisation_servers: typing_extensions.Annotated[
        typing.Optional[AuthorisationServers],
        FieldMetadata(alias="AuthorisationServers"),
        pydantic.Field(alias="AuthorisationServers"),
    ] = None
    contacts: typing_extensions.Annotated[
        typing.Optional[Contacts], FieldMetadata(alias="Contacts"), pydantic.Field(alias="Contacts")
    ] = None
    org_domain_claims: typing_extensions.Annotated[
        typing.Optional[OrganisationAuthorityDomainClaims],
        FieldMetadata(alias="OrgDomainClaims"),
        pydantic.Field(alias="OrgDomainClaims"),
    ] = None
    org_domain_role_claims: typing_extensions.Annotated[
        typing.Optional[OrganisationAuthorityClaims],
        FieldMetadata(alias="OrgDomainRoleClaims"),
        pydantic.Field(alias="OrgDomainRoleClaims"),
    ] = None
    organisation_certificates: typing_extensions.Annotated[
        typing.Optional[CertificatesOrKeys],
        FieldMetadata(alias="OrganisationCertificates"),
        pydantic.Field(alias="OrganisationCertificates"),
    ] = None
    organisation_details: typing_extensions.Annotated[
        typing.Optional[Organisation],
        FieldMetadata(alias="OrganisationDetails"),
        pydantic.Field(alias="OrganisationDetails"),
    ] = None
    software_statements: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, OrganisationSnapshotSoftwareStatementsValue]],
        FieldMetadata(alias="SoftwareStatements"),
        pydantic.Field(alias="SoftwareStatements"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
