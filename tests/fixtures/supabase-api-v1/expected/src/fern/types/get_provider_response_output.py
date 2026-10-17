

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_provider_response_output_domains_item import GetProviderResponseOutputDomainsItem
from .get_provider_response_output_saml import GetProviderResponseOutputSaml


class GetProviderResponseOutput(UniversalBaseModel):
    id: str
    saml: typing.Optional[GetProviderResponseOutputSaml] = None
    domains: typing.Optional[typing.List[GetProviderResponseOutputDomainsItem]] = None
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
