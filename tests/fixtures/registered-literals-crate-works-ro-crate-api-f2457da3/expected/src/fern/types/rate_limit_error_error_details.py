

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RateLimitErrorErrorDetails(UniversalBaseModel):
    """
    Additional error details specific to the error type
    """

    retry_after: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="retryAfter"),
        pydantic.Field(alias="retryAfter", description="Number of seconds to wait before retrying"),
    ] = None
    """
    Number of seconds to wait before retrying
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
