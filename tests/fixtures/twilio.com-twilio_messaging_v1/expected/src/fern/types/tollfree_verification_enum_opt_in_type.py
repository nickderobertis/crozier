

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TollfreeVerificationEnumOptInType(enum.StrEnum):
    VERBAL = "VERBAL"
    WEB_FORM = "WEB_FORM"
    PAPER_FORM = "PAPER_FORM"
    VIA_TEXT = "VIA_TEXT"
    MOBILE_QR_CODE = "MOBILE_QR_CODE"

    def visit(
        self,
        verbal: typing.Callable[[], T_Result],
        web_form: typing.Callable[[], T_Result],
        paper_form: typing.Callable[[], T_Result],
        via_text: typing.Callable[[], T_Result],
        mobile_qr_code: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TollfreeVerificationEnumOptInType.VERBAL:
            return verbal()
        if self is TollfreeVerificationEnumOptInType.WEB_FORM:
            return web_form()
        if self is TollfreeVerificationEnumOptInType.PAPER_FORM:
            return paper_form()
        if self is TollfreeVerificationEnumOptInType.VIA_TEXT:
            return via_text()
        if self is TollfreeVerificationEnumOptInType.MOBILE_QR_CODE:
            return mobile_qr_code()
