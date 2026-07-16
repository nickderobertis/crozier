

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_attributes import NotificationAttributes


class Notification(UniversalBaseModel):
    always: typing.Optional[bool] = None
    attributes: typing.Optional[NotificationAttributes] = None
    calendar_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="calendarId"), pydantic.Field(alias="calendarId")
    ] = None
    id: typing.Optional[int] = None
    mail: typing.Optional[bool] = None
    sms: typing.Optional[bool] = None
    type: typing.Optional[str] = None
    web: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
