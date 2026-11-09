

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conference_record_start_parameters_file_format import ConferenceRecordStartParametersFileFormat


class ConferenceRecordStartParameters(UniversalBaseModel):
    conference_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ConferenceName"),
        pydantic.Field(alias="ConferenceName", description="Name of the conference in question"),
    ]
    """
    Name of the conference in question
    """

    file_format: typing_extensions.Annotated[
        typing.Optional[ConferenceRecordStartParametersFileFormat],
        FieldMetadata(alias="FileFormat"),
        pydantic.Field(alias="FileFormat", description="File format (extension)"),
    ] = None
    """
    File format (extension)
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FileName"),
        pydantic.Field(
            alias="FileName",
            description="Recording file name (without extension); if empty, a timestamp based file name will be generated",
        ),
    ] = None
    """
    Recording file name (without extension); if empty, a timestamp based file name will be generated
    """

    file_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FilePath"),
        pydantic.Field(alias="FilePath", description="Directory path/URI where the recording file will be saved"),
    ] = None
    """
    Directory path/URI where the recording file will be saved
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
