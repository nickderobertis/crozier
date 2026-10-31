

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_attempt import ExtractionAttempt
from .extraction_grounding_result import ExtractionGroundingResult
from .extraction_terminal_result_reasoning_effort import ExtractionTerminalResultReasoningEffort
from .extraction_usage_totals import ExtractionUsageTotals
from .job_id import JobId
from .lineage_document import LineageDocument
from .llm_model import LlmModel
from .parsed_document import ParsedDocument


class ExtractionTerminalResult(UniversalBaseModel):
    """
    Terminal extraction result returned by sync `200` and embedded in succeeded jobs.
    """

    output: typing.Any
    parsed_document: ParsedDocument
    llm_model: LlmModel
    parse_job_id: typing.Optional[JobId] = pydantic.Field(default=None)
    """
    Present only when extraction reused this source parse job without running OCR again.
    """

    reasoning_effort: typing.Optional[ExtractionTerminalResultReasoningEffort] = None
    attempts: typing.List[ExtractionAttempt]
    usage: typing.Optional[ExtractionUsageTotals] = None
    grounding: typing.Optional[ExtractionGroundingResult] = pydantic.Field(default=None)
    """
    Present only for successful `grounding: field` jobs. Omitted for ordinary extraction.
    """

    lineage: typing.Optional[LineageDocument] = pydantic.Field(default=None)
    """
    Portable `lineage@1` derivation DAG present with successful field grounding. It connects every output value to document evidence and the OCR/extraction activities that produced it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
