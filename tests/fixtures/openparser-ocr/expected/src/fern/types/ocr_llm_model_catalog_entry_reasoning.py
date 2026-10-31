

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_llm_model_catalog_entry_reasoning_default_effort import OcrLlmModelCatalogEntryReasoningDefaultEffort
from .ocr_llm_model_catalog_entry_reasoning_supported_efforts_item import (
    OcrLlmModelCatalogEntryReasoningSupportedEffortsItem,
)


class OcrLlmModelCatalogEntryReasoning(UniversalBaseModel):
    supported_efforts: typing.Optional[typing.List[OcrLlmModelCatalogEntryReasoningSupportedEffortsItem]] = None
    default_effort: typing.Optional[OcrLlmModelCatalogEntryReasoningDefaultEffort] = None
    mandatory: bool
    supports_max_tokens: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
