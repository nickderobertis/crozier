

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class TransferConfigurationGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/configuration/get`
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the dollar amount, e.g. "USD".
    """

    max_daily_credit_amount: str = pydantic.Field()
    """
    The max limit of sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g. "10.00").
    """

    max_daily_debit_amount: str = pydantic.Field()
    """
    The max limit of sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g. "10.00").
    """

    max_monthly_amount: str = pydantic.Field()
    """
    The max limit of sum of dollar amount of credit and debit transfers in one calendar month (decimal string with two digits of precision e.g. "10.00").
    """

    max_single_transfer_amount: str = pydantic.Field()
    """
    The max limit of dollar amount of a single transfer (decimal string with two digits of precision e.g. "10.00").
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
