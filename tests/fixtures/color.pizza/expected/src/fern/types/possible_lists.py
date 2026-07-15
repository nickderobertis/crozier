

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PossibleLists(str, enum.Enum):
    DEFAULT = "default"
    BEST_OF = "bestOf"
    WIKIPEDIA = "wikipedia"
    FRENCH = "french"
    RIDGWAY = "ridgway"
    RISOGRAPH = "risograph"
    BASIC = "basic"
    CHINESE_TRADITIONAL = "chineseTraditional"
    HTML = "html"
    JAPANESE_TRADITIONAL = "japaneseTraditional"
    LE_CORBUSIER = "leCorbusier"
    NBS_ISCC = "nbsIscc"
    NTC = "ntc"
    OSXCRAYONS = "osxcrayons"
    RAL = "ral"
    SANZO_WADA_I = "sanzoWadaI"
    THESAURUS = "thesaurus"
    WERNER = "werner"
    WINDOWS = "windows"
    X11 = "x11"
    XKCD = "xkcd"

    def visit(
        self,
        default: typing.Callable[[], T_Result],
        best_of: typing.Callable[[], T_Result],
        wikipedia: typing.Callable[[], T_Result],
        french: typing.Callable[[], T_Result],
        ridgway: typing.Callable[[], T_Result],
        risograph: typing.Callable[[], T_Result],
        basic: typing.Callable[[], T_Result],
        chinese_traditional: typing.Callable[[], T_Result],
        html: typing.Callable[[], T_Result],
        japanese_traditional: typing.Callable[[], T_Result],
        le_corbusier: typing.Callable[[], T_Result],
        nbs_iscc: typing.Callable[[], T_Result],
        ntc: typing.Callable[[], T_Result],
        osxcrayons: typing.Callable[[], T_Result],
        ral: typing.Callable[[], T_Result],
        sanzo_wada_i: typing.Callable[[], T_Result],
        thesaurus: typing.Callable[[], T_Result],
        werner: typing.Callable[[], T_Result],
        windows: typing.Callable[[], T_Result],
        x11: typing.Callable[[], T_Result],
        xkcd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PossibleLists.DEFAULT:
            return default()
        if self is PossibleLists.BEST_OF:
            return best_of()
        if self is PossibleLists.WIKIPEDIA:
            return wikipedia()
        if self is PossibleLists.FRENCH:
            return french()
        if self is PossibleLists.RIDGWAY:
            return ridgway()
        if self is PossibleLists.RISOGRAPH:
            return risograph()
        if self is PossibleLists.BASIC:
            return basic()
        if self is PossibleLists.CHINESE_TRADITIONAL:
            return chinese_traditional()
        if self is PossibleLists.HTML:
            return html()
        if self is PossibleLists.JAPANESE_TRADITIONAL:
            return japanese_traditional()
        if self is PossibleLists.LE_CORBUSIER:
            return le_corbusier()
        if self is PossibleLists.NBS_ISCC:
            return nbs_iscc()
        if self is PossibleLists.NTC:
            return ntc()
        if self is PossibleLists.OSXCRAYONS:
            return osxcrayons()
        if self is PossibleLists.RAL:
            return ral()
        if self is PossibleLists.SANZO_WADA_I:
            return sanzo_wada_i()
        if self is PossibleLists.THESAURUS:
            return thesaurus()
        if self is PossibleLists.WERNER:
            return werner()
        if self is PossibleLists.WINDOWS:
            return windows()
        if self is PossibleLists.X11:
            return x11()
        if self is PossibleLists.XKCD:
            return xkcd()
