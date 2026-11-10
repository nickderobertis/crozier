

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .item_status import ItemStatus


class ItemStatusNullable(ItemStatus):
    """
    Information about the last successful and failed transactions update for the Item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
