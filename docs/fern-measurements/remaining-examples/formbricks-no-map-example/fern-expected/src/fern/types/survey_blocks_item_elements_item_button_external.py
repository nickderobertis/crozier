

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_button_external_scale import SurveyBlocksItemElementsItemButtonExternalScale
from .survey_blocks_item_elements_item_button_external_type import SurveyBlocksItemElementsItemButtonExternalType


class SurveyBlocksItemElementsItemButtonExternal(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemButtonExternalType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemButtonExternalScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    button_external: typing_extensions.Annotated[
        bool, FieldMetadata(alias="buttonExternal"), pydantic.Field(alias="buttonExternal")
    ]
    button_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="buttonUrl"), pydantic.Field(alias="buttonUrl")
    ] = None
    cta_button_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="ctaButtonLabel"),
        pydantic.Field(alias="ctaButtonLabel"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
