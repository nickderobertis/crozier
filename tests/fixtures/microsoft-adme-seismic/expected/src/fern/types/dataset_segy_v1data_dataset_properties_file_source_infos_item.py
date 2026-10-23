

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DatasetSegyV1DataDatasetPropertiesFileSourceInfosItem(UniversalBaseModel):
    """
    A schema fragment to describe file source information.
    """

    file_source: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="FileSource"),
        pydantic.Field(
            alias="FileSource",
            description="The location of the file. It can be a relative path. The actual access is provided via the File Service. When used in context of a FileCollection (dataset--FileCollection*) FileSource is a relative path from the FileCollectionPath. It can be used by consumers to pull an individual file if they so choose by concatenating the FileCollectionPath with the FileSource. This property is required.",
        ),
    ]
    """
    The location of the file. It can be a relative path. The actual access is provided via the File Service. When used in context of a FileCollection (dataset--FileCollection*) FileSource is a relative path from the FileCollectionPath. It can be used by consumers to pull an individual file if they so choose by concatenating the FileCollectionPath with the FileSource. This property is required.
    """

    preload_file_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PreloadFilePath"),
        pydantic.Field(
            alias="PreloadFilePath",
            description="File system path to the data file as it existed before loading to the data platform.",
        ),
    ] = None
    """
    File system path to the data file as it existed before loading to the data platform.
    """

    preload_file_create_user: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PreloadFileCreateUser"),
        pydantic.Field(
            alias="PreloadFileCreateUser",
            description="Optional user name or reference, who created the file prior to up-loading to the platform.",
        ),
    ] = None
    """
    Optional user name or reference, who created the file prior to up-loading to the platform.
    """

    preload_file_create_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="PreloadFileCreateDate"),
        pydantic.Field(
            alias="PreloadFileCreateDate",
            description="Optional create date and time of the file prior to up-loading to the platform.",
        ),
    ] = None
    """
    Optional create date and time of the file prior to up-loading to the platform.
    """

    preload_file_modify_user: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PreloadFileModifyUser"),
        pydantic.Field(
            alias="PreloadFileModifyUser",
            description="Optional user name or reference, who last modified the file prior to up-loading to the platform.",
        ),
    ] = None
    """
    Optional user name or reference, who last modified the file prior to up-loading to the platform.
    """

    preload_file_modify_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="PreloadFileModifyDate"),
        pydantic.Field(
            alias="PreloadFileModifyDate",
            description="Optional last modified date and time of the file prior to up-loading to the platform.",
        ),
    ] = None
    """
    Optional last modified date and time of the file prior to up-loading to the platform.
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Optional, user-friendly file name."),
    ] = None
    """
    Optional, user-friendly file name.
    """

    file_size: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FileSize"),
        pydantic.Field(
            alias="FileSize",
            description="Length of file in bytes. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
        ),
    ] = None
    """
    Length of file in bytes. Implemented as string. The value must be convertible to a long integer (sizes can become very large).
    """

    encoding_format_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EncodingFormatTypeID"),
        pydantic.Field(
            alias="EncodingFormatTypeID",
            description="Only used in FileCollection where the EncodingFormatType differs from data DatasetDefault specified in data.EncodingFormatTypeID: the media type specification for this dataset.",
        ),
    ] = None
    """
    Only used in FileCollection where the EncodingFormatType differs from data DatasetDefault specified in data.EncodingFormatTypeID: the media type specification for this dataset.
    """

    checksum: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Checksum"),
        pydantic.Field(
            alias="Checksum", description="Checksum of file bytes - a hexadecimal number with even number of bytes."
        ),
    ] = None
    """
    Checksum of file bytes - a hexadecimal number with even number of bytes.
    """

    checksum_algorithm: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ChecksumAlgorithm"),
        pydantic.Field(alias="ChecksumAlgorithm", description="The name of the checksum algorithm e.g. MD5, SHA-256."),
    ] = None
    """
    The name of the checksum algorithm e.g. MD5, SHA-256.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
