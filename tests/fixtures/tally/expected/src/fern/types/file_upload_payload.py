

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .allowed_files import AllowedFiles
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .file_upload_payload_max_file_size_unit import FileUploadPayloadMaxFileSizeUnit
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name


class FileUploadPayload(UniversalBaseModel):
    """
    Payload for FILE_UPLOAD block type. Used for file upload fields.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[IsRequired], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    has_multiple_files: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMultipleFiles"),
        pydantic.Field(alias="hasMultipleFiles", description="When true, allows uploading multiple files."),
    ] = None
    """
    When true, allows uploading multiple files.
    """

    has_min_files: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMinFiles"),
        pydantic.Field(
            alias="hasMinFiles",
            description="Set to true to enable minFiles validation. When true, minFiles must be provided.",
        ),
    ] = None
    """
    Set to true to enable minFiles validation. When true, minFiles must be provided.
    """

    min_files: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minFiles"),
        pydantic.Field(
            alias="minFiles", description="Minimum number of files required. Required when hasMinFiles is true."
        ),
    ] = None
    """
    Minimum number of files required. Required when hasMinFiles is true.
    """

    has_max_files: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMaxFiles"),
        pydantic.Field(
            alias="hasMaxFiles",
            description="Set to true to enable maxFiles validation. When true, maxFiles must be provided.",
        ),
    ] = None
    """
    Set to true to enable maxFiles validation. When true, maxFiles must be provided.
    """

    max_files: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxFiles"),
        pydantic.Field(
            alias="maxFiles", description="Maximum number of files allowed. Required when hasMaxFiles is true."
        ),
    ] = None
    """
    Maximum number of files allowed. Required when hasMaxFiles is true.
    """

    has_max_file_size: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMaxFileSize"),
        pydantic.Field(
            alias="hasMaxFileSize",
            description="Set to true to enable maxFileSize validation. When true, maxFileSize and maxFileSizeUnit must be provided.",
        ),
    ] = None
    """
    Set to true to enable maxFileSize validation. When true, maxFileSize and maxFileSizeUnit must be provided.
    """

    max_file_size: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxFileSize"),
        pydantic.Field(alias="maxFileSize", description="Maximum file size. Required when hasMaxFileSize is true."),
    ] = None
    """
    Maximum file size. Required when hasMaxFileSize is true.
    """

    max_file_size_unit: typing_extensions.Annotated[
        typing.Optional[FileUploadPayloadMaxFileSizeUnit],
        FieldMetadata(alias="maxFileSizeUnit"),
        pydantic.Field(
            alias="maxFileSizeUnit", description="Unit for maxFileSize. Required when hasMaxFileSize is true."
        ),
    ] = None
    """
    Unit for maxFileSize. Required when hasMaxFileSize is true.
    """

    allowed_files: typing_extensions.Annotated[
        typing.Optional[AllowedFiles], FieldMetadata(alias="allowedFiles"), pydantic.Field(alias="allowedFiles")
    ] = None
    column_list_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnListUuid], FieldMetadata(alias="columnListUuid"), pydantic.Field(alias="columnListUuid")
    ] = None
    column_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnUuid], FieldMetadata(alias="columnUuid"), pydantic.Field(alias="columnUuid")
    ] = None
    column_ratio: typing_extensions.Annotated[
        typing.Optional[ColumnRatio], FieldMetadata(alias="columnRatio"), pydantic.Field(alias="columnRatio")
    ] = None
    name: typing.Optional[Name] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
