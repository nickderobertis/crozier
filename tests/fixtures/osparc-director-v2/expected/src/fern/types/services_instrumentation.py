

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServicesInstrumentation(UniversalBaseModel):
    start_requested_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    moment in which the process of starting the service was requested
    """

    close_requested_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    moment in which the process of stopping the service was requested
    """

    request_trace_carrier: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    W3C traceparent and tracestate headers from the originating request for span linking
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
