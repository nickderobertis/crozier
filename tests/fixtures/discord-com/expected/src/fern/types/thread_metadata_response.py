

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_auto_archive_duration import ThreadAutoArchiveDuration


class ThreadMetadataResponse(UniversalBaseModel):
    archived: bool
    archive_timestamp: typing.Optional[dt.datetime] = None
    auto_archive_duration: ThreadAutoArchiveDuration
    locked: bool
    create_timestamp: typing.Optional[dt.datetime] = None
    invitable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
