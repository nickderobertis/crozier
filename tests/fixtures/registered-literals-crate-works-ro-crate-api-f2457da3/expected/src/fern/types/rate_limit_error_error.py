

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rate_limit_error_error_code import RateLimitErrorErrorCode
from .rate_limit_error_error_details import RateLimitErrorErrorDetails


class RateLimitErrorError(UniversalBaseModel):
    code: RateLimitErrorErrorCode
    message: str = pydantic.Field()
    """
    Human-readable error message
    """

    details: typing.Optional[RateLimitErrorErrorDetails] = pydantic.Field(default=None)
    """
    Additional error details specific to the error type
    """

    request_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique identifier for this request, useful for debugging"),
    ] = None
    """
    Unique identifier for this request, useful for debugging
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
