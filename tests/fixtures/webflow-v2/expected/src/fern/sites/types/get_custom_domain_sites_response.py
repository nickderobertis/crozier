

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_custom_domain_sites_response_custom_domains_item import GetCustomDomainSitesResponseCustomDomainsItem


class GetCustomDomainSitesResponse(UniversalBaseModel):
    custom_domains: typing_extensions.Annotated[
        typing.Optional[typing.List[GetCustomDomainSitesResponseCustomDomainsItem]],
        FieldMetadata(alias="customDomains"),
        pydantic.Field(alias="customDomains"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
