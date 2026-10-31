

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .place_fulfillment_order_request_shipping_data_address import PlaceFulfillmentOrderRequestShippingDataAddress
from .place_fulfillment_order_request_shipping_data_logistics_info_item import (
    PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem,
)


class PlaceFulfillmentOrderRequestShippingData(UniversalBaseModel):
    """
    Shipping information.
    """

    address: typing.Optional[PlaceFulfillmentOrderRequestShippingDataAddress] = pydantic.Field(default=None)
    """
    Shipping address.
    """

    logistics_info: typing_extensions.Annotated[
        typing.Optional[typing.List[PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem]],
        FieldMetadata(alias="logisticsInfo"),
        pydantic.Field(
            alias="logisticsInfo", description="Array of objects containing logistics information of each item."
        ),
    ] = None
    """
    Array of objects containing logistics information of each item.
    """

    update_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updateStatus"),
        pydantic.Field(
            alias="updateStatus",
            description="Indicate whether this object's information is up to date according to the order's items. An order can not be placed if `\"outdated\"`",
        ),
    ] = None
    """
    Indicate whether this object's information is up to date according to the order's items. An order can not be placed if `"outdated"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
