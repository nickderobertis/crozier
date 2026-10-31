

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_llm_model_catalog_entry import OcrLlmModelCatalogEntry
from .ocr_llm_models_response_mode import OcrLlmModelsResponseMode


class OcrLlmModelsResponse(UniversalBaseModel):
    """
    Normalized OpenRouter LLM catalog for OpenParser extraction. Includes catalog version,
    stale flag, and pagination metadata for search mode.
    """

    mode: OcrLlmModelsResponseMode
    catalog_version: str
    fetched_at: dt.datetime
    stale: bool
    data: typing.List[OcrLlmModelCatalogEntry]
    page: int
    limit: int
    total: int
    has_more: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
