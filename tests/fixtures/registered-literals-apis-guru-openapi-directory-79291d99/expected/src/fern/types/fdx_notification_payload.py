

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fdx_fi_attribute import FdxFiAttribute
from .fdx_notification_payload_id_type import FdxNotificationPayloadIdType


class FdxNotificationPayload(UniversalBaseModel):
    """
    Custom key-value pairs payload for a notification
    """

    custom_fields: typing_extensions.Annotated[
        typing.Optional[FdxFiAttribute], FieldMetadata(alias="customFields"), pydantic.Field(alias="customFields")
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID for the origination entity related to the notification
    """

    id_type: typing_extensions.Annotated[
        typing.Optional[FdxNotificationPayloadIdType], FieldMetadata(alias="idType"), pydantic.Field(alias="idType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
