

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_get_response_data_tools_item import ToolsGetResponseDataToolsItem


class ToolsGetResponseData(UniversalBaseModel):
    tools: typing.List[ToolsGetResponseDataToolsItem] = pydantic.Field()
    """
    List of available tools
    """

    total: float = pydantic.Field()
    """
    Total number of tools
    """

    categories: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Available categories
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Available tags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
