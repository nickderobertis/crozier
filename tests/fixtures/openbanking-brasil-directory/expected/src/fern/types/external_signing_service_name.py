

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExternalSigningServiceName(enum.StrEnum):
    """
    The Name of the External Signing Service
    """

    DOCU_SIGN = "DocuSign"

    def visit(self, docu_sign: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExternalSigningServiceName.DOCU_SIGN:
            return docu_sign()
