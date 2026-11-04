

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_text_content_param_type import InputTextContentParamType


class InputTextContentParam(UniversalBaseModel):
    """
    A text input to the model.
    """

    type: InputTextContentParamType = pydantic.Field()
    """
    The type of the input item. Always `input_text`.
    """

    text: str = pydantic.Field()
    """
    The text input to the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
