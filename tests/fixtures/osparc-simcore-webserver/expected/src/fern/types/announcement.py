

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .announcement_widgets_item import AnnouncementWidgetsItem


class Announcement(UniversalBaseModel):
    id: str
    products: typing.List[str]
    start: dt.datetime
    end: dt.datetime
    title: str
    description: str
    link: str
    widgets: typing.List[AnnouncementWidgetsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
