

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rest_api_response_error import RestApiResponseError
from .rest_api_response_meta import RestApiResponseMeta


class RestApiResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether the request was successful
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Response data
    """

    error: typing.Optional[RestApiResponseError] = None
    meta: typing.Optional[RestApiResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
