

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_watchlist_code import EntityWatchlistCode
from .entity_watchlist_program_id import EntityWatchlistProgramId
from .entity_watchlist_screening_program_name import EntityWatchlistScreeningProgramName
from .program_archived import ProgramArchived
from .program_name_sensitivity import ProgramNameSensitivity
from .timestamp import Timestamp
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail


class EntityWatchlistProgram(UniversalBaseModel):
    """
    A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of entities.
    """

    audit_trail: WatchlistScreeningAuditTrail
    created_at: Timestamp
    id: EntityWatchlistProgramId
    is_archived: ProgramArchived
    is_rescanning_enabled: bool = pydantic.Field()
    """
    Indicator specifying whether the program is enabled and will perform daily rescans.
    """

    lists_enabled: typing.List[EntityWatchlistCode] = pydantic.Field()
    """
    Watchlists enabled for the associated program
    """

    name: EntityWatchlistScreeningProgramName
    name_sensitivity: ProgramNameSensitivity

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
