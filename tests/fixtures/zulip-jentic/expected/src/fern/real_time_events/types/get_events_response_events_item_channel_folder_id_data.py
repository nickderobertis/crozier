

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemChannelFolderIdData(UniversalBaseModel):
    """
    Dictionary containing the changed details of the channel folder.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new name of the channel folder. Only present if the channel
    folder's name changed.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new description of the channel folder. Only present if the
    description changed.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    rendered_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new rendered description of the channel folder. Only present
    if the description changed.
    """

    is_archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the channel folder is archived or not. Only present if
    the channel folder is archived or unarchived.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
