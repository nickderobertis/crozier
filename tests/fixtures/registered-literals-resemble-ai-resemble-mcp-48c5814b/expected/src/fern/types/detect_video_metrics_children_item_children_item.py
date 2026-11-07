

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .detect_video_metrics_children_item_children_item_children_item import (
    DetectVideoMetricsChildrenItemChildrenItemChildrenItem,
)


class DetectVideoMetricsChildrenItemChildrenItem(UniversalBaseModel):
    type: str
    conclusion: str
    score: float
    certainty: float
    certainty_: typing_extensions.Annotated[
        str, FieldMetadata(alias="certainty (%)"), pydantic.Field(alias="certainty (%)")
    ]
    timestamp: float = pydantic.Field()
    """
    Timestamp in seconds
    """

    children: typing.List[DetectVideoMetricsChildrenItemChildrenItemChildrenItem] = pydantic.Field()
    """
    Segment-level detection results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
