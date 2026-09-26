

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_config_models_value_modalities_input_item import ProviderConfigModelsValueModalitiesInputItem
from .provider_config_models_value_modalities_output_item import ProviderConfigModelsValueModalitiesOutputItem


class ProviderConfigModelsValueModalities(UniversalBaseModel):
    input: typing.List[ProviderConfigModelsValueModalitiesInputItem]
    output: typing.List[ProviderConfigModelsValueModalitiesOutputItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
