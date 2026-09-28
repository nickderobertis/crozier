

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_tool_name_post_error400error import ToolsToolNamePostError400Error
from .tools_tool_name_post_error400meta import ToolsToolNamePostError400Meta


class ToolsToolNamePostError400(UniversalBaseModel):
    success: bool
    error: ToolsToolNamePostError400Error
    meta: typing.Optional[ToolsToolNamePostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
