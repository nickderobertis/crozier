

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_catalog_page_items_item_pairs_item import AppCatalogPageItemsItemPairsItem
from .app_catalog_page_items_item_status import AppCatalogPageItemsItemStatus


class AppCatalogPageItemsItem(UniversalBaseModel):
    symbol: str
    name: str
    status: AppCatalogPageItemsItemStatus
    label: str
    pairs: typing.List[AppCatalogPageItemsItemPairsItem]
    markets_url: typing_extensions.Annotated[str, FieldMetadata(alias="marketsUrl"), pydantic.Field(alias="marketsUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
