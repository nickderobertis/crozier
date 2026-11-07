

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_navigation_entry_order import CoreNavigationEntryOrder


class CoreNavigationEntry(UniversalBaseModel):
    id: str
    order: CoreNavigationEntryOrder
    href: str
    icon: str
    type: str
    name: str
    active: bool
    classes: str
    unread: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
