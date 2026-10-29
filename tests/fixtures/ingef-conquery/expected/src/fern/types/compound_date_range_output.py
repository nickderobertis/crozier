

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .output_description_base import OutputDescriptionBase


class CompoundDateRangeOutput(OutputDescriptionBase):
    """
    Creates a virtual daterange column as a composite of its neighboring DATE-columns (not csv columns). This helps avoid copying multiple values of the same column, when they can be reused.
    """

    start_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startColumn"), pydantic.Field(alias="startColumn")
    ] = None
    end_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endColumn"), pydantic.Field(alias="endColumn")
    ] = None
    allow_open: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowOpen"), pydantic.Field(alias="allowOpen")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
