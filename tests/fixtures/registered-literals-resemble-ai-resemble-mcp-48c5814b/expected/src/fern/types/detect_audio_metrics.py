

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DetectAudioMetrics(UniversalBaseModel):
    """
    Audio detection metrics (for audio and video media types)
    """

    label: str = pydantic.Field()
    """
    Detection label (fake or real)
    """

    score: typing.List[str] = pydantic.Field()
    """
    Array of prediction scores per chunk
    """

    consistency: str = pydantic.Field()
    """
    Consistency metric across chunks
    """

    aggregated_score: str = pydantic.Field()
    """
    Overall aggregated detection score
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to visualization heatmap image (if visualize=true)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
