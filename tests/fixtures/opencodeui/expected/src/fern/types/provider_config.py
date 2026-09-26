

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_config_models_value import ProviderConfigModelsValue
from .provider_config_options import ProviderConfigOptions


class ProviderConfig(UniversalBaseModel):
    api: typing.Optional[str] = None
    name: typing.Optional[str] = None
    env: typing.Optional[typing.List[str]] = None
    id: typing.Optional[str] = None
    npm: typing.Optional[str] = None
    models: typing.Optional[typing.Dict[str, ProviderConfigModelsValue]] = None
    whitelist: typing.Optional[typing.List[str]] = None
    blacklist: typing.Optional[typing.List[str]] = None
    options: typing.Optional[ProviderConfigOptions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
