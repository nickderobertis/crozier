

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPlaylistsRequestSort(enum.StrEnum):
    RECENT_ADDED_FIRST = "recent_added_first"
    OLDEST_ADDED_FIRST = "oldest_added_first"
    NAME_A_TO_Z = "name_a_to_z"
    NAME_Z_TO_A = "name_z_to_a"

    def visit(
        self,
        recent_added_first: typing.Callable[[], T_Result],
        oldest_added_first: typing.Callable[[], T_Result],
        name_a_to_z: typing.Callable[[], T_Result],
        name_z_to_a: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPlaylistsRequestSort.RECENT_ADDED_FIRST:
            return recent_added_first()
        if self is GetPlaylistsRequestSort.OLDEST_ADDED_FIRST:
            return oldest_added_first()
        if self is GetPlaylistsRequestSort.NAME_A_TO_Z:
            return name_a_to_z()
        if self is GetPlaylistsRequestSort.NAME_Z_TO_A:
            return name_z_to_a()
