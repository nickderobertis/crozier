

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .logistics_info import LogisticsInfo
from .selected_address import SelectedAddress


class ShippingData(UniversalBaseModel):
    is_fob: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isFob"),
        pydantic.Field(
            alias="isFob",
            description="Boolean that indicates whether the order's delivery is the marketplace responsibility. Optional, defaulting to false.",
        ),
    ]
    """
    Boolean that indicates whether the order's delivery is the marketplace responsibility. Optional, defaulting to false.
    """

    is_marketplace_fulfillment: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isMarketplaceFulfillment"),
        pydantic.Field(
            alias="isMarketplaceFulfillment",
            description="Boolean that indicates whether the order's inventory in warehouse is the marketplace's responsibility. Optional, defaulting to false.",
        ),
    ]
    """
    Boolean that indicates whether the order's inventory in warehouse is the marketplace's responsibility. Optional, defaulting to false.
    """

    logistics_info: typing_extensions.Annotated[
        typing.List[LogisticsInfo],
        FieldMetadata(alias="logisticsInfo"),
        pydantic.Field(
            alias="logisticsInfo",
            description="List that references the SLAs responsible for delivering each item in the order.  \n\nThis list must contain the same number of items as the `items` list, previously defined. For example: if the order contains 3 SKUs, you must describe 3 SLAs in this list, one for each SKU (even in cases where the same SLA will deliver all of them).  \n\nThe order of the SLAs in this list must also follow the same order as in the `items` list. For example: if the SLA named **Correios Express** will be responsible for delivering the SKU with ID equal to **1015**, which is found at index 0 of the `items` list, it must be in index 0 of the `logisticsInfo` list as well.",
        ),
    ]
    """
    List that references the SLAs responsible for delivering each item in the order.  
    
    This list must contain the same number of items as the `items` list, previously defined. For example: if the order contains 3 SKUs, you must describe 3 SLAs in this list, one for each SKU (even in cases where the same SLA will deliver all of them).  
    
    The order of the SLAs in this list must also follow the same order as in the `items` list. For example: if the SLA named **Correios Express** will be responsible for delivering the SKU with ID equal to **1015**, which is found at index 0 of the `items` list, it must be in index 0 of the `logisticsInfo` list as well.
    """

    selected_addresses: typing_extensions.Annotated[
        typing.List[SelectedAddress],
        FieldMetadata(alias="selectedAddresses"),
        pydantic.Field(alias="selectedAddresses", description=""),
    ]
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
