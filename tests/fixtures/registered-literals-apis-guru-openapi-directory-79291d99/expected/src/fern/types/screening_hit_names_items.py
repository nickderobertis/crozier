

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .individual_screening_hit_names import IndividualScreeningHitNames
from .match_summary import MatchSummary


class ScreeningHitNamesItems(UniversalBaseModel):
    """
    Analyzed name information for the associated hit
    """

    analysis: typing.Optional[MatchSummary] = None
    data: typing.Optional[IndividualScreeningHitNames] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
