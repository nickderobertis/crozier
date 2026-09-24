

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_console_handler import LogConsoleHandler
from .log_file_handler import LogFileHandler


class LogConfig(UniversalBaseModel):
    file: LogFileHandler
    console: LogConsoleHandler

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
