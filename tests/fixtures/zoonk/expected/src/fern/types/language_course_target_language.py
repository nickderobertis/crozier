

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LanguageCourseTargetLanguage(enum.StrEnum):
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
        if self is LanguageCourseTargetLanguage.AF:
            return af()
        if self is LanguageCourseTargetLanguage.AM:
            return am()
        if self is LanguageCourseTargetLanguage.AR:
            return ar()
        if self is LanguageCourseTargetLanguage.AZ:
            return az()
        if self is LanguageCourseTargetLanguage.BE:
            return be()
        if self is LanguageCourseTargetLanguage.BG:
            return bg()
        if self is LanguageCourseTargetLanguage.BN:
            return bn()
        if self is LanguageCourseTargetLanguage.CA:
            return ca()
        if self is LanguageCourseTargetLanguage.CS:
            return cs()
        if self is LanguageCourseTargetLanguage.DA:
            return da()
        if self is LanguageCourseTargetLanguage.DE:
            return de()
        if self is LanguageCourseTargetLanguage.EL:
            return el()
        if self is LanguageCourseTargetLanguage.EN:
            return en()
        if self is LanguageCourseTargetLanguage.ES:
            return es()
        if self is LanguageCourseTargetLanguage.ET:
            return et()
        if self is LanguageCourseTargetLanguage.EU:
            return eu()
        if self is LanguageCourseTargetLanguage.FA:
            return fa()
        if self is LanguageCourseTargetLanguage.FI:
            return fi()
        if self is LanguageCourseTargetLanguage.FR:
            return fr()
        if self is LanguageCourseTargetLanguage.GA:
            return ga()
        if self is LanguageCourseTargetLanguage.GU:
            return gu()
        if self is LanguageCourseTargetLanguage.HI:
            return hi()
        if self is LanguageCourseTargetLanguage.HR:
            return hr()
        if self is LanguageCourseTargetLanguage.HU:
            return hu()
        if self is LanguageCourseTargetLanguage.HY:
            return hy()
        if self is LanguageCourseTargetLanguage.ID:
            return id()
        if self is LanguageCourseTargetLanguage.IS:
            return is_()
        if self is LanguageCourseTargetLanguage.IT:
            return it()
        if self is LanguageCourseTargetLanguage.JA:
            return ja()
        if self is LanguageCourseTargetLanguage.JV:
            return jv()
        if self is LanguageCourseTargetLanguage.KA:
            return ka()
        if self is LanguageCourseTargetLanguage.KN:
            return kn()
        if self is LanguageCourseTargetLanguage.KO:
            return ko()
        if self is LanguageCourseTargetLanguage.LO:
            return lo()
        if self is LanguageCourseTargetLanguage.LV:
            return lv()
        if self is LanguageCourseTargetLanguage.LT:
            return lt()
        if self is LanguageCourseTargetLanguage.MK:
            return mk()
        if self is LanguageCourseTargetLanguage.MG:
            return mg()
        if self is LanguageCourseTargetLanguage.ML:
            return ml()
        if self is LanguageCourseTargetLanguage.MN:
            return mn()
        if self is LanguageCourseTargetLanguage.MR:
            return mr()
        if self is LanguageCourseTargetLanguage.MS:
            return ms()
        if self is LanguageCourseTargetLanguage.MY:
            return my()
        if self is LanguageCourseTargetLanguage.NE:
            return ne()
        if self is LanguageCourseTargetLanguage.NL:
            return nl()
        if self is LanguageCourseTargetLanguage.NO:
            return no()
        if self is LanguageCourseTargetLanguage.OR:
            return or_()
        if self is LanguageCourseTargetLanguage.PA:
            return pa()
        if self is LanguageCourseTargetLanguage.PL:
            return pl()
        if self is LanguageCourseTargetLanguage.PS:
            return ps()
        if self is LanguageCourseTargetLanguage.PT:
            return pt()
        if self is LanguageCourseTargetLanguage.RO:
            return ro()
        if self is LanguageCourseTargetLanguage.RU:
            return ru()
        if self is LanguageCourseTargetLanguage.SD:
            return sd()
        if self is LanguageCourseTargetLanguage.SI:
            return si()
        if self is LanguageCourseTargetLanguage.SK:
            return sk()
        if self is LanguageCourseTargetLanguage.SL:
            return sl()
        if self is LanguageCourseTargetLanguage.SQ:
            return sq()
        if self is LanguageCourseTargetLanguage.SR:
            return sr()
        if self is LanguageCourseTargetLanguage.SV:
            return sv()
        if self is LanguageCourseTargetLanguage.SW:
            return sw()
        if self is LanguageCourseTargetLanguage.TA:
            return ta()
        if self is LanguageCourseTargetLanguage.TE:
            return te()
        if self is LanguageCourseTargetLanguage.TH:
            return th()
        if self is LanguageCourseTargetLanguage.TL:
            return tl()
        if self is LanguageCourseTargetLanguage.TR:
            return tr()
        if self is LanguageCourseTargetLanguage.UK:
            return uk()
        if self is LanguageCourseTargetLanguage.UR:
            return ur()
        if self is LanguageCourseTargetLanguage.VI:
            return vi()
        if self is LanguageCourseTargetLanguage.ZH:
            return zh()
