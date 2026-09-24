

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_rule_policy_filter_cloud_type_item import AlertRulePolicyFilterCloudTypeItem


class AlertRulePolicyFilter(UniversalBaseModel):
    """
    Model for Alert Rule Policy Filter
    """

    available_policy_filters: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="availablePolicyFilters"),
        pydantic.Field(alias="availablePolicyFilters", description="List of available Alert Rule Policy Filters"),
    ] = None
    """
    List of available Alert Rule Policy Filters
    """

    cloud_type: typing_extensions.Annotated[
        typing.Optional[typing.List[AlertRulePolicyFilterCloudTypeItem]],
        FieldMetadata(alias="cloud.type"),
        pydantic.Field(alias="cloud.type", description="Cloud Type Filter"),
    ] = None
    """
    Cloud Type Filter
    """

    policy_compliance_standard: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="policy.complianceStandard"),
        pydantic.Field(alias="policy.complianceStandard", description="Compliance Standard Filter"),
    ] = None
    """
    Compliance Standard Filter
    """

    policy_label: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="policy.label"),
        pydantic.Field(alias="policy.label", description="Policy Label Filter"),
    ] = None
    """
    Policy Label Filter
    """

    policy_severity: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="policy.severity"),
        pydantic.Field(alias="policy.severity", description="Policy Severity Filter"),
    ] = None
    """
    Policy Severity Filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
