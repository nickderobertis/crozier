

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .match_summary import MatchSummary
from .watchlist_screening_document import WatchlistScreeningDocument


class ScreeningHitDocumentsItems(UniversalBaseModel):
    """
    Analyzed document information for the associated hit
    """

    analysis: typing.Optional[MatchSummary] = None
    data: typing.Optional[WatchlistScreeningDocument] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
