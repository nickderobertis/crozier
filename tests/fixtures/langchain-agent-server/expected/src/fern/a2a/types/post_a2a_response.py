

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_a2a_response_error import PostA2AResponseError
from .post_a2a_response_jsonrpc import PostA2AResponseJsonrpc


class PostA2AResponse(UniversalBaseModel):
    jsonrpc: PostA2AResponseJsonrpc
    id: str
    result: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Success result containing task information or task details
    """

    error: typing.Optional[PostA2AResponseError] = pydantic.Field(default=None)
    """
    Error information if request failed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
