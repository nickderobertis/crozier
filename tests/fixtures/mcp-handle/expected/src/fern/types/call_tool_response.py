

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .call_tool_result import CallToolResult


class CallToolResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether the API call was successful
    """

    result: typing.Optional[CallToolResult] = pydantic.Field(default=None)
    """
    The result of the tool call, if successful
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message, if the tool call failed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
