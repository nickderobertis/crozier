

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_type_enum import FunctionTypeEnum


class FunctionIdGlobalFunction(UniversalBaseModel):
    """
    Global function name
    """

    global_function: str = pydantic.Field()
    """
    The name of the global function. Currently, the global namespace includes the functions in autoevals
    """

    function_type: typing.Optional[FunctionTypeEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
