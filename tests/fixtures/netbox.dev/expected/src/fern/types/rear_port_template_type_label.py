

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RearPortTemplateTypeLabel(str, enum.Enum):
    EIGHT_P8C = "8P8C"
    EIGHT_P6C = "8P6C"
    EIGHT_P4C = "8P4C"
    EIGHT_P2C = "8P2C"
    SIX_P6C = "6P6C"
    SIX_P4C = "6P4C"
    SIX_P2C = "6P2C"
    FOUR_P4C = "4P4C"
    FOUR_P2C = "4P2C"
    GG45 = "GG45"
    TERA4P = "TERA 4P"
    TERA2P = "TERA 2P"
    TERA1P = "TERA 1P"
    ONE_HUNDRED_TEN_PUNCH = "110 Punch"
    BNC = "BNC"
    F_CONNECTOR = "F Connector"
    N_CONNECTOR = "N Connector"
    MRJ21 = "MRJ21"
    FC = "FC"
    LC = "LC"
    LC_PC = "LC/PC"
    LC_UPC = "LC/UPC"
    LC_APC = "LC/APC"
    LSH = "LSH"
    LSH_PC = "LSH/PC"
    LSH_UPC = "LSH/UPC"
    LSH_APC = "LSH/APC"
    MPO = "MPO"
    MTRJ = "MTRJ"
    SC = "SC"
    SC_PC = "SC/PC"
    SC_UPC = "SC/UPC"
    SC_APC = "SC/APC"
    ST = "ST"
    CS = "CS"
    SN = "SN"
    SMA905 = "SMA 905"
    SMA906 = "SMA 906"
    URM_P2 = "URM-P2"
    URM_P4 = "URM-P4"
    URM_P8 = "URM-P8"
    SPLICE = "Splice"
    OTHER = "Other"

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
        f_connector: typing.Callable[[], T_Result],
        n_connector: typing.Callable[[], T_Result],
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
        if self is RearPortTemplateTypeLabel.EIGHT_P8C:
            return eight_p8c()
        if self is RearPortTemplateTypeLabel.EIGHT_P6C:
            return eight_p6c()
        if self is RearPortTemplateTypeLabel.EIGHT_P4C:
            return eight_p4c()
        if self is RearPortTemplateTypeLabel.EIGHT_P2C:
            return eight_p2c()
        if self is RearPortTemplateTypeLabel.SIX_P6C:
            return six_p6c()
        if self is RearPortTemplateTypeLabel.SIX_P4C:
            return six_p4c()
        if self is RearPortTemplateTypeLabel.SIX_P2C:
            return six_p2c()
        if self is RearPortTemplateTypeLabel.FOUR_P4C:
            return four_p4c()
        if self is RearPortTemplateTypeLabel.FOUR_P2C:
            return four_p2c()
        if self is RearPortTemplateTypeLabel.GG45:
            return gg45()
        if self is RearPortTemplateTypeLabel.TERA4P:
            return tera4p()
        if self is RearPortTemplateTypeLabel.TERA2P:
            return tera2p()
        if self is RearPortTemplateTypeLabel.TERA1P:
            return tera1p()
        if self is RearPortTemplateTypeLabel.ONE_HUNDRED_TEN_PUNCH:
            return one_hundred_ten_punch()
        if self is RearPortTemplateTypeLabel.BNC:
            return bnc()
        if self is RearPortTemplateTypeLabel.F_CONNECTOR:
            return f_connector()
        if self is RearPortTemplateTypeLabel.N_CONNECTOR:
            return n_connector()
        if self is RearPortTemplateTypeLabel.MRJ21:
            return mrj21()
        if self is RearPortTemplateTypeLabel.FC:
            return fc()
        if self is RearPortTemplateTypeLabel.LC:
            return lc()
        if self is RearPortTemplateTypeLabel.LC_PC:
            return lc_pc()
        if self is RearPortTemplateTypeLabel.LC_UPC:
            return lc_upc()
        if self is RearPortTemplateTypeLabel.LC_APC:
            return lc_apc()
        if self is RearPortTemplateTypeLabel.LSH:
            return lsh()
        if self is RearPortTemplateTypeLabel.LSH_PC:
            return lsh_pc()
        if self is RearPortTemplateTypeLabel.LSH_UPC:
            return lsh_upc()
        if self is RearPortTemplateTypeLabel.LSH_APC:
            return lsh_apc()
        if self is RearPortTemplateTypeLabel.MPO:
            return mpo()
        if self is RearPortTemplateTypeLabel.MTRJ:
            return mtrj()
        if self is RearPortTemplateTypeLabel.SC:
            return sc()
        if self is RearPortTemplateTypeLabel.SC_PC:
            return sc_pc()
        if self is RearPortTemplateTypeLabel.SC_UPC:
            return sc_upc()
        if self is RearPortTemplateTypeLabel.SC_APC:
            return sc_apc()
        if self is RearPortTemplateTypeLabel.ST:
            return st()
        if self is RearPortTemplateTypeLabel.CS:
            return cs()
        if self is RearPortTemplateTypeLabel.SN:
            return sn()
        if self is RearPortTemplateTypeLabel.SMA905:
            return sma905()
        if self is RearPortTemplateTypeLabel.SMA906:
            return sma906()
        if self is RearPortTemplateTypeLabel.URM_P2:
            return urm_p2()
        if self is RearPortTemplateTypeLabel.URM_P4:
            return urm_p4()
        if self is RearPortTemplateTypeLabel.URM_P8:
            return urm_p8()
        if self is RearPortTemplateTypeLabel.SPLICE:
            return splice()
        if self is RearPortTemplateTypeLabel.OTHER:
            return other()
