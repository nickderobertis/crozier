

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organisation_authorisation_id import OrganisationAuthorisationId
from .organisation_authority_claim_id import OrganisationAuthorityClaimId
from .status_enum import StatusEnum


class OrganisationAuthorityClaimAuthorisation(UniversalBaseModel):
    member_state: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MemberState"),
        pydantic.Field(alias="MemberState", description="Abbreviated states information i.e. GB, IE, NL etc"),
    ] = None
    """
    Abbreviated states information i.e. GB, IE, NL etc
    """

    organisation_authorisation_id: typing_extensions.Annotated[
        typing.Optional[OrganisationAuthorisationId],
        FieldMetadata(alias="OrganisationAuthorisationId"),
        pydantic.Field(alias="OrganisationAuthorisationId"),
    ] = None
    organisation_authority_claim_id: typing_extensions.Annotated[
        typing.Optional[OrganisationAuthorityClaimId],
        FieldMetadata(alias="OrganisationAuthorityClaimId"),
        pydantic.Field(alias="OrganisationAuthorityClaimId"),
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
