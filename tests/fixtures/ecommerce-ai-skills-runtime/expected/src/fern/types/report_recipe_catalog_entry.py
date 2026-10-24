

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .report_recipe_amazon_report_type import ReportRecipeAmazonReportType
from .report_recipe_evidence_report_type import ReportRecipeEvidenceReportType
from .report_recipe_key import ReportRecipeKey


class ReportRecipeCatalogEntry(UniversalBaseModel):
    key: ReportRecipeKey
    label: str
    amazon_report_type: ReportRecipeAmazonReportType
    evidence_report_type: ReportRecipeEvidenceReportType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
