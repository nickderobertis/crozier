

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_schedule_interval import PaymentScheduleInterval


class PaymentInitiationStandingOrderMetadata(UniversalBaseModel):
    """
    Metadata specifically related to valid Payment Initiation standing order configurations for the institution.
    """

    supports_standing_order_end_date: bool = pydantic.Field()
    """
    Indicates whether the institution supports closed-ended standing orders by providing an end date.
    """

    supports_standing_order_negative_execution_days: bool = pydantic.Field()
    """
    This is only applicable to `MONTHLY` standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a `MONTHLY` standing order relative to the end of the month.
    """

    valid_standing_order_intervals: typing.List[PaymentScheduleInterval] = pydantic.Field()
    """
    A list of the valid standing order intervals supported by the institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
