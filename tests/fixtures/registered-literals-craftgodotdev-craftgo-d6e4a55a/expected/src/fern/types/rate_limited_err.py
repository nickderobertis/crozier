

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RateLimitedErr(UniversalBaseModel):
    """
    TooManyRequests error response (HTTP 429).
    """

    bucket: typing.Optional[str] = None
    retry_after: typing_extensions.Annotated[int, FieldMetadata(alias="retryAfter"), pydantic.Field(alias="retryAfter")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
