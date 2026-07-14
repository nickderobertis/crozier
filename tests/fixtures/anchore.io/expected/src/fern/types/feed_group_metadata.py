

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FeedGroupMetadata(UniversalBaseModel):
    created_at: typing.Optional[dt.datetime] = None
    last_sync: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = None
    record_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
