

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_tool_name_post_error404error import ToolsToolNamePostError404Error
from .tools_tool_name_post_error404meta import ToolsToolNamePostError404Meta


class ToolsToolNamePostError404(UniversalBaseModel):
    success: bool
    error: ToolsToolNamePostError404Error
    meta: typing.Optional[ToolsToolNamePostError404Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
