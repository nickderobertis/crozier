

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseUpdatePacerOptionsRefreshType(enum.StrEnum):
    """
    This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.

    Only one of the two values is allowed:
    -   fetchNewDocketEntries:
        >   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested.
    -   fetchAllDocketEntries:
        >   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available.
    """

    FETCH_NEW_DOCKET_ENTRIES = "fetchNewDocketEntries"
    FETCH_ALL_DOCKET_ENTRIES = "fetchAllDocketEntries"

    def visit(
        self,
        fetch_new_docket_entries: typing.Callable[[], T_Result],
        fetch_all_docket_entries: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseUpdatePacerOptionsRefreshType.FETCH_NEW_DOCKET_ENTRIES:
            return fetch_new_docket_entries()
        if self is CaseUpdatePacerOptionsRefreshType.FETCH_ALL_DOCKET_ENTRIES:
            return fetch_all_docket_entries()
