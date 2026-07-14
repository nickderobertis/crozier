

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .analysis_archive_rules_summary import AnalysisArchiveRulesSummary
from .analysis_archive_summary import AnalysisArchiveSummary


class ArchiveSummary(UniversalBaseModel):
    """
    A summarization of the available archives, a place to for long-term storage of audit, analysis, or other data to remove it from the system's working set but keep it available.
    """

    images: typing.Optional[AnalysisArchiveSummary] = None
    rules: typing.Optional[AnalysisArchiveRulesSummary] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
