

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .multiple_live_items_items_item import MultipleLiveItemsItemsItem


class MultipleLiveItems(UniversalBaseModel):
    items: typing.Optional[typing.List[MultipleLiveItemsItemsItem]] = pydantic.Field(default=None)
    """
    The items to create. Each entry needs its own `fieldData`. Don't send a top-level `fieldData` with this shape.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
