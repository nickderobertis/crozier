

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IndividualWatchlistCode(enum.StrEnum):
    """
    Shorthand identifier for a specific screening list for individuals.
    """

    AU_CON = "AU_CON"
    CA_CON = "CA_CON"
    EU_CON = "EU_CON"
    IZ_CIA = "IZ_CIA"
    IZ_IPL = "IZ_IPL"
    IZ_PEP = "IZ_PEP"
    IZ_UNC = "IZ_UNC"
    IZ_WBK = "IZ_WBK"
    UK_HMC = "UK_HMC"
    US_DPL = "US_DPL"
    US_DTC = "US_DTC"
    US_FBI = "US_FBI"
    US_FSE = "US_FSE"
    US_ISN = "US_ISN"
    US_MBS = "US_MBS"
    US_PLC = "US_PLC"
    US_SDN = "US_SDN"
    US_SSI = "US_SSI"
    SG_SOF = "SG_SOF"
    TR_TWL = "TR_TWL"
    TR_DFD = "TR_DFD"
    TR_FOR = "TR_FOR"
    TR_WMD = "TR_WMD"
    TR_CMB = "TR_CMB"

    def visit(
        self,
        au_con: typing.Callable[[], T_Result],
        ca_con: typing.Callable[[], T_Result],
        eu_con: typing.Callable[[], T_Result],
        iz_cia: typing.Callable[[], T_Result],
        iz_ipl: typing.Callable[[], T_Result],
        iz_pep: typing.Callable[[], T_Result],
        iz_unc: typing.Callable[[], T_Result],
        iz_wbk: typing.Callable[[], T_Result],
        uk_hmc: typing.Callable[[], T_Result],
        us_dpl: typing.Callable[[], T_Result],
        us_dtc: typing.Callable[[], T_Result],
        us_fbi: typing.Callable[[], T_Result],
        us_fse: typing.Callable[[], T_Result],
        us_isn: typing.Callable[[], T_Result],
        us_mbs: typing.Callable[[], T_Result],
        us_plc: typing.Callable[[], T_Result],
        us_sdn: typing.Callable[[], T_Result],
        us_ssi: typing.Callable[[], T_Result],
        sg_sof: typing.Callable[[], T_Result],
        tr_twl: typing.Callable[[], T_Result],
        tr_dfd: typing.Callable[[], T_Result],
        tr_for: typing.Callable[[], T_Result],
        tr_wmd: typing.Callable[[], T_Result],
        tr_cmb: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IndividualWatchlistCode.AU_CON:
            return au_con()
        if self is IndividualWatchlistCode.CA_CON:
            return ca_con()
        if self is IndividualWatchlistCode.EU_CON:
            return eu_con()
        if self is IndividualWatchlistCode.IZ_CIA:
            return iz_cia()
        if self is IndividualWatchlistCode.IZ_IPL:
            return iz_ipl()
        if self is IndividualWatchlistCode.IZ_PEP:
            return iz_pep()
        if self is IndividualWatchlistCode.IZ_UNC:
            return iz_unc()
        if self is IndividualWatchlistCode.IZ_WBK:
            return iz_wbk()
        if self is IndividualWatchlistCode.UK_HMC:
            return uk_hmc()
        if self is IndividualWatchlistCode.US_DPL:
            return us_dpl()
        if self is IndividualWatchlistCode.US_DTC:
            return us_dtc()
        if self is IndividualWatchlistCode.US_FBI:
            return us_fbi()
        if self is IndividualWatchlistCode.US_FSE:
            return us_fse()
        if self is IndividualWatchlistCode.US_ISN:
            return us_isn()
        if self is IndividualWatchlistCode.US_MBS:
            return us_mbs()
        if self is IndividualWatchlistCode.US_PLC:
            return us_plc()
        if self is IndividualWatchlistCode.US_SDN:
            return us_sdn()
        if self is IndividualWatchlistCode.US_SSI:
            return us_ssi()
        if self is IndividualWatchlistCode.SG_SOF:
            return sg_sof()
        if self is IndividualWatchlistCode.TR_TWL:
            return tr_twl()
        if self is IndividualWatchlistCode.TR_DFD:
            return tr_dfd()
        if self is IndividualWatchlistCode.TR_FOR:
            return tr_for()
        if self is IndividualWatchlistCode.TR_WMD:
            return tr_wmd()
        if self is IndividualWatchlistCode.TR_CMB:
            return tr_cmb()
