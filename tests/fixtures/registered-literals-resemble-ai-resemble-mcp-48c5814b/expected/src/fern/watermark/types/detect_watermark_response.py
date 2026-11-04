

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detect_watermark_response_item import DetectWatermarkResponseItem


class DetectWatermarkResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    item: typing.Optional[DetectWatermarkResponseItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
