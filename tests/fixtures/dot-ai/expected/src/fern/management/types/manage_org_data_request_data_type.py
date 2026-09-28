

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ManageOrgDataRequestDataType(enum.StrEnum):
    """
    Type of cluster data to manage: "capabilities" for resource capabilities. (Note: organizational knowledge/patterns/policies are managed via manageKnowledge tool)
    """

    CAPABILITIES = "capabilities"

    def visit(self, capabilities: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManageOrgDataRequestDataType.CAPABILITIES:
            return capabilities()
