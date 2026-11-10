

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_screening_hit_analysis import EntityScreeningHitAnalysis
from .entity_screening_hit_data import EntityScreeningHitData
from .entity_watchlist_code import EntityWatchlistCode
from .entity_watchlist_screening_hit_id import EntityWatchlistScreeningHitId
from .internal_uid import InternalUid
from .source_uid import SourceUid
from .timestamp import Timestamp
from .timestamp_nullable import TimestampNullable
from .watchlist_screening_hit_status import WatchlistScreeningHitStatus


class EntityWatchlistScreeningHit(UniversalBaseModel):
    """
    Data from a government watchlist that has been attached to the screening.
    """

    analysis: typing.Optional[EntityScreeningHitAnalysis] = None
    data: typing.Optional[EntityScreeningHitData] = None
    first_active: Timestamp
    historical_since: typing.Optional[TimestampNullable] = None
    id: EntityWatchlistScreeningHitId
    inactive_since: typing.Optional[TimestampNullable] = None
    list_code: EntityWatchlistCode
    plaid_uid: InternalUid
    review_status: WatchlistScreeningHitStatus
    source_uid: typing.Optional[SourceUid] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
