

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_personalized_survey_link_response_data import GetPersonalizedSurveyLinkResponseData


class GetPersonalizedSurveyLinkResponse(UniversalBaseModel):
    data: typing.Optional[GetPersonalizedSurveyLinkResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
