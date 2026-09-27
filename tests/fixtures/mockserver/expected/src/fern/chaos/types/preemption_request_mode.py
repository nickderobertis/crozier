

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PreemptionRequestMode(enum.StrEnum):
    """
    how draining is signalled: reject503 = 503 + Connection: close; goaway = HTTP/2 GOAWAY frame; both = both
    """

    REJECT503 = "reject503"
    GOAWAY = "goaway"
    BOTH = "both"

    def visit(
        self,
        reject503: typing.Callable[[], T_Result],
        goaway: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreemptionRequestMode.REJECT503:
            return reject503()
        if self is PreemptionRequestMode.GOAWAY:
            return goaway()
        if self is PreemptionRequestMode.BOTH:
            return both()
