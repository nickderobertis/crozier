

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret_keys_with_provider_provider import SecretKeysWithProviderProvider


class SecretKeysWithProvider(UniversalBaseModel):
    keys: typing.List[str]
    name: str
    provider: SecretKeysWithProviderProvider

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
