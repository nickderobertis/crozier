

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry_availability import OcrModelCatalogEntryAvailability
from .ocr_model_catalog_entry_benchmark import OcrModelCatalogEntryBenchmark
from .ocr_model_catalog_entry_capabilities import OcrModelCatalogEntryCapabilities
from .ocr_model_catalog_entry_guidance import OcrModelCatalogEntryGuidance
from .ocr_model_catalog_entry_option_controls_item import OcrModelCatalogEntryOptionControlsItem
from .ocr_model_catalog_entry_pricing import OcrModelCatalogEntryPricing
from .ocr_model_catalog_entry_provider import OcrModelCatalogEntryProvider


class OcrModelCatalogEntry(UniversalBaseModel):
    """
    Public OCR model registry entry. `pricing.usd_per_page` is the
    customer retail page price at option defaults (`basis: customer_retail`).
    Optional `pricing.configurations` lists exact named retail totals for
    price-affecting option combinations — never additive surcharges.
    """

    id: str
    label: str
    is_default: bool
    provider: OcrModelCatalogEntryProvider
    guidance: OcrModelCatalogEntryGuidance
    benchmark: typing.Optional[OcrModelCatalogEntryBenchmark] = None
    output_summary: str
    capabilities: OcrModelCatalogEntryCapabilities
    option_defaults: typing.Dict[str, typing.Any]
    option_controls: typing.List[OcrModelCatalogEntryOptionControlsItem]
    pricing: OcrModelCatalogEntryPricing
    availability: OcrModelCatalogEntryAvailability

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
