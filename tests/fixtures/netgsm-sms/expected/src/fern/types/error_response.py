

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_response import BaseResponse


class ErrorResponse(BaseResponse):
    jobs: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Empty report list
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
