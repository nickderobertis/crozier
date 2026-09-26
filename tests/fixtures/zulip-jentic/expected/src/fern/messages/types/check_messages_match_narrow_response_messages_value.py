

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CheckMessagesMatchNarrowResponseMessagesValue(UniversalBaseModel):
    """
    `message_id`: The ID of the message that matches the narrow. No record will be returned
    for queried messages that do not match the narrow.
    """

    match_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTML content of a queried message that matches the narrow. If the
    narrow is a search narrow, `<span class="highlight">` elements
    will be included, wrapping the matches for the search keywords.
    """

    match_subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTML-escaped topic of a queried message that matches the narrow. If the
    narrow is a search narrow, `<span class="highlight">` elements
    will be included wrapping the matches for the search keywords.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
