

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListChangeSetsInput(UniversalBaseModel):
    """
    The input for the <a>ListChangeSets</a> action.
    """

    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName",
            description="The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.",
        ),
    ]
    """
    The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="A string (provided by the <a>ListChangeSets</a> response output) that identifies the next page of change sets that you want to retrieve.",
        ),
    ] = None
    """
    A string (provided by the <a>ListChangeSets</a> response output) that identifies the next page of change sets that you want to retrieve.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
