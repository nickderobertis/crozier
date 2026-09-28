

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logs_get_error400error import LogsGetError400Error
from .logs_get_error400meta import LogsGetError400Meta


class LogsGetError400(UniversalBaseModel):
    success: bool
    error: LogsGetError400Error
    meta: typing.Optional[LogsGetError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
