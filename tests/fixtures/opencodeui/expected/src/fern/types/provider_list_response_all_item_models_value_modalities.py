

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_list_response_all_item_models_value_modalities_input_item import (
    ProviderListResponseAllItemModelsValueModalitiesInputItem,
)
from .provider_list_response_all_item_models_value_modalities_output_item import (
    ProviderListResponseAllItemModelsValueModalitiesOutputItem,
)


class ProviderListResponseAllItemModelsValueModalities(UniversalBaseModel):
    input: typing.List[ProviderListResponseAllItemModelsValueModalitiesInputItem]
    output: typing.List[ProviderListResponseAllItemModelsValueModalitiesOutputItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
