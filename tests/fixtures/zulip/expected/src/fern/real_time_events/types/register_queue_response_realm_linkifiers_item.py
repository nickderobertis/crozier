

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseRealmLinkifiersItem(UniversalBaseModel):
    pattern: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [Python regular expression](https://docs.python.org/3/howto/regex.html)
    pattern which represents the pattern that should be linkified on matching.
    """

    url_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html) compliant URL
    template with which the pattern matching string should be linkified.
    
    **Changes**: New in Zulip 7.0 (feature level 176). This replaced `url_format`,
    which contained a URL format string.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the linkifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
