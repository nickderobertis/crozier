

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_user_id_nullable import ClientUserIdNullable
from .dashboard_user_id_nullable import DashboardUserIdNullable
from .request_id import RequestId
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
from .watchlist_screening_individual_id import WatchlistScreeningIndividualId
from .watchlist_screening_search_terms import WatchlistScreeningSearchTerms
from .watchlist_screening_status import WatchlistScreeningStatus


class WatchlistScreeningIndividualGetResponse(UniversalBaseModel):
    """
    The screening object allows you to represent a customer in your system, update their profile, and search for them on various watchlists. Note: Rejected customers will not receive new hits, regardless of program configuration.
    """

    assignee: typing.Optional[DashboardUserIdNullable] = None
    audit_trail: WatchlistScreeningAuditTrail
    client_user_id: typing.Optional[ClientUserIdNullable] = None
    id: WatchlistScreeningIndividualId
    request_id: RequestId
    search_terms: WatchlistScreeningSearchTerms
    status: WatchlistScreeningStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
