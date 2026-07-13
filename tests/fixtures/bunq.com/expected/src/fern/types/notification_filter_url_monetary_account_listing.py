

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class NotificationFilterUrlMonetaryAccountListing(UniversalBaseModel):
    notification_filters: typing.Optional[typing.List["NotificationFilterUrl"]] = pydantic.Field(default=None)
    """
    The types of notifications that will result in a url notification for this monetary account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .notification_filter_url import NotificationFilterUrl

update_forward_refs(NotificationFilterUrlMonetaryAccountListing)
