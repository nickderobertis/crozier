

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MappingJobStateCode(enum.StrEnum):
    AB = "AB"
    AC = "AC"
    AH = "AH"
    AK = "AK"
    AL = "AL"
    AM = "AM"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AZ = "AZ"
    BC = "BC"
    BJ = "BJ"
    CA = "CA"
    CB = "CB"
    CO = "CO"
    CQ = "CQ"
    CT = "CT"
    CZ = "CZ"
    DC = "DC"
    DE = "DE"
    EH = "EH"
    FH = "FH"
    FI = "FI"
    FJ = "FJ"
    FL = "FL"
    FO = "FO"
    FS = "FS"
    GA = "GA"
    GD = "GD"
    GF = "GF"
    GM = "GM"
    GS = "GS"
    GU = "GU"
    GX = "GX"
    GZ = "GZ"
    HA = "HA"
    HB = "HB"
    HE = "HE"
    HG = "HG"
    HI = "HI"
    HL = "HL"
    HN = "HN"
    HO = "HO"
    HS = "HS"
    IA = "IA"
    ID = "ID"
    IG = "IG"
    IK = "IK"
    IL = "IL"
    IN = "IN"
    IT = "IT"
    JL = "JL"
    JS = "JS"
    JX = "JX"
    KA = "KA"
    KC = "KC"
    KN = "KN"
    KO = "KO"
    KS = "KS"
    KT = "KT"
    KU = "KU"
    KY = "KY"
    LA = "LA"
    LN = "LN"
    MA = "MA"
    MB = "MB"
    MD = "MD"
    ME = "ME"
    MG = "MG"
    MI = "MI"
    MN = "MN"
    MO = "MO"
    MS = "MS"
    MT = "MT"
    MZ = "MZ"
    NB = "NB"
    NC = "NC"
    ND = "ND"
    NE = "NE"
    NG = "NG"
    NH = "NH"
    NJ = "NJ"
    NL = "NL"
    NM = "NM"
    NN = "NN"
    NR = "NR"
    NS = "NS"
    NT = "NT"
    NU = "NU"
    NV = "NV"
    NW = "NW"
    NX = "NX"
    NY = "NY"
    OH = "OH"
    OK = "OK"
    ON = "ON"
    OR = "OR"
    OS = "OS"
    OT = "OT"
    OY = "OY"
    PA = "PA"
    PE = "PE"
    PR = "PR"
    QC = "QC"
    QH = "QH"
    QL = "QL"
    RI = "RI"
    SA = "SA"
    SC = "SC"
    SD = "SD"
    SH = "SH"
    SI = "SI"
    SK = "SK"
    SN = "SN"
    ST = "ST"
    SX = "SX"
    SZ = "SZ"
    TA = "TA"
    TG = "TG"
    TJ = "TJ"
    TK = "TK"
    TN = "TN"
    TS = "TS"
    TT = "TT"
    TX = "TX"
    TY = "TY"
    UT = "UT"
    VA = "VA"
    VI = "VI"
    VT = "VT"
    WA = "WA"
    WI = "WI"
    WK = "WK"
    WV = "WV"
    WY = "WY"
    XJ = "XJ"
    XZ = "XZ"
    YA = "YA"
    YN = "YN"
    YT = "YT"
    YU = "YU"
    ZJ = "ZJ"

    def visit(
        self,
        ab: typing.Callable[[], T_Result],
        ac: typing.Callable[[], T_Result],
        ah: typing.Callable[[], T_Result],
        ak: typing.Callable[[], T_Result],
        al: typing.Callable[[], T_Result],
        am: typing.Callable[[], T_Result],
        ar: typing.Callable[[], T_Result],
        as_: typing.Callable[[], T_Result],
        at: typing.Callable[[], T_Result],
        az: typing.Callable[[], T_Result],
        bc: typing.Callable[[], T_Result],
        bj: typing.Callable[[], T_Result],
        ca: typing.Callable[[], T_Result],
        cb: typing.Callable[[], T_Result],
        co: typing.Callable[[], T_Result],
        cq: typing.Callable[[], T_Result],
        ct: typing.Callable[[], T_Result],
        cz: typing.Callable[[], T_Result],
        dc: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
        eh: typing.Callable[[], T_Result],
        fh: typing.Callable[[], T_Result],
        fi: typing.Callable[[], T_Result],
        fj: typing.Callable[[], T_Result],
        fl: typing.Callable[[], T_Result],
        fo: typing.Callable[[], T_Result],
        fs: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        gd: typing.Callable[[], T_Result],
        gf: typing.Callable[[], T_Result],
        gm: typing.Callable[[], T_Result],
        gs: typing.Callable[[], T_Result],
        gu: typing.Callable[[], T_Result],
        gx: typing.Callable[[], T_Result],
        gz: typing.Callable[[], T_Result],
        ha: typing.Callable[[], T_Result],
        hb: typing.Callable[[], T_Result],
        he: typing.Callable[[], T_Result],
        hg: typing.Callable[[], T_Result],
        hi: typing.Callable[[], T_Result],
        hl: typing.Callable[[], T_Result],
        hn: typing.Callable[[], T_Result],
        ho: typing.Callable[[], T_Result],
        hs: typing.Callable[[], T_Result],
        ia: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        ig: typing.Callable[[], T_Result],
        ik: typing.Callable[[], T_Result],
        il: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        it: typing.Callable[[], T_Result],
        jl: typing.Callable[[], T_Result],
        js: typing.Callable[[], T_Result],
        jx: typing.Callable[[], T_Result],
        ka: typing.Callable[[], T_Result],
        kc: typing.Callable[[], T_Result],
        kn: typing.Callable[[], T_Result],
        ko: typing.Callable[[], T_Result],
        ks: typing.Callable[[], T_Result],
        kt: typing.Callable[[], T_Result],
        ku: typing.Callable[[], T_Result],
        ky: typing.Callable[[], T_Result],
        la: typing.Callable[[], T_Result],
        ln: typing.Callable[[], T_Result],
        ma: typing.Callable[[], T_Result],
        mb: typing.Callable[[], T_Result],
        md: typing.Callable[[], T_Result],
        me: typing.Callable[[], T_Result],
        mg: typing.Callable[[], T_Result],
        mi: typing.Callable[[], T_Result],
        mn: typing.Callable[[], T_Result],
        mo: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
        mt: typing.Callable[[], T_Result],
        mz: typing.Callable[[], T_Result],
        nb: typing.Callable[[], T_Result],
        nc: typing.Callable[[], T_Result],
        nd: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        ng: typing.Callable[[], T_Result],
        nh: typing.Callable[[], T_Result],
        nj: typing.Callable[[], T_Result],
        nl: typing.Callable[[], T_Result],
        nm: typing.Callable[[], T_Result],
        nn: typing.Callable[[], T_Result],
        nr: typing.Callable[[], T_Result],
        ns: typing.Callable[[], T_Result],
        nt: typing.Callable[[], T_Result],
        nu: typing.Callable[[], T_Result],
        nv: typing.Callable[[], T_Result],
        nw: typing.Callable[[], T_Result],
        nx: typing.Callable[[], T_Result],
        ny: typing.Callable[[], T_Result],
        oh: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
        on: typing.Callable[[], T_Result],
        or_: typing.Callable[[], T_Result],
        os: typing.Callable[[], T_Result],
        ot: typing.Callable[[], T_Result],
        oy: typing.Callable[[], T_Result],
        pa: typing.Callable[[], T_Result],
        pe: typing.Callable[[], T_Result],
        pr: typing.Callable[[], T_Result],
        qc: typing.Callable[[], T_Result],
        qh: typing.Callable[[], T_Result],
        ql: typing.Callable[[], T_Result],
        ri: typing.Callable[[], T_Result],
        sa: typing.Callable[[], T_Result],
        sc: typing.Callable[[], T_Result],
        sd: typing.Callable[[], T_Result],
        sh: typing.Callable[[], T_Result],
        si: typing.Callable[[], T_Result],
        sk: typing.Callable[[], T_Result],
        sn: typing.Callable[[], T_Result],
        st: typing.Callable[[], T_Result],
        sx: typing.Callable[[], T_Result],
        sz: typing.Callable[[], T_Result],
        ta: typing.Callable[[], T_Result],
        tg: typing.Callable[[], T_Result],
        tj: typing.Callable[[], T_Result],
        tk: typing.Callable[[], T_Result],
        tn: typing.Callable[[], T_Result],
        ts: typing.Callable[[], T_Result],
        tt: typing.Callable[[], T_Result],
        tx: typing.Callable[[], T_Result],
        ty: typing.Callable[[], T_Result],
        ut: typing.Callable[[], T_Result],
        va: typing.Callable[[], T_Result],
        vi: typing.Callable[[], T_Result],
        vt: typing.Callable[[], T_Result],
        wa: typing.Callable[[], T_Result],
        wi: typing.Callable[[], T_Result],
        wk: typing.Callable[[], T_Result],
        wv: typing.Callable[[], T_Result],
        wy: typing.Callable[[], T_Result],
        xj: typing.Callable[[], T_Result],
        xz: typing.Callable[[], T_Result],
        ya: typing.Callable[[], T_Result],
        yn: typing.Callable[[], T_Result],
        yt: typing.Callable[[], T_Result],
        yu: typing.Callable[[], T_Result],
        zj: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MappingJobStateCode.AB:
            return ab()
        if self is MappingJobStateCode.AC:
            return ac()
        if self is MappingJobStateCode.AH:
            return ah()
        if self is MappingJobStateCode.AK:
            return ak()
        if self is MappingJobStateCode.AL:
            return al()
        if self is MappingJobStateCode.AM:
            return am()
        if self is MappingJobStateCode.AR:
            return ar()
        if self is MappingJobStateCode.AS:
            return as_()
        if self is MappingJobStateCode.AT:
            return at()
        if self is MappingJobStateCode.AZ:
            return az()
        if self is MappingJobStateCode.BC:
            return bc()
        if self is MappingJobStateCode.BJ:
            return bj()
        if self is MappingJobStateCode.CA:
            return ca()
        if self is MappingJobStateCode.CB:
            return cb()
        if self is MappingJobStateCode.CO:
            return co()
        if self is MappingJobStateCode.CQ:
            return cq()
        if self is MappingJobStateCode.CT:
            return ct()
        if self is MappingJobStateCode.CZ:
            return cz()
        if self is MappingJobStateCode.DC:
            return dc()
        if self is MappingJobStateCode.DE:
            return de()
        if self is MappingJobStateCode.EH:
            return eh()
        if self is MappingJobStateCode.FH:
            return fh()
        if self is MappingJobStateCode.FI:
            return fi()
        if self is MappingJobStateCode.FJ:
            return fj()
        if self is MappingJobStateCode.FL:
            return fl()
        if self is MappingJobStateCode.FO:
            return fo()
        if self is MappingJobStateCode.FS:
            return fs()
        if self is MappingJobStateCode.GA:
            return ga()
        if self is MappingJobStateCode.GD:
            return gd()
        if self is MappingJobStateCode.GF:
            return gf()
        if self is MappingJobStateCode.GM:
            return gm()
        if self is MappingJobStateCode.GS:
            return gs()
        if self is MappingJobStateCode.GU:
            return gu()
        if self is MappingJobStateCode.GX:
            return gx()
        if self is MappingJobStateCode.GZ:
            return gz()
        if self is MappingJobStateCode.HA:
            return ha()
        if self is MappingJobStateCode.HB:
            return hb()
        if self is MappingJobStateCode.HE:
            return he()
        if self is MappingJobStateCode.HG:
            return hg()
        if self is MappingJobStateCode.HI:
            return hi()
        if self is MappingJobStateCode.HL:
            return hl()
        if self is MappingJobStateCode.HN:
            return hn()
        if self is MappingJobStateCode.HO:
            return ho()
        if self is MappingJobStateCode.HS:
            return hs()
        if self is MappingJobStateCode.IA:
            return ia()
        if self is MappingJobStateCode.ID:
            return id()
        if self is MappingJobStateCode.IG:
            return ig()
        if self is MappingJobStateCode.IK:
            return ik()
        if self is MappingJobStateCode.IL:
            return il()
        if self is MappingJobStateCode.IN:
            return in_()
        if self is MappingJobStateCode.IT:
            return it()
        if self is MappingJobStateCode.JL:
            return jl()
        if self is MappingJobStateCode.JS:
            return js()
        if self is MappingJobStateCode.JX:
            return jx()
        if self is MappingJobStateCode.KA:
            return ka()
        if self is MappingJobStateCode.KC:
            return kc()
        if self is MappingJobStateCode.KN:
            return kn()
        if self is MappingJobStateCode.KO:
            return ko()
        if self is MappingJobStateCode.KS:
            return ks()
        if self is MappingJobStateCode.KT:
            return kt()
        if self is MappingJobStateCode.KU:
            return ku()
        if self is MappingJobStateCode.KY:
            return ky()
        if self is MappingJobStateCode.LA:
            return la()
        if self is MappingJobStateCode.LN:
            return ln()
        if self is MappingJobStateCode.MA:
            return ma()
        if self is MappingJobStateCode.MB:
            return mb()
        if self is MappingJobStateCode.MD:
            return md()
        if self is MappingJobStateCode.ME:
            return me()
        if self is MappingJobStateCode.MG:
            return mg()
        if self is MappingJobStateCode.MI:
            return mi()
        if self is MappingJobStateCode.MN:
            return mn()
        if self is MappingJobStateCode.MO:
            return mo()
        if self is MappingJobStateCode.MS:
            return ms()
        if self is MappingJobStateCode.MT:
            return mt()
        if self is MappingJobStateCode.MZ:
            return mz()
        if self is MappingJobStateCode.NB:
            return nb()
        if self is MappingJobStateCode.NC:
            return nc()
        if self is MappingJobStateCode.ND:
            return nd()
        if self is MappingJobStateCode.NE:
            return ne()
        if self is MappingJobStateCode.NG:
            return ng()
        if self is MappingJobStateCode.NH:
            return nh()
        if self is MappingJobStateCode.NJ:
            return nj()
        if self is MappingJobStateCode.NL:
            return nl()
        if self is MappingJobStateCode.NM:
            return nm()
        if self is MappingJobStateCode.NN:
            return nn()
        if self is MappingJobStateCode.NR:
            return nr()
        if self is MappingJobStateCode.NS:
            return ns()
        if self is MappingJobStateCode.NT:
            return nt()
        if self is MappingJobStateCode.NU:
            return nu()
        if self is MappingJobStateCode.NV:
            return nv()
        if self is MappingJobStateCode.NW:
            return nw()
        if self is MappingJobStateCode.NX:
            return nx()
        if self is MappingJobStateCode.NY:
            return ny()
        if self is MappingJobStateCode.OH:
            return oh()
        if self is MappingJobStateCode.OK:
            return ok()
        if self is MappingJobStateCode.ON:
            return on()
        if self is MappingJobStateCode.OR:
            return or_()
        if self is MappingJobStateCode.OS:
            return os()
        if self is MappingJobStateCode.OT:
            return ot()
        if self is MappingJobStateCode.OY:
            return oy()
        if self is MappingJobStateCode.PA:
            return pa()
        if self is MappingJobStateCode.PE:
            return pe()
        if self is MappingJobStateCode.PR:
            return pr()
        if self is MappingJobStateCode.QC:
            return qc()
        if self is MappingJobStateCode.QH:
            return qh()
        if self is MappingJobStateCode.QL:
            return ql()
        if self is MappingJobStateCode.RI:
            return ri()
        if self is MappingJobStateCode.SA:
            return sa()
        if self is MappingJobStateCode.SC:
            return sc()
        if self is MappingJobStateCode.SD:
            return sd()
        if self is MappingJobStateCode.SH:
            return sh()
        if self is MappingJobStateCode.SI:
            return si()
        if self is MappingJobStateCode.SK:
            return sk()
        if self is MappingJobStateCode.SN:
            return sn()
        if self is MappingJobStateCode.ST:
            return st()
        if self is MappingJobStateCode.SX:
            return sx()
        if self is MappingJobStateCode.SZ:
            return sz()
        if self is MappingJobStateCode.TA:
            return ta()
        if self is MappingJobStateCode.TG:
            return tg()
        if self is MappingJobStateCode.TJ:
            return tj()
        if self is MappingJobStateCode.TK:
            return tk()
        if self is MappingJobStateCode.TN:
            return tn()
        if self is MappingJobStateCode.TS:
            return ts()
        if self is MappingJobStateCode.TT:
            return tt()
        if self is MappingJobStateCode.TX:
            return tx()
        if self is MappingJobStateCode.TY:
            return ty()
        if self is MappingJobStateCode.UT:
            return ut()
        if self is MappingJobStateCode.VA:
            return va()
        if self is MappingJobStateCode.VI:
            return vi()
        if self is MappingJobStateCode.VT:
            return vt()
        if self is MappingJobStateCode.WA:
            return wa()
        if self is MappingJobStateCode.WI:
            return wi()
        if self is MappingJobStateCode.WK:
            return wk()
        if self is MappingJobStateCode.WV:
            return wv()
        if self is MappingJobStateCode.WY:
            return wy()
        if self is MappingJobStateCode.XJ:
            return xj()
        if self is MappingJobStateCode.XZ:
            return xz()
        if self is MappingJobStateCode.YA:
            return ya()
        if self is MappingJobStateCode.YN:
            return yn()
        if self is MappingJobStateCode.YT:
            return yt()
        if self is MappingJobStateCode.YU:
            return yu()
        if self is MappingJobStateCode.ZJ:
            return zj()
