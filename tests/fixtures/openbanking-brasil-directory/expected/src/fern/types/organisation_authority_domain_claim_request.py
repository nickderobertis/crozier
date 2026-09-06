

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganisationAuthorityDomainClaimRequest(UniversalBaseModel):
    authorisation_domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorisationDomainName"),
        pydantic.Field(alias="AuthorisationDomainName", description="The authorisation domain name"),
    ]
    """
    The authorisation domain name
    """

    authority_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="AuthorityId"), pydantic.Field(alias="AuthorityId", description="The Authority ID")
    ]
    """
    The Authority ID
    """

    registration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RegistrationId"),
        pydantic.Field(alias="RegistrationId", description="The registration ID"),
    ] = None
    """
    The registration ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
