

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .terminal_checkout import TerminalCheckout


class SearchTerminalCheckoutsResponse(UniversalBaseModel):
    """ """

    checkouts: typing.Optional[typing.List[TerminalCheckout]] = pydantic.Field(default=None)
    """
    The requested search result of `TerminalCheckout` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If empty,
    this is the final response.
    
    See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
