

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logs_get_error500error import LogsGetError500Error
from .logs_get_error500meta import LogsGetError500Meta


class LogsGetError500(UniversalBaseModel):
    success: bool
    error: LogsGetError500Error
    meta: typing.Optional[LogsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
