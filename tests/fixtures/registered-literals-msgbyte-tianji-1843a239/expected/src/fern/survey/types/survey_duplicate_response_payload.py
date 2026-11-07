

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_duplicate_response_payload_items_item import SurveyDuplicateResponsePayloadItemsItem


class SurveyDuplicateResponsePayload(UniversalBaseModel):
    items: typing.List[SurveyDuplicateResponsePayloadItemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
