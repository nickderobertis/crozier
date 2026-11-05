

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConferenceRecordStopParameters(UniversalBaseModel):
    conference_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ConferenceName"),
        pydantic.Field(alias="ConferenceName", description="Name of the conference in question"),
    ]
    """
    Name of the conference in question
    """

    record_file: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="RecordFile"),
        pydantic.Field(
            alias="RecordFile",
            description="Full path to recording file, as returned by ConferenceRecordStart; `all` shorthand is also available",
        ),
    ]
    """
    Full path to recording file, as returned by ConferenceRecordStart; `all` shorthand is also available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
