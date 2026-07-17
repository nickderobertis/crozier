

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delete_stack_instances_input_operation_preferences_region_concurrency_type import (
    DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType,
)
from .region import Region


class DeleteStackInstancesInputOperationPreferences(UniversalBaseModel):
    """
    Preferences for how CloudFormation performs this stack set operation.
    """

    region_concurrency_type: typing_extensions.Annotated[
        typing.Optional[DeleteStackInstancesInputOperationPreferencesRegionConcurrencyType],
        FieldMetadata(alias="RegionConcurrencyType"),
        pydantic.Field(
            alias="RegionConcurrencyType",
            description="The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.",
        ),
    ] = None
    """
    The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.
    """

    region_order: typing_extensions.Annotated[
        typing.Optional[typing.List[Region]],
        FieldMetadata(alias="RegionOrder"),
        pydantic.Field(
            alias="RegionOrder",
            description="The order of the Regions in where you want to perform the stack operation.",
        ),
    ] = None
    """
    The order of the Regions in where you want to perform the stack operation.
    """

    failure_tolerance_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="FailureToleranceCount"),
        pydantic.Field(
            alias="FailureToleranceCount",
            description="<p>The number of accounts, per Region, for which this operation can fail before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.</p> <p>Conditional: You must specify either <code>FailureToleranceCount</code> or <code>FailureTolerancePercentage</code> (but not both).</p> <p>By default, <code>0</code> is specified.</p>",
        ),
    ] = None
    """
    <p>The number of accounts, per Region, for which this operation can fail before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.</p> <p>Conditional: You must specify either <code>FailureToleranceCount</code> or <code>FailureTolerancePercentage</code> (but not both).</p> <p>By default, <code>0</code> is specified.</p>
    """

    failure_tolerance_percentage: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="FailureTolerancePercentage"),
        pydantic.Field(
            alias="FailureTolerancePercentage",
            description="<p>The percentage of accounts, per Region, for which this stack operation can fail before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.</p> <p>When calculating the number of accounts based on the specified percentage, CloudFormation rounds <i>down</i> to the next whole number.</p> <p>Conditional: You must specify either <code>FailureToleranceCount</code> or <code>FailureTolerancePercentage</code>, but not both.</p> <p>By default, <code>0</code> is specified.</p>",
        ),
    ] = None
    """
    <p>The percentage of accounts, per Region, for which this stack operation can fail before CloudFormation stops the operation in that Region. If the operation is stopped in a Region, CloudFormation doesn't attempt the operation in any subsequent Regions.</p> <p>When calculating the number of accounts based on the specified percentage, CloudFormation rounds <i>down</i> to the next whole number.</p> <p>Conditional: You must specify either <code>FailureToleranceCount</code> or <code>FailureTolerancePercentage</code>, but not both.</p> <p>By default, <code>0</code> is specified.</p>
    """

    max_concurrent_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MaxConcurrentCount"),
        pydantic.Field(
            alias="MaxConcurrentCount",
            description="<p>The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of <code>FailureToleranceCount</code>.<code>MaxConcurrentCount</code> is at most one more than the <code>FailureToleranceCount</code>.</p> <p>Note that this setting lets you specify the <i>maximum</i> for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>Conditional: You must specify either <code>MaxConcurrentCount</code> or <code>MaxConcurrentPercentage</code>, but not both.</p> <p>By default, <code>1</code> is specified.</p>",
        ),
    ] = None
    """
    <p>The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of <code>FailureToleranceCount</code>.<code>MaxConcurrentCount</code> is at most one more than the <code>FailureToleranceCount</code>.</p> <p>Note that this setting lets you specify the <i>maximum</i> for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>Conditional: You must specify either <code>MaxConcurrentCount</code> or <code>MaxConcurrentPercentage</code>, but not both.</p> <p>By default, <code>1</code> is specified.</p>
    """

    max_concurrent_percentage: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MaxConcurrentPercentage"),
        pydantic.Field(
            alias="MaxConcurrentPercentage",
            description="<p>The maximum percentage of accounts in which to perform this operation at one time.</p> <p>When calculating the number of accounts based on the specified percentage, CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.</p> <p>Note that this setting lets you specify the <i>maximum</i> for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>Conditional: You must specify either <code>MaxConcurrentCount</code> or <code>MaxConcurrentPercentage</code>, but not both.</p> <p>By default, <code>1</code> is specified.</p>",
        ),
    ] = None
    """
    <p>The maximum percentage of accounts in which to perform this operation at one time.</p> <p>When calculating the number of accounts based on the specified percentage, CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.</p> <p>Note that this setting lets you specify the <i>maximum</i> for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.</p> <p>Conditional: You must specify either <code>MaxConcurrentCount</code> or <code>MaxConcurrentPercentage</code>, but not both.</p> <p>By default, <code>1</code> is specified.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
