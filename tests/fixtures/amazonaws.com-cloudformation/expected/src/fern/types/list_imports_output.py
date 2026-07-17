

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_name import StackName


class ListImportsOutput(UniversalBaseModel):
    imports: typing_extensions.Annotated[
        typing.Optional[typing.List[StackName]],
        FieldMetadata(alias="Imports"),
        pydantic.Field(
            alias="Imports", description="A list of stack names that are importing the specified exported output value."
        ),
    ] = None
    """
    A list of stack names that are importing the specified exported output value.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="A string that identifies the next page of exports. If there is no additional page, this value is null.",
        ),
    ] = None
    """
    A string that identifies the next page of exports. If there is no additional page, this value is null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
