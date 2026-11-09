

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Recurrence(UniversalBaseModel):
    """
    Insights relating to expenses and deposits that are predicted to occur on a scheduled basis, such as biweekly, monthly, or annually.

    Common examples include loan payments, bill payments, subscriptions, and payroll income.

    This is a beta field, available to all users.
    """

    is_recurring: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the transaction is periodically recurring.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
