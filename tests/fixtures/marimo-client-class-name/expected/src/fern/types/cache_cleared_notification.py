

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cache_cleared_notification_op import CacheClearedNotificationOp


class CacheClearedNotification(UniversalBaseModel):
    """
    Execution cache cleared result.

        Attributes:
            bytes_freed: Bytes freed by clearing cache.
    """

    bytes_freed: int
    op: CacheClearedNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
