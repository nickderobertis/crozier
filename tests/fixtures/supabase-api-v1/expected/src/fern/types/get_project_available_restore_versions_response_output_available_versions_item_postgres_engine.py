

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine(enum.StrEnum):
    THIRTEEN = "13"
    FOURTEEN = "14"
    FIFTEEN = "15"
    SEVENTEEN = "17"
    SEVENTEEN_ORIOLE = "17-oriole"

    def visit(
        self,
        thirteen: typing.Callable[[], T_Result],
        fourteen: typing.Callable[[], T_Result],
        fifteen: typing.Callable[[], T_Result],
        seventeen: typing.Callable[[], T_Result],
        seventeen_oriole: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine.THIRTEEN:
            return thirteen()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine.FOURTEEN:
            return fourteen()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine.FIFTEEN:
            return fifteen()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine.SEVENTEEN:
            return seventeen()
        if self is GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine.SEVENTEEN_ORIOLE:
            return seventeen_oriole()
