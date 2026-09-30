

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The application error message
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The http error message
    """

    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    The http error code
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp the error occurred
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The path of the request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
