

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorResponse(UniversalBaseModel):
    error_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code identifier
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
