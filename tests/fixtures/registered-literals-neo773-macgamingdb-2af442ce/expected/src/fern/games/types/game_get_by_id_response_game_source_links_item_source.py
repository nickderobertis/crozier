

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetByIdResponseGameSourceLinksItemSource(enum.StrEnum):
    STEAM = "steam"
    IGDB = "igdb"

    def visit(self, steam: typing.Callable[[], T_Result], igdb: typing.Callable[[], T_Result]) -> T_Result:
        if self is GameGetByIdResponseGameSourceLinksItemSource.STEAM:
            return steam()
        if self is GameGetByIdResponseGameSourceLinksItemSource.IGDB:
            return igdb()
