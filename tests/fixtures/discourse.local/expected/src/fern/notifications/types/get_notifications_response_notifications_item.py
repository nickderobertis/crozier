

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_notifications_response_notifications_item_data import GetNotificationsResponseNotificationsItemData


class GetNotificationsResponseNotificationsItem(UniversalBaseModel):
    created_at: typing.Optional[str] = None
    data: typing.Optional[GetNotificationsResponseNotificationsItemData] = None
    id: typing.Optional[int] = None
    notification_type: typing.Optional[int] = None
    post_number: typing.Optional[str] = None
    read: typing.Optional[bool] = None
    slug: typing.Optional[str] = None
    topic_id: typing.Optional[int] = None
    user_id: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
