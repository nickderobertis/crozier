

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fdx_content_types import FdxContentTypes
from .fdx_hateoas_link_action import FdxHateoasLinkAction


class FdxHateoasLink(UniversalBaseModel):
    """
    REST application constraint (Hypermedia As The Engine Of Application State)
    """

    action: typing.Optional[FdxHateoasLinkAction] = None
    href: str = pydantic.Field()
    """
    URL to invoke the action on the resource
    """

    rel: typing.Optional[str] = pydantic.Field(default=None)
    """
    Relation of this link to its containing entity, as defined by and with many example relation values at [IETF RFC5988](https://datatracker.ietf.org/doc/html/rfc5988)
    """

    types: typing.Optional[typing.List[FdxContentTypes]] = pydantic.Field(default=None)
    """
    Content-types that can be used in the Accept header
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
