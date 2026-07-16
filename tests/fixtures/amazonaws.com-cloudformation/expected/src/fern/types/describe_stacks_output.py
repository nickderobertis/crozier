

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack import Stack


class DescribeStacksOutput(UniversalBaseModel):
    """
    The output for a <a>DescribeStacks</a> action.
    """

    stacks: typing_extensions.Annotated[typing.Optional[typing.List[Stack]], FieldMetadata(alias="Stacks")] = (
        pydantic.Field(default=None)
    )
    """
    A list of stack structures.
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
