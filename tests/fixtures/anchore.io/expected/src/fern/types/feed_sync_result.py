

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feed_sync_result_status import FeedSyncResultStatus
from .group_sync_result import GroupSyncResult


class FeedSyncResult(UniversalBaseModel):
    """
    The result of a sync of a single feed
    """

    feed: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the feed synced
    """

    groups: typing.Optional[typing.List[GroupSyncResult]] = pydantic.Field(default=None)
    """
    Array of group sync results
    """

    status: typing.Optional[FeedSyncResultStatus] = pydantic.Field(default=None)
    """
    The result of the sync operations, either co
    """

    total_time_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    The duratin, in seconds, of the sync of the feed, the sum of all the group syncs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
