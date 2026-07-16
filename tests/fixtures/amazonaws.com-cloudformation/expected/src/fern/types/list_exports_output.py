

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .export import Export


class ListExportsOutput(UniversalBaseModel):
    exports: typing_extensions.Annotated[
        typing.Optional[typing.List[Export]],
        FieldMetadata(alias="Exports"),
        pydantic.Field(alias="Exports", description="The output for the <a>ListExports</a> action."),
    ] = None
    """
    The output for the <a>ListExports</a> action.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.",
        ),
    ] = None
    """
    If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
