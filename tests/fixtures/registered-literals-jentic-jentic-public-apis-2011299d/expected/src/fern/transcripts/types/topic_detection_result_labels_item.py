

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TopicDetectionResultLabelsItem(UniversalBaseModel):
    relevance: float = pydantic.Field()
    """
    How relevant the detected topic is of a detected topic
    """

    label: str = pydantic.Field()
    """
    The IAB taxonomical label for the label of the detected topic, where > denotes supertopic/subtopic relationship
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
