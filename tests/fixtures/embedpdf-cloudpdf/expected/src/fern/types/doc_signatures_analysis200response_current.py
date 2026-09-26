

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_analysis200response_current_findings_item import (
    DocSignaturesAnalysis200ResponseCurrentFindingsItem,
)
from .doc_signatures_analysis200response_current_method import DocSignaturesAnalysis200ResponseCurrentMethod
from .doc_signatures_analysis200response_current_primary import DocSignaturesAnalysis200ResponseCurrentPrimary
from .doc_signatures_analysis200response_current_verdict import DocSignaturesAnalysis200ResponseCurrentVerdict


class DocSignaturesAnalysis200ResponseCurrent(UniversalBaseModel):
    verdict: DocSignaturesAnalysis200ResponseCurrentVerdict
    complete: bool
    primary: typing.Optional[DocSignaturesAnalysis200ResponseCurrentPrimary] = None
    findings: typing.List[DocSignaturesAnalysis200ResponseCurrentFindingsItem]
    method: DocSignaturesAnalysis200ResponseCurrentMethod

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
