

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_choices_choices_item import SurveyBlocksItemElementsItemChoicesChoicesItem
from .survey_blocks_item_elements_item_choices_scale import SurveyBlocksItemElementsItemChoicesScale
from .survey_blocks_item_elements_item_choices_shuffle_option import SurveyBlocksItemElementsItemChoicesShuffleOption
from .survey_blocks_item_elements_item_choices_type import SurveyBlocksItemElementsItemChoicesType


class SurveyBlocksItemElementsItemChoices(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemChoicesType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemChoicesScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    choices: typing.List[SurveyBlocksItemElementsItemChoicesChoicesItem]
    other_option_placeholder: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="otherOptionPlaceholder"),
        pydantic.Field(alias="otherOptionPlaceholder"),
    ] = None
    shuffle_option: typing_extensions.Annotated[
        typing.Optional[SurveyBlocksItemElementsItemChoicesShuffleOption],
        FieldMetadata(alias="shuffleOption"),
        pydantic.Field(alias="shuffleOption"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
