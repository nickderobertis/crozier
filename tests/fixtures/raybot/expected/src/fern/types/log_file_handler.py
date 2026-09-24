

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .log_file_handler_format import LogFileHandlerFormat
from .log_file_handler_level import LogFileHandlerLevel


class LogFileHandler(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable the file log
    """

    path: str = pydantic.Field()
    """
    The path to the file log
    """

    rotation_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="rotationCount"),
        pydantic.Field(alias="rotationCount", description="The number of log files to keep"),
    ]
    """
    The number of log files to keep
    """

    level: LogFileHandlerLevel = pydantic.Field()
    """
    The global log level for the application
    """

    format: LogFileHandlerFormat = pydantic.Field()
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
