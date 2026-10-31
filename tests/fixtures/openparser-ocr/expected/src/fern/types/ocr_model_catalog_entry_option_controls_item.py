

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_model_catalog_entry_option_controls_item_choices_item import OcrModelCatalogEntryOptionControlsItemChoicesItem
from .ocr_model_catalog_entry_option_controls_item_kind import OcrModelCatalogEntryOptionControlsItemKind


class OcrModelCatalogEntryOptionControlsItem(UniversalBaseModel):
    key: str
    label: str
    summary: str
    kind: OcrModelCatalogEntryOptionControlsItemKind
    choices: typing.Optional[typing.List[OcrModelCatalogEntryOptionControlsItemChoicesItem]] = None
    placeholder: typing.Optional[str] = None
    nullable_sentinel: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
