

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .report_recipe_amazon_report_type import ReportRecipeAmazonReportType
from .report_recipe_evidence_report_type import ReportRecipeEvidenceReportType
from .report_recipe_key import ReportRecipeKey


class ReportRecipe(UniversalBaseModel):
    id: str
    tenant_id: str
    connector_account_id: str
    created_by: str
    name: str
    recipe_key: ReportRecipeKey
    amazon_report_type: ReportRecipeAmazonReportType
    evidence_report_type: ReportRecipeEvidenceReportType
    marketplace_ids: typing.List[str]
    interval_minutes: int
    lookback_days: int
    enabled: bool
    next_run_at: dt.datetime
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
