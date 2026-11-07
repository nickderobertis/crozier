

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_response_error_code import ErrorResponseErrorCode


class ErrorResponse(UniversalBaseModel):
    status: typing.Optional[int] = None
    message: typing.Optional[str] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[ErrorResponseErrorCode], FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")
    ] = None
    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
