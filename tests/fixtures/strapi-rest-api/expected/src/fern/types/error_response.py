

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_response_error import ErrorResponseError


class ErrorResponse(UniversalBaseModel):
    """
    Strapi's uniform error envelope.
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = None
    error: typing.Optional[ErrorResponseError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
