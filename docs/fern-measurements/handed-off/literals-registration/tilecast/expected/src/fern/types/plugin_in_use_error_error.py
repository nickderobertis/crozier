

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plugin_in_use_error_error_code import PluginInUseErrorErrorCode
from .plugin_in_use_error_error_details import PluginInUseErrorErrorDetails


class PluginInUseErrorError(UniversalBaseModel):
    code: PluginInUseErrorErrorCode
    message: str
    details: PluginInUseErrorErrorDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
