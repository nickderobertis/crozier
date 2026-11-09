

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio_intelligence_model_status import AudioIntelligenceModelStatus
from .content_safety_label_result import ContentSafetyLabelResult
from .severity_score_summary import SeverityScoreSummary


class ContentSafetyLabelsResult(UniversalBaseModel):
    """
    An array of results for the Content Moderation model, if it is enabled.
    See [Content moderation](https://www.assemblyai.com/docs/content-moderation) for more information.
    """

    status: typing.Optional[AudioIntelligenceModelStatus] = pydantic.Field(default=None)
    """
    The status of the Content Moderation model. Either success, or unavailable in the rare case that the model failed.
    """

    results: typing.Optional[typing.List[ContentSafetyLabelResult]] = pydantic.Field(default=None)
    """
    An array of results for the Content Moderation model
    """

    summary: typing.Optional[typing.Dict[str, float]] = pydantic.Field(default=None)
    """
    A summary of the Content Moderation confidence results for the entire audio file
    """

    severity_score_summary: typing.Optional[typing.Dict[str, SeverityScoreSummary]] = pydantic.Field(default=None)
    """
    A summary of the Content Moderation severity results for the entire audio file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
