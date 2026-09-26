

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_file_watcher_updated_properties_event import EventFileWatcherUpdatedPropertiesEvent


class EventFileWatcherUpdatedProperties(UniversalBaseModel):
    file: str
    event: EventFileWatcherUpdatedPropertiesEvent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
