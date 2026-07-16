

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .physical_resource_id_context_key_value_pair import PhysicalResourceIdContextKeyValuePair
from .property_difference import PropertyDifference
from .stack_resource_drift_module_info import StackResourceDriftModuleInfo
from .stack_resource_drift_stack_resource_drift_status import StackResourceDriftStackResourceDriftStatus


class StackResourceDrift(UniversalBaseModel):
    """
    <p>Contains the drift information for a resource that has been checked for drift. This includes actual and expected property values for resources in which CloudFormation has detected drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p>
    """

    stack_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="StackId"), pydantic.Field(alias="StackId", description="The ID of the stack.")
    ]
    """
    The ID of the stack.
    """

    logical_resource_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogicalResourceId"),
        pydantic.Field(
            alias="LogicalResourceId", description="The logical name of the resource specified in the template."
        ),
    ]
    """
    The logical name of the resource specified in the template.
    """

    physical_resource_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PhysicalResourceId"),
        pydantic.Field(
            alias="PhysicalResourceId",
            description="The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.",
        ),
    ] = None
    """
    The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.
    """

    physical_resource_id_context: typing_extensions.Annotated[
        typing.Optional[typing.List[PhysicalResourceIdContextKeyValuePair]],
        FieldMetadata(alias="PhysicalResourceIdContext"),
        pydantic.Field(
            alias="PhysicalResourceIdContext",
            description="Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resource's logical and physical IDs aren't enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.",
        ),
    ] = None
    """
    Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resource's logical and physical IDs aren't enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.
    """

    resource_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ResourceType"),
        pydantic.Field(alias="ResourceType", description="The type of the resource."),
    ]
    """
    The type of the resource.
    """

    expected_properties: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExpectedProperties"),
        pydantic.Field(
            alias="ExpectedProperties",
            description="<p>A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>",
        ),
    ] = None
    """
    <p>A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>
    """

    actual_properties: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ActualProperties"),
        pydantic.Field(
            alias="ActualProperties",
            description="<p>A JSON structure containing the actual property values of the stack resource.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>",
        ),
    ] = None
    """
    <p>A JSON structure containing the actual property values of the stack resource.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>
    """

    property_differences: typing_extensions.Annotated[
        typing.Optional[typing.List[PropertyDifference]],
        FieldMetadata(alias="PropertyDifferences"),
        pydantic.Field(
            alias="PropertyDifferences",
            description="A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose <code>StackResourceDriftStatus</code> is <code>MODIFIED</code>.",
        ),
    ] = None
    """
    A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose <code>StackResourceDriftStatus</code> is <code>MODIFIED</code>.
    """

    stack_resource_drift_status: typing_extensions.Annotated[
        StackResourceDriftStackResourceDriftStatus,
        FieldMetadata(alias="StackResourceDriftStatus"),
        pydantic.Field(
            alias="StackResourceDriftStatus",
            description="<p>Status of the resource's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration because the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation does not currently return this value.</p> </li> </ul>",
        ),
    ]
    """
    <p>Status of the resource's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration because the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation does not currently return this value.</p> </li> </ul>
    """

    timestamp: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(
            alias="Timestamp",
            description="Time at which CloudFormation performed drift detection on the stack resource.",
        ),
    ]
    """
    Time at which CloudFormation performed drift detection on the stack resource.
    """

    module_info: typing_extensions.Annotated[
        typing.Optional[StackResourceDriftModuleInfo],
        FieldMetadata(alias="ModuleInfo"),
        pydantic.Field(
            alias="ModuleInfo",
            description="Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.",
        ),
    ] = None
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
