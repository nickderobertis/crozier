

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_cal_host_scale import SurveyBlocksItemElementsItemCalHostScale
from .survey_blocks_item_elements_item_cal_host_type import SurveyBlocksItemElementsItemCalHostType


class SurveyBlocksItemElementsItemCalHost(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemCalHostType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemCalHostScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    cal_user_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="calUserName"), pydantic.Field(alias="calUserName")
    ]
    cal_host: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="calHost"), pydantic.Field(alias="calHost")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
