

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_cause import NotificationCause


class QosFlowNotifyItem(UniversalBaseModel):
    qfi: int
    notification_cause: typing_extensions.Annotated[
        NotificationCause, FieldMetadata(alias="notificationCause"), pydantic.Field(alias="notificationCause")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
