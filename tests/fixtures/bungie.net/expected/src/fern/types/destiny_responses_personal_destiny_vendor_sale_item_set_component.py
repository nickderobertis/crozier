

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_entities_vendors_destiny_vendor_sale_item_component import (
    DestinyEntitiesVendorsDestinyVendorSaleItemComponent,
)


class DestinyResponsesPersonalDestinyVendorSaleItemSetComponent(UniversalBaseModel):
    sale_items: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyEntitiesVendorsDestinyVendorSaleItemComponent]],
        FieldMetadata(alias="saleItems"),
        pydantic.Field(alias="saleItems"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
