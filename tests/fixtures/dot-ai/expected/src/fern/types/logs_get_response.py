

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logs_get_response_data import LogsGetResponseData
from .logs_get_response_meta import LogsGetResponseMeta


class LogsGetResponse(UniversalBaseModel):
    success: bool
    data: LogsGetResponseData
    meta: typing.Optional[LogsGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
