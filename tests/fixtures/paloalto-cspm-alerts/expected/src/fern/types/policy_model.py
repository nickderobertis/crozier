

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .compliance_metadata_model import ComplianceMetadataModel
from .policy_model_cloud_type import PolicyModelCloudType
from .policy_model_policy_sub_types_item import PolicyModelPolicySubTypesItem
from .policy_model_policy_type import PolicyModelPolicyType
from .policy_model_remediation import PolicyModelRemediation
from .policy_model_rule import PolicyModelRule
from .policy_model_severity import PolicyModelSeverity


class PolicyModel(UniversalBaseModel):
    """
    Model for Policy
    """

    cloud_type: typing_extensions.Annotated[
        typing.Optional[PolicyModelCloudType],
        FieldMetadata(alias="cloudType"),
        pydantic.Field(
            alias="cloudType",
            description="Cloud type (Required for config policies). Not case-sensitive. Default is **ALL**.",
        ),
    ] = None
    """
    Cloud type (Required for config policies). Not case-sensitive. Default is **ALL**.
    """

    compliance_metadata: typing_extensions.Annotated[
        typing.Optional[typing.List[ComplianceMetadataModel]],
        FieldMetadata(alias="complianceMetadata"),
        pydantic.Field(
            alias="complianceMetadata",
            description="List of compliance data. Each item has compliance standard, requirement, and/or section information.",
        ),
    ] = None
    """
    List of compliance data. Each item has compliance standard, requirement, and/or section information.
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="Created by"),
    ] = None
    """
    Created by
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Created on this timestamp"),
    ] = None
    """
    Created on this timestamp
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deleted
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Policy description
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true=enabled. false=disabled.
    """

    finding_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="findingTypes"),
        pydantic.Field(alias="findingTypes", description="Finding Type"),
    ] = None
    """
    Finding Type
    """

    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Labels
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
        pydantic.Field(alias="lastModifiedOn", description="Last modified on this timestamp"),
    ] = None
    """
    Last modified on this timestamp
    """

    name: str = pydantic.Field()
    """
    Policy name
    """

    overridden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Overridden
    """

    policy_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="policyId"), pydantic.Field(alias="policyId", description="Policy ID")
    ] = None
    """
    Policy ID
    """

    policy_sub_types: typing_extensions.Annotated[
        typing.Optional[typing.List[PolicyModelPolicySubTypesItem]],
        FieldMetadata(alias="policySubTypes"),
        pydantic.Field(alias="policySubTypes", description="Policy subtype"),
    ] = None
    """
    Policy subtype
    """

    policy_type: typing_extensions.Annotated[
        PolicyModelPolicyType,
        FieldMetadata(alias="policyType"),
        pydantic.Field(alias="policyType", description="Policy type. Policy type **anomaly** is read-only."),
    ]
    """
    Policy type. Policy type **anomaly** is read-only.
    """

    policy_upi: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="policyUpi"),
        pydantic.Field(alias="policyUpi", description="Policy UPI"),
    ] = None
    """
    Policy UPI
    """

    recommendation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remediation recommendation
    """

    remediable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    isRemediable
    """

    remediation: typing.Optional[PolicyModelRemediation] = pydantic.Field(default=None)
    """
    Auto remediation info. Available only if policy is remediable.
    """

    restrict_alert_dismissal: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="restrictAlertDismissal"),
        pydantic.Field(alias="restrictAlertDismissal", description="Restrict alert dismissal"),
    ] = None
    """
    Restrict alert dismissal
    """

    rule: PolicyModelRule = pydantic.Field()
    """
    Policy rule (Contains RQL search query or saved search)
    """

    rule_last_modified_on: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ruleLastModifiedOn"),
        pydantic.Field(alias="ruleLastModifiedOn", description="Rule last modified on"),
    ] = None
    """
    Rule last modified on
    """

    severity: PolicyModelSeverity = pydantic.Field()
    """
    Severity
    """

    system_default: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="systemDefault"),
        pydantic.Field(alias="systemDefault", description="true = Policy is a Prisma Cloud system default policy"),
    ] = None
    """
    true = Policy is a Prisma Cloud system default policy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
