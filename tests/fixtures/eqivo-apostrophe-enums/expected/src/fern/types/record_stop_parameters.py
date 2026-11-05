

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RecordStopParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call"),
    ]
    """
    Unique identifier of the call
    """

    record_file: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="RecordFile"),
        pydantic.Field(
            alias="RecordFile",
            description="Full path to recording file, as returned by RecordStart; `all` shorthand is also available",
        ),
    ]
    """
    Full path to recording file, as returned by RecordStart; `all` shorthand is also available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
