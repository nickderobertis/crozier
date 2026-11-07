

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_body_errcode import BadRequestErrorBodyErrcode


class BadRequestErrorBody(UniversalBaseModel):
    """
    A Matrix-like error response
    """

    errcode: typing.Optional[BadRequestErrorBodyErrcode] = pydantic.Field(default=None)
    """
    A Matrix-like error code
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
