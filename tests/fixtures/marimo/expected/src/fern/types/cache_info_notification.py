

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cache_info_notification_op import CacheInfoNotificationOp


class CacheInfoNotification(UniversalBaseModel):
    """
    Execution cache statistics.

        Attributes:
            hits: Cache hits.
            misses: Cache misses.
            time: Time spent on cache operations (seconds).
            disk_to_free: Disk space that could be freed (bytes).
            disk_total: Total disk space used (bytes).
    """

    disk_to_free: int
    disk_total: int
    hits: int
    misses: int
    op: CacheInfoNotificationOp
    time: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
