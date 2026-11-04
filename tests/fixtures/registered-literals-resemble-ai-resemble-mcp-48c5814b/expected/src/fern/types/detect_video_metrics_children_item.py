

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .detect_video_metrics_children_item_children_item import DetectVideoMetricsChildrenItemChildrenItem


class DetectVideoMetricsChildrenItem(UniversalBaseModel):
    type: str
    conclusion: str
    score: float
    certainty: float
    certainty_: typing_extensions.Annotated[
        str, FieldMetadata(alias="certainty (%)"), pydantic.Field(alias="certainty (%)")
    ]
    children: typing.List[DetectVideoMetricsChildrenItemChildrenItem] = pydantic.Field()
    """
    Frame-level detection results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
