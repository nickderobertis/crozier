

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error422message import Error422Message
from .error422name import Error422Name
from .error_details import ErrorDetails
from .error_link_description import ErrorLinkDescription


class UnprocessableEntityErrorBody(UniversalBaseModel):
    name: typing.Optional[Error422Name] = None
    message: typing.Optional[Error422Message] = None
    details: typing.Optional[typing.List[ErrorDetails]] = None
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
