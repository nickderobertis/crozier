

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .summarization_request_body_summarization_effort import SummarizationRequestBodySummarizationEffort
from .summarization_request_body_summarization_summary_type import SummarizationRequestBodySummarizationSummaryType


class SummarizationRequestBodySummarization(UniversalBaseModel):
    summary_type: SummarizationRequestBodySummarizationSummaryType = pydantic.Field()
    """
    Type of summary. Bullets returns short bullet point style summaries, paragraph is generally more verbose and detailed.
    """

    effort: typing.Optional[SummarizationRequestBodySummarizationEffort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
