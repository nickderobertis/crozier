

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_two_choices_item import SurveyBlocksItemElementsItemTwoChoicesItem
from .survey_blocks_item_elements_item_two_scale import SurveyBlocksItemElementsItemTwoScale
from .survey_blocks_item_elements_item_two_shuffle_option import SurveyBlocksItemElementsItemTwoShuffleOption
from .survey_blocks_item_elements_item_two_type import SurveyBlocksItemElementsItemTwoType


class SurveyBlocksItemElementsItemTwo(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemTwoType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemTwoScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    choices: typing.List[SurveyBlocksItemElementsItemTwoChoicesItem]
    shuffle_option: typing_extensions.Annotated[
        typing.Optional[SurveyBlocksItemElementsItemTwoShuffleOption],
        FieldMetadata(alias="shuffleOption"),
        pydantic.Field(alias="shuffleOption"),
    ] = None
    other_option_placeholder: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="otherOptionPlaceholder"),
        pydantic.Field(alias="otherOptionPlaceholder"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
