

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_preference import NotificationPreference


class ContactDetails(UniversalBaseModel):
    """
    Contact Details.
    """

    contact_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="contactName"),
        pydantic.Field(alias="contactName", description="Contact name of the person."),
    ]
    """
    Contact name of the person.
    """

    email_list: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="emailList"),
        pydantic.Field(alias="emailList", description="List of Email-ids to be notified about job progress."),
    ]
    """
    List of Email-ids to be notified about job progress.
    """

    mobile: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mobile number of the contact person.
    """

    notification_preference: typing_extensions.Annotated[
        typing.Optional[typing.List[NotificationPreference]],
        FieldMetadata(alias="notificationPreference"),
        pydantic.Field(alias="notificationPreference", description="Notification preference for a job stage."),
    ] = None
    """
    Notification preference for a job stage.
    """

    phone: str = pydantic.Field()
    """
    Phone number of the contact person.
    """

    phone_extension: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="phoneExtension"),
        pydantic.Field(alias="phoneExtension", description="Phone extension number of the contact person."),
    ] = None
    """
    Phone extension number of the contact person.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
