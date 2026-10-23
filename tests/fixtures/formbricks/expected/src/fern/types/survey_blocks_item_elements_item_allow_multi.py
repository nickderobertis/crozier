

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_allow_multi_choices_item import SurveyBlocksItemElementsItemAllowMultiChoicesItem
from .survey_blocks_item_elements_item_allow_multi_scale import SurveyBlocksItemElementsItemAllowMultiScale
from .survey_blocks_item_elements_item_allow_multi_type import SurveyBlocksItemElementsItemAllowMultiType


class SurveyBlocksItemElementsItemAllowMulti(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemAllowMultiType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemAllowMultiScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    allow_multi: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowMulti"), pydantic.Field(alias="allowMulti")
    ]
    choices: typing.List[SurveyBlocksItemElementsItemAllowMultiChoicesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
