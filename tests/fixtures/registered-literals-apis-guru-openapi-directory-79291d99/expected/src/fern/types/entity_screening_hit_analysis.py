

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .match_summary_code import MatchSummaryCode


class EntityScreeningHitAnalysis(UniversalBaseModel):
    """
    Analysis information describing why a screening hit matched the provided entity information
    """

    documents: typing.Optional[MatchSummaryCode] = None
    email_addresses: typing.Optional[MatchSummaryCode] = None
    locations: typing.Optional[MatchSummaryCode] = None
    names: typing.Optional[MatchSummaryCode] = None
    phone_numbers: typing.Optional[MatchSummaryCode] = None
    search_terms_version: float = pydantic.Field()
    """
    The version of the entity screening's `search_terms` that were compared when the entity screening hit was added. entity screening hits are immutable once they have been reviewed. If changes are detected due to updates to the entity screening's `search_terms`, the associated entity program, or the list's source data prior to review, the entity screening hit will be updated to reflect those changes.
    """

    urls: typing.Optional[MatchSummaryCode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
