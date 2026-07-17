

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_set_operation_result_summary import StackSetOperationResultSummary


class ListStackSetOperationResultsOutput(UniversalBaseModel):
    summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[StackSetOperationResultSummary]],
        FieldMetadata(alias="Summaries"),
        pydantic.Field(
            alias="Summaries",
            description="A list of <code>StackSetOperationResultSummary</code> structures that contain information about the specified operation results, for accounts and Amazon Web Services Regions that are included in the operation.",
        ),
    ] = None
    """
    A list of <code>StackSetOperationResultSummary</code> structures that contain information about the specified operation results, for accounts and Amazon Web Services Regions that are included in the operation.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the request doesn't return all results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, <code>NextToken</code> is set to <code>null</code>.",
        ),
    ] = None
    """
    If the request doesn't return all results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, <code>NextToken</code> is set to <code>null</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
