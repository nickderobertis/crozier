

import typing

from .ocr_model_catalog_entry_pricing_configurations_item_options_value_one import (
    OcrModelCatalogEntryPricingConfigurationsItemOptionsValueOne,
)
from .ocr_model_catalog_entry_pricing_configurations_item_options_value_two import (
    OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo,
)

OcrModelCatalogEntryPricingConfigurationsItemOptionsValue = typing.Union[
    bool,
    OcrModelCatalogEntryPricingConfigurationsItemOptionsValueOne,
    OcrModelCatalogEntryPricingConfigurationsItemOptionsValueTwo,
]
