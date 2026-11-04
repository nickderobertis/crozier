

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StemmerType(enum.StrEnum):
    """
    Defines stemming behavior, reducing inflected words to their word stem, base or root form.
    Stemming increases recall, but decreases precision. It can introduce false positive results.
    """

    NONE = "None"
    ARABIC = "Arabic"
    ARMENIAN = "Armenian"
    BASQUE = "Basque"
    CATALAN = "Catalan"
    CZECH = "Czech"
    DANISH = "Danish"
    DUTCH = "Dutch"
    DUTCH_PORTER = "DutchPorter"
    ENGLISH = "English"
    ESPERANTO = "Esperanto"
    ESTONIAN = "Estonian"
    FINNISH = "Finnish"
    FRENCH = "French"
    GERMAN = "German"
    GREEK = "Greek"
    HINDI = "Hindi"
    HUNGARIAN = "Hungarian"
    INDONESIAN = "Indonesian"
    IRISH = "Irish"
    ITALIAN = "Italian"
    LITHUANIAN = "Lithuanian"
    LOVINS = "Lovins"
    NEPALI = "Nepali"
    NORWEGIAN = "Norwegian"
    PERSIAN = "Persian"
    POLISH = "Polish"
    PORTER = "Porter"
    PORTUGUESE = "Portuguese"
    ROMANIAN = "Romanian"
    RUSSIAN = "Russian"
    SERBIAN = "Serbian"
    SESOTHO = "Sesotho"
    SPANISH = "Spanish"
    SWEDISH = "Swedish"
    TAMIL = "Tamil"
    TURKISH = "Turkish"
    UKRAINIAN = "Ukrainian"
    YIDDISH = "Yiddish"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        arabic: typing.Callable[[], T_Result],
        armenian: typing.Callable[[], T_Result],
        basque: typing.Callable[[], T_Result],
        catalan: typing.Callable[[], T_Result],
        czech: typing.Callable[[], T_Result],
        danish: typing.Callable[[], T_Result],
        dutch: typing.Callable[[], T_Result],
        dutch_porter: typing.Callable[[], T_Result],
        english: typing.Callable[[], T_Result],
        esperanto: typing.Callable[[], T_Result],
        estonian: typing.Callable[[], T_Result],
        finnish: typing.Callable[[], T_Result],
        french: typing.Callable[[], T_Result],
        german: typing.Callable[[], T_Result],
        greek: typing.Callable[[], T_Result],
        hindi: typing.Callable[[], T_Result],
        hungarian: typing.Callable[[], T_Result],
        indonesian: typing.Callable[[], T_Result],
        irish: typing.Callable[[], T_Result],
        italian: typing.Callable[[], T_Result],
        lithuanian: typing.Callable[[], T_Result],
        lovins: typing.Callable[[], T_Result],
        nepali: typing.Callable[[], T_Result],
        norwegian: typing.Callable[[], T_Result],
        persian: typing.Callable[[], T_Result],
        polish: typing.Callable[[], T_Result],
        porter: typing.Callable[[], T_Result],
        portuguese: typing.Callable[[], T_Result],
        romanian: typing.Callable[[], T_Result],
        russian: typing.Callable[[], T_Result],
        serbian: typing.Callable[[], T_Result],
        sesotho: typing.Callable[[], T_Result],
        spanish: typing.Callable[[], T_Result],
        swedish: typing.Callable[[], T_Result],
        tamil: typing.Callable[[], T_Result],
        turkish: typing.Callable[[], T_Result],
        ukrainian: typing.Callable[[], T_Result],
        yiddish: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StemmerType.NONE:
            return none()
        if self is StemmerType.ARABIC:
            return arabic()
        if self is StemmerType.ARMENIAN:
            return armenian()
        if self is StemmerType.BASQUE:
            return basque()
        if self is StemmerType.CATALAN:
            return catalan()
        if self is StemmerType.CZECH:
            return czech()
        if self is StemmerType.DANISH:
            return danish()
        if self is StemmerType.DUTCH:
            return dutch()
        if self is StemmerType.DUTCH_PORTER:
            return dutch_porter()
        if self is StemmerType.ENGLISH:
            return english()
        if self is StemmerType.ESPERANTO:
            return esperanto()
        if self is StemmerType.ESTONIAN:
            return estonian()
        if self is StemmerType.FINNISH:
            return finnish()
        if self is StemmerType.FRENCH:
            return french()
        if self is StemmerType.GERMAN:
            return german()
        if self is StemmerType.GREEK:
            return greek()
        if self is StemmerType.HINDI:
            return hindi()
        if self is StemmerType.HUNGARIAN:
            return hungarian()
        if self is StemmerType.INDONESIAN:
            return indonesian()
        if self is StemmerType.IRISH:
            return irish()
        if self is StemmerType.ITALIAN:
            return italian()
        if self is StemmerType.LITHUANIAN:
            return lithuanian()
        if self is StemmerType.LOVINS:
            return lovins()
        if self is StemmerType.NEPALI:
            return nepali()
        if self is StemmerType.NORWEGIAN:
            return norwegian()
        if self is StemmerType.PERSIAN:
            return persian()
        if self is StemmerType.POLISH:
            return polish()
        if self is StemmerType.PORTER:
            return porter()
        if self is StemmerType.PORTUGUESE:
            return portuguese()
        if self is StemmerType.ROMANIAN:
            return romanian()
        if self is StemmerType.RUSSIAN:
            return russian()
        if self is StemmerType.SERBIAN:
            return serbian()
        if self is StemmerType.SESOTHO:
            return sesotho()
        if self is StemmerType.SPANISH:
            return spanish()
        if self is StemmerType.SWEDISH:
            return swedish()
        if self is StemmerType.TAMIL:
            return tamil()
        if self is StemmerType.TURKISH:
            return turkish()
        if self is StemmerType.UKRAINIAN:
            return ukrainian()
        if self is StemmerType.YIDDISH:
            return yiddish()
