

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_get_response_payload_items_item_type import SurveyGetResponsePayloadItemsItemType


class SurveyGetResponsePayloadItemsItem(UniversalBaseModel):
    label: str
    name: str
    type: SurveyGetResponsePayloadItemsItemType
    options: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
