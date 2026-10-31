

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationResponseLogisticsInfoItemDeliveryChannelsItem(UniversalBaseModel):
    """
    Object containing ID and stockbalance of each delivery channel.
    """

    id: str = pydantic.Field()
    """
    Identifies the channel type whose stock balance will be informed in the next field. Possible values are: pickup-in-point for pickup point and delivery for regular delivery.
    """

    stock_balance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="stockBalance"),
        pydantic.Field(
            alias="stockBalance", description="Stock balance for the channel type selected in the previous field."
        ),
    ]
    """
    Stock balance for the channel type selected in the previous field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
