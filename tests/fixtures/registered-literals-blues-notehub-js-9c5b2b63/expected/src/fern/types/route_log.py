

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RouteLog(UniversalBaseModel):
    attn: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, an error was returned when routing
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date of the logs.
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The duration of the route in milliseconds
    """

    event_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event UID.
    """

    route_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The route UID.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the event.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The response body of the route.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the route.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
