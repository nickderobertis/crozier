

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_rule_notification_config_model import AlertRuleNotificationConfigModel
from .policy_scan_config_model_target import PolicyScanConfigModelTarget


class PolicyScanConfigModel(UniversalBaseModel):
    """
    Model for Policy Scan Config
    """

    alert_rule_notification_config: typing_extensions.Annotated[
        typing.Optional[typing.List[AlertRuleNotificationConfigModel]],
        FieldMetadata(alias="alertRuleNotificationConfig"),
        pydantic.Field(
            alias="alertRuleNotificationConfig", description="List of data for notifications to third-party tools"
        ),
    ] = None
    """
    List of data for notifications to third-party tools
    """

    allow_auto_remediate: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowAutoRemediate"),
        pydantic.Field(alias="allowAutoRemediate", description="Allow Auto-Remediation"),
    ] = None
    """
    Allow Auto-Remediation
    """

    delay_notification_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="delayNotificationMs"),
        pydantic.Field(alias="delayNotificationMs", description="Delay notifications by the specified milliseconds"),
    ] = None
    """
    Delay notifications by the specified milliseconds
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rule/Scan description
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Rule/Scan is enabled
    """

    last_modified_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastModifiedBy"),
        pydantic.Field(alias="lastModifiedBy", description="Last modified by"),
    ] = None
    """
    Last modified by
    """

    last_modified_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastModifiedOn"),
        pydantic.Field(alias="lastModifiedOn", description="Last modified on this date/time in milliseconds"),
    ] = None
    """
    Last modified on this date/time in milliseconds
    """

    name: str = pydantic.Field()
    """
    Rule/Scan name
    """

    notify_on_dismissed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="notifyOnDismissed"),
        pydantic.Field(alias="notifyOnDismissed", description="include dismissed alerts in notification"),
    ] = None
    """
    include dismissed alerts in notification
    """

    notify_on_open: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="notifyOnOpen"),
        pydantic.Field(alias="notifyOnOpen", description="include open alerts in notification"),
    ] = None
    """
    include open alerts in notification
    """

    notify_on_resolved: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="notifyOnResolved"),
        pydantic.Field(alias="notifyOnResolved", description="include resolved alerts in notification"),
    ] = None
    """
    include resolved alerts in notification
    """

    notify_on_snoozed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="notifyOnSnoozed"),
        pydantic.Field(alias="notifyOnSnoozed", description="include snoozed alerts in notification"),
    ] = None
    """
    include snoozed alerts in notification
    """

    policies: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of specific policies to scan
    """

    policy_labels: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="policyLabels"),
        pydantic.Field(alias="policyLabels", description="Policy labels"),
    ] = None
    """
    Policy labels
    """

    policy_scan_config_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="policyScanConfigId"),
        pydantic.Field(alias="policyScanConfigId", description="Policy Scan Config ID"),
    ] = None
    """
    Policy Scan Config ID
    """

    scan_all: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="scanAll"),
        pydantic.Field(alias="scanAll", description="Scan all policies"),
    ] = None
    """
    Scan all policies
    """

    target: PolicyScanConfigModelTarget = pydantic.Field()
    """
    TargetFilter model (target accounts)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
