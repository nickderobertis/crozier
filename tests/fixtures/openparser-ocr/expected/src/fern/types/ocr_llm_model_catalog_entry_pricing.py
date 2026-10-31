

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ocr_llm_model_catalog_entry_pricing_basis import OcrLlmModelCatalogEntryPricingBasis


class OcrLlmModelCatalogEntryPricing(UniversalBaseModel):
    prompt_usd_per1m: typing_extensions.Annotated[
        float, FieldMetadata(alias="prompt_usd_per_1m"), pydantic.Field(alias="prompt_usd_per_1m")
    ]
    completion_usd_per1m: typing_extensions.Annotated[
        float, FieldMetadata(alias="completion_usd_per_1m"), pydantic.Field(alias="completion_usd_per_1m")
    ]
    basis: OcrLlmModelCatalogEntryPricingBasis

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
