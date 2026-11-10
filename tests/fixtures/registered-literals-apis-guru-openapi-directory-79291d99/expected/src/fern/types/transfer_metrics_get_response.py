

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class TransferMetricsGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/metrics/get`
    """

    daily_credit_transfer_volume: str = pydantic.Field()
    """
    Sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g. "10.00").
    """

    daily_debit_transfer_volume: str = pydantic.Field()
    """
    Sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g. "10.00").
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the dollar amount, e.g. "USD".
    """

    monthly_transfer_volume: str = pydantic.Field()
    """
    Sum of dollar amount of credit and debit transfers in current calendar month (decimal string with two digits of precision e.g. "10.00").
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
