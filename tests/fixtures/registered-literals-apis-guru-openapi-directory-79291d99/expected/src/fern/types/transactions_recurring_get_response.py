

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .transaction_stream import TransactionStream


class TransactionsRecurringGetResponse(UniversalBaseModel):
    """
    TransactionsRecurringGetResponse defines the response schema for `/transactions/recurring/get`
    """

    inflow_streams: typing.List[TransactionStream] = pydantic.Field()
    """
    An array of depository transaction streams.
    """

    outflow_streams: typing.List[TransactionStream] = pydantic.Field()
    """
    An array of expense transaction streams.
    """

    request_id: RequestId
    updated_datetime: dt.datetime = pydantic.Field()
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the last time transaction streams for the given account were updated on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
