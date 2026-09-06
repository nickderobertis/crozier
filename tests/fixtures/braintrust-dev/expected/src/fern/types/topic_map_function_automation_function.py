

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_type_enum import FunctionTypeEnum
from .topic_map_function_automation_function_type import TopicMapFunctionAutomationFunctionType


class TopicMapFunctionAutomationFunction(UniversalBaseModel):
    type: typing.Optional[TopicMapFunctionAutomationFunctionType] = None
    id: typing.Optional[str] = None
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the function
    """

    name: typing.Optional[str] = None
    function_type: typing.Optional[FunctionTypeEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
