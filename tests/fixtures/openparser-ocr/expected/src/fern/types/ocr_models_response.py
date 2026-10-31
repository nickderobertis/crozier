

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry import OcrModelCatalogEntry


class OcrModelsResponse(UniversalBaseModel):
    """
    OCR model discovery response for `GET /models/ocr`.
    """

    data: typing.List[OcrModelCatalogEntry]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
