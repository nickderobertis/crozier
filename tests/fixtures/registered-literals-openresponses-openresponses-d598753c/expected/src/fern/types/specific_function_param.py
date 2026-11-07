

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .specific_function_param_type import SpecificFunctionParamType


class SpecificFunctionParam(UniversalBaseModel):
    type: SpecificFunctionParamType = pydantic.Field()
    """
    The tool to call. Always `function`.
    """

    name: str = pydantic.Field()
    """
    The name of the function tool to call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
