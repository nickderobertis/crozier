

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_detect_intelligence_question_response_item import GetDetectIntelligenceQuestionResponseItem


class GetDetectIntelligenceQuestionResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    item: typing.Optional[GetDetectIntelligenceQuestionResponseItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
