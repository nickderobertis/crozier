

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdIssuerRequestKind(enum.StrEnum):
    BASE_PROSPECTUS = "base_prospectus"
    SUPPLEMENT = "supplement"
    NOTICE = "notice"
    FINAL_TERMS = "final_terms"
    OTHER = "other"

    def visit(
        self,
        base_prospectus: typing.Callable[[], T_Result],
        supplement: typing.Callable[[], T_Result],
        notice: typing.Callable[[], T_Result],
        final_terms: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdIssuerRequestKind.BASE_PROSPECTUS:
            return base_prospectus()
        if self is GetChainsChainIdIssuerRequestKind.SUPPLEMENT:
            return supplement()
        if self is GetChainsChainIdIssuerRequestKind.NOTICE:
            return notice()
        if self is GetChainsChainIdIssuerRequestKind.FINAL_TERMS:
            return final_terms()
        if self is GetChainsChainIdIssuerRequestKind.OTHER:
            return other()
