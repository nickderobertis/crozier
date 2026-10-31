

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delivery_ids import DeliveryIds


class LogisticsInfo(UniversalBaseModel):
    """
    List that references the SLAs responsible for delivering each item in the order.

    This list must contain the same number of items as the `items` list, previously defined. For example: if the order contains 3 SKUs, you must describe 3 SLAs in this list, one for each SKU (even in cases where the same SLA will deliver all of them).

    The order of the SLAs in this list must also follow the same order as in the `items` list. For example: if the SLA named **Correios Express** will be responsible for delivering the SKU with ID equal to **1015**, which is found at index 0 of the `items` list, it must be in index 0 of the `logisticsInfo` list as well.
    """

    delivery_ids: typing_extensions.Annotated[
        DeliveryIds, FieldMetadata(alias="deliveryIds"), pydantic.Field(alias="deliveryIds")
    ]
    lock_ttl: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lockTTL"),
        pydantic.Field(
            alias="lockTTL",
            description="String with the inventory reservation period in VTEX's logistics system. To fill in this field insert the number of days, followed by the letter for the chosen unit. \n\n- Days: `d` \n\n- Business days: `bd`. \n\nExample formats: `12d`, `5d`.",
        ),
    ]
    """
    String with the inventory reservation period in VTEX's logistics system. To fill in this field insert the number of days, followed by the letter for the chosen unit. 
    
    - Days: `d` 
    
    - Business days: `bd`. 
    
    Example formats: `12d`, `5d`.
    """

    price: int = pydantic.Field()
    """
    Integer indicating the shipping price for this SKU. If the value is `USD20.50`, convert it to the format → `2050`.
    """

    selected_delivery_channel: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="selectedDeliveryChannel"),
        pydantic.Field(
            alias="selectedDeliveryChannel",
            description="String with the selected delivery channel. This field supports the following values:  \n\n- `delivery`,  \n\n- `pickup-in-point`.",
        ),
    ]
    """
    String with the selected delivery channel. This field supports the following values:  
    
    - `delivery`,  
    
    - `pickup-in-point`.
    """

    selected_sla: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="selectedSla"),
        pydantic.Field(alias="selectedSla", description="String with the selected delivery SLA."),
    ]
    """
    String with the selected delivery SLA.
    """

    shipping_estimate: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="shippingEstimate"),
        pydantic.Field(
            alias="shippingEstimate",
            description="String with the order's estimated delivery time. To fill in this field, insert a number,  followed by the letter for the chosen unit. \n\n- Days: `d` \n\n- Business days: `bd`. \n\n- Hours: `h` \n\n- Minutes: `m`. \n\nExample formats: `12d`, `5bd`, `3h`, `50m`.",
        ),
    ]
    """
    String with the order's estimated delivery time. To fill in this field, insert a number,  followed by the letter for the chosen unit. 
    
    - Days: `d` 
    
    - Business days: `bd`. 
    
    - Hours: `h` 
    
    - Minutes: `m`. 
    
    Example formats: `12d`, `5bd`, `3h`, `50m`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
