

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_styling_card_arrangement_app_surveys import SurveyStylingCardArrangementAppSurveys
from .survey_styling_card_arrangement_link_surveys import SurveyStylingCardArrangementLinkSurveys


class SurveyStylingCardArrangement(UniversalBaseModel):
    link_surveys: typing_extensions.Annotated[
        SurveyStylingCardArrangementLinkSurveys, FieldMetadata(alias="linkSurveys"), pydantic.Field(alias="linkSurveys")
    ]
    app_surveys: typing_extensions.Annotated[
        SurveyStylingCardArrangementAppSurveys, FieldMetadata(alias="appSurveys"), pydantic.Field(alias="appSurveys")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
