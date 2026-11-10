

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .item import Item
from .request_id import RequestId


class AccountsGetResponse(UniversalBaseModel):
    """
    AccountsGetResponse defines the response schema for `/accounts/get` and `/accounts/balance/get`.
    """

    accounts: typing.List[AccountBase] = pydantic.Field()
    """
    An array of financial institution accounts associated with the Item.
    If `/accounts/balance/get` was called, each account will include real-time balance information.
    """

    item: Item
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
