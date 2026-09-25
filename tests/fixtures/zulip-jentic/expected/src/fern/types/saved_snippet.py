

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SavedSnippet(UniversalBaseModel):
    """
    Object containing the details of the saved snippet.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the saved snippet.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the saved snippet.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content of the saved snippet in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.
    
    Clients should insert this content into a message when using
    a saved snippet.
    """

    date_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the saved snippet was created, in
    UTC seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
