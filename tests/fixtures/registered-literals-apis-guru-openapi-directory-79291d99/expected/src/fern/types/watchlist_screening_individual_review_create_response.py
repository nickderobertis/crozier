

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .review_comment import ReviewComment
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
from .watchlist_screening_hit_id import WatchlistScreeningHitId
from .watchlist_screening_review_id import WatchlistScreeningReviewId


class WatchlistScreeningIndividualReviewCreateResponse(UniversalBaseModel):
    """
    A review submitted by a team member for an individual watchlist screening. A review can be either a comment on the current screening state, actions taken
    against hits attached to the watchlist screening, or both.
    """

    audit_trail: WatchlistScreeningAuditTrail
    comment: typing.Optional[ReviewComment] = None
    confirmed_hits: typing.List[WatchlistScreeningHitId] = pydantic.Field()
    """
    Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected.
    """

    dismissed_hits: typing.List[WatchlistScreeningHitId] = pydantic.Field()
    """
    Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed.
    """

    id: WatchlistScreeningReviewId
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
