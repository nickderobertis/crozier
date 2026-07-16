

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .payment import Payment


class ListPaymentsResponse(UniversalBaseModel):
    """
    Defines the response returned by [ListPayments](https://developer.squareup.com/reference/square_2021-08-18/payments-api/list-payments).
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

    payments: typing.Optional[typing.List[Payment]] = pydantic.Field(default=None)
    """
    The requested list of payments.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
