

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .provider_list_response_all_item_models_value_cost_context_over200k import (
    ProviderListResponseAllItemModelsValueCostContextOver200K,
)


class ProviderListResponseAllItemModelsValueCost(UniversalBaseModel):
    input: float
    output: float
    cache_read: typing.Optional[float] = None
    cache_write: typing.Optional[float] = None
    context_over200k: typing_extensions.Annotated[
        typing.Optional[ProviderListResponseAllItemModelsValueCostContextOver200K],
        FieldMetadata(alias="context_over_200k"),
        pydantic.Field(alias="context_over_200k"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
