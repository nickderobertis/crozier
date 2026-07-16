

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .x_com_collection_item import XComCollectionItem


class XCom(XComCollectionItem):
    """
    Full representations of XCom entry.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
