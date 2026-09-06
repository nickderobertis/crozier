

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory
from .global_resources_shared_models_global_image_state import GlobalResourcesSharedModelsGlobalImageState


class GlobalResourcesSharedModelsGlobalImage(UniversalBaseModel):
    """
    An image from the Global Image library.
    """

    crc: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CRC"),
        pydantic.Field(alias="CRC", description="The Hash of the file (SHA256, HEX-encoded)."),
    ]
    """
    The Hash of the file (SHA256, HEX-encoded).
    """

    categories: typing_extensions.Annotated[
        typing.Optional[typing.List[GlobalResourcesSharedModelsGlobalImageCategory]],
        FieldMetadata(alias="Categories"),
        pydantic.Field(alias="Categories", description="The category of the file."),
    ] = None
    """
    The category of the file.
    """

    date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="Date"),
        pydantic.Field(alias="Date", description="The date of the file."),
    ] = None
    """
    The date of the file.
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the file."),
    ]
    """
    The description of the file.
    """

    height: typing_extensions.Annotated[
        int, FieldMetadata(alias="Height"), pydantic.Field(alias="Height", description="The height of the file.")
    ]
    """
    The height of the file.
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The Id of the GlobalImage Metadata."),
    ] = None
    """
    The Id of the GlobalImage Metadata.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the file when downloaded."),
    ]
    """
    The name of the file when downloaded.
    """

    publisher: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Publisher"),
        pydantic.Field(alias="Publisher", description="The Publisher of the file."),
    ] = None
    """
    The Publisher of the file.
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
        GlobalResourcesSharedModelsGlobalImageState,
        FieldMetadata(alias="State"),
        pydantic.Field(
            alias="State", description="Indicates the state of this file. Must be 'Created' when created. Read Only."
        ),
    ]
    """
    Indicates the state of this file. Must be 'Created' when created. Read Only.
    """

    thumbnail_crc: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ThumbnailCRC"),
        pydantic.Field(alias="ThumbnailCRC", description="The Hash of the thumbnail file (SHA256, HEX-encoded)."),
    ]
    """
    The Hash of the thumbnail file (SHA256, HEX-encoded).
    """

    thumbnail_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ThumbnailSize"),
        pydantic.Field(
            alias="ThumbnailSize",
            description="The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only",
        ),
    ] = None
    """
    The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only
    """

    width: typing_extensions.Annotated[
        int, FieldMetadata(alias="Width"), pydantic.Field(alias="Width", description="The width of the file.")
    ]
    """
    The width of the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
