

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry_provider_logo_data_paths_item import OcrModelCatalogEntryProviderLogoDataPathsItem


class OcrModelCatalogEntryProviderLogoData(UniversalBaseModel):
    title: str
    view_box: str
    paths: typing.List[OcrModelCatalogEntryProviderLogoDataPathsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
