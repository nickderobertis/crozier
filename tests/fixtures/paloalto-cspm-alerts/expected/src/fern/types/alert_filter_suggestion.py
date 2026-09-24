

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_filter_suggestion_alert_id import AlertFilterSuggestionAlertId
from .alert_filter_suggestion_alert_status import AlertFilterSuggestionAlertStatus
from .alert_filter_suggestion_cloud_type import AlertFilterSuggestionCloudType
from .alert_filter_suggestion_policy_remediable import AlertFilterSuggestionPolicyRemediable
from .alert_filter_suggestion_policy_subtype import AlertFilterSuggestionPolicySubtype
from .alert_filter_suggestion_risk_grade import AlertFilterSuggestionRiskGrade
from .filter_suggestion import FilterSuggestion


class AlertFilterSuggestion(UniversalBaseModel):
    """
    Model for AlertFilterSuggestion
    """

    account_group: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="account.group"), pydantic.Field(alias="account.group")
    ] = None
    alert_id: typing_extensions.Annotated[
        typing.Optional[AlertFilterSuggestionAlertId],
        FieldMetadata(alias="alert.id"),
        pydantic.Field(alias="alert.id", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    alert_status: typing_extensions.Annotated[
        typing.Optional[AlertFilterSuggestionAlertStatus],
        FieldMetadata(alias="alert.status"),
        pydantic.Field(alias="alert.status", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    alert_rule_name: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="alertRule.name"), pydantic.Field(alias="alertRule.name")
    ] = None
    asset_class: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="asset.class"), pydantic.Field(alias="asset.class")
    ] = None
    buildtime_resource_name: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="buildtime.resourceName"),
        pydantic.Field(alias="buildtime.resourceName"),
    ] = None
    cloud_account: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="cloud.account"), pydantic.Field(alias="cloud.account")
    ] = None
    cloud_account_id: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="cloud.accountId"),
        pydantic.Field(alias="cloud.accountId"),
    ] = None
    cloud_region: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="cloud.region"), pydantic.Field(alias="cloud.region")
    ] = None
    cloud_service: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="cloud.service"), pydantic.Field(alias="cloud.service")
    ] = None
    cloud_type: typing_extensions.Annotated[
        typing.Optional[AlertFilterSuggestionCloudType],
        FieldMetadata(alias="cloud.type"),
        pydantic.Field(alias="cloud.type", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    git_filename: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="git.filename"), pydantic.Field(alias="git.filename")
    ] = None
    git_provider: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="git.provider"), pydantic.Field(alias="git.provider")
    ] = None
    git_repository: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="git.repository"), pydantic.Field(alias="git.repository")
    ] = None
    iac_framework: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="iac.framework"), pydantic.Field(alias="iac.framework")
    ] = None
    malware: typing.Optional[FilterSuggestion] = None
    object_classification: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="object.classification"),
        pydantic.Field(alias="object.classification"),
    ] = None
    object_exposure: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="object.exposure"),
        pydantic.Field(alias="object.exposure"),
    ] = None
    object_identifier: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="object.identifier"),
        pydantic.Field(alias="object.identifier"),
    ] = None
    policy_compliance_requirement: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="policy.complianceRequirement"),
        pydantic.Field(alias="policy.complianceRequirement"),
    ] = None
    policy_compliance_section: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="policy.complianceSection"),
        pydantic.Field(alias="policy.complianceSection"),
    ] = None
    policy_compliance_standard: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="policy.complianceStandard"),
        pydantic.Field(alias="policy.complianceStandard"),
    ] = None
    policy_label: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="policy.label"), pydantic.Field(alias="policy.label")
    ] = None
    policy_name: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="policy.name"), pydantic.Field(alias="policy.name")
    ] = None
    policy_remediable: typing_extensions.Annotated[
        typing.Optional[AlertFilterSuggestionPolicyRemediable],
        FieldMetadata(alias="policy.remediable"),
        pydantic.Field(alias="policy.remediable", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    policy_severity: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="policy.severity"),
        pydantic.Field(alias="policy.severity"),
    ] = None
    policy_subtype: typing_extensions.Annotated[
        typing.Optional[AlertFilterSuggestionPolicySubtype],
        FieldMetadata(alias="policy.subtype"),
        pydantic.Field(alias="policy.subtype", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    policy_type: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="policy.type"), pydantic.Field(alias="policy.type")
    ] = None
    resource_group: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="resource.group"), pydantic.Field(alias="resource.group")
    ] = None
    resource_id: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="resource.id"), pydantic.Field(alias="resource.id")
    ] = None
    resource_name: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="resource.name"), pydantic.Field(alias="resource.name")
    ] = None
    resource_tagv2: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="resource.tagv2"), pydantic.Field(alias="resource.tagv2")
    ] = None
    resource_type: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="resource.type"), pydantic.Field(alias="resource.type")
    ] = None
    risk_grade: typing_extensions.Annotated[
        typing.Optional[AlertFilterSuggestionRiskGrade],
        FieldMetadata(alias="risk.grade"),
        pydantic.Field(alias="risk.grade", description="Model for FilterSuggestion"),
    ] = None
    """
    Model for FilterSuggestion
    """

    time_range_type: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion], FieldMetadata(alias="timeRange.type"), pydantic.Field(alias="timeRange.type")
    ] = None
    vulnerability_severity: typing_extensions.Annotated[
        typing.Optional[FilterSuggestion],
        FieldMetadata(alias="vulnerability.severity"),
        pydantic.Field(alias="vulnerability.severity"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
