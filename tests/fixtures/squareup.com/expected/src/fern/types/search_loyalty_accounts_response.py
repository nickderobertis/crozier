

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .loyalty_account import LoyaltyAccount


class SearchLoyaltyAccountsResponse(UniversalBaseModel):
    """
    A response that includes loyalty accounts that satisfy the search criteria.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to use in a subsequent 
    request. If empty, this is the final response.
    For more information, 
    see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    loyalty_accounts: typing.Optional[typing.List[LoyaltyAccount]] = pydantic.Field(default=None)
    """
    The loyalty accounts that met the search criteria,  
    in order of creation date.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
