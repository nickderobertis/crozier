

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rest_api_response_error import RestApiResponseError
from .rest_api_response_meta import RestApiResponseMeta
from .tool_execution_response_data import ToolExecutionResponseData


class ToolExecutionResponse(UniversalBaseModel):
    data: typing.Optional[ToolExecutionResponseData] = pydantic.Field(default=None)
    """
    Response data
    """

    success: bool = pydantic.Field()
    """
    Whether the request was successful
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
