

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_screening_hit_urls import EntityScreeningHitUrls
from .match_summary import MatchSummary


class EntityScreeningHitUrlsItems(UniversalBaseModel):
    """
    Analyzed URLs for the associated hit
    """

    analysis: typing.Optional[MatchSummary] = None
    data: typing.Optional[EntityScreeningHitUrls] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
