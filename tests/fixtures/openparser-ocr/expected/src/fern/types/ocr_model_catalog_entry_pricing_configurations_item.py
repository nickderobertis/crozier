

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry_pricing_configurations_item_options_value import (
    OcrModelCatalogEntryPricingConfigurationsItemOptionsValue,
)


class OcrModelCatalogEntryPricingConfigurationsItem(UniversalBaseModel):
    label: str
    usd_per_page: float
    options: typing.Dict[str, OcrModelCatalogEntryPricingConfigurationsItemOptionsValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
