

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.function_type_enum import FunctionTypeEnum
from ...types.prompt_data import PromptData


class RunEvalScoresItemName(UniversalBaseModel):
    """
    Inline prompt definition
    """

    inline_prompt: PromptData
    function_type: typing.Optional[FunctionTypeEnum] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the inline prompt
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
