

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_response import BaseResponse


class CancelErrorResponse(BaseResponse):
    jobid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job ID of the SMS that failed to cancel
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
