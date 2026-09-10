

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_description_method import LinkDescriptionMethod


class LinkDescription(UniversalBaseModel):
    """
    The request-related [HATEOAS link](/docs/api/reference/api-responses/#hateoas-links) information.
    """

    href: str = pydantic.Field()
    """
    The complete target URL. To make the related call, combine the method with this [URI Template-formatted](https://tools.ietf.org/html/rfc6570) link. For pre-processing, include the `$`, `(`, and `)` characters. The `href` is the key HATEOAS component that links a completed call with a subsequent call.
    """

    rel: str = pydantic.Field()
    """
    The [link relation type](https://tools.ietf.org/html/rfc5988#section-4), which serves as an ID for a link that unambiguously describes the semantics of the link. See [Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml).
    """

    method: typing.Optional[LinkDescriptionMethod] = pydantic.Field(default=None)
    """
    The HTTP method required to make the related call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
