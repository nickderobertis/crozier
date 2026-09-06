

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .software_authority_claim_id import SoftwareAuthorityClaimId
from .software_statement_id import SoftwareStatementId
from .status_enum import StatusEnum


class SoftwareAuthorityClaim(UniversalBaseModel):
    authorisation_domain: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomain"),
        pydantic.Field(alias="AuthorisationDomain", description="Authorisation domain for the authority"),
    ] = None
    """
    Authorisation domain for the authority
    """

    role: typing_extensions.Annotated[
        typing.Optional[AuthorisationDomainRoleName], FieldMetadata(alias="Role"), pydantic.Field(alias="Role")
    ] = None
    software_authority_claim_id: typing_extensions.Annotated[
        typing.Optional[SoftwareAuthorityClaimId],
        FieldMetadata(alias="SoftwareAuthorityClaimId"),
        pydantic.Field(alias="SoftwareAuthorityClaimId"),
    ] = None
    software_statement_id: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementId],
        FieldMetadata(alias="SoftwareStatementId"),
        pydantic.Field(alias="SoftwareStatementId"),
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
