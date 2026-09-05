

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_level import LogLevel


class Log(UniversalBaseModel):
    level: typing.Optional[LogLevel] = pydantic.Field(default=None)
    """
    log level
    """

    message: str = pydantic.Field()
    """
    log message. If logger is USER, then it MUST be human readable
    """

    logger: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the logger receiving this message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
