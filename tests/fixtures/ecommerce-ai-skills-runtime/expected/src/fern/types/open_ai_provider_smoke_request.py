

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_provider_smoke_request_provider import OpenAiProviderSmokeRequestProvider


class OpenAiProviderSmokeRequest(UniversalBaseModel):
    provider: OpenAiProviderSmokeRequestProvider

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
