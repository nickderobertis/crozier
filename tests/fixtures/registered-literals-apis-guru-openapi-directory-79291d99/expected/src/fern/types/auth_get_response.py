

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .auth_get_numbers import AuthGetNumbers
from .item import Item
from .request_id import RequestId


class AuthGetResponse(UniversalBaseModel):
    """
    AuthGetResponse defines the response schema for `/auth/get`
    """

    accounts: typing.List[AccountBase] = pydantic.Field()
    """
    The `accounts` for which numbers are being retrieved.
    """

    item: Item
    numbers: AuthGetNumbers
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
