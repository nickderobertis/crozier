

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_sync_result_status import GroupSyncResultStatus


class GroupSyncResult(UniversalBaseModel):
    group: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the group
    """

    status: typing.Optional[GroupSyncResultStatus] = None
    total_time_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    The duration of the group sync in seconds
    """

    updated_image_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of images updated by the this group sync, across all accounts. This is typically only non-zero for vulnerability feeds which update images' vulnerability results during the sync.
    """

    updated_record_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of feed data records synced down as either updates or new records
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
