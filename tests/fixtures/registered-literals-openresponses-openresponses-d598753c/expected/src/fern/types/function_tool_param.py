

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .empty_model_param import EmptyModelParam
from .function_tool_param_type import FunctionToolParamType


class FunctionToolParam(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    parameters: typing.Optional[EmptyModelParam] = None
    strict: typing.Optional[bool] = None
    type: FunctionToolParamType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
