

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_event import StackEvent


class DescribeStackEventsOutput(UniversalBaseModel):
    """
    The output for a <a>DescribeStackEvents</a> action.
    """

    stack_events: typing_extensions.Annotated[
        typing.Optional[typing.List[StackEvent]],
        FieldMetadata(alias="StackEvents"),
        pydantic.Field(alias="StackEvents", description="A list of <code>StackEvents</code> structures."),
    ] = None
    """
    A list of <code>StackEvents</code> structures.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the output exceeds 1 MB in size, a string that identifies the next page of events. If no additional page exists, this value is null.",
        ),
    ] = None
    """
    If the output exceeds 1 MB in size, a string that identifies the next page of events. If no additional page exists, this value is null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
