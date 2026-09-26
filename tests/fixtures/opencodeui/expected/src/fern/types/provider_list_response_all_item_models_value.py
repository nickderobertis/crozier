

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_list_response_all_item_models_value_cost import ProviderListResponseAllItemModelsValueCost
from .provider_list_response_all_item_models_value_interleaved import ProviderListResponseAllItemModelsValueInterleaved
from .provider_list_response_all_item_models_value_limit import ProviderListResponseAllItemModelsValueLimit
from .provider_list_response_all_item_models_value_modalities import ProviderListResponseAllItemModelsValueModalities
from .provider_list_response_all_item_models_value_provider import ProviderListResponseAllItemModelsValueProvider
from .provider_list_response_all_item_models_value_status import ProviderListResponseAllItemModelsValueStatus


class ProviderListResponseAllItemModelsValue(UniversalBaseModel):
    id: str
    name: str
    family: typing.Optional[str] = None
    release_date: str
    attachment: bool
    reasoning: bool
    temperature: bool
    tool_call: bool
    interleaved: typing.Optional[ProviderListResponseAllItemModelsValueInterleaved] = None
    cost: typing.Optional[ProviderListResponseAllItemModelsValueCost] = None
    limit: ProviderListResponseAllItemModelsValueLimit
    modalities: typing.Optional[ProviderListResponseAllItemModelsValueModalities] = None
    experimental: typing.Optional[bool] = None
    status: typing.Optional[ProviderListResponseAllItemModelsValueStatus] = None
    options: typing.Dict[str, typing.Any]
    headers: typing.Optional[typing.Dict[str, str]] = None
    provider: typing.Optional[ProviderListResponseAllItemModelsValueProvider] = None
    variants: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
