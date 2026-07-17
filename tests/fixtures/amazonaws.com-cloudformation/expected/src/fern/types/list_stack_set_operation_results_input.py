

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_stack_set_operation_results_input_call_as import ListStackSetOperationResultsInputCallAs
from .operation_result_filter import OperationResultFilter


class ListStackSetOperationResultsInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackSetName"),
        pydantic.Field(
            alias="StackSetName",
            description="The name or unique ID of the stack set that you want to get operation results for.",
        ),
    ]
    """
    The name or unique ID of the stack set that you want to get operation results for.
    """

    operation_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="OperationId"),
        pydantic.Field(alias="OperationId", description="The ID of the stack set operation."),
    ]
    """
    The ID of the stack set operation.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the previous request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.",
        ),
    ] = None
    """
    If the previous request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
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

    call_as: typing_extensions.Annotated[
        typing.Optional[ListStackSetOperationResultsInputCallAs],
        FieldMetadata(alias="CallAs"),
        pydantic.Field(
            alias="CallAs",
            description='<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization\'s management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    """

    filters: typing_extensions.Annotated[
        typing.Optional[typing.List[OperationResultFilter]],
        FieldMetadata(alias="Filters"),
        pydantic.Field(alias="Filters", description="The filter to apply to operation results."),
    ] = None
    """
    The filter to apply to operation results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
