

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_stack_instances_input_call_as import ListStackInstancesInputCallAs
from .stack_instance_filter import StackInstanceFilter


class ListStackInstancesInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackSetName"),
        pydantic.Field(
            alias="StackSetName",
            description="The name or unique ID of the stack set that you want to list stack instances for.",
        ),
    ]
    """
    The name or unique ID of the stack set that you want to list stack instances for.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the previous request didn't return all the remaining results, the response's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.",
        ),
    ] = None
    """
    If the previous request didn't return all the remaining results, the response's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    """

    max_results: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MaxResults"),
        pydantic.Field(
            alias="MaxResults",
            description="The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.",
        ),
    ] = None
    """
    The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    """

    filters: typing_extensions.Annotated[
        typing.Optional[typing.List[StackInstanceFilter]],
        FieldMetadata(alias="Filters"),
        pydantic.Field(alias="Filters", description="The filter to apply to stack instances"),
    ] = None
    """
    The filter to apply to stack instances
    """

    stack_instance_account: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackInstanceAccount"),
        pydantic.Field(
            alias="StackInstanceAccount",
            description="The name of the Amazon Web Services account that you want to list stack instances for.",
        ),
    ] = None
    """
    The name of the Amazon Web Services account that you want to list stack instances for.
    """

    stack_instance_region: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackInstanceRegion"),
        pydantic.Field(
            alias="StackInstanceRegion", description="The name of the Region where you want to list stack instances."
        ),
    ] = None
    """
    The name of the Region where you want to list stack instances.
    """

    call_as: typing_extensions.Annotated[
        typing.Optional[ListStackInstancesInputCallAs],
        FieldMetadata(alias="CallAs"),
        pydantic.Field(
            alias="CallAs",
            description='<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization\'s management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
