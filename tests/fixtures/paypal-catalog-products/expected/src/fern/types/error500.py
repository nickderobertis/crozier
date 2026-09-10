

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error500message import Error500Message
from .error500name import Error500Name
from .error_link_description import ErrorLinkDescription


class Error500(UniversalBaseModel):
    """
    This is either a system or application error, and generally indicates that although the client appeared to provide a correct request, something unexpected has gone wrong on the server.
    """

    name: typing.Optional[Error500Name] = None
    message: typing.Optional[Error500Message] = None
    debug_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The PayPal internal ID. Used for correlation purposes.
    """

    links: typing.Optional[typing.List[ErrorLinkDescription]] = pydantic.Field(default=None)
    """
    An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
