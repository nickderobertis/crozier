

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feed_group_metadata import FeedGroupMetadata


class FeedMetadata(UniversalBaseModel):
    """
    Metadata on a single feed based on what the engine finds from querying the endpoints
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date the metadata record was created in engine (first seen on source)
    """

    groups: typing.Optional[typing.List[FeedGroupMetadata]] = None
    last_full_sync: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the feed
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date the metadata was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
