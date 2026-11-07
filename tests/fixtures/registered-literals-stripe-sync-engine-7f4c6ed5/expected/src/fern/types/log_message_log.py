

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_message_log_level import LogMessageLogLevel


class LogMessageLog(UniversalBaseModel):
    """
    Structured log output from a connector.
    """

    level: LogMessageLogLevel = pydantic.Field()
    """
    Log severity level.
    """

    message: str = pydantic.Field()
    """
    Human-readable log message.
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Structured log fields emitted alongside the message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
