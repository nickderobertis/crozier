

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResolveCoursePromptRequestLanguageTargetLanguage(enum.StrEnum):
    """
    Target language, which must differ from the source language
    """

    AF = "af"
    AM = "am"
    AR = "ar"
    AZ = "az"
    BE = "be"
    BG = "bg"
    BN = "bn"
    CA = "ca"
    CS = "cs"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    ES = "es"
    ET = "et"
    EU = "eu"
    FA = "fa"
    FI = "fi"
    FR = "fr"
    GA = "ga"
    GU = "gu"
    HI = "hi"
    HR = "hr"
    HU = "hu"
    HY = "hy"
    ID = "id"
    IS = "is"
    IT = "it"
    JA = "ja"
    JV = "jv"
    KA = "ka"
    KN = "kn"
    KO = "ko"
    LO = "lo"
    LV = "lv"
    LT = "lt"
    MK = "mk"
    MG = "mg"
    ML = "ml"
    MN = "mn"
    MR = "mr"
    MS = "ms"
    MY = "my"
    NE = "ne"
    NL = "nl"
    NO = "no"
    OR = "or"
    PA = "pa"
    PL = "pl"
    PS = "ps"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SD = "sd"
    SI = "si"
    SK = "sk"
    SL = "sl"
    SQ = "sq"
    SR = "sr"
    SV = "sv"
    SW = "sw"
    TA = "ta"
    TE = "te"
    TH = "th"
    TL = "tl"
    TR = "tr"
    UK = "uk"
    UR = "ur"
    VI = "vi"
    ZH = "zh"

    def visit(
        self,
        af: typing.Callable[[], T_Result],
        am: typing.Callable[[], T_Result],
        ar: typing.Callable[[], T_Result],
        az: typing.Callable[[], T_Result],
        be: typing.Callable[[], T_Result],
        bg: typing.Callable[[], T_Result],
        bn: typing.Callable[[], T_Result],
        ca: typing.Callable[[], T_Result],
        cs: typing.Callable[[], T_Result],
        da: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
        el: typing.Callable[[], T_Result],
        en: typing.Callable[[], T_Result],
        es: typing.Callable[[], T_Result],
        et: typing.Callable[[], T_Result],
        eu: typing.Callable[[], T_Result],
        fa: typing.Callable[[], T_Result],
        fi: typing.Callable[[], T_Result],
        fr: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        gu: typing.Callable[[], T_Result],
        hi: typing.Callable[[], T_Result],
        hr: typing.Callable[[], T_Result],
        hu: typing.Callable[[], T_Result],
        hy: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        is_: typing.Callable[[], T_Result],
        it: typing.Callable[[], T_Result],
        ja: typing.Callable[[], T_Result],
        jv: typing.Callable[[], T_Result],
        ka: typing.Callable[[], T_Result],
        kn: typing.Callable[[], T_Result],
        ko: typing.Callable[[], T_Result],
        lo: typing.Callable[[], T_Result],
        lv: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        mk: typing.Callable[[], T_Result],
        mg: typing.Callable[[], T_Result],
        ml: typing.Callable[[], T_Result],
        mn: typing.Callable[[], T_Result],
        mr: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
        my: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        nl: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        or_: typing.Callable[[], T_Result],
        pa: typing.Callable[[], T_Result],
        pl: typing.Callable[[], T_Result],
        ps: typing.Callable[[], T_Result],
        pt: typing.Callable[[], T_Result],
        ro: typing.Callable[[], T_Result],
        ru: typing.Callable[[], T_Result],
        sd: typing.Callable[[], T_Result],
        si: typing.Callable[[], T_Result],
        sk: typing.Callable[[], T_Result],
        sl: typing.Callable[[], T_Result],
        sq: typing.Callable[[], T_Result],
        sr: typing.Callable[[], T_Result],
        sv: typing.Callable[[], T_Result],
        sw: typing.Callable[[], T_Result],
        ta: typing.Callable[[], T_Result],
        te: typing.Callable[[], T_Result],
        th: typing.Callable[[], T_Result],
        tl: typing.Callable[[], T_Result],
        tr: typing.Callable[[], T_Result],
        uk: typing.Callable[[], T_Result],
        ur: typing.Callable[[], T_Result],
        vi: typing.Callable[[], T_Result],
        zh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.AF:
            return af()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.AM:
            return am()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.AR:
            return ar()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.AZ:
            return az()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.BE:
            return be()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.BG:
            return bg()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.BN:
            return bn()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.CA:
            return ca()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.CS:
            return cs()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.DA:
            return da()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.DE:
            return de()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.EL:
            return el()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.EN:
            return en()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.ES:
            return es()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.ET:
            return et()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.EU:
            return eu()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.FA:
            return fa()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.FI:
            return fi()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.FR:
            return fr()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.GA:
            return ga()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.GU:
            return gu()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.HI:
            return hi()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.HR:
            return hr()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.HU:
            return hu()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.HY:
            return hy()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.ID:
            return id()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.IS:
            return is_()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.IT:
            return it()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.JA:
            return ja()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.JV:
            return jv()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.KA:
            return ka()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.KN:
            return kn()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.KO:
            return ko()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.LO:
            return lo()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.LV:
            return lv()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.LT:
            return lt()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.MK:
            return mk()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.MG:
            return mg()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.ML:
            return ml()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.MN:
            return mn()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.MR:
            return mr()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.MS:
            return ms()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.MY:
            return my()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.NE:
            return ne()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.NL:
            return nl()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.NO:
            return no()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.OR:
            return or_()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.PA:
            return pa()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.PL:
            return pl()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.PS:
            return ps()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.PT:
            return pt()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.RO:
            return ro()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.RU:
            return ru()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SD:
            return sd()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SI:
            return si()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SK:
            return sk()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SL:
            return sl()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SQ:
            return sq()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SR:
            return sr()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SV:
            return sv()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.SW:
            return sw()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.TA:
            return ta()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.TE:
            return te()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.TH:
            return th()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.TL:
            return tl()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.TR:
            return tr()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.UK:
            return uk()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.UR:
            return ur()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.VI:
            return vi()
        if self is ResolveCoursePromptRequestLanguageTargetLanguage.ZH:
            return zh()
