

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_page_items_item import ActionPageItemsItem


class ActionPage(UniversalBaseModel):
    items: typing.List[ActionPageItemsItem]
    page: int
    size: int
    has_more: bool
    total: int
    total_is_estimated: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
