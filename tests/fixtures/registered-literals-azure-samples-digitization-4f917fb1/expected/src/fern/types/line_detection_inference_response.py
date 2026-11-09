

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_details import ImageDetails
from .line_segment import LineSegment


class LineDetectionInferenceResponse(UniversalBaseModel):
    """
    This class represents the response of the line detection service.
    """

    image_url: str
    image_details: ImageDetails
    line_segments_count: int
    line_segments: typing.List[LineSegment]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
