

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .watch_event_data import WatchEventData
from .watch_event_spec_version import WatchEventSpecVersion


class WatchEvent(UniversalBaseModel):
    specversion: WatchEventSpecVersion
    id: str
    source: str
    type: str
    datacontenttype: str
    time: dt.datetime
    data: WatchEventData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
