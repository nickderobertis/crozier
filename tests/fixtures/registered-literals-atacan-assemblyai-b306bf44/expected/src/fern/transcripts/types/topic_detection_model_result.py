

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio_intelligence_model_status import AudioIntelligenceModelStatus
from .topic_detection_result import TopicDetectionResult


class TopicDetectionModelResult(UniversalBaseModel):
    """
    The result of the Topic Detection model, if it is enabled.
    See [Topic Detection](https://www.assemblyai.com/docs/models/topic-detection) for more information.
    """

    status: typing.Optional[AudioIntelligenceModelStatus] = pydantic.Field(default=None)
    """
    The status of the Topic Detection model. Either success, or unavailable in the rare case that the model failed.
    """

    results: typing.Optional[typing.List[TopicDetectionResult]] = pydantic.Field(default=None)
    """
    An array of results for the Topic Detection model
    """

    summary: typing.Optional[typing.Dict[str, float]] = pydantic.Field(default=None)
    """
    The overall relevance of topic to the entire audio file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
