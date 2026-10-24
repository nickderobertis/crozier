

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .evidence_report_type import EvidenceReportType


class AmazonReportImportActionRequestPayload(UniversalBaseModel):
    external_account_id: str
    report_id: str
    evidence_report_type: EvidenceReportType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
