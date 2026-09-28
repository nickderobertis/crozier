

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monitored_resource import MonitoredResource


class IncidentList(UniversalBaseModel):
    """
    A widget that displays a list of incidents
    """

    monitored_resources: typing_extensions.Annotated[
        typing.Optional[typing.List[MonitoredResource]],
        FieldMetadata(alias="monitoredResources"),
        pydantic.Field(
            alias="monitoredResources",
            description="Optional. The monitored resource for which incidents are listed. The resource doesn't need to be fully specified. That is, you can specify the resource type but not the values of the resource labels. The resource type and labels are used for filtering.",
        ),
    ] = None
    """
    Optional. The monitored resource for which incidents are listed. The resource doesn't need to be fully specified. That is, you can specify the resource type but not the values of the resource labels. The resource type and labels are used for filtering.
    """

    policy_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="policyNames"),
        pydantic.Field(
            alias="policyNames",
            description="Optional. A list of alert policy names to filter the incident list by. Don't include the project ID prefix in the policy name. For example, use alertPolicies/utilization.",
        ),
    ] = None
    """
    Optional. A list of alert policy names to filter the incident list by. Don't include the project ID prefix in the policy name. For example, use alertPolicies/utilization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
