

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_spapi_import_report_proposal_payload import AmazonSpapiImportReportProposalPayload
from .proposal_risk import ProposalRisk


class AmazonSpapiImportReportProposalCreateRequest(UniversalBaseModel):
    daily_ops_run_id: str
    priority_rank: int
    rollback_plan: str
    payload: AmazonSpapiImportReportProposalPayload
    risk: ProposalRisk
    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
