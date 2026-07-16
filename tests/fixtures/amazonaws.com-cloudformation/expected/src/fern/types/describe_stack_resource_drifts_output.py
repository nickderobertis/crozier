

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_resource_drift import StackResourceDrift


class DescribeStackResourceDriftsOutput(UniversalBaseModel):
    stack_resource_drifts: typing_extensions.Annotated[
        typing.List[StackResourceDrift], FieldMetadata(alias="StackResourceDrifts")
    ] = pydantic.Field()
    """
    <p>Drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that do not currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>DescribeStackResourceDrifts</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
