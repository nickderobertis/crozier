

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LiabilitiesGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/liabilities/get` results. If provided, `options` cannot be null.
    """

    account_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of accounts to retrieve for the Item.
    
    An error will be returned if a provided `account_id` is not associated with the Item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
