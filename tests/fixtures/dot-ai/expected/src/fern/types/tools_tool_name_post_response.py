

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_tool_name_post_response_data import ToolsToolNamePostResponseData
from .tools_tool_name_post_response_meta import ToolsToolNamePostResponseMeta


class ToolsToolNamePostResponse(UniversalBaseModel):
    success: bool
    data: ToolsToolNamePostResponseData
    meta: typing.Optional[ToolsToolNamePostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
