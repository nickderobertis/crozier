

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry_pricing_basis import OcrModelCatalogEntryPricingBasis
from .ocr_model_catalog_entry_pricing_configurations_item import OcrModelCatalogEntryPricingConfigurationsItem


class OcrModelCatalogEntryPricing(UniversalBaseModel):
    usd_per_page: float
    basis: OcrModelCatalogEntryPricingBasis
    configurations: typing.Optional[typing.List[OcrModelCatalogEntryPricingConfigurationsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
