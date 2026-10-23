

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_unavailable_error_body_items_item_pairs_item import ServiceUnavailableErrorBodyItemsItemPairsItem
from .service_unavailable_error_body_items_item_status import ServiceUnavailableErrorBodyItemsItemStatus


class ServiceUnavailableErrorBodyItemsItem(UniversalBaseModel):
    symbol: str
    name: str
    status: ServiceUnavailableErrorBodyItemsItemStatus
    label: str
    pairs: typing.List[ServiceUnavailableErrorBodyItemsItemPairsItem]
    markets_url: typing_extensions.Annotated[str, FieldMetadata(alias="marketsUrl"), pydantic.Field(alias="marketsUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
