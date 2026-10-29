

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .major_type import MajorType
from .output_description_base import OutputDescriptionBase


class CopyOutput(OutputDescriptionBase):
    """
    Parses and emits the values in inputColumn as the provided type.
    """

    input_column: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="inputColumn"),
        pydantic.Field(alias="inputColumn", description="Name of the csv column to process."),
    ] = None
    """
    Name of the csv column to process.
    """

    input_type: typing_extensions.Annotated[
        typing.Optional[MajorType], FieldMetadata(alias="inputType"), pydantic.Field(alias="inputType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
