

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .output_description_base import OutputDescriptionBase


class EpochOutput(OutputDescriptionBase):
    """
    Parses `startColumn` integer, emitting it as dates in the Unix-Epoch (i.e. days since 01-01-1970)
    """

    input_column: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputColumn"), pydantic.Field(alias="inputColumn")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
