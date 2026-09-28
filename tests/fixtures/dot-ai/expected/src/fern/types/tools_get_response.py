

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tools_get_response_data import ToolsGetResponseData
from .tools_get_response_meta import ToolsGetResponseMeta


class ToolsGetResponse(UniversalBaseModel):
    success: bool
    data: ToolsGetResponseData
    meta: typing.Optional[ToolsGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
