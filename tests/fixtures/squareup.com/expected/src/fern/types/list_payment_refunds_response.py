

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .payment_refund import PaymentRefund


class ListPaymentRefundsResponse(UniversalBaseModel):
    """
    Defines the response returned by [ListPaymentRefunds](https://developer.squareup.com/reference/square_2021-08-18/refunds-api/list-payment-refunds).

    Either `errors` or `refunds` is present in a given response (never both).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If empty,
    this is the final response.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    refunds: typing.Optional[typing.List[PaymentRefund]] = pydantic.Field(default=None)
    """
    The list of requested refunds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
