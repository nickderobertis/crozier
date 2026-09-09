

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error503message import Error503Message
from .error_link_description import ErrorLinkDescription


class Error503(UniversalBaseModel):
    """
    The server is temporarily unable to handle the request, for example, because of planned maintenance or downtime.
    """

    message: typing.Optional[Error503Message] = None
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
