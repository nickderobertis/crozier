

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RealmPlayground(UniversalBaseModel):
    """
    Object containing details about a realm playground.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID for the realm playground.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-visible display name of the playground. Clients
    should display this in UI for picking which playground to
    open a code block in, to differentiate between multiple
    configured playground options for a given pygments
    language.
    
    **Changes**: New in Zulip 4.0 (feature level 49).
    """

    pygments_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the Pygments language lexer for that
    programming language.
    """

    url_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html)
    compliant URL template for the playground. The template contains
    exactly one variable named `code`, which determines how the
    extracted code should be substituted in the playground URL.
    
    **Changes**: New in Zulip 8.0 (feature level 196). This replaced the
    `url_prefix` parameter, which was used to construct URLs by just
    concatenating url_prefix and code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
