

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vanity_subdomain_config_response_output_status import VanitySubdomainConfigResponseOutputStatus


class VanitySubdomainConfigResponseOutput(UniversalBaseModel):
    status: VanitySubdomainConfigResponseOutputStatus
    custom_domain: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
