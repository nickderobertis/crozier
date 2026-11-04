

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetWatermarkDetectionResultResponseItemMetrics(UniversalBaseModel):
    """
    Detection results including has_watermark. Audio also includes confidence.
    """

    has_watermark: typing.Optional[bool] = None
    confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    Confidence score (audio only).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
