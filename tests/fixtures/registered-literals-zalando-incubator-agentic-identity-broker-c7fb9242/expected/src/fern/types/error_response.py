

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    error: str = pydantic.Field()
    """
    Machine-readable error code or type. Used for programmatic error handling.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional human-readable error message. Provides additional context about the error. May be empty for generic errors.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
