

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChannelFolder(UniversalBaseModel):
    """
    Object containing the channel folder's attributes.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the channel folder.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the channel folder.
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    This value determines in which order the channel folder should be
    displayed in the UI. The value is 0 indexed, and a channel folder with
    a lower value should be displayed before channel folders with higher
    values.
    
    **Changes**: New in Zulip 11.0 (feature level 414).
    """

    date_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the channel folder was created,
    in UTC seconds.
    """

    creator_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who created the channel folder.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the channel folder. Can be an empty string.
    
    See [Markdown message formatting](/api/message-formatting) for details
    on Zulip's HTML format.
    """

    rendered_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the channel folder rendered as HTML, intended to be
    used for UI that displays the channel folder description.
    
    Clients should use the standard Zulip rendered_markdown CSS when
    displaying this content so that emoji, LaTeX, and other syntax work
    correctly. And any client-side security logic for user-generated
    message content should be applied when displaying this HTML as though
    it were the body of a Zulip message.
    """

    is_archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the channel folder is archived or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
