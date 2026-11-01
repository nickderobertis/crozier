

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_state import ListState


class List(UniversalBaseModel):
    """
    The list object
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the list in question
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account timezone used for datetime fields
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of creation
    """

    created_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of creation in ISO format
    """

    modified: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of last modification made
    """

    modified_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of last modification in ISO format
    """

    state: typing.Optional[ListState] = pydantic.Field(default=None)
    """
    Status of the list: active or deleted
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name given to the list in question
    """

    locked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If a list is locked, it cannot be changed by a user of the application. (true or false)
    """

    remarks: typing.Optional[str] = pydantic.Field(default=None)
    """
    Potential remarks
    """

    subscribe_notification_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address to which a notification will be sent upon a subscription
    """

    unsubscribe_notification_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address to which a notification will be sent upon the cancelling of a subscription
    """

    members: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Information in regards to the number of active, unsubscribed and cleaned (deleted) members
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the account this list belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
