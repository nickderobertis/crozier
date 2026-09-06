

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .status_enum import StatusEnum


class AuthorisationDomain(UniversalBaseModel):
    authorisation_domain_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainDescription"),
        pydantic.Field(alias="AuthorisationDomainDescription", description="The authorisation domain description"),
    ] = None
    """
    The authorisation domain description
    """

    authorisation_domain_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainName"),
        pydantic.Field(alias="AuthorisationDomainName", description="The authorisation domain name"),
    ] = None
    """
    The authorisation domain name
    """

    authorisation_domain_region: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorisationDomainRegion"),
        pydantic.Field(alias="AuthorisationDomainRegion", description="The authorisation domain region"),
    ] = None
    """
    The authorisation domain region
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
