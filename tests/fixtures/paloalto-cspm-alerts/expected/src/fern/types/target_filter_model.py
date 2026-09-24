

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .target_filter_model_alert_rule_policy_filter import TargetFilterModelAlertRulePolicyFilter
from .target_filter_model_included_resource_lists import TargetFilterModelIncludedResourceLists
from .target_tag_model import TargetTagModel


class TargetFilterModel(UniversalBaseModel):
    """
    Model for Target Filter
    """

    account_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="accountGroups"),
        pydantic.Field(alias="accountGroups", description="List of Account group(s)"),
    ] = None
    """
    List of Account group(s)
    """

    alert_rule_policy_filter: typing_extensions.Annotated[
        typing.Optional[TargetFilterModelAlertRulePolicyFilter],
        FieldMetadata(alias="alertRulePolicyFilter"),
        pydantic.Field(alias="alertRulePolicyFilter", description="Policy Filters for the Alert Rule"),
    ] = None
    """
    Policy Filters for the Alert Rule
    """

    excluded_accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="excludedAccounts"),
        pydantic.Field(alias="excludedAccounts", description="List of excluded accounts"),
    ] = None
    """
    List of excluded accounts
    """

    included_resource_lists: typing_extensions.Annotated[
        typing.Optional[TargetFilterModelIncludedResourceLists],
        FieldMetadata(alias="includedResourceLists"),
        pydantic.Field(
            alias="includedResourceLists",
            description="List of resource lists included which the resource has to match on.",
        ),
    ] = None
    """
    List of resource lists included which the resource has to match on.
    """

    regions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of regions for which alerts will be triggered for account groups. Alerts not associated with specific regions will be triggered regardless of listed regions. If no regions are specified, then the alerts will be triggered for all regions.
    """

    tags: typing.Optional[typing.List[TargetTagModel]] = pydantic.Field(default=None)
    """
    List of TargetTag models (resource tags) for which alerts should be triggered
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
