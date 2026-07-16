

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderFulfillmentPickupDetailsCurbsidePickupDetails(UniversalBaseModel):
    """
    Specific details for curbside pickup.
    """

    buyer_arrived_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) 
    indicating when the buyer arrived and is waiting for pickup. The timestamp must be in RFC 3339 format
    (for example, "2016-09-04T23:59:33.123Z").
    """

    curbside_details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specific details for curbside pickup, such as parking number and vehicle model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
