

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .summarization_request_body_summarization import SummarizationRequestBodySummarization


class SummarizationRequestBody(UniversalBaseModel):
    """
    Request body for [Summarization](https://www.assemblyai.com/docs/speech-understanding/summarization).
    """

    summarization: SummarizationRequestBodySummarization

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
