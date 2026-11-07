

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .notification_spec import NotificationSpec


class Notification(UniversalBaseModel):
    """
    Notification extension that stores an on-site notification delivered to a Halo user.

     <p>Supports the following operations:

     <ul>
       <li>Marked as read: {@link NotificationSpec#setUnread(boolean) NotificationSpec#setUnread(boolean)}
       <li>Get the last read time: {@link NotificationSpec#getLastReadAt NotificationSpec#getLastReadAt()}
       <li>Filter by recipient: {@link NotificationSpec#getRecipient NotificationSpec#getRecipient()}
     </ul>
    """

    api_version: typing_extensions.Annotated[str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")]
    kind: str
    metadata: Metadata
    spec: typing.Optional[NotificationSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
