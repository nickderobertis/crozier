

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_product_access_nullable import AccountProductAccessNullable


class AccountAccess(UniversalBaseModel):
    """
    Allow or disallow product access by account. Unlisted (e.g. missing) accounts will be considered `new_accounts`.
    """

    account_product_access: typing.Optional[AccountProductAccessNullable] = None
    authorized: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow the application to see this account (and associated details, including balance) in the list of accounts  If unset, defaults to `true`.
    """

    unique_id: str = pydantic.Field()
    """
    The unique account identifier for this account. This value must match that returned by the data access API for this account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
