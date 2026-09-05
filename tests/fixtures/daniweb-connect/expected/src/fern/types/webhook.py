

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app import App
from .user import User
from .webhook_event import WebhookEvent
from .webhook_object import WebhookObject


class Webhook(UniversalBaseModel):
    app: typing.Optional[App] = None
    event: typing.Optional[WebhookEvent] = None
    id: int
    name: typing.Optional[str] = None
    object: typing.Optional[WebhookObject] = None
    uri: typing.Optional[str] = None
    user: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
