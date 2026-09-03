

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinkedAuthenticateV2ResponseResponseConsentAction(enum.StrEnum):
    """
    This field indicates the need to capture user consent or not
    """

    CAPTURE = "CAPTURE"
    NOCAPTURE = "NOCAPTURE"

    def visit(self, capture: typing.Callable[[], T_Result], nocapture: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostLinkedAuthenticateV2ResponseResponseConsentAction.CAPTURE:
            return capture()
        if self is PostLinkedAuthenticateV2ResponseResponseConsentAction.NOCAPTURE:
            return nocapture()
