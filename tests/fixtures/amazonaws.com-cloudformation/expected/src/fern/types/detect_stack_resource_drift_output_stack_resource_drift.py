

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .detect_stack_resource_drift_output_stack_resource_drift_module_info import (
    DetectStackResourceDriftOutputStackResourceDriftModuleInfo,
)
from .detect_stack_resource_drift_output_stack_resource_drift_stack_resource_drift_status import (
    DetectStackResourceDriftOutputStackResourceDriftStackResourceDriftStatus,
)
from .physical_resource_id_context_key_value_pair import PhysicalResourceIdContextKeyValuePair
from .property_difference import PropertyDifference


class DetectStackResourceDriftOutputStackResourceDrift(UniversalBaseModel):
    """
    Information about whether the resource's actual configuration has drifted from its expected template configuration, including actual and expected property values and any differences detected.
    """

    stack_id: typing_extensions.Annotated[str, FieldMetadata(alias="StackId")] = pydantic.Field()
    """
    The ID of the stack.
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

    physical_resource_id_context: typing_extensions.Annotated[
        typing.Optional[typing.List[PhysicalResourceIdContextKeyValuePair]],
        FieldMetadata(alias="PhysicalResourceIdContext"),
    ] = pydantic.Field(default=None)
    """
    Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resource's logical and physical IDs aren't enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.
    """

    resource_type: typing_extensions.Annotated[str, FieldMetadata(alias="ResourceType")] = pydantic.Field()
    """
    The type of the resource.
    """

    expected_properties: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ExpectedProperties")
    ] = pydantic.Field(default=None)
    """
    <p>A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>
    """

    actual_properties: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ActualProperties")] = (
        pydantic.Field(default=None)
    )
    """
    <p>A JSON structure containing the actual property values of the stack resource.</p> <p>For resources whose <code>StackResourceDriftStatus</code> is <code>DELETED</code>, this structure will not be present.</p>
    """

    property_differences: typing_extensions.Annotated[
        typing.Optional[typing.List[PropertyDifference]], FieldMetadata(alias="PropertyDifferences")
    ] = pydantic.Field(default=None)
    """
    A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose <code>StackResourceDriftStatus</code> is <code>MODIFIED</code>.
    """

    stack_resource_drift_status: typing_extensions.Annotated[
        DetectStackResourceDriftOutputStackResourceDriftStackResourceDriftStatus,
        FieldMetadata(alias="StackResourceDriftStatus"),
    ] = pydantic.Field()
    """
    <p>Status of the resource's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration because the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation does not currently return this value.</p> </li> </ul>
    """

    timestamp: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="Timestamp")] = pydantic.Field()
    """
    Time at which CloudFormation performed drift detection on the stack resource.
    """

    module_info: typing_extensions.Annotated[
        typing.Optional[DetectStackResourceDriftOutputStackResourceDriftModuleInfo], FieldMetadata(alias="ModuleInfo")
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
