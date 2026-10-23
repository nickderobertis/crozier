

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_address_line1address_line1 import (
    SurveyBlocksItemElementsItemAddressLine1AddressLine1,
)
from .survey_blocks_item_elements_item_address_line1address_line2 import (
    SurveyBlocksItemElementsItemAddressLine1AddressLine2,
)
from .survey_blocks_item_elements_item_address_line1city import SurveyBlocksItemElementsItemAddressLine1City
from .survey_blocks_item_elements_item_address_line1country import SurveyBlocksItemElementsItemAddressLine1Country
from .survey_blocks_item_elements_item_address_line1scale import SurveyBlocksItemElementsItemAddressLine1Scale
from .survey_blocks_item_elements_item_address_line1state import SurveyBlocksItemElementsItemAddressLine1State
from .survey_blocks_item_elements_item_address_line1type import SurveyBlocksItemElementsItemAddressLine1Type
from .survey_blocks_item_elements_item_address_line1zip import SurveyBlocksItemElementsItemAddressLine1Zip


class SurveyBlocksItemElementsItemAddressLine1(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemAddressLine1Type
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemAddressLine1Scale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    address_line1: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemAddressLine1AddressLine1,
        FieldMetadata(alias="addressLine1"),
        pydantic.Field(alias="addressLine1"),
    ]
    address_line2: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemAddressLine1AddressLine2,
        FieldMetadata(alias="addressLine2"),
        pydantic.Field(alias="addressLine2"),
    ]
    city: SurveyBlocksItemElementsItemAddressLine1City
    state: SurveyBlocksItemElementsItemAddressLine1State
    zip: SurveyBlocksItemElementsItemAddressLine1Zip
    country: SurveyBlocksItemElementsItemAddressLine1Country

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
