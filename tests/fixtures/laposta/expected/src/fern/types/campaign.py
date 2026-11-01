

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Campaign(UniversalBaseModel):
    """
    The campaign object
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of this account
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of this campaign
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

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of campaign (currently only possible: regular)
    """

    delivery_requested: typing.Optional[str] = pydantic.Field(default=None)
    """
    When to send
    """

    delivery_requested_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    When to send in ISO format
    """

    delivery_started: typing.Optional[str] = pydantic.Field(default=None)
    """
    Start of last transmission
    """

    delivery_started_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Start of last transmission in ISO format
    """

    delivery_ended: typing.Optional[str] = pydantic.Field(default=None)
    """
    End of last transmission
    """

    delivery_ended_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    End of last transmission in ISO format
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Internal name of campaign
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subject line
    """

    from_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Sender (name en email address)"),
    ] = None
    """
    Sender (name en email address)
    """

    reply_to: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address for receiving replies
    """

    list_ids: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Linked lists and segments
    """

    stats: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Linked web statistics
    """

    web: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to web version
    """

    screenshot: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Screenshots of campaign
    """

    previewtext: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preheader shown after the subject line in the inbox.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
