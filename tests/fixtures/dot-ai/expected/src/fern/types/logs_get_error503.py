

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logs_get_error503error import LogsGetError503Error
from .logs_get_error503meta import LogsGetError503Meta


class LogsGetError503(UniversalBaseModel):
    success: bool
    error: LogsGetError503Error
    meta: typing.Optional[LogsGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
