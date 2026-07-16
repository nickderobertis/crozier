

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FrontPortTemplateTypeValue(str, enum.Enum):
    EIGHT_P8C = "8p8c"
    EIGHT_P6C = "8p6c"
    EIGHT_P4C = "8p4c"
    EIGHT_P2C = "8p2c"
    SIX_P6C = "6p6c"
    SIX_P4C = "6p4c"
    SIX_P2C = "6p2c"
    FOUR_P4C = "4p4c"
    FOUR_P2C = "4p2c"
    GG45 = "gg45"
    TERA4P = "tera-4p"
    TERA2P = "tera-2p"
    TERA1P = "tera-1p"
    ONE_HUNDRED_TEN_PUNCH = "110-punch"
    BNC = "bnc"
    F = "f"
    N = "n"
    MRJ21 = "mrj21"
    FC = "fc"
    LC = "lc"
    LC_PC = "lc-pc"
    LC_UPC = "lc-upc"
    LC_APC = "lc-apc"
    LSH = "lsh"
    LSH_PC = "lsh-pc"
    LSH_UPC = "lsh-upc"
    LSH_APC = "lsh-apc"
    MPO = "mpo"
    MTRJ = "mtrj"
    SC = "sc"
    SC_PC = "sc-pc"
    SC_UPC = "sc-upc"
    SC_APC = "sc-apc"
    ST = "st"
    CS = "cs"
    SN = "sn"
    SMA905 = "sma-905"
    SMA906 = "sma-906"
    URM_P2 = "urm-p2"
    URM_P4 = "urm-p4"
    URM_P8 = "urm-p8"
    SPLICE = "splice"
    OTHER = "other"

    def visit(
        self,
        eight_p8c: typing.Callable[[], T_Result],
        eight_p6c: typing.Callable[[], T_Result],
        eight_p4c: typing.Callable[[], T_Result],
        eight_p2c: typing.Callable[[], T_Result],
        six_p6c: typing.Callable[[], T_Result],
        six_p4c: typing.Callable[[], T_Result],
        six_p2c: typing.Callable[[], T_Result],
        four_p4c: typing.Callable[[], T_Result],
        four_p2c: typing.Callable[[], T_Result],
        gg45: typing.Callable[[], T_Result],
        tera4p: typing.Callable[[], T_Result],
        tera2p: typing.Callable[[], T_Result],
        tera1p: typing.Callable[[], T_Result],
        one_hundred_ten_punch: typing.Callable[[], T_Result],
        bnc: typing.Callable[[], T_Result],
        f: typing.Callable[[], T_Result],
        n: typing.Callable[[], T_Result],
        mrj21: typing.Callable[[], T_Result],
        fc: typing.Callable[[], T_Result],
        lc: typing.Callable[[], T_Result],
        lc_pc: typing.Callable[[], T_Result],
        lc_upc: typing.Callable[[], T_Result],
        lc_apc: typing.Callable[[], T_Result],
        lsh: typing.Callable[[], T_Result],
        lsh_pc: typing.Callable[[], T_Result],
        lsh_upc: typing.Callable[[], T_Result],
        lsh_apc: typing.Callable[[], T_Result],
        mpo: typing.Callable[[], T_Result],
        mtrj: typing.Callable[[], T_Result],
        sc: typing.Callable[[], T_Result],
        sc_pc: typing.Callable[[], T_Result],
        sc_upc: typing.Callable[[], T_Result],
        sc_apc: typing.Callable[[], T_Result],
        st: typing.Callable[[], T_Result],
        cs: typing.Callable[[], T_Result],
        sn: typing.Callable[[], T_Result],
        sma905: typing.Callable[[], T_Result],
        sma906: typing.Callable[[], T_Result],
        urm_p2: typing.Callable[[], T_Result],
        urm_p4: typing.Callable[[], T_Result],
        urm_p8: typing.Callable[[], T_Result],
        splice: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FrontPortTemplateTypeValue.EIGHT_P8C:
            return eight_p8c()
        if self is FrontPortTemplateTypeValue.EIGHT_P6C:
            return eight_p6c()
        if self is FrontPortTemplateTypeValue.EIGHT_P4C:
            return eight_p4c()
        if self is FrontPortTemplateTypeValue.EIGHT_P2C:
            return eight_p2c()
        if self is FrontPortTemplateTypeValue.SIX_P6C:
            return six_p6c()
        if self is FrontPortTemplateTypeValue.SIX_P4C:
            return six_p4c()
        if self is FrontPortTemplateTypeValue.SIX_P2C:
            return six_p2c()
        if self is FrontPortTemplateTypeValue.FOUR_P4C:
            return four_p4c()
        if self is FrontPortTemplateTypeValue.FOUR_P2C:
            return four_p2c()
        if self is FrontPortTemplateTypeValue.GG45:
            return gg45()
        if self is FrontPortTemplateTypeValue.TERA4P:
            return tera4p()
        if self is FrontPortTemplateTypeValue.TERA2P:
            return tera2p()
        if self is FrontPortTemplateTypeValue.TERA1P:
            return tera1p()
        if self is FrontPortTemplateTypeValue.ONE_HUNDRED_TEN_PUNCH:
            return one_hundred_ten_punch()
        if self is FrontPortTemplateTypeValue.BNC:
            return bnc()
        if self is FrontPortTemplateTypeValue.F:
            return f()
        if self is FrontPortTemplateTypeValue.N:
            return n()
        if self is FrontPortTemplateTypeValue.MRJ21:
            return mrj21()
        if self is FrontPortTemplateTypeValue.FC:
            return fc()
        if self is FrontPortTemplateTypeValue.LC:
            return lc()
        if self is FrontPortTemplateTypeValue.LC_PC:
            return lc_pc()
        if self is FrontPortTemplateTypeValue.LC_UPC:
            return lc_upc()
        if self is FrontPortTemplateTypeValue.LC_APC:
            return lc_apc()
        if self is FrontPortTemplateTypeValue.LSH:
            return lsh()
        if self is FrontPortTemplateTypeValue.LSH_PC:
            return lsh_pc()
        if self is FrontPortTemplateTypeValue.LSH_UPC:
            return lsh_upc()
        if self is FrontPortTemplateTypeValue.LSH_APC:
            return lsh_apc()
        if self is FrontPortTemplateTypeValue.MPO:
            return mpo()
        if self is FrontPortTemplateTypeValue.MTRJ:
            return mtrj()
        if self is FrontPortTemplateTypeValue.SC:
            return sc()
        if self is FrontPortTemplateTypeValue.SC_PC:
            return sc_pc()
        if self is FrontPortTemplateTypeValue.SC_UPC:
            return sc_upc()
        if self is FrontPortTemplateTypeValue.SC_APC:
            return sc_apc()
        if self is FrontPortTemplateTypeValue.ST:
            return st()
        if self is FrontPortTemplateTypeValue.CS:
            return cs()
        if self is FrontPortTemplateTypeValue.SN:
            return sn()
        if self is FrontPortTemplateTypeValue.SMA905:
            return sma905()
        if self is FrontPortTemplateTypeValue.SMA906:
            return sma906()
        if self is FrontPortTemplateTypeValue.URM_P2:
            return urm_p2()
        if self is FrontPortTemplateTypeValue.URM_P4:
            return urm_p4()
        if self is FrontPortTemplateTypeValue.URM_P8:
            return urm_p8()
        if self is FrontPortTemplateTypeValue.SPLICE:
            return splice()
        if self is FrontPortTemplateTypeValue.OTHER:
            return other()
