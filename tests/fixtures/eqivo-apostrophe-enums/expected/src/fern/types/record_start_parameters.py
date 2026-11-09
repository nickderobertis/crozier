

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .record_start_parameters_file_format import RecordStartParametersFileFormat


class RecordStartParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call to be recorded"),
    ] = None
    """
    Unique identifier of the call to be recorded
    """

    file_format: typing_extensions.Annotated[
        typing.Optional[RecordStartParametersFileFormat],
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

    time_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TimeLimit"),
        pydantic.Field(alias="TimeLimit", description="Maximum recording length, in seconds"),
    ] = None
    """
    Maximum recording length, in seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
