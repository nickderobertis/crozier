

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_console_handler_format import LogConsoleHandlerFormat
from .log_console_handler_level import LogConsoleHandlerLevel


class LogConsoleHandler(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable the console log
    """

    level: LogConsoleHandlerLevel = pydantic.Field()
    """
    The global log level for the application
    """

    format: LogConsoleHandlerFormat = pydantic.Field()
    """
    The log format for the application
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
