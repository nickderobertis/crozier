

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_cores import SurveyCores
from .survey_strata import SurveyStrata


class Survey(UniversalBaseModel):
    strata: typing.Optional[SurveyStrata] = pydantic.Field(default=None)
    """
    Rock layers recorded, declared untyped with empty items beside properties.
    """

    cores: typing.Optional[SurveyCores] = pydantic.Field(default=None)
    """
    Drill cores, untyped with empty items and nested properties.
    """

    surveyor: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
