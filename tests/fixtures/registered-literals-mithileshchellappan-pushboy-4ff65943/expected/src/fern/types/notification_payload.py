

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notification_payload_priority import NotificationPayloadPriority


class NotificationPayload(UniversalBaseModel):
    title: typing.Optional[str] = None
    body: typing.Optional[str] = None
    image_url: typing.Optional[str] = None
    sound: typing.Optional[str] = None
    badge: typing.Optional[int] = None
    data: typing.Optional[typing.Dict[str, str]] = None
    silent: typing.Optional[bool] = None
    collapse_id: typing.Optional[str] = None
    priority: typing.Optional[NotificationPayloadPriority] = None
    ttl: typing.Optional[int] = pydantic.Field(default=None)
    """
    Seconds until expiration.
    """

    thread_id: typing.Optional[str] = None
    category: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
