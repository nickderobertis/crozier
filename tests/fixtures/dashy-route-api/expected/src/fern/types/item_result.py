

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .item import Item
from .write_result import WriteResult


class ItemResult(WriteResult):
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Array index of the item
    """

    item: typing.Optional[Item] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
