

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_tool_name_post_error500error import ToolsToolNamePostError500Error
from .tools_tool_name_post_error500meta import ToolsToolNamePostError500Meta


class ToolsToolNamePostError500(UniversalBaseModel):
    success: bool
    error: ToolsToolNamePostError500Error
    meta: typing.Optional[ToolsToolNamePostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
