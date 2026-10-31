

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo(
    UniversalBaseModel
):
    """
    Information on the pickup store.
    """

    additional_info: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="additionalInfo"),
        pydantic.Field(alias="additionalInfo", description="Additional information."),
    ] = None
    """
    Additional information.
    """

    address: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Address information.
    """

    dock_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dockId"),
        pydantic.Field(alias="dockId", description="Corresponding dock ID."),
    ] = None
    """
    Corresponding dock ID.
    """

    friendly_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="friendlyName"),
        pydantic.Field(alias="friendlyName", description="Friendly name."),
    ] = None
    """
    Friendly name.
    """

    is_pickup_store: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPickupStore"),
        pydantic.Field(alias="isPickupStore", description="Indicates whether it is the pickup store."),
    ] = None
    """
    Indicates whether it is the pickup store.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
