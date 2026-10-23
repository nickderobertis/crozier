

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_app_catalog_response_items_item_pairs_item import GetAppCatalogResponseItemsItemPairsItem
from .get_app_catalog_response_items_item_status import GetAppCatalogResponseItemsItemStatus


class GetAppCatalogResponseItemsItem(UniversalBaseModel):
    symbol: str
    name: str
    status: GetAppCatalogResponseItemsItemStatus
    label: str
    pairs: typing.List[GetAppCatalogResponseItemsItemPairsItem]
    markets_url: typing_extensions.Annotated[str, FieldMetadata(alias="marketsUrl"), pydantic.Field(alias="marketsUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
