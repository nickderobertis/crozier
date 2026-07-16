

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_resource_summary_drift_information import StackResourceSummaryDriftInformation
from .stack_resource_summary_module_info import StackResourceSummaryModuleInfo
from .stack_resource_summary_resource_status import StackResourceSummaryResourceStatus


class StackResourceSummary(UniversalBaseModel):
    """
    Contains high-level information about the specified stack resource.
    """

    logical_resource_id: typing_extensions.Annotated[str, FieldMetadata(alias="LogicalResourceId")] = pydantic.Field()
    """
    The logical name of the resource specified in the template.
    """

    physical_resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PhysicalResourceId")
    ] = pydantic.Field(default=None)
    """
    The name or unique identifier that corresponds to a physical instance ID of the resource.
    """

    resource_type: typing_extensions.Annotated[str, FieldMetadata(alias="ResourceType")] = pydantic.Field()
    """
    Type of resource. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a> in the CloudFormation User Guide.)
    """

    last_updated_timestamp: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="LastUpdatedTimestamp")] = (
        pydantic.Field()
    )
    """
    Time the status was updated.
    """

    resource_status: typing_extensions.Annotated[
        StackResourceSummaryResourceStatus, FieldMetadata(alias="ResourceStatus")
    ] = pydantic.Field()
    """
    Current status of the resource.
    """

    resource_status_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ResourceStatusReason")
    ] = pydantic.Field(default=None)
    """
    Success/failure message associated with the resource.
    """

    drift_information: typing_extensions.Annotated[
        typing.Optional[StackResourceSummaryDriftInformation], FieldMetadata(alias="DriftInformation")
    ] = pydantic.Field(default=None)
    """
    Information about whether the resource's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.
    """

    module_info: typing_extensions.Annotated[
        typing.Optional[StackResourceSummaryModuleInfo], FieldMetadata(alias="ModuleInfo")
    ] = pydantic.Field(default=None)
    """
    Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
