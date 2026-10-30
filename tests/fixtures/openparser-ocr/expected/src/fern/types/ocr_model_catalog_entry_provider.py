

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry_provider_logo_data import OcrModelCatalogEntryProviderLogoData


class OcrModelCatalogEntryProvider(UniversalBaseModel):
    key: str
    label: str
    logo: typing.Optional[str] = None
    logo_data: typing.Optional[OcrModelCatalogEntryProviderLogoData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
