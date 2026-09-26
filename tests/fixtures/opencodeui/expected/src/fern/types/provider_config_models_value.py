

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_config_models_value_cost import ProviderConfigModelsValueCost
from .provider_config_models_value_interleaved import ProviderConfigModelsValueInterleaved
from .provider_config_models_value_limit import ProviderConfigModelsValueLimit
from .provider_config_models_value_modalities import ProviderConfigModelsValueModalities
from .provider_config_models_value_provider import ProviderConfigModelsValueProvider
from .provider_config_models_value_status import ProviderConfigModelsValueStatus
from .provider_config_models_value_variants_value import ProviderConfigModelsValueVariantsValue


class ProviderConfigModelsValue(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    family: typing.Optional[str] = None
    release_date: typing.Optional[str] = None
    attachment: typing.Optional[bool] = None
    reasoning: typing.Optional[bool] = None
    temperature: typing.Optional[bool] = None
    tool_call: typing.Optional[bool] = None
    interleaved: typing.Optional[ProviderConfigModelsValueInterleaved] = None
    cost: typing.Optional[ProviderConfigModelsValueCost] = None
    limit: typing.Optional[ProviderConfigModelsValueLimit] = None
    modalities: typing.Optional[ProviderConfigModelsValueModalities] = None
    experimental: typing.Optional[bool] = None
    status: typing.Optional[ProviderConfigModelsValueStatus] = None
    options: typing.Optional[typing.Dict[str, typing.Any]] = None
    headers: typing.Optional[typing.Dict[str, str]] = None
    provider: typing.Optional[ProviderConfigModelsValueProvider] = None
    variants: typing.Optional[typing.Dict[str, ProviderConfigModelsValueVariantsValue]] = pydantic.Field(default=None)
    """
    Variant-specific configuration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
