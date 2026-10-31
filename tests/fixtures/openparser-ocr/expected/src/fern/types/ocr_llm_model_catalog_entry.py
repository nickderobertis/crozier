

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_llm_model_catalog_entry_pricing import OcrLlmModelCatalogEntryPricing
from .ocr_llm_model_catalog_entry_reasoning import OcrLlmModelCatalogEntryReasoning
from .ocr_llm_model_catalog_entry_recommendation import OcrLlmModelCatalogEntryRecommendation


class OcrLlmModelCatalogEntry(UniversalBaseModel):
    """
    One compatible extraction LLM. `recommendation` is `suggested` or `compatible`.
    `certified_grounding` / `certified_suggest` mark Eigenpal-tested quality tiers;
    `supports_grounding` is true for every compatible model while `supports_suggest`
    matches certification. `pricing` is customer retail USD per 1M tokens
    (`basis: customer_retail`) — the rates customers are charged, not raw provider list cost.
    """

    id: str
    label: str
    provider: str
    created_at: typing.Optional[dt.datetime] = None
    context_length: typing.Optional[int] = None
    recommendation: OcrLlmModelCatalogEntryRecommendation
    is_default: bool
    certified_grounding: bool
    certified_suggest: bool
    supports_grounding: bool
    supports_suggest: bool
    pricing_known: bool
    reasoning: typing.Optional[OcrLlmModelCatalogEntryReasoning] = None
    deprecated_at: typing.Optional[dt.datetime] = None
    pricing: OcrLlmModelCatalogEntryPricing

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
