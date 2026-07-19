

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    NSMF_PDUSESSION = "nsmf-pdusession"
    """
    Access to the nsmf-pdusession API
    """

    def visit(self, nsmf_pdusession: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.NSMF_PDUSESSION:
            return nsmf_pdusession()
