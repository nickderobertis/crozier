

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .status_enum import StatusEnum


class AuthorityAuthorisationDomain(UniversalBaseModel):
    authorisation_domain_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainName"),
        pydantic.Field(alias="AuthorisationDomainName", description="The authorisation domain name"),
    ] = None
    """
    The authorisation domain name
    """

    authority_authorisation_domain_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityAuthorisationDomainId"),
        pydantic.Field(alias="AuthorityAuthorisationDomainId", description="The GUID of the Authority-Domain mapping"),
    ] = None
    """
    The GUID of the Authority-Domain mapping
    """

    authority_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityId"),
        pydantic.Field(alias="AuthorityId", description="The GUID of the Authority"),
    ] = None
    """
    The GUID of the Authority
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
