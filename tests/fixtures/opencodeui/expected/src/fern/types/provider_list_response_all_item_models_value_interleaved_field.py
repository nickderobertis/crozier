

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_list_response_all_item_models_value_interleaved_field_field import (
    ProviderListResponseAllItemModelsValueInterleavedFieldField,
)


class ProviderListResponseAllItemModelsValueInterleavedField(UniversalBaseModel):
    field: ProviderListResponseAllItemModelsValueInterleavedFieldField

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
