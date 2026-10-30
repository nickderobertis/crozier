

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .member_state import MemberState


class Member(UniversalBaseModel):
    """
    The member object
    """

    member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of this member object
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the related list
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address
    """

    state: typing.Optional[MemberState] = pydantic.Field(default=None)
    """
    The current status of this subscriber: active, unsubscribed, unconfirmed or cleaned
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account timezone used for datetime fields
    """

    signup_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of subscription
    """

    signup_date_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of subscription in ISO format
    """

    modified: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of last modification made
    """

    modified_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of last modification in ISO format
    """

    confirm_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of confirmation
    """

    confirm_date_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of confirmation in ISO format
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    IP from which the subscriber is registered
    """

    source_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL from which the subscriber is registered
    """

    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    An array with the value of all additional fields of the corresponding list. If there are fields where several options can be selected, these options are listed in an array. If the list has labels, `labels` is included as well, with the labels of that subscriber as an array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
