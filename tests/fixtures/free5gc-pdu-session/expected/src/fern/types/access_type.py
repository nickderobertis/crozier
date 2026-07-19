

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessType(enum.StrEnum):
    THREE_GPP_ACCESS = "3GPP_ACCESS"
    NON3GPP_ACCESS = "NON_3GPP_ACCESS"

    def visit(
        self, three_gpp_access: typing.Callable[[], T_Result], non3gpp_access: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AccessType.THREE_GPP_ACCESS:
            return three_gpp_access()
        if self is AccessType.NON3GPP_ACCESS:
            return non3gpp_access()
