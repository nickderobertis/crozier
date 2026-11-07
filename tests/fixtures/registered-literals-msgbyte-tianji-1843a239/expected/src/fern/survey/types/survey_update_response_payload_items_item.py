

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_update_response_payload_items_item_type import SurveyUpdateResponsePayloadItemsItemType


class SurveyUpdateResponsePayloadItemsItem(UniversalBaseModel):
    label: str
    name: str
    type: SurveyUpdateResponsePayloadItemsItemType
    options: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
