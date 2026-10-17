

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_provider_response_output_domains_item import CreateProviderResponseOutputDomainsItem
from .create_provider_response_output_saml import CreateProviderResponseOutputSaml


class CreateProviderResponseOutput(UniversalBaseModel):
    id: str
    saml: typing.Optional[CreateProviderResponseOutputSaml] = None
    domains: typing.Optional[typing.List[CreateProviderResponseOutputDomainsItem]] = None
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
