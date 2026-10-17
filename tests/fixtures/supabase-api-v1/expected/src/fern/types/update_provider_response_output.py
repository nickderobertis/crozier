

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_provider_response_output_domains_item import UpdateProviderResponseOutputDomainsItem
from .update_provider_response_output_saml import UpdateProviderResponseOutputSaml


class UpdateProviderResponseOutput(UniversalBaseModel):
    id: str
    saml: typing.Optional[UpdateProviderResponseOutputSaml] = None
    domains: typing.Optional[typing.List[UpdateProviderResponseOutputDomainsItem]] = None
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
