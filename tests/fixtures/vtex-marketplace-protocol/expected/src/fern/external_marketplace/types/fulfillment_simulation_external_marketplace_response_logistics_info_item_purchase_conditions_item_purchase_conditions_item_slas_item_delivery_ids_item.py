

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem(
    UniversalBaseModel
):
    courier_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courierId"),
        pydantic.Field(alias="courierId", description="Courier ID."),
    ] = None
    """
    Courier ID.
    """

    courier_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courierName"),
        pydantic.Field(alias="courierName", description="Courier name."),
    ] = None
    """
    Courier name.
    """

    dock_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dockId"), pydantic.Field(alias="dockId", description="Warehouse ID.")
    ] = None
    """
    Warehouse ID.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Quantity.
    """

    warehouse_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="warehouseId"),
        pydantic.Field(alias="warehouseId", description="Warehouse ID."),
    ] = None
    """
    Warehouse ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
