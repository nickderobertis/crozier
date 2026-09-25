

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaymentPlanItem(UniversalBaseModel):
    due_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Due date for this installment
    """

    purchase_amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Amount for this installment in cents
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State of the installment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
