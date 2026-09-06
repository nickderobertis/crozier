

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_type_enum import FunctionTypeEnum
from .prompt_data import PromptData


class FunctionIdInlineFunction(UniversalBaseModel):
    """
    Inline function definition
    """

    inline_prompt: typing.Optional[PromptData] = None
    inline_function: typing.Dict[str, typing.Any]
    function_type: typing.Optional[FunctionTypeEnum] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the inline function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
