

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Snippet(UniversalBaseModel):
    """
    Represents the snippet that is added to a Square Online site. The snippet code is injected into the `head` element of all pages on the site, except for checkout pages.
    """

    content: str = pydantic.Field()
    """
    The snippet code, which can contain valid HTML, JavaScript, or both.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the snippet was initially added to the site, in RFC 3339 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID for the snippet.
    """

    site_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the site that contains the snippet.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the snippet was last updated on the site, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
