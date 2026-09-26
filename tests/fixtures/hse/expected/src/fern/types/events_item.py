

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .events_item_level import EventsItemLevel


class EventsItem(UniversalBaseModel):
    path: typing.Optional[str] = None
    level: typing.Optional[EventsItemLevel] = None
    odometer: typing.Optional[int] = None
    odometer_timestamp: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
