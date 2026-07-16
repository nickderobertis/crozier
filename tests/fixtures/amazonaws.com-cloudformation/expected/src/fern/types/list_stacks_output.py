

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_summary import StackSummary


class ListStacksOutput(UniversalBaseModel):
    """
    The output for <a>ListStacks</a> action.
    """

    stack_summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[StackSummary]], FieldMetadata(alias="StackSummaries")
    ] = pydantic.Field(default=None)
    """
    A list of <code>StackSummary</code> structures containing information about the specified stacks.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
