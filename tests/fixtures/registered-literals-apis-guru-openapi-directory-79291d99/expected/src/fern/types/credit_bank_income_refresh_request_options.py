

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditBankIncomeRefreshRequestOptions(UniversalBaseModel):
    """
    An optional object for `/credit/bank_income/refresh` request options.
    """

    days_requested: typing.Optional[int] = pydantic.Field(default=None)
    """
    How many days of data to include in the refresh. If not specified, this will default to the days requested in the most recently generated bank income report for the user.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL where Plaid will send the bank income webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
