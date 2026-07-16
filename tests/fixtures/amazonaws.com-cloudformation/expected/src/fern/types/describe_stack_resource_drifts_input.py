

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_resource_drift_status import StackResourceDriftStatus


class DescribeStackResourceDriftsInput(UniversalBaseModel):
    stack_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackName")] = pydantic.Field()
    """
    The name of the stack for which you want drift information.
    """

    stack_resource_drift_status_filters: typing_extensions.Annotated[
        typing.Optional[typing.List[StackResourceDriftStatus]], FieldMetadata(alias="StackResourceDriftStatusFilters")
    ] = pydantic.Field(default=None)
    """
    <p>The resource drift status values to use as filters for the resource drift results returned.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> </ul>
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    A string that identifies the next page of stack resource drift results.
    """

    max_results: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="MaxResults")] = pydantic.Field(
        default=None
    )
    """
    The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
