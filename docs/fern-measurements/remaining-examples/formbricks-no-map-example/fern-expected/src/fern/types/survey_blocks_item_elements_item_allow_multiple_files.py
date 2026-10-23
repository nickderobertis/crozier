

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_allow_multiple_files_allowed_file_extensions_item import (
    SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem,
)
from .survey_blocks_item_elements_item_allow_multiple_files_scale import (
    SurveyBlocksItemElementsItemAllowMultipleFilesScale,
)
from .survey_blocks_item_elements_item_allow_multiple_files_type import (
    SurveyBlocksItemElementsItemAllowMultipleFilesType,
)


class SurveyBlocksItemElementsItemAllowMultipleFiles(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemAllowMultipleFilesType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemAllowMultipleFilesScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    allow_multiple_files: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowMultipleFiles"), pydantic.Field(alias="allowMultipleFiles")
    ]
    max_size_in_mb: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxSizeInMB"), pydantic.Field(alias="maxSizeInMB")
    ] = None
    allowed_file_extensions: typing_extensions.Annotated[
        typing.Optional[typing.List[SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem]],
        FieldMetadata(alias="allowedFileExtensions"),
        pydantic.Field(alias="allowedFileExtensions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
