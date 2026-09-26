

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_part_input_time import TextPartInputTime


class TextPartInput(UniversalBaseModel):
    id: typing.Optional[str] = None
    text: str
    synthetic: typing.Optional[bool] = None
    ignored: typing.Optional[bool] = None
    time: typing.Optional[TextPartInputTime] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
