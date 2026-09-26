

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_nav_menu_data_items_item import MarimoNavMenuDataItemsItem
from .marimo_nav_menu_data_orientation import MarimoNavMenuDataOrientation


class MarimoNavMenuData(UniversalBaseModel):
    items: typing.List[MarimoNavMenuDataItemsItem]
    orientation: MarimoNavMenuDataOrientation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
