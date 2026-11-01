

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_format import ToolFormat


class ListToolsResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether the list tools request was successful
    """

    tools: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    List of tools in the requested format
    """

    format: ToolFormat = pydantic.Field()
    """
    The format of the returned tools
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message, if the request failed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
