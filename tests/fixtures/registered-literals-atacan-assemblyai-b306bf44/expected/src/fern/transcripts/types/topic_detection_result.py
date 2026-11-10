

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp import Timestamp
from .topic_detection_result_labels_item import TopicDetectionResultLabelsItem


class TopicDetectionResult(UniversalBaseModel):
    """
    The result of the topic detection model
    """

    text: str = pydantic.Field()
    """
    The text in the transcript in which a detected topic occurs
    """

    labels: typing.Optional[typing.List[TopicDetectionResultLabelsItem]] = pydantic.Field(default=None)
    """
    An array of detected topics in the text
    """

    timestamp: typing.Optional[Timestamp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
