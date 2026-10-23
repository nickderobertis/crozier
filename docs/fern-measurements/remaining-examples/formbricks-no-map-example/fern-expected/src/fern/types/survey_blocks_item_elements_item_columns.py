

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_columns_columns_item import SurveyBlocksItemElementsItemColumnsColumnsItem
from .survey_blocks_item_elements_item_columns_rows_item import SurveyBlocksItemElementsItemColumnsRowsItem
from .survey_blocks_item_elements_item_columns_scale import SurveyBlocksItemElementsItemColumnsScale
from .survey_blocks_item_elements_item_columns_shuffle_option import SurveyBlocksItemElementsItemColumnsShuffleOption
from .survey_blocks_item_elements_item_columns_type import SurveyBlocksItemElementsItemColumnsType


class SurveyBlocksItemElementsItemColumns(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemColumnsType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemColumnsScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    rows: typing.List[SurveyBlocksItemElementsItemColumnsRowsItem]
    columns: typing.List[SurveyBlocksItemElementsItemColumnsColumnsItem]
    shuffle_option: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemColumnsShuffleOption,
        FieldMetadata(alias="shuffleOption"),
        pydantic.Field(alias="shuffleOption"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
