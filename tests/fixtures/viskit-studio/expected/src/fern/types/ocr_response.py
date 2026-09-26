

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_box_out import TextBoxOut


class OcrResponse(UniversalBaseModel):
    available: typing.Optional[bool] = None
    boxes: typing.List[TextBoxOut]
    engine: str
    unavailable_reason: typing.Optional[str] = None
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
