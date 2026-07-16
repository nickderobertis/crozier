

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Country(str, enum.Enum):
    """
    Indicates the country associated with another entity, such as a business.
    Values are in [ISO 3166-1-alpha-2 format](http://www.iso.org/iso/home/standards/country_codes.htm).
    """

    ZZ = "ZZ"
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AQ = "AQ"
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
    CU = "CU"
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
    IR = "IR"
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
    KP = "KP"
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
    PR = "PR"
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
    SD = "SD"
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
    SY = "SY"
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
        zz: typing.Callable[[], T_Result],
        ad: typing.Callable[[], T_Result],
        ae: typing.Callable[[], T_Result],
        af: typing.Callable[[], T_Result],
        ag: typing.Callable[[], T_Result],
        ai: typing.Callable[[], T_Result],
        al: typing.Callable[[], T_Result],
        am: typing.Callable[[], T_Result],
        ao: typing.Callable[[], T_Result],
        aq: typing.Callable[[], T_Result],
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
        cu: typing.Callable[[], T_Result],
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
        ir: typing.Callable[[], T_Result],
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
        kp: typing.Callable[[], T_Result],
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
        pr: typing.Callable[[], T_Result],
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
        sd: typing.Callable[[], T_Result],
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
        sy: typing.Callable[[], T_Result],
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
        if self is Country.ZZ:
            return zz()
        if self is Country.AD:
            return ad()
        if self is Country.AE:
            return ae()
        if self is Country.AF:
            return af()
        if self is Country.AG:
            return ag()
        if self is Country.AI:
            return ai()
        if self is Country.AL:
            return al()
        if self is Country.AM:
            return am()
        if self is Country.AO:
            return ao()
        if self is Country.AQ:
            return aq()
        if self is Country.AR:
            return ar()
        if self is Country.AS:
            return as_()
        if self is Country.AT:
            return at()
        if self is Country.AU:
            return au()
        if self is Country.AW:
            return aw()
        if self is Country.AX:
            return ax()
        if self is Country.AZ:
            return az()
        if self is Country.BA:
            return ba()
        if self is Country.BB:
            return bb()
        if self is Country.BD:
            return bd()
        if self is Country.BE:
            return be()
        if self is Country.BF:
            return bf()
        if self is Country.BG:
            return bg()
        if self is Country.BH:
            return bh()
        if self is Country.BI:
            return bi()
        if self is Country.BJ:
            return bj()
        if self is Country.BL:
            return bl()
        if self is Country.BM:
            return bm()
        if self is Country.BN:
            return bn()
        if self is Country.BO:
            return bo()
        if self is Country.BQ:
            return bq()
        if self is Country.BR:
            return br()
        if self is Country.BS:
            return bs()
        if self is Country.BT:
            return bt()
        if self is Country.BV:
            return bv()
        if self is Country.BW:
            return bw()
        if self is Country.BY:
            return by()
        if self is Country.BZ:
            return bz()
        if self is Country.CA:
            return ca()
        if self is Country.CC:
            return cc()
        if self is Country.CD:
            return cd()
        if self is Country.CF:
            return cf()
        if self is Country.CG:
            return cg()
        if self is Country.CH:
            return ch()
        if self is Country.CI:
            return ci()
        if self is Country.CK:
            return ck()
        if self is Country.CL:
            return cl()
        if self is Country.CM:
            return cm()
        if self is Country.CN:
            return cn()
        if self is Country.CO:
            return co()
        if self is Country.CR:
            return cr()
        if self is Country.CU:
            return cu()
        if self is Country.CV:
            return cv()
        if self is Country.CW:
            return cw()
        if self is Country.CX:
            return cx()
        if self is Country.CY:
            return cy()
        if self is Country.CZ:
            return cz()
        if self is Country.DE:
            return de()
        if self is Country.DJ:
            return dj()
        if self is Country.DK:
            return dk()
        if self is Country.DM:
            return dm()
        if self is Country.DO:
            return do()
        if self is Country.DZ:
            return dz()
        if self is Country.EC:
            return ec()
        if self is Country.EE:
            return ee()
        if self is Country.EG:
            return eg()
        if self is Country.EH:
            return eh()
        if self is Country.ER:
            return er()
        if self is Country.ES:
            return es()
        if self is Country.ET:
            return et()
        if self is Country.FI:
            return fi()
        if self is Country.FJ:
            return fj()
        if self is Country.FK:
            return fk()
        if self is Country.FM:
            return fm()
        if self is Country.FO:
            return fo()
        if self is Country.FR:
            return fr()
        if self is Country.GA:
            return ga()
        if self is Country.GB:
            return gb()
        if self is Country.GD:
            return gd()
        if self is Country.GE:
            return ge()
        if self is Country.GF:
            return gf()
        if self is Country.GG:
            return gg()
        if self is Country.GH:
            return gh()
        if self is Country.GI:
            return gi()
        if self is Country.GL:
            return gl()
        if self is Country.GM:
            return gm()
        if self is Country.GN:
            return gn()
        if self is Country.GP:
            return gp()
        if self is Country.GQ:
            return gq()
        if self is Country.GR:
            return gr()
        if self is Country.GS:
            return gs()
        if self is Country.GT:
            return gt()
        if self is Country.GU:
            return gu()
        if self is Country.GW:
            return gw()
        if self is Country.GY:
            return gy()
        if self is Country.HK:
            return hk()
        if self is Country.HM:
            return hm()
        if self is Country.HN:
            return hn()
        if self is Country.HR:
            return hr()
        if self is Country.HT:
            return ht()
        if self is Country.HU:
            return hu()
        if self is Country.ID:
            return id()
        if self is Country.IE:
            return ie()
        if self is Country.IL:
            return il()
        if self is Country.IM:
            return im()
        if self is Country.IN:
            return in_()
        if self is Country.IO:
            return io()
        if self is Country.IQ:
            return iq()
        if self is Country.IR:
            return ir()
        if self is Country.IS:
            return is_()
        if self is Country.IT:
            return it()
        if self is Country.JE:
            return je()
        if self is Country.JM:
            return jm()
        if self is Country.JO:
            return jo()
        if self is Country.JP:
            return jp()
        if self is Country.KE:
            return ke()
        if self is Country.KG:
            return kg()
        if self is Country.KH:
            return kh()
        if self is Country.KI:
            return ki()
        if self is Country.KM:
            return km()
        if self is Country.KN:
            return kn()
        if self is Country.KP:
            return kp()
        if self is Country.KR:
            return kr()
        if self is Country.KW:
            return kw()
        if self is Country.KY:
            return ky()
        if self is Country.KZ:
            return kz()
        if self is Country.LA:
            return la()
        if self is Country.LB:
            return lb()
        if self is Country.LC:
            return lc()
        if self is Country.LI:
            return li()
        if self is Country.LK:
            return lk()
        if self is Country.LR:
            return lr()
        if self is Country.LS:
            return ls()
        if self is Country.LT:
            return lt()
        if self is Country.LU:
            return lu()
        if self is Country.LV:
            return lv()
        if self is Country.LY:
            return ly()
        if self is Country.MA:
            return ma()
        if self is Country.MC:
            return mc()
        if self is Country.MD:
            return md()
        if self is Country.ME:
            return me()
        if self is Country.MF:
            return mf()
        if self is Country.MG:
            return mg()
        if self is Country.MH:
            return mh()
        if self is Country.MK:
            return mk()
        if self is Country.ML:
            return ml()
        if self is Country.MM:
            return mm()
        if self is Country.MN:
            return mn()
        if self is Country.MO:
            return mo()
        if self is Country.MP:
            return mp()
        if self is Country.MQ:
            return mq()
        if self is Country.MR:
            return mr()
        if self is Country.MS:
            return ms()
        if self is Country.MT:
            return mt()
        if self is Country.MU:
            return mu()
        if self is Country.MV:
            return mv()
        if self is Country.MW:
            return mw()
        if self is Country.MX:
            return mx()
        if self is Country.MY:
            return my()
        if self is Country.MZ:
            return mz()
        if self is Country.NA:
            return na()
        if self is Country.NC:
            return nc()
        if self is Country.NE:
            return ne()
        if self is Country.NF:
            return nf()
        if self is Country.NG:
            return ng()
        if self is Country.NI:
            return ni()
        if self is Country.NL:
            return nl()
        if self is Country.NO:
            return no()
        if self is Country.NP:
            return np()
        if self is Country.NR:
            return nr()
        if self is Country.NU:
            return nu()
        if self is Country.NZ:
            return nz()
        if self is Country.OM:
            return om()
        if self is Country.PA:
            return pa()
        if self is Country.PE:
            return pe()
        if self is Country.PF:
            return pf()
        if self is Country.PG:
            return pg()
        if self is Country.PH:
            return ph()
        if self is Country.PK:
            return pk()
        if self is Country.PL:
            return pl()
        if self is Country.PM:
            return pm()
        if self is Country.PN:
            return pn()
        if self is Country.PR:
            return pr()
        if self is Country.PS:
            return ps()
        if self is Country.PT:
            return pt()
        if self is Country.PW:
            return pw()
        if self is Country.PY:
            return py()
        if self is Country.QA:
            return qa()
        if self is Country.RE:
            return re()
        if self is Country.RO:
            return ro()
        if self is Country.RS:
            return rs()
        if self is Country.RU:
            return ru()
        if self is Country.RW:
            return rw()
        if self is Country.SA:
            return sa()
        if self is Country.SB:
            return sb()
        if self is Country.SC:
            return sc()
        if self is Country.SD:
            return sd()
        if self is Country.SE:
            return se()
        if self is Country.SG:
            return sg()
        if self is Country.SH:
            return sh()
        if self is Country.SI:
            return si()
        if self is Country.SJ:
            return sj()
        if self is Country.SK:
            return sk()
        if self is Country.SL:
            return sl()
        if self is Country.SM:
            return sm()
        if self is Country.SN:
            return sn()
        if self is Country.SO:
            return so()
        if self is Country.SR:
            return sr()
        if self is Country.SS:
            return ss()
        if self is Country.ST:
            return st()
        if self is Country.SV:
            return sv()
        if self is Country.SX:
            return sx()
        if self is Country.SY:
            return sy()
        if self is Country.SZ:
            return sz()
        if self is Country.TC:
            return tc()
        if self is Country.TD:
            return td()
        if self is Country.TF:
            return tf()
        if self is Country.TG:
            return tg()
        if self is Country.TH:
            return th()
        if self is Country.TJ:
            return tj()
        if self is Country.TK:
            return tk()
        if self is Country.TL:
            return tl()
        if self is Country.TM:
            return tm()
        if self is Country.TN:
            return tn()
        if self is Country.TO:
            return to()
        if self is Country.TR:
            return tr()
        if self is Country.TT:
            return tt()
        if self is Country.TV:
            return tv()
        if self is Country.TW:
            return tw()
        if self is Country.TZ:
            return tz()
        if self is Country.UA:
            return ua()
        if self is Country.UG:
            return ug()
        if self is Country.UM:
            return um()
        if self is Country.US:
            return us()
        if self is Country.UY:
            return uy()
        if self is Country.UZ:
            return uz()
        if self is Country.VA:
            return va()
        if self is Country.VC:
            return vc()
        if self is Country.VE:
            return ve()
        if self is Country.VG:
            return vg()
        if self is Country.VI:
            return vi()
        if self is Country.VN:
            return vn()
        if self is Country.VU:
            return vu()
        if self is Country.WF:
            return wf()
        if self is Country.WS:
            return ws()
        if self is Country.YE:
            return ye()
        if self is Country.YT:
            return yt()
        if self is Country.ZA:
            return za()
        if self is Country.ZM:
            return zm()
        if self is Country.ZW:
            return zw()
