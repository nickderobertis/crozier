

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_input_style_types import TextInputStyleTypes


class TextInputComponentForModalRequest(UniversalBaseModel):
    type: int
    custom_id: str
    style: TextInputStyleTypes
    label: str
    value: typing.Optional[str] = None
    placeholder: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    min_length: typing.Optional[int] = None
    max_length: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
