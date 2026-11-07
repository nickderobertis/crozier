

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_all_response_item_payload_items_item_type import SurveyAllResponseItemPayloadItemsItemType


class SurveyAllResponseItemPayloadItemsItem(UniversalBaseModel):
    label: str
    name: str
    type: SurveyAllResponseItemPayloadItemsItemType
    options: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
