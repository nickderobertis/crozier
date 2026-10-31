

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DeliveryIds(UniversalBaseModel):
    """
    List of delivery IDs, used for orders where the marketplace is responsible for the fulfillment of the order, including keeping inventory at a warehouse as well as the delivery.
    """

    warehouse_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="warehouseId"),
        pydantic.Field(
            alias="warehouseId",
            description="String with the ID of the warehouse used for marketplace fulfillment. Required when `isFob` = `true` and `isMarketplaceFulfillment` = `true`.",
        ),
    ]
    """
    String with the ID of the warehouse used for marketplace fulfillment. Required when `isFob` = `true` and `isMarketplaceFulfillment` = `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
