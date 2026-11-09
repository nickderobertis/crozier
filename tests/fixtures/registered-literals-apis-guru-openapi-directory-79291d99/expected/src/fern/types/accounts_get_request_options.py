

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AccountsGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/accounts/get` results.
    """

    account_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of `account_ids` to retrieve for the Account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
