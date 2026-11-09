

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .item_id import ItemId
from .plaid_error import PlaidError


class Cause(PlaidError):
    """
    An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items.
    """

    item_id: ItemId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
