

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GenericNotificationPayload(UniversalBaseModel):
    """
    Parent class for Notification Payloads
    """

    notification_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="notificationId")] = None
    subscription_key: typing.Optional[str] = None
    subscription_type: typing.Optional[str] = None
    user_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
