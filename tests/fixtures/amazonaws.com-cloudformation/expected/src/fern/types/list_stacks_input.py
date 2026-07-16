

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_status import StackStatus


class ListStacksInput(UniversalBaseModel):
    """
    The input for <a>ListStacks</a> action.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    A string that identifies the next page of stacks that you want to retrieve.
    """

    stack_status_filter: typing_extensions.Annotated[
        typing.Optional[typing.List[StackStatus]], FieldMetadata(alias="StackStatusFilter")
    ] = pydantic.Field(default=None)
    """
    Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the <code>StackStatus</code> parameter of the <a>Stack</a> data type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
