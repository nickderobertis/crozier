

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_attribution_model import AlertAttributionModel
from .alert_model_investigate_options import AlertModelInvestigateOptions
from .alert_model_risk_detail import AlertModelRiskDetail
from .alert_model_status import AlertModelStatus
from .cloud_resource_model import CloudResourceModel
from .connection_detail import ConnectionDetail
from .history_model import HistoryModel
from .policy_model import PolicyModel
from .policy_scan_config_model import PolicyScanConfigModel


class AlertModel(UniversalBaseModel):
    """
    Model for Alert
    """

    alert_additional_info: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="alertAdditionalInfo"),
        pydantic.Field(alias="alertAdditionalInfo"),
    ] = None
    alert_attribution: typing_extensions.Annotated[
        typing.Optional[AlertAttributionModel],
        FieldMetadata(alias="alertAttribution"),
        pydantic.Field(alias="alertAttribution"),
    ] = None
    alert_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="alertCount"), pydantic.Field(alias="alertCount")
    ] = None
    alert_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[PolicyScanConfigModel]],
        FieldMetadata(alias="alertRules"),
        pydantic.Field(alias="alertRules"),
    ] = None
    alert_time: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="alertTime"),
        pydantic.Field(
            alias="alertTime",
            description="Timestamp when alert was last reopened for resource update, or the same as **firstSeen** if there are no status changes.",
        ),
    ] = None
    """
    Timestamp when alert was last reopened for resource update, or the same as **firstSeen** if there are no status changes.
    """

    app_metadata: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, str]]],
        FieldMetadata(alias="appMetadata"),
        pydantic.Field(alias="appMetadata", description="Application Metadata from AppDna"),
    ] = None
    """
    Application Metadata from AppDna
    """

    connection_details: typing_extensions.Annotated[
        typing.Optional[typing.List[ConnectionDetail]],
        FieldMetadata(alias="connectionDetails"),
        pydantic.Field(alias="connectionDetails", description="ConnectionDetails for network_event alerts"),
    ] = None
    """
    ConnectionDetails for network_event alerts
    """

    dismissal_duration: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dismissalDuration"),
        pydantic.Field(alias="dismissalDuration", description="Dismissal Duration"),
    ] = None
    """
    Dismissal Duration
    """

    dismissal_note: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dismissalNote"),
        pydantic.Field(alias="dismissalNote", description="Dismissal note"),
    ] = None
    """
    Dismissal note
    """

    dismissal_until_ts: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="dismissalUntilTs"),
        pydantic.Field(alias="dismissalUntilTs", description="Dismiss until this timestamp"),
    ] = None
    """
    Dismiss until this timestamp
    """

    dismissed_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dismissedBy"),
        pydantic.Field(alias="dismissedBy", description="Dismissed by"),
    ] = None
    """
    Dismissed by
    """

    event_occurred: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="eventOccurred"),
        pydantic.Field(
            alias="eventOccurred", description="Timestamp when the event occurred. Set only for Audit Event policies."
        ),
    ] = None
    """
    Timestamp when the event occurred. Set only for Audit Event policies.
    """

    first_seen: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="firstSeen"),
        pydantic.Field(
            alias="firstSeen",
            description="Timestamp of the first policy violation for the alert resource (i.e. the alert creation timestamp)",
        ),
    ] = None
    """
    Timestamp of the first policy violation for the alert resource (i.e. the alert creation timestamp)
    """

    history: typing.Optional[typing.List[HistoryModel]] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Alert ID
    """

    investigate_options: typing_extensions.Annotated[
        typing.Optional[AlertModelInvestigateOptions],
        FieldMetadata(alias="investigateOptions"),
        pydantic.Field(alias="investigateOptions", description="Investigate Options for search using RQL"),
    ] = None
    """
    Investigate Options for search using RQL
    """

    last_seen: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastSeen"),
        pydantic.Field(alias="lastSeen", description="Timestamp when alert status was last updated."),
    ] = None
    """
    Timestamp when alert status was last updated.
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(
            alias="lastUpdated",
            description="Timestamp when alert was last updated. Updates include but are not limited to resource updates, policy updates, alert rule updates, and alert status changes.",
        ),
    ] = None
    """
    Timestamp when alert was last updated. Updates include but are not limited to resource updates, policy updates, alert rule updates, and alert status changes.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Raw JSON metadata for the alert
    """

    policy: typing.Optional[PolicyModel] = None
    policy_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="policyId"), pydantic.Field(alias="policyId", description="Policy ID")
    ] = None
    """
    Policy ID
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for an alert's status. For more information on Alert reasons see [View and Respond to Prisma Cloud Alerts](https://docs.prismacloud.io/en/enterprise-edition/content-collections/alerts/view-respond-to-prisma-cloud-alerts) and [Prisma Cloud Alert Resolution Reasons](https://docs.prismacloud.io/en/enterprise-edition/content-collections/alerts/prisma-cloud-alert-resolution-reasons)
    """

    resource: typing.Optional[CloudResourceModel] = None
    risk_detail: typing_extensions.Annotated[
        typing.Optional[AlertModelRiskDetail],
        FieldMetadata(alias="riskDetail"),
        pydantic.Field(alias="riskDetail", description="Risk detail (Deprecated)"),
    ] = None
    """
    Risk detail (Deprecated)
    """

    save_search_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="saveSearchId"),
        pydantic.Field(alias="saveSearchId", description="Saved Search ID"),
    ] = None
    """
    Saved Search ID
    """

    status: typing.Optional[AlertModelStatus] = pydantic.Field(default=None)
    """
    Status
    """

    triggered_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="triggeredBy"),
        pydantic.Field(alias="triggeredBy", description="Triggered By"),
    ] = None
    """
    Triggered By
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
