

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_notifications_response_notifications_item import GetNotificationsResponseNotificationsItem


class GetNotificationsResponse(UniversalBaseModel):
    load_more_notifications: typing.Optional[str] = None
    notifications: typing.Optional[typing.List[GetNotificationsResponseNotificationsItem]] = None
    seen_notification_id: typing.Optional[int] = None
    total_rows_notifications: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
