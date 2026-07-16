

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_vendors_destiny_public_vendor_sale_item_component import (
    DestinyComponentsVendorsDestinyPublicVendorSaleItemComponent,
)


class DestinyResponsesPublicDestinyVendorSaleItemSetComponent(UniversalBaseModel):
    sale_items: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyComponentsVendorsDestinyPublicVendorSaleItemComponent]],
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
