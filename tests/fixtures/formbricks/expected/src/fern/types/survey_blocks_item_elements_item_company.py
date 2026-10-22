

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_blocks_item_elements_item_company_company import SurveyBlocksItemElementsItemCompanyCompany
from .survey_blocks_item_elements_item_company_email import SurveyBlocksItemElementsItemCompanyEmail
from .survey_blocks_item_elements_item_company_first_name import SurveyBlocksItemElementsItemCompanyFirstName
from .survey_blocks_item_elements_item_company_last_name import SurveyBlocksItemElementsItemCompanyLastName
from .survey_blocks_item_elements_item_company_phone import SurveyBlocksItemElementsItemCompanyPhone
from .survey_blocks_item_elements_item_company_scale import SurveyBlocksItemElementsItemCompanyScale
from .survey_blocks_item_elements_item_company_type import SurveyBlocksItemElementsItemCompanyType


class SurveyBlocksItemElementsItemCompany(UniversalBaseModel):
    id: str
    type: SurveyBlocksItemElementsItemCompanyType
    headline: typing.Dict[str, str]
    subheader: typing.Optional[typing.Dict[str, str]] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None
    required: bool
    scale: typing.Optional[SurveyBlocksItemElementsItemCompanyScale] = None
    range: typing.Optional[float] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    first_name: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemCompanyFirstName,
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName"),
    ]
    last_name: typing_extensions.Annotated[
        SurveyBlocksItemElementsItemCompanyLastName, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ]
    email: SurveyBlocksItemElementsItemCompanyEmail
    phone: SurveyBlocksItemElementsItemCompanyPhone
    company: SurveyBlocksItemElementsItemCompanyCompany

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
