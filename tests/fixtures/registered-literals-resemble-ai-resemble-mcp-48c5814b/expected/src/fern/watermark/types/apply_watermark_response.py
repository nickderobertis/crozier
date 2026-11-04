

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apply_watermark_response_item import ApplyWatermarkResponseItem


class ApplyWatermarkResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    item: typing.Optional[ApplyWatermarkResponseItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
