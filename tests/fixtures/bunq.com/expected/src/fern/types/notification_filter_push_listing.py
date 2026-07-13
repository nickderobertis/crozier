

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class NotificationFilterPushListing(UniversalBaseModel):
    notification_filters: typing.Optional[typing.List["NotificationFilterPush"]] = pydantic.Field(default=None)
    """
    The types of notifications that will result in a push notification for this user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .notification_filter_push import NotificationFilterPush

update_forward_refs(NotificationFilterPushListing)
