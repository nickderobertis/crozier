

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .allowed_files_application_item import AllowedFilesApplicationItem
from .allowed_files_audio_item import AllowedFilesAudioItem
from .allowed_files_image_item import AllowedFilesImageItem
from .allowed_files_text_item import AllowedFilesTextItem
from .allowed_files_video_item import AllowedFilesVideoItem


class AllowedFiles(UniversalBaseModel):
    """
    Allowed file types for upload. Keys are MIME type categories, values are arrays of file extensions or ['*'] for all types in that category.
    """

    image: typing_extensions.Annotated[
        typing.Optional[typing.List[AllowedFilesImageItem]],
        FieldMetadata(alias="image/*"),
        pydantic.Field(alias="image/*", description="Image file extensions or ['*'] for all image types."),
    ] = None
    """
    Image file extensions or ['*'] for all image types.
    """

    video: typing_extensions.Annotated[
        typing.Optional[typing.List[AllowedFilesVideoItem]],
        FieldMetadata(alias="video/*"),
        pydantic.Field(alias="video/*", description="Video file extensions or ['*'] for all video types."),
    ] = None
    """
    Video file extensions or ['*'] for all video types.
    """

    audio: typing_extensions.Annotated[
        typing.Optional[typing.List[AllowedFilesAudioItem]],
        FieldMetadata(alias="audio/*"),
        pydantic.Field(alias="audio/*", description="Audio file extensions or ['*'] for all audio types."),
    ] = None
    """
    Audio file extensions or ['*'] for all audio types.
    """

    text: typing_extensions.Annotated[
        typing.Optional[typing.List[AllowedFilesTextItem]],
        FieldMetadata(alias="text/*"),
        pydantic.Field(alias="text/*", description="Text file extensions or ['*'] for all text types."),
    ] = None
    """
    Text file extensions or ['*'] for all text types.
    """

    application: typing_extensions.Annotated[
        typing.Optional[typing.List[AllowedFilesApplicationItem]],
        FieldMetadata(alias="application/*"),
        pydantic.Field(
            alias="application/*",
            description="Application/document file extensions or ['*'] for all application types.",
        ),
    ] = None
    """
    Application/document file extensions or ['*'] for all application types.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
