

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    Stable snake_case error code (e.g. ``validation_error``, ``unknown_model_version``, ``invalid_url``, ``invalid_api_key``, ``rate_limit_exceeded``).
    """

    message: str = pydantic.Field()
    """
    Human-readable detail.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
