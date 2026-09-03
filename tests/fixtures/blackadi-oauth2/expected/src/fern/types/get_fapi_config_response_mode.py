

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetFapiConfigResponseMode(enum.StrEnum):
    """
    FAPI mode derived from the service's fapiModes. sp=FAPI 2.0 Security Profile, ms=FAPI 2.0 Message Signing, fapi1-advanced/fapi1-baseline=the FAPI 1.0 parts. 'disabled' means no mode is set; 'unknown' means a mode is set that this server does not recognise — the two are deliberately distinct, so an unrecognised profile is never reported as off.
    """

    SP = "sp"
    MS = "ms"
    FAPI1ADVANCED = "fapi1-advanced"
    FAPI1BASELINE = "fapi1-baseline"
    UNKNOWN = "unknown"
    DISABLED = "disabled"

    def visit(
        self,
        sp: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
        fapi1advanced: typing.Callable[[], T_Result],
        fapi1baseline: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFapiConfigResponseMode.SP:
            return sp()
        if self is GetFapiConfigResponseMode.MS:
            return ms()
        if self is GetFapiConfigResponseMode.FAPI1ADVANCED:
            return fapi1advanced()
        if self is GetFapiConfigResponseMode.FAPI1BASELINE:
            return fapi1baseline()
        if self is GetFapiConfigResponseMode.UNKNOWN:
            return unknown()
        if self is GetFapiConfigResponseMode.DISABLED:
            return disabled()
