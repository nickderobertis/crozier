

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_resource_summary import StackResourceSummary


class ListStackResourcesOutput(UniversalBaseModel):
    """
    The output for a <a>ListStackResources</a> action.
    """

    stack_resource_summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[StackResourceSummary]],
        FieldMetadata(alias="StackResourceSummaries"),
        pydantic.Field(
            alias="StackResourceSummaries", description="A list of <code>StackResourceSummary</code> structures."
        ),
    ] = None
    """
    A list of <code>StackResourceSummary</code> structures.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no additional page exists, this value is null.",
        ),
    ] = None
    """
    If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no additional page exists, this value is null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
