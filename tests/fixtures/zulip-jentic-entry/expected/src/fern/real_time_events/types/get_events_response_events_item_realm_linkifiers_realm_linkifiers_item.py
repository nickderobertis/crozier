

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemRealmLinkifiersRealmLinkifiersItem(UniversalBaseModel):
    pattern: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [Python regular expression](https://docs.python.org/3/howto/regex.html)
    that represents the pattern that should be linkified by this linkifier.
    """

    url_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html) compliant
    URL template to be used for linkifying matches.
    
    **Changes**: New in Zulip 7.0 (feature level 176). This replaced `url_format`,
    which contained a URL format string.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the linkifier.
    """

    example_input: typing.Optional[str] = pydantic.Field(default=None)
    """
    An example input string that matches the linkifier's pattern.
    This is required for reverse linkifiers.
    
    **Changes**: New in Zulip 12.0 (feature level 471).
    """

    reverse_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    A simple template using `{variable}` for variables that can
    be used to generate the Markdown linkifier syntax, given a
    URL matching the URL template.
    
    `{{ "{{/}}" }}` can be used for literal `{/}` characters.
    
    **Changes**: New in Zulip 12.0 (feature level 471).
    """

    alternative_url_templates: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of additional [RFC 6570][rfc6570] compliant URL
    template strings that are used for reverse linkification
    (converting pasted URLs to linkifier pattern text). These
    templates have no effect on forward linkification.
    
    [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html
    
    **Changes**: New in Zulip 12.0 (feature level e2b257).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
