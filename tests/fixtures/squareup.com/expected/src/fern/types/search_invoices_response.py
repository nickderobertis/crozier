

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .invoice import Invoice


class SearchInvoicesResponse(UniversalBaseModel):
    """
    Describes a `SearchInvoices` response.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    When a response is truncated, it includes a cursor that you can use in a 
    subsequent request to fetch the next set of invoices. If empty, this is the final 
    response. 
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    invoices: typing.Optional[typing.List[Invoice]] = pydantic.Field(default=None)
    """
    The list of invoices returned by the search.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
