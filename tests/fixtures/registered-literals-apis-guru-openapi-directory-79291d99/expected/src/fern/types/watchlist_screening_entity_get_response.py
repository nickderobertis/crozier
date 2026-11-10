

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_user_id_nullable import ClientUserIdNullable
from .dashboard_user_id_nullable import DashboardUserIdNullable
from .entity_watchlist_screening_id import EntityWatchlistScreeningId
from .entity_watchlist_screening_search_terms import EntityWatchlistScreeningSearchTerms
from .request_id import RequestId
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
from .watchlist_screening_status import WatchlistScreeningStatus


class WatchlistScreeningEntityGetResponse(UniversalBaseModel):
    """
    The entity screening object allows you to represent an entity in your system, update its profile, and search for it on various watchlists. Note: Rejected entity screenings will not receive new hits, regardless of entity program configuration.
    """

    assignee: typing.Optional[DashboardUserIdNullable] = None
    audit_trail: WatchlistScreeningAuditTrail
    client_user_id: typing.Optional[ClientUserIdNullable] = None
    id: EntityWatchlistScreeningId
    request_id: RequestId
    search_terms: EntityWatchlistScreeningSearchTerms
    status: WatchlistScreeningStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
