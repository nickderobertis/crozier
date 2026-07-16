

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_resource_drift_information import StackResourceDriftInformation
from .stack_resource_module_info import StackResourceModuleInfo
from .stack_resource_resource_status import StackResourceResourceStatus


class StackResource(UniversalBaseModel):
    """
    The StackResource data type.
    """

    stack_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackName")] = pydantic.Field(
        default=None
    )
    """
    The name associated with the stack.
    """

    stack_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackId")] = pydantic.Field(
        default=None
    )
    """
    Unique identifier of the stack.
    """

    logical_resource_id: typing_extensions.Annotated[str, FieldMetadata(alias="LogicalResourceId")] = pydantic.Field()
    """
    The logical name of the resource specified in the template.
    """

    physical_resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PhysicalResourceId")
    ] = pydantic.Field(default=None)
    """
    The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.
    """

    resource_type: typing_extensions.Annotated[str, FieldMetadata(alias="ResourceType")] = pydantic.Field()
    """
    Type of resource. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a> in the CloudFormation User Guide.
    """

    timestamp: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="Timestamp")] = pydantic.Field()
    """
    Time the status was updated.
    """

    resource_status: typing_extensions.Annotated[StackResourceResourceStatus, FieldMetadata(alias="ResourceStatus")] = (
        pydantic.Field()
    )
    """
    Current status of the resource.
    """

    resource_status_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ResourceStatusReason")
    ] = pydantic.Field(default=None)
    """
    Success/failure message associated with the resource.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    User defined description associated with the resource.
    """

    drift_information: typing_extensions.Annotated[
        typing.Optional[StackResourceDriftInformation], FieldMetadata(alias="DriftInformation")
    ] = pydantic.Field(default=None)
    """
    Information about whether the resource's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.
    """

    module_info: typing_extensions.Annotated[
        typing.Optional[StackResourceModuleInfo], FieldMetadata(alias="ModuleInfo")
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
