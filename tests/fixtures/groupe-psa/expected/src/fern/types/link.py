

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .url import Url


class Link(UniversalBaseModel):
    """
    A Link Object as defined by [JSONHAL#Link Object](https://tools.ietf.org/html/draft-kelly-json-hal-08#section-5).
    """

    href: Url
    templated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    SHOULD be true when the Link Object's "href" property is an [URI Template](https://tools.ietf.org/html/rfc6570)
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    a hint to indicate the media type expected when dereferencing the target resource.
    """

    deprecation: typing.Optional[str] = pydantic.Field(default=None)
    """
    indicates that the link is to be deprecated (i.e. removed) at a future date.  Its value is a URL that SHOULD provide further information about the deprecation.
    """

    name: typing.Optional[str] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Its value is a string and is intended for labelling the link with a human-readable identifier (as defined by [RFC5988](https://tools.ietf.org/html/rfc5988)).
    """

    profile: typing.Optional[str] = pydantic.Field(default=None)
    """
    Its value is a string and is intended for indicating the language of the target resource (as defined by [RFC5988]).
    """

    hreflang: typing.Optional[str] = pydantic.Field(default=None)
    """
    Its value is a string which is a URI that hints about the profile (as defined by [I-D.wilde-profile-link](https://tools.ietf.org/html/draft-kelly-json-hal-08#ref-I-D.wilde-profile-link)) of the target resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
