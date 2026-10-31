

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_response_items_item import FulfillmentSimulationResponseItemsItem
from .fulfillment_simulation_response_logistics_info_item import FulfillmentSimulationResponseLogisticsInfoItem


class FulfillmentSimulationResponse(UniversalBaseModel):
    """
    Expected response body of fulfillment simulation
    """

    country: str = pydantic.Field()
    """
    ISO 3-digit code of the country where the delivery address is located. If you don’t want to send it, use the value null.
    """

    items: typing.List[FulfillmentSimulationResponseItemsItem] = pydantic.Field()
    """
    Contains the data about each SKU in the cart.
    """

    logistics_info: typing_extensions.Annotated[
        typing.List[FulfillmentSimulationResponseLogisticsInfoItem],
        FieldMetadata(alias="logisticsInfo"),
        pydantic.Field(
            alias="logisticsInfo",
            description="Array that contains the data regarding the delivery methods and stock for each item. If all products are unavailable, this field should return empty.",
        ),
    ]
    """
    Array that contains the data regarding the delivery methods and stock for each item. If all products are unavailable, this field should return empty.
    """

    postal_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="postalCode"),
        pydantic.Field(
            alias="postalCode",
            description="Postal code of the delivery address. This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.",
        ),
    ]
    """
    Postal code of the delivery address. This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
