

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventAccumulatePoints(UniversalBaseModel):
    """
    Provides metadata when the event `type` is `ACCUMULATE_POINTS`.
    """

    loyalty_program_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram).
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) for which the buyer accumulated the points.
    This field is returned only if the Orders API is used to process orders.
    """

    points: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of points accumulated by the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
