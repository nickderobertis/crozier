

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_server_id import AuthorisationServerId
from .notification_webhook_status_enum import NotificationWebhookStatusEnum


class WebhookStatusResponse(UniversalBaseModel):
    authorisation_server_id: typing_extensions.Annotated[
        typing.Optional[AuthorisationServerId],
        FieldMetadata(alias="AuthorisationServerId"),
        pydantic.Field(alias="AuthorisationServerId"),
    ] = None
    webhook_status: typing_extensions.Annotated[
        typing.Optional[NotificationWebhookStatusEnum],
        FieldMetadata(alias="WebhookStatus"),
        pydantic.Field(alias="WebhookStatus"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
