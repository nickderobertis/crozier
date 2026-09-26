

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_info import ToolInfo


class ToolDiscoveryResponseData(UniversalBaseModel):
    """
    Response data
    """

    tools: typing.Optional[typing.List[ToolInfo]] = None
    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total number of tools
    """

    categories: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Available tool categories
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Available tool tags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
