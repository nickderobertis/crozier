

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_delete_response_payload_items_item import SurveyDeleteResponsePayloadItemsItem


class SurveyDeleteResponsePayload(UniversalBaseModel):
    items: typing.List[SurveyDeleteResponsePayloadItemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
