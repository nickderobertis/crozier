

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_get_error500error import ToolsGetError500Error
from .tools_get_error500meta import ToolsGetError500Meta


class ToolsGetError500(UniversalBaseModel):
    success: bool
    error: ToolsGetError500Error
    meta: typing.Optional[ToolsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
