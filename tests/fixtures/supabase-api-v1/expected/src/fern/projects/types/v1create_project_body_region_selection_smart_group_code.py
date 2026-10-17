

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1CreateProjectBodyRegionSelectionSmartGroupCode(enum.StrEnum):
    """
    The Smart Region Group's code. The codes supported are not a stable API, and should be retrieved from the /available-regions endpoint.
    """

    AMERICAS = "americas"
    EMEA = "emea"
    APAC = "apac"

    def visit(
        self,
        americas: typing.Callable[[], T_Result],
        emea: typing.Callable[[], T_Result],
        apac: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1CreateProjectBodyRegionSelectionSmartGroupCode.AMERICAS:
            return americas()
        if self is V1CreateProjectBodyRegionSelectionSmartGroupCode.EMEA:
            return emea()
        if self is V1CreateProjectBodyRegionSelectionSmartGroupCode.APAC:
            return apac()
