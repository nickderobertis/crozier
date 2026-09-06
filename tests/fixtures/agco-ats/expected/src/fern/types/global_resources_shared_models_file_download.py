

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_resources_shared_models_file_download_state import GlobalResourcesSharedModelsFileDownloadState


class GlobalResourcesSharedModelsFileDownload(UniversalBaseModel):
    """
    A language used for string translations.
    """

    crc: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CRC"),
        pydantic.Field(
            alias="CRC", description="The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file."
        ),
    ]
    """
    The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.
    """

    content_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ContentType"),
        pydantic.Field(alias="ContentType", description="The type of file; sent as the content-type header."),
    ]
    """
    The type of file; sent as the content-type header.
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the file."),
    ]
    """
    The description of the file.
    """

    id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Id"), pydantic.Field(alias="Id", description="The Id of the file.")
    ] = None
    """
    The Id of the file.
    """

    is_public: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="IsPublic"),
        pydantic.Field(
            alias="IsPublic", description="Indicates whether this file is available to the public for download."
        ),
    ]
    """
    Indicates whether this file is available to the public for download.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the file when downloaded."),
    ]
    """
    The name of the file when downloaded.
    """

    path: typing_extensions.Annotated[
        str, FieldMetadata(alias="Path"), pydantic.Field(alias="Path", description="The Path of the file.")
    ]
    """
    The Path of the file.
    """

    size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Size"),
        pydantic.Field(
            alias="Size",
            description="The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only",
        ),
    ] = None
    """
    The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only
    """

    state: typing_extensions.Annotated[
        GlobalResourcesSharedModelsFileDownloadState,
        FieldMetadata(alias="State"),
        pydantic.Field(alias="State", description="Indicates the state of this file. Must be 'Created' when created."),
    ]
    """
    Indicates the state of this file. Must be 'Created' when created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
