

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_list_response_all_item_models_value import ProviderListResponseAllItemModelsValue


class ProviderListResponseAllItem(UniversalBaseModel):
    api: typing.Optional[str] = None
    name: str
    env: typing.List[str]
    id: str
    npm: typing.Optional[str] = None
    models: typing.Dict[str, ProviderListResponseAllItemModelsValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
