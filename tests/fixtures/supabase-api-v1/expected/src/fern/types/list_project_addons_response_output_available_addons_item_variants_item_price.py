

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_project_addons_response_output_available_addons_item_variants_item_price_interval import (
    ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceInterval,
)
from .list_project_addons_response_output_available_addons_item_variants_item_price_type import (
    ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceType,
)


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPrice(UniversalBaseModel):
    description: str
    type: ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceType
    interval: ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceInterval
    amount: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
