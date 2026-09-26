

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_response_error import ErrorResponseError
from .rest_api_response_meta import RestApiResponseMeta


class ErrorResponse(UniversalBaseModel):
    success: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the request was successful
    """

    error: ErrorResponseError
    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Response data
    """

    meta: typing.Optional[RestApiResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
