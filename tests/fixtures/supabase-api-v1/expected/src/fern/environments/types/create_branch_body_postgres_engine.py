

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateBranchBodyPostgresEngine(enum.StrEnum):
    """
    Postgres engine version. If not provided, the latest version will be used.
    """

    FIFTEEN = "15"
    SEVENTEEN = "17"
    SEVENTEEN_ORIOLE = "17-oriole"

    def visit(
        self,
        fifteen: typing.Callable[[], T_Result],
        seventeen: typing.Callable[[], T_Result],
        seventeen_oriole: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateBranchBodyPostgresEngine.FIFTEEN:
            return fifteen()
        if self is CreateBranchBodyPostgresEngine.SEVENTEEN:
            return seventeen()
        if self is CreateBranchBodyPostgresEngine.SEVENTEEN_ORIOLE:
            return seventeen_oriole()
