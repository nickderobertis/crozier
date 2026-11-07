

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detect_video_metrics_children_item import DetectVideoMetricsChildrenItem


class DetectVideoMetrics(UniversalBaseModel):
    """
    Video detection metrics (for video media type)
    """

    label: str = pydantic.Field()
    """
    Overall video detection label
    """

    score: float = pydantic.Field()
    """
    Overall detection score
    """

    certainty: float = pydantic.Field()
    """
    Overall certainty score
    """

    treeview: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional tree visualization data
    """

    children: typing.List[DetectVideoMetricsChildrenItem] = pydantic.Field()
    """
    Hierarchical detection results across frames
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
