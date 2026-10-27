

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .output_description_base import OutputDescriptionBase


class EpochDateRangeOutput(OutputDescriptionBase):
    """
    Parses `startColumn` and `endColumn` as integers, interpreting them as dates in the Unix-Epoch (i.e. days since 01-01-1970), then emits them as a daterange.
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
