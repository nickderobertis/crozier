

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .account_product_access import AccountProductAccess


class AccountProductAccessNullable(AccountProductAccess):
    """
    Allow the application to access specific products on this account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
