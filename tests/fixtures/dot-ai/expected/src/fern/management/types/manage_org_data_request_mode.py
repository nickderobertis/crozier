

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ManageOrgDataRequestMode(enum.StrEnum):
    """
    Scan mode: "full" triggers a fire-and-forget full cluster scan that returns immediately and scans all resources in the cluster. Mutually exclusive with resourceList.
    """

    FULL = "full"

    def visit(self, full: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManageOrgDataRequestMode.FULL:
            return full()
