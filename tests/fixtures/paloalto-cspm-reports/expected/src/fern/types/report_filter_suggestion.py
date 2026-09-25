

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .report_filter_suggestion_account_group import ReportFilterSuggestionAccountGroup
from .report_filter_suggestion_cloud_account import ReportFilterSuggestionCloudAccount
from .report_filter_suggestion_cloud_region import ReportFilterSuggestionCloudRegion
from .report_filter_suggestion_cloud_type import ReportFilterSuggestionCloudType
from .report_filter_suggestion_policy_compliance_standard import ReportFilterSuggestionPolicyComplianceStandard
from .report_filter_suggestion_report_email_recipients import ReportFilterSuggestionReportEmailRecipients
from .report_filter_suggestion_report_frequency import ReportFilterSuggestionReportFrequency
from .report_filter_suggestion_report_schedule import ReportFilterSuggestionReportSchedule
from .report_filter_suggestion_schedule_status import ReportFilterSuggestionScheduleStatus


class ReportFilterSuggestion(UniversalBaseModel):
    """
    Model for ReportFilterSuggestion
    """

    account_group: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionAccountGroup],
        FieldMetadata(alias="account.group"),
        pydantic.Field(alias="account.group", description="Account group"),
    ] = None
    """
    Account group
    """

    cloud_account: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionCloudAccount],
        FieldMetadata(alias="cloud.account"),
        pydantic.Field(alias="cloud.account", description="Cloud account"),
    ] = None
    """
    Cloud account
    """

    cloud_region: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionCloudRegion],
        FieldMetadata(alias="cloud.region"),
        pydantic.Field(alias="cloud.region", description="Cloud region"),
    ] = None
    """
    Cloud region
    """

    cloud_type: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionCloudType],
        FieldMetadata(alias="cloud.type"),
        pydantic.Field(alias="cloud.type", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    policy_compliance_standard: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionPolicyComplianceStandard],
        FieldMetadata(alias="policy.complianceStandard"),
        pydantic.Field(alias="policy.complianceStandard", description="Policy compliance standard"),
    ] = None
    """
    Policy compliance standard
    """

    report_email_recipients: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionReportEmailRecipients],
        FieldMetadata(alias="report.email.recipients"),
        pydantic.Field(alias="report.email.recipients", description="Report email recepients"),
    ] = None
    """
    Report email recepients
    """

    report_frequency: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionReportFrequency],
        FieldMetadata(alias="report.frequency"),
        pydantic.Field(alias="report.frequency", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    report_schedule: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionReportSchedule],
        FieldMetadata(alias="report.schedule"),
        pydantic.Field(alias="report.schedule", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    schedule_status: typing_extensions.Annotated[
        typing.Optional[ReportFilterSuggestionScheduleStatus],
        FieldMetadata(alias="schedule.status"),
        pydantic.Field(alias="schedule.status", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
