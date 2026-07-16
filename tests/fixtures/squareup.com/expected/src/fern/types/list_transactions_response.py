

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .transaction import Transaction


class ListTransactionsResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [ListTransactions](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/list-transactions) endpoint.

    One of `errors` or `transactions` is present in a given response (never both).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor for retrieving the next set of results,
    if any remain. Provide this value as the `cursor` parameter in a subsequent
    request to this endpoint.
    
    See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    transactions: typing.Optional[typing.List[Transaction]] = pydantic.Field(default=None)
    """
    An array of transactions that match your query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
