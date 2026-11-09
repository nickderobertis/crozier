

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferExpectedSettlementScheduleItem(UniversalBaseModel):
    """
    Defines an expected sweep date and amount.
    """

    settled_amount: str = pydantic.Field()
    """
    The accumulated amount that have been swept by `settlement_date`.
    """

    settlement_date: dt.date = pydantic.Field()
    """
    The settlement date of a sweep for this transfer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
