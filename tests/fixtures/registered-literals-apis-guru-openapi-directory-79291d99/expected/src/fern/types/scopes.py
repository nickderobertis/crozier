

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_access import AccountAccess
from .product_access import ProductAccess


class Scopes(UniversalBaseModel):
    """
    The scopes object
    """

    accounts: typing.Optional[typing.List[AccountAccess]] = None
    new_accounts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to newly opened accounts as they are opened. If unset, defaults to `true`.
    """

    product_access: typing.Optional[ProductAccess] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
