

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_analysis200response_current_findings_item import DocVersionsAnalysis200ResponseCurrentFindingsItem
from .doc_versions_analysis200response_current_method import DocVersionsAnalysis200ResponseCurrentMethod
from .doc_versions_analysis200response_current_primary import DocVersionsAnalysis200ResponseCurrentPrimary
from .doc_versions_analysis200response_current_verdict import DocVersionsAnalysis200ResponseCurrentVerdict


class DocVersionsAnalysis200ResponseCurrent(UniversalBaseModel):
    verdict: DocVersionsAnalysis200ResponseCurrentVerdict
    complete: bool
    primary: typing.Optional[DocVersionsAnalysis200ResponseCurrentPrimary] = None
    findings: typing.List[DocVersionsAnalysis200ResponseCurrentFindingsItem]
    method: DocVersionsAnalysis200ResponseCurrentMethod

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
