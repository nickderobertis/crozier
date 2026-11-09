

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .individual_watchlist_code import IndividualWatchlistCode
from .internal_uid import InternalUid
from .screening_hit_analysis import ScreeningHitAnalysis
from .screening_hit_data import ScreeningHitData
from .source_uid import SourceUid
from .timestamp import Timestamp
from .timestamp_nullable import TimestampNullable
from .watchlist_screening_hit_id import WatchlistScreeningHitId
from .watchlist_screening_hit_status import WatchlistScreeningHitStatus


class WatchlistScreeningHit(UniversalBaseModel):
    """
    Data from a government watchlist or PEP list that has been attached to the screening.
    """

    analysis: typing.Optional[ScreeningHitAnalysis] = None
    data: typing.Optional[ScreeningHitData] = None
    first_active: Timestamp
    historical_since: typing.Optional[TimestampNullable] = None
    id: WatchlistScreeningHitId
    inactive_since: typing.Optional[TimestampNullable] = None
    list_code: IndividualWatchlistCode
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
