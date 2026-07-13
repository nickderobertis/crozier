

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .amount import Amount
from .avatar import Avatar
from .notification_filter import NotificationFilter
from .pointer import Pointer
from .relation_user import RelationUser
from .tax_resident import TaxResident


class UserPerson(UniversalBaseModel):
    address_main: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The person's main address.
    """

    address_postal: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The person's postal address.
    """

    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The aliases of the user.
    """

    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The user's avatar.
    """

    avatar_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public UUID of the user's avatar.
    """

    country_of_birth: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's country of birth. Formatted as a SO 3166-1 alpha-2 country code.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the person object's creation.
    """

    daily_limit_without_confirmation_login: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount the user can pay in the session without asking for credentials.
    """

    date_of_birth: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's date of birth. Accepts ISO8601 date formats.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name for the person.
    """

    document_back_attachment_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The reference to the uploaded picture/scan of the back side of the identification document.
    """

    document_country_of_issuance: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country which issued the identification document the person registered with.
    """

    document_front_attachment_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The reference to the uploaded picture/scan of the front side of the identification document.
    """

    document_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identification document number the person registered with.
    """

    document_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of identification document the person registered with.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's first name.
    """

    gender: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's gender. Can be MALE, FEMALE or UNKNOWN.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the modified person object.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's last name.
    """

    legal_guardian_alias: typing.Optional[Pointer] = pydantic.Field(default=None)
    """
    The legal guardian of the user. Required for minors.
    """

    legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's legal name.
    """

    middle_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's middle name.
    """

    nationality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's nationality. Formatted as a SO 3166-1 alpha-2 country code.
    """

    notification_filters: typing.Optional[typing.List[NotificationFilter]] = pydantic.Field(default=None)
    """
    The types of notifications that will result in a push notification or URL callback for this UserPerson.
    """

    place_of_birth: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's place of birth.
    """

    public_nick_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public nick name for the person.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's public UUID.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.
    """

    relations: typing.Optional[typing.List[RelationUser]] = pydantic.Field(default=None)
    """
    The relations for this user.
    """

    session_timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    The setting for the session timeout of the user in seconds.
    """

    signup_track_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of signup track the user is following.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user status. The user status. Can be: ACTIVE, BLOCKED, SIGNUP, RECOVERY, DENIED or ABORTED.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.
    """

    subscription_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subscription type the user should start on.
    """

    tax_resident: typing.Optional[typing.List[TaxResident]] = pydantic.Field(default=None)
    """
    The user's tax residence numbers for different countries.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the person object's last update.
    """

    version_terms_of_service: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the terms of service accepted by the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
