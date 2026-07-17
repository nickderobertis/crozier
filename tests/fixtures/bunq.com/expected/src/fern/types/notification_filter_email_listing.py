

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class NotificationFilterEmailListing(UniversalBaseModel):
    notification_filters: typing.Optional[typing.List["NotificationFilterEmail"]] = pydantic.Field(default=None)
    """
    The types of notifications that will result in a email notification for this user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .notification_filter_email import NotificationFilterEmail

update_forward_refs(NotificationFilterEmailListing, NotificationFilterEmail=NotificationFilterEmail)
