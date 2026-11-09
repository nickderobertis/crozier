

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditPayrollIncomeRefreshRequestOptions(UniversalBaseModel):
    """
    An optional object for `/credit/payroll_income/refresh` request options.
    """

    item_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of `item_id`s to be refreshed. Each `item_id` should uniquely identify a payroll income item.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL where Plaid will send the payroll income refresh webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
