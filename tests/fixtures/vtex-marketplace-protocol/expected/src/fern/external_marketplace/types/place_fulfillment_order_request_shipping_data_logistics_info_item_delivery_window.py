

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItemDeliveryWindow(UniversalBaseModel):
    """
    In case of scheduled delivery, this object will contain information on the delivery window selected by the shopper.
    """

    end_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endDateUtc"),
        pydantic.Field(alias="endDateUtc", description="Delivery window ending day and time in UTC."),
    ] = None
    """
    Delivery window ending day and time in UTC.
    """

    lis_price: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lisPrice"),
        pydantic.Field(alias="lisPrice", description="Delivery window list price."),
    ] = None
    """
    Delivery window list price.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Delivery window price.
    """

    start_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startDateUtc"),
        pydantic.Field(alias="startDateUtc", description="Delivery window starting day and time in UTC."),
    ] = None
    """
    Delivery window starting day and time in UTC.
    """

    tax: typing.Optional[int] = pydantic.Field(default=None)
    """
    Delivery window tax.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
