

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PutShopRequestLegalCountryCode(str, enum.Enum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"

    def visit(
        self,
        ad: typing.Callable[[], T_Result],
        ae: typing.Callable[[], T_Result],
        af: typing.Callable[[], T_Result],
        ag: typing.Callable[[], T_Result],
        ai: typing.Callable[[], T_Result],
        al: typing.Callable[[], T_Result],
        am: typing.Callable[[], T_Result],
        ao: typing.Callable[[], T_Result],
        ar: typing.Callable[[], T_Result],
        as_: typing.Callable[[], T_Result],
        at: typing.Callable[[], T_Result],
        au: typing.Callable[[], T_Result],
        aw: typing.Callable[[], T_Result],
        ax: typing.Callable[[], T_Result],
        az: typing.Callable[[], T_Result],
        ba: typing.Callable[[], T_Result],
        bb: typing.Callable[[], T_Result],
        bd: typing.Callable[[], T_Result],
        be: typing.Callable[[], T_Result],
        bf: typing.Callable[[], T_Result],
        bg: typing.Callable[[], T_Result],
        bh: typing.Callable[[], T_Result],
        bi: typing.Callable[[], T_Result],
        bj: typing.Callable[[], T_Result],
        bl: typing.Callable[[], T_Result],
        bm: typing.Callable[[], T_Result],
        bn: typing.Callable[[], T_Result],
        bo: typing.Callable[[], T_Result],
        bq: typing.Callable[[], T_Result],
        br: typing.Callable[[], T_Result],
        bs: typing.Callable[[], T_Result],
        bt: typing.Callable[[], T_Result],
        bv: typing.Callable[[], T_Result],
        bw: typing.Callable[[], T_Result],
        by: typing.Callable[[], T_Result],
        bz: typing.Callable[[], T_Result],
        ca: typing.Callable[[], T_Result],
        cc: typing.Callable[[], T_Result],
        cd: typing.Callable[[], T_Result],
        cf: typing.Callable[[], T_Result],
        cg: typing.Callable[[], T_Result],
        ch: typing.Callable[[], T_Result],
        ci: typing.Callable[[], T_Result],
        ck: typing.Callable[[], T_Result],
        cl: typing.Callable[[], T_Result],
        cm: typing.Callable[[], T_Result],
        cn: typing.Callable[[], T_Result],
        co: typing.Callable[[], T_Result],
        cr: typing.Callable[[], T_Result],
        cv: typing.Callable[[], T_Result],
        cw: typing.Callable[[], T_Result],
        cx: typing.Callable[[], T_Result],
        cy: typing.Callable[[], T_Result],
        cz: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
        dj: typing.Callable[[], T_Result],
        dk: typing.Callable[[], T_Result],
        dm: typing.Callable[[], T_Result],
        do: typing.Callable[[], T_Result],
        dz: typing.Callable[[], T_Result],
        ec: typing.Callable[[], T_Result],
        ee: typing.Callable[[], T_Result],
        eg: typing.Callable[[], T_Result],
        eh: typing.Callable[[], T_Result],
        er: typing.Callable[[], T_Result],
        es: typing.Callable[[], T_Result],
        et: typing.Callable[[], T_Result],
        fi: typing.Callable[[], T_Result],
        fj: typing.Callable[[], T_Result],
        fk: typing.Callable[[], T_Result],
        fm: typing.Callable[[], T_Result],
        fo: typing.Callable[[], T_Result],
        fr: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        gb: typing.Callable[[], T_Result],
        gd: typing.Callable[[], T_Result],
        ge: typing.Callable[[], T_Result],
        gf: typing.Callable[[], T_Result],
        gg: typing.Callable[[], T_Result],
        gh: typing.Callable[[], T_Result],
        gi: typing.Callable[[], T_Result],
        gl: typing.Callable[[], T_Result],
        gm: typing.Callable[[], T_Result],
        gn: typing.Callable[[], T_Result],
        gp: typing.Callable[[], T_Result],
        gq: typing.Callable[[], T_Result],
        gr: typing.Callable[[], T_Result],
        gs: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
        gu: typing.Callable[[], T_Result],
        gw: typing.Callable[[], T_Result],
        gy: typing.Callable[[], T_Result],
        hk: typing.Callable[[], T_Result],
        hm: typing.Callable[[], T_Result],
        hn: typing.Callable[[], T_Result],
        hr: typing.Callable[[], T_Result],
        ht: typing.Callable[[], T_Result],
        hu: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        ie: typing.Callable[[], T_Result],
        il: typing.Callable[[], T_Result],
        im: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        io: typing.Callable[[], T_Result],
        iq: typing.Callable[[], T_Result],
        is_: typing.Callable[[], T_Result],
        it: typing.Callable[[], T_Result],
        je: typing.Callable[[], T_Result],
        jm: typing.Callable[[], T_Result],
        jo: typing.Callable[[], T_Result],
        jp: typing.Callable[[], T_Result],
        ke: typing.Callable[[], T_Result],
        kg: typing.Callable[[], T_Result],
        kh: typing.Callable[[], T_Result],
        ki: typing.Callable[[], T_Result],
        km: typing.Callable[[], T_Result],
        kn: typing.Callable[[], T_Result],
        kr: typing.Callable[[], T_Result],
        kw: typing.Callable[[], T_Result],
        ky: typing.Callable[[], T_Result],
        kz: typing.Callable[[], T_Result],
        la: typing.Callable[[], T_Result],
        lb: typing.Callable[[], T_Result],
        lc: typing.Callable[[], T_Result],
        li: typing.Callable[[], T_Result],
        lk: typing.Callable[[], T_Result],
        lr: typing.Callable[[], T_Result],
        ls: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        lu: typing.Callable[[], T_Result],
        lv: typing.Callable[[], T_Result],
        ly: typing.Callable[[], T_Result],
        ma: typing.Callable[[], T_Result],
        mc: typing.Callable[[], T_Result],
        md: typing.Callable[[], T_Result],
        me: typing.Callable[[], T_Result],
        mf: typing.Callable[[], T_Result],
        mg: typing.Callable[[], T_Result],
        mh: typing.Callable[[], T_Result],
        mk: typing.Callable[[], T_Result],
        ml: typing.Callable[[], T_Result],
        mm: typing.Callable[[], T_Result],
        mn: typing.Callable[[], T_Result],
        mo: typing.Callable[[], T_Result],
        mp: typing.Callable[[], T_Result],
        mq: typing.Callable[[], T_Result],
        mr: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
        mt: typing.Callable[[], T_Result],
        mu: typing.Callable[[], T_Result],
        mv: typing.Callable[[], T_Result],
        mw: typing.Callable[[], T_Result],
        mx: typing.Callable[[], T_Result],
        my: typing.Callable[[], T_Result],
        mz: typing.Callable[[], T_Result],
        na: typing.Callable[[], T_Result],
        nc: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        nf: typing.Callable[[], T_Result],
        ng: typing.Callable[[], T_Result],
        ni: typing.Callable[[], T_Result],
        nl: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        np: typing.Callable[[], T_Result],
        nr: typing.Callable[[], T_Result],
        nu: typing.Callable[[], T_Result],
        nz: typing.Callable[[], T_Result],
        om: typing.Callable[[], T_Result],
        pa: typing.Callable[[], T_Result],
        pe: typing.Callable[[], T_Result],
        pf: typing.Callable[[], T_Result],
        pg: typing.Callable[[], T_Result],
        ph: typing.Callable[[], T_Result],
        pk: typing.Callable[[], T_Result],
        pl: typing.Callable[[], T_Result],
        pm: typing.Callable[[], T_Result],
        pn: typing.Callable[[], T_Result],
        ps: typing.Callable[[], T_Result],
        pt: typing.Callable[[], T_Result],
        pw: typing.Callable[[], T_Result],
        py: typing.Callable[[], T_Result],
        qa: typing.Callable[[], T_Result],
        re: typing.Callable[[], T_Result],
        ro: typing.Callable[[], T_Result],
        rs: typing.Callable[[], T_Result],
        ru: typing.Callable[[], T_Result],
        rw: typing.Callable[[], T_Result],
        sa: typing.Callable[[], T_Result],
        sb: typing.Callable[[], T_Result],
        sc: typing.Callable[[], T_Result],
        se: typing.Callable[[], T_Result],
        sg: typing.Callable[[], T_Result],
        sh: typing.Callable[[], T_Result],
        si: typing.Callable[[], T_Result],
        sj: typing.Callable[[], T_Result],
        sk: typing.Callable[[], T_Result],
        sl: typing.Callable[[], T_Result],
        sm: typing.Callable[[], T_Result],
        sn: typing.Callable[[], T_Result],
        so: typing.Callable[[], T_Result],
        sr: typing.Callable[[], T_Result],
        ss: typing.Callable[[], T_Result],
        st: typing.Callable[[], T_Result],
        sv: typing.Callable[[], T_Result],
        sx: typing.Callable[[], T_Result],
        sz: typing.Callable[[], T_Result],
        tc: typing.Callable[[], T_Result],
        td: typing.Callable[[], T_Result],
        tf: typing.Callable[[], T_Result],
        tg: typing.Callable[[], T_Result],
        th: typing.Callable[[], T_Result],
        tj: typing.Callable[[], T_Result],
        tk: typing.Callable[[], T_Result],
        tl: typing.Callable[[], T_Result],
        tm: typing.Callable[[], T_Result],
        tn: typing.Callable[[], T_Result],
        to: typing.Callable[[], T_Result],
        tr: typing.Callable[[], T_Result],
        tt: typing.Callable[[], T_Result],
        tv: typing.Callable[[], T_Result],
        tw: typing.Callable[[], T_Result],
        tz: typing.Callable[[], T_Result],
        ua: typing.Callable[[], T_Result],
        ug: typing.Callable[[], T_Result],
        um: typing.Callable[[], T_Result],
        us: typing.Callable[[], T_Result],
        uy: typing.Callable[[], T_Result],
        uz: typing.Callable[[], T_Result],
        va: typing.Callable[[], T_Result],
        vc: typing.Callable[[], T_Result],
        ve: typing.Callable[[], T_Result],
        vg: typing.Callable[[], T_Result],
        vi: typing.Callable[[], T_Result],
        vn: typing.Callable[[], T_Result],
        vu: typing.Callable[[], T_Result],
        wf: typing.Callable[[], T_Result],
        ws: typing.Callable[[], T_Result],
        ye: typing.Callable[[], T_Result],
        yt: typing.Callable[[], T_Result],
        za: typing.Callable[[], T_Result],
        zm: typing.Callable[[], T_Result],
        zw: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutShopRequestLegalCountryCode.AD:
            return ad()
        if self is PutShopRequestLegalCountryCode.AE:
            return ae()
        if self is PutShopRequestLegalCountryCode.AF:
            return af()
        if self is PutShopRequestLegalCountryCode.AG:
            return ag()
        if self is PutShopRequestLegalCountryCode.AI:
            return ai()
        if self is PutShopRequestLegalCountryCode.AL:
            return al()
        if self is PutShopRequestLegalCountryCode.AM:
            return am()
        if self is PutShopRequestLegalCountryCode.AO:
            return ao()
        if self is PutShopRequestLegalCountryCode.AR:
            return ar()
        if self is PutShopRequestLegalCountryCode.AS:
            return as_()
        if self is PutShopRequestLegalCountryCode.AT:
            return at()
        if self is PutShopRequestLegalCountryCode.AU:
            return au()
        if self is PutShopRequestLegalCountryCode.AW:
            return aw()
        if self is PutShopRequestLegalCountryCode.AX:
            return ax()
        if self is PutShopRequestLegalCountryCode.AZ:
            return az()
        if self is PutShopRequestLegalCountryCode.BA:
            return ba()
        if self is PutShopRequestLegalCountryCode.BB:
            return bb()
        if self is PutShopRequestLegalCountryCode.BD:
            return bd()
        if self is PutShopRequestLegalCountryCode.BE:
            return be()
        if self is PutShopRequestLegalCountryCode.BF:
            return bf()
        if self is PutShopRequestLegalCountryCode.BG:
            return bg()
        if self is PutShopRequestLegalCountryCode.BH:
            return bh()
        if self is PutShopRequestLegalCountryCode.BI:
            return bi()
        if self is PutShopRequestLegalCountryCode.BJ:
            return bj()
        if self is PutShopRequestLegalCountryCode.BL:
            return bl()
        if self is PutShopRequestLegalCountryCode.BM:
            return bm()
        if self is PutShopRequestLegalCountryCode.BN:
            return bn()
        if self is PutShopRequestLegalCountryCode.BO:
            return bo()
        if self is PutShopRequestLegalCountryCode.BQ:
            return bq()
        if self is PutShopRequestLegalCountryCode.BR:
            return br()
        if self is PutShopRequestLegalCountryCode.BS:
            return bs()
        if self is PutShopRequestLegalCountryCode.BT:
            return bt()
        if self is PutShopRequestLegalCountryCode.BV:
            return bv()
        if self is PutShopRequestLegalCountryCode.BW:
            return bw()
        if self is PutShopRequestLegalCountryCode.BY:
            return by()
        if self is PutShopRequestLegalCountryCode.BZ:
            return bz()
        if self is PutShopRequestLegalCountryCode.CA:
            return ca()
        if self is PutShopRequestLegalCountryCode.CC:
            return cc()
        if self is PutShopRequestLegalCountryCode.CD:
            return cd()
        if self is PutShopRequestLegalCountryCode.CF:
            return cf()
        if self is PutShopRequestLegalCountryCode.CG:
            return cg()
        if self is PutShopRequestLegalCountryCode.CH:
            return ch()
        if self is PutShopRequestLegalCountryCode.CI:
            return ci()
        if self is PutShopRequestLegalCountryCode.CK:
            return ck()
        if self is PutShopRequestLegalCountryCode.CL:
            return cl()
        if self is PutShopRequestLegalCountryCode.CM:
            return cm()
        if self is PutShopRequestLegalCountryCode.CN:
            return cn()
        if self is PutShopRequestLegalCountryCode.CO:
            return co()
        if self is PutShopRequestLegalCountryCode.CR:
            return cr()
        if self is PutShopRequestLegalCountryCode.CV:
            return cv()
        if self is PutShopRequestLegalCountryCode.CW:
            return cw()
        if self is PutShopRequestLegalCountryCode.CX:
            return cx()
        if self is PutShopRequestLegalCountryCode.CY:
            return cy()
        if self is PutShopRequestLegalCountryCode.CZ:
            return cz()
        if self is PutShopRequestLegalCountryCode.DE:
            return de()
        if self is PutShopRequestLegalCountryCode.DJ:
            return dj()
        if self is PutShopRequestLegalCountryCode.DK:
            return dk()
        if self is PutShopRequestLegalCountryCode.DM:
            return dm()
        if self is PutShopRequestLegalCountryCode.DO:
            return do()
        if self is PutShopRequestLegalCountryCode.DZ:
            return dz()
        if self is PutShopRequestLegalCountryCode.EC:
            return ec()
        if self is PutShopRequestLegalCountryCode.EE:
            return ee()
        if self is PutShopRequestLegalCountryCode.EG:
            return eg()
        if self is PutShopRequestLegalCountryCode.EH:
            return eh()
        if self is PutShopRequestLegalCountryCode.ER:
            return er()
        if self is PutShopRequestLegalCountryCode.ES:
            return es()
        if self is PutShopRequestLegalCountryCode.ET:
            return et()
        if self is PutShopRequestLegalCountryCode.FI:
            return fi()
        if self is PutShopRequestLegalCountryCode.FJ:
            return fj()
        if self is PutShopRequestLegalCountryCode.FK:
            return fk()
        if self is PutShopRequestLegalCountryCode.FM:
            return fm()
        if self is PutShopRequestLegalCountryCode.FO:
            return fo()
        if self is PutShopRequestLegalCountryCode.FR:
            return fr()
        if self is PutShopRequestLegalCountryCode.GA:
            return ga()
        if self is PutShopRequestLegalCountryCode.GB:
            return gb()
        if self is PutShopRequestLegalCountryCode.GD:
            return gd()
        if self is PutShopRequestLegalCountryCode.GE:
            return ge()
        if self is PutShopRequestLegalCountryCode.GF:
            return gf()
        if self is PutShopRequestLegalCountryCode.GG:
            return gg()
        if self is PutShopRequestLegalCountryCode.GH:
            return gh()
        if self is PutShopRequestLegalCountryCode.GI:
            return gi()
        if self is PutShopRequestLegalCountryCode.GL:
            return gl()
        if self is PutShopRequestLegalCountryCode.GM:
            return gm()
        if self is PutShopRequestLegalCountryCode.GN:
            return gn()
        if self is PutShopRequestLegalCountryCode.GP:
            return gp()
        if self is PutShopRequestLegalCountryCode.GQ:
            return gq()
        if self is PutShopRequestLegalCountryCode.GR:
            return gr()
        if self is PutShopRequestLegalCountryCode.GS:
            return gs()
        if self is PutShopRequestLegalCountryCode.GT:
            return gt()
        if self is PutShopRequestLegalCountryCode.GU:
            return gu()
        if self is PutShopRequestLegalCountryCode.GW:
            return gw()
        if self is PutShopRequestLegalCountryCode.GY:
            return gy()
        if self is PutShopRequestLegalCountryCode.HK:
            return hk()
        if self is PutShopRequestLegalCountryCode.HM:
            return hm()
        if self is PutShopRequestLegalCountryCode.HN:
            return hn()
        if self is PutShopRequestLegalCountryCode.HR:
            return hr()
        if self is PutShopRequestLegalCountryCode.HT:
            return ht()
        if self is PutShopRequestLegalCountryCode.HU:
            return hu()
        if self is PutShopRequestLegalCountryCode.ID:
            return id()
        if self is PutShopRequestLegalCountryCode.IE:
            return ie()
        if self is PutShopRequestLegalCountryCode.IL:
            return il()
        if self is PutShopRequestLegalCountryCode.IM:
            return im()
        if self is PutShopRequestLegalCountryCode.IN:
            return in_()
        if self is PutShopRequestLegalCountryCode.IO:
            return io()
        if self is PutShopRequestLegalCountryCode.IQ:
            return iq()
        if self is PutShopRequestLegalCountryCode.IS:
            return is_()
        if self is PutShopRequestLegalCountryCode.IT:
            return it()
        if self is PutShopRequestLegalCountryCode.JE:
            return je()
        if self is PutShopRequestLegalCountryCode.JM:
            return jm()
        if self is PutShopRequestLegalCountryCode.JO:
            return jo()
        if self is PutShopRequestLegalCountryCode.JP:
            return jp()
        if self is PutShopRequestLegalCountryCode.KE:
            return ke()
        if self is PutShopRequestLegalCountryCode.KG:
            return kg()
        if self is PutShopRequestLegalCountryCode.KH:
            return kh()
        if self is PutShopRequestLegalCountryCode.KI:
            return ki()
        if self is PutShopRequestLegalCountryCode.KM:
            return km()
        if self is PutShopRequestLegalCountryCode.KN:
            return kn()
        if self is PutShopRequestLegalCountryCode.KR:
            return kr()
        if self is PutShopRequestLegalCountryCode.KW:
            return kw()
        if self is PutShopRequestLegalCountryCode.KY:
            return ky()
        if self is PutShopRequestLegalCountryCode.KZ:
            return kz()
        if self is PutShopRequestLegalCountryCode.LA:
            return la()
        if self is PutShopRequestLegalCountryCode.LB:
            return lb()
        if self is PutShopRequestLegalCountryCode.LC:
            return lc()
        if self is PutShopRequestLegalCountryCode.LI:
            return li()
        if self is PutShopRequestLegalCountryCode.LK:
            return lk()
        if self is PutShopRequestLegalCountryCode.LR:
            return lr()
        if self is PutShopRequestLegalCountryCode.LS:
            return ls()
        if self is PutShopRequestLegalCountryCode.LT:
            return lt()
        if self is PutShopRequestLegalCountryCode.LU:
            return lu()
        if self is PutShopRequestLegalCountryCode.LV:
            return lv()
        if self is PutShopRequestLegalCountryCode.LY:
            return ly()
        if self is PutShopRequestLegalCountryCode.MA:
            return ma()
        if self is PutShopRequestLegalCountryCode.MC:
            return mc()
        if self is PutShopRequestLegalCountryCode.MD:
            return md()
        if self is PutShopRequestLegalCountryCode.ME:
            return me()
        if self is PutShopRequestLegalCountryCode.MF:
            return mf()
        if self is PutShopRequestLegalCountryCode.MG:
            return mg()
        if self is PutShopRequestLegalCountryCode.MH:
            return mh()
        if self is PutShopRequestLegalCountryCode.MK:
            return mk()
        if self is PutShopRequestLegalCountryCode.ML:
            return ml()
        if self is PutShopRequestLegalCountryCode.MM:
            return mm()
        if self is PutShopRequestLegalCountryCode.MN:
            return mn()
        if self is PutShopRequestLegalCountryCode.MO:
            return mo()
        if self is PutShopRequestLegalCountryCode.MP:
            return mp()
        if self is PutShopRequestLegalCountryCode.MQ:
            return mq()
        if self is PutShopRequestLegalCountryCode.MR:
            return mr()
        if self is PutShopRequestLegalCountryCode.MS:
            return ms()
        if self is PutShopRequestLegalCountryCode.MT:
            return mt()
        if self is PutShopRequestLegalCountryCode.MU:
            return mu()
        if self is PutShopRequestLegalCountryCode.MV:
            return mv()
        if self is PutShopRequestLegalCountryCode.MW:
            return mw()
        if self is PutShopRequestLegalCountryCode.MX:
            return mx()
        if self is PutShopRequestLegalCountryCode.MY:
            return my()
        if self is PutShopRequestLegalCountryCode.MZ:
            return mz()
        if self is PutShopRequestLegalCountryCode.NA:
            return na()
        if self is PutShopRequestLegalCountryCode.NC:
            return nc()
        if self is PutShopRequestLegalCountryCode.NE:
            return ne()
        if self is PutShopRequestLegalCountryCode.NF:
            return nf()
        if self is PutShopRequestLegalCountryCode.NG:
            return ng()
        if self is PutShopRequestLegalCountryCode.NI:
            return ni()
        if self is PutShopRequestLegalCountryCode.NL:
            return nl()
        if self is PutShopRequestLegalCountryCode.NO:
            return no()
        if self is PutShopRequestLegalCountryCode.NP:
            return np()
        if self is PutShopRequestLegalCountryCode.NR:
            return nr()
        if self is PutShopRequestLegalCountryCode.NU:
            return nu()
        if self is PutShopRequestLegalCountryCode.NZ:
            return nz()
        if self is PutShopRequestLegalCountryCode.OM:
            return om()
        if self is PutShopRequestLegalCountryCode.PA:
            return pa()
        if self is PutShopRequestLegalCountryCode.PE:
            return pe()
        if self is PutShopRequestLegalCountryCode.PF:
            return pf()
        if self is PutShopRequestLegalCountryCode.PG:
            return pg()
        if self is PutShopRequestLegalCountryCode.PH:
            return ph()
        if self is PutShopRequestLegalCountryCode.PK:
            return pk()
        if self is PutShopRequestLegalCountryCode.PL:
            return pl()
        if self is PutShopRequestLegalCountryCode.PM:
            return pm()
        if self is PutShopRequestLegalCountryCode.PN:
            return pn()
        if self is PutShopRequestLegalCountryCode.PS:
            return ps()
        if self is PutShopRequestLegalCountryCode.PT:
            return pt()
        if self is PutShopRequestLegalCountryCode.PW:
            return pw()
        if self is PutShopRequestLegalCountryCode.PY:
            return py()
        if self is PutShopRequestLegalCountryCode.QA:
            return qa()
        if self is PutShopRequestLegalCountryCode.RE:
            return re()
        if self is PutShopRequestLegalCountryCode.RO:
            return ro()
        if self is PutShopRequestLegalCountryCode.RS:
            return rs()
        if self is PutShopRequestLegalCountryCode.RU:
            return ru()
        if self is PutShopRequestLegalCountryCode.RW:
            return rw()
        if self is PutShopRequestLegalCountryCode.SA:
            return sa()
        if self is PutShopRequestLegalCountryCode.SB:
            return sb()
        if self is PutShopRequestLegalCountryCode.SC:
            return sc()
        if self is PutShopRequestLegalCountryCode.SE:
            return se()
        if self is PutShopRequestLegalCountryCode.SG:
            return sg()
        if self is PutShopRequestLegalCountryCode.SH:
            return sh()
        if self is PutShopRequestLegalCountryCode.SI:
            return si()
        if self is PutShopRequestLegalCountryCode.SJ:
            return sj()
        if self is PutShopRequestLegalCountryCode.SK:
            return sk()
        if self is PutShopRequestLegalCountryCode.SL:
            return sl()
        if self is PutShopRequestLegalCountryCode.SM:
            return sm()
        if self is PutShopRequestLegalCountryCode.SN:
            return sn()
        if self is PutShopRequestLegalCountryCode.SO:
            return so()
        if self is PutShopRequestLegalCountryCode.SR:
            return sr()
        if self is PutShopRequestLegalCountryCode.SS:
            return ss()
        if self is PutShopRequestLegalCountryCode.ST:
            return st()
        if self is PutShopRequestLegalCountryCode.SV:
            return sv()
        if self is PutShopRequestLegalCountryCode.SX:
            return sx()
        if self is PutShopRequestLegalCountryCode.SZ:
            return sz()
        if self is PutShopRequestLegalCountryCode.TC:
            return tc()
        if self is PutShopRequestLegalCountryCode.TD:
            return td()
        if self is PutShopRequestLegalCountryCode.TF:
            return tf()
        if self is PutShopRequestLegalCountryCode.TG:
            return tg()
        if self is PutShopRequestLegalCountryCode.TH:
            return th()
        if self is PutShopRequestLegalCountryCode.TJ:
            return tj()
        if self is PutShopRequestLegalCountryCode.TK:
            return tk()
        if self is PutShopRequestLegalCountryCode.TL:
            return tl()
        if self is PutShopRequestLegalCountryCode.TM:
            return tm()
        if self is PutShopRequestLegalCountryCode.TN:
            return tn()
        if self is PutShopRequestLegalCountryCode.TO:
            return to()
        if self is PutShopRequestLegalCountryCode.TR:
            return tr()
        if self is PutShopRequestLegalCountryCode.TT:
            return tt()
        if self is PutShopRequestLegalCountryCode.TV:
            return tv()
        if self is PutShopRequestLegalCountryCode.TW:
            return tw()
        if self is PutShopRequestLegalCountryCode.TZ:
            return tz()
        if self is PutShopRequestLegalCountryCode.UA:
            return ua()
        if self is PutShopRequestLegalCountryCode.UG:
            return ug()
        if self is PutShopRequestLegalCountryCode.UM:
            return um()
        if self is PutShopRequestLegalCountryCode.US:
            return us()
        if self is PutShopRequestLegalCountryCode.UY:
            return uy()
        if self is PutShopRequestLegalCountryCode.UZ:
            return uz()
        if self is PutShopRequestLegalCountryCode.VA:
            return va()
        if self is PutShopRequestLegalCountryCode.VC:
            return vc()
        if self is PutShopRequestLegalCountryCode.VE:
            return ve()
        if self is PutShopRequestLegalCountryCode.VG:
            return vg()
        if self is PutShopRequestLegalCountryCode.VI:
            return vi()
        if self is PutShopRequestLegalCountryCode.VN:
            return vn()
        if self is PutShopRequestLegalCountryCode.VU:
            return vu()
        if self is PutShopRequestLegalCountryCode.WF:
            return wf()
        if self is PutShopRequestLegalCountryCode.WS:
            return ws()
        if self is PutShopRequestLegalCountryCode.YE:
            return ye()
        if self is PutShopRequestLegalCountryCode.YT:
            return yt()
        if self is PutShopRequestLegalCountryCode.ZA:
            return za()
        if self is PutShopRequestLegalCountryCode.ZM:
            return zm()
        if self is PutShopRequestLegalCountryCode.ZW:
            return zw()
