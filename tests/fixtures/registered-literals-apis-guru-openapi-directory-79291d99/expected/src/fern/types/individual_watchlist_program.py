

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .individual_watchlist_code import IndividualWatchlistCode
from .individual_watchlist_screening_program_name import IndividualWatchlistScreeningProgramName
from .program_archived import ProgramArchived
from .program_name_sensitivity import ProgramNameSensitivity
from .timestamp import Timestamp
from .watchlist_program_id import WatchlistProgramId
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail


class IndividualWatchlistProgram(UniversalBaseModel):
    """
    A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of individuals.
    """

    audit_trail: WatchlistScreeningAuditTrail
    created_at: Timestamp
    id: WatchlistProgramId
    is_archived: ProgramArchived
    is_rescanning_enabled: bool = pydantic.Field()
    """
    Indicator specifying whether the program is enabled and will perform daily rescans.
    """

    lists_enabled: typing.List[IndividualWatchlistCode] = pydantic.Field()
    """
    Watchlists enabled for the associated program
    """

    name: IndividualWatchlistScreeningProgramName
    name_sensitivity: ProgramNameSensitivity

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
