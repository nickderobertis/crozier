

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CountryCode(enum.StrEnum):
    """
    ISO-3166-1 alpha-2 country code standard.
    """

    US = "US"
    GB = "GB"
    ES = "ES"
    NL = "NL"
    FR = "FR"
    IE = "IE"
    CA = "CA"
    DE = "DE"
    IT = "IT"
    PL = "PL"
    DK = "DK"
    NO = "NO"
    SE = "SE"
    EE = "EE"
    LT = "LT"
    LV = "LV"
    PT = "PT"

    def visit(
        self,
        us: typing.Callable[[], T_Result],
        gb: typing.Callable[[], T_Result],
        es: typing.Callable[[], T_Result],
        nl: typing.Callable[[], T_Result],
        fr: typing.Callable[[], T_Result],
        ie: typing.Callable[[], T_Result],
        ca: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
        it: typing.Callable[[], T_Result],
        pl: typing.Callable[[], T_Result],
        dk: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        se: typing.Callable[[], T_Result],
        ee: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        lv: typing.Callable[[], T_Result],
        pt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CountryCode.US:
            return us()
        if self is CountryCode.GB:
            return gb()
        if self is CountryCode.ES:
            return es()
        if self is CountryCode.NL:
            return nl()
        if self is CountryCode.FR:
            return fr()
        if self is CountryCode.IE:
            return ie()
        if self is CountryCode.CA:
            return ca()
        if self is CountryCode.DE:
            return de()
        if self is CountryCode.IT:
            return it()
        if self is CountryCode.PL:
            return pl()
        if self is CountryCode.DK:
            return dk()
        if self is CountryCode.NO:
            return no()
        if self is CountryCode.SE:
            return se()
        if self is CountryCode.EE:
            return ee()
        if self is CountryCode.LT:
            return lt()
        if self is CountryCode.LV:
            return lv()
        if self is CountryCode.PT:
            return pt()
