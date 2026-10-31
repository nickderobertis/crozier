

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_response_logistics_info_item_slas_item_pickup_store_info_address import (
    FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfoAddress,
)


class FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfo(UniversalBaseModel):
    """
    Contains the data about the pickup point. If you don’t want to send this, use the value `null`.
    """

    additional_info: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="additionalInfo"),
        pydantic.Field(alias="additionalInfo", description="Description or extra information about the pickup point."),
    ]
    """
    Description or extra information about the pickup point.
    """

    address: FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfoAddress = pydantic.Field()
    """
    Address data of the pickup point.
    """

    friendly_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="friendlyName"),
        pydantic.Field(alias="friendlyName", description="Friendly name of the pickup point."),
    ]
    """
    Friendly name of the pickup point.
    """

    is_pickup_store: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isPickupStore"),
        pydantic.Field(alias="isPickupStore", description="`true` if it is a pickup point."),
    ]
    """
    `true` if it is a pickup point.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
