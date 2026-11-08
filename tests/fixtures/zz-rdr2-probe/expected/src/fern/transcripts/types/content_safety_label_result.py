

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_safety_label import ContentSafetyLabel
from .timestamp import Timestamp


class ContentSafetyLabelResult(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The transcript of the section flagged by the Content Moderation model
    """

    labels: typing.List[ContentSafetyLabel] = pydantic.Field()
    """
    An array of safety labels, one per sensitive topic that was detected in the section
    """

    sentences_idx_start: int = pydantic.Field()
    """
    The sentence index at which the section begins
    """

    sentences_idx_end: int = pydantic.Field()
    """
    The sentence index at which the section ends
    """

    timestamp: Timestamp = pydantic.Field()
    """
    Timestamp information for the section
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
