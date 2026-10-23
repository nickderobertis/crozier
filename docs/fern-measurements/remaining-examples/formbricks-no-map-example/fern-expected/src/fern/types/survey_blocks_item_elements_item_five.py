

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_five_scale import SurveyBlocksItemElementsItemFiveScale
from .survey_blocks_item_elements_item_five_type import SurveyBlocksItemElementsItemFiveType


class SurveyBlocksItemElementsItemFive(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemFiveType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: SurveyBlocksItemElementsItemFiveScale
    range: float
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    lower_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="lowerLabel"), pydantic.Field(alias="lowerLabel")
    ] = None
    upper_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="upperLabel"), pydantic.Field(alias="upperLabel")
    ] = None
    is_color_coding_enabled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isColorCodingEnabled"), pydantic.Field(alias="isColorCodingEnabled")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
