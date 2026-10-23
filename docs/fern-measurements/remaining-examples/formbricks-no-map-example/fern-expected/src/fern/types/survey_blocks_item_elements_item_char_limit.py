

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_char_limit_char_limit import SurveyBlocksItemElementsItemCharLimitCharLimit
from .survey_blocks_item_elements_item_char_limit_input_type import SurveyBlocksItemElementsItemCharLimitInputType
from .survey_blocks_item_elements_item_char_limit_scale import SurveyBlocksItemElementsItemCharLimitScale
from .survey_blocks_item_elements_item_char_limit_type import SurveyBlocksItemElementsItemCharLimitType


class SurveyBlocksItemElementsItemCharLimit(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemCharLimitType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemCharLimitScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    placeholder: typing.Optional[typing.Dict[str, str]] = None
    long_answer: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="longAnswer"), pydantic.Field(alias="longAnswer")
    ] = None
    input_type: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemCharLimitInputType,
        FieldMetadata(alias="inputType"),
        pydantic.Field(alias="inputType"),
    ]
    insights_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="insightsEnabled"), pydantic.Field(alias="insightsEnabled")
    ] = None
    char_limit: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemCharLimitCharLimit,
        FieldMetadata(alias="charLimit"),
        pydantic.Field(alias="charLimit"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
