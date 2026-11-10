

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .min_last_updated_datetime import MinLastUpdatedDatetime


class AccountsBalanceGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/accounts/balance/get` results.
    """

    account_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of `account_ids` to retrieve for the Item. The default value is `null`.
    
    Note: An error will be returned if a provided `account_id` is not associated with the Item.
    """

    min_last_updated_datetime: typing.Optional[MinLastUpdatedDatetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
