

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListBankAccountsRequest(UniversalBaseModel):
    """
    Request object for fetching all `BankAccount`
    objects linked to a account.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor returned by a previous call to this endpoint.
    Use it in the next `ListBankAccounts` request to retrieve the next set 
    of results.
    
    See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Upper limit on the number of bank accounts to return in the response. 
    Currently, 1000 is the largest supported limit. You can specify a limit 
    of up to 1000 bank accounts. This is also the default limit.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location ID. You can specify this optional filter 
    to retrieve only the linked bank accounts belonging to a specific location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
