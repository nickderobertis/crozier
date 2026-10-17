

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_project_addons_response_output_selected_addons_item_variant_price_interval import (
    ListProjectAddonsResponseOutputSelectedAddonsItemVariantPriceInterval,
)
from .list_project_addons_response_output_selected_addons_item_variant_price_type import (
    ListProjectAddonsResponseOutputSelectedAddonsItemVariantPriceType,
)


class ListProjectAddonsResponseOutputSelectedAddonsItemVariantPrice(UniversalBaseModel):
    description: str
    type: ListProjectAddonsResponseOutputSelectedAddonsItemVariantPriceType
    interval: ListProjectAddonsResponseOutputSelectedAddonsItemVariantPriceInterval
    amount: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
