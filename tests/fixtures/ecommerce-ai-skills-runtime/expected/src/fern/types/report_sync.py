

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .report_recipe_amazon_report_type import ReportRecipeAmazonReportType
from .report_recipe_evidence_report_type import ReportRecipeEvidenceReportType
from .report_recipe_key import ReportRecipeKey
from .report_sync_processing_status import ReportSyncProcessingStatus
from .report_sync_status import ReportSyncStatus


class ReportSync(UniversalBaseModel):
    id: str
    tenant_id: str
    recipe_id: str
    connector_account_id: str
    created_by: str
    amazon_report_id: typing.Optional[str] = None
    status: ReportSyncStatus
    processing_status: typing.Optional[ReportSyncProcessingStatus] = None
    period_start: dt.datetime
    period_end: dt.datetime
    available_at: dt.datetime
    attempt_count: int
    max_attempts: int
    evidence_import_id: typing.Optional[str] = None
    error_code: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    recipe_key: ReportRecipeKey
    amazon_report_type: ReportRecipeAmazonReportType
    evidence_report_type: ReportRecipeEvidenceReportType
    created_at: dt.datetime
    updated_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
