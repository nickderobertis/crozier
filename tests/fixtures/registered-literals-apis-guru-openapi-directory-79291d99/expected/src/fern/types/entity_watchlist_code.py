

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityWatchlistCode(enum.StrEnum):
    """
    Shorthand identifier for a specific screening list for entities.
    """

    CA_CON = "CA_CON"
    EU_CON = "EU_CON"
    IZ_SOE = "IZ_SOE"
    IZ_UNC = "IZ_UNC"
    IZ_WBK = "IZ_WBK"
    US_CAP = "US_CAP"
    US_FSE = "US_FSE"
    US_MBS = "US_MBS"
    US_SDN = "US_SDN"
    US_SSI = "US_SSI"
    US_CMC = "US_CMC"
    US_UVL = "US_UVL"
    AU_CON = "AU_CON"
    UK_HMC = "UK_HMC"

    def visit(
        self,
        ca_con: typing.Callable[[], T_Result],
        eu_con: typing.Callable[[], T_Result],
        iz_soe: typing.Callable[[], T_Result],
        iz_unc: typing.Callable[[], T_Result],
        iz_wbk: typing.Callable[[], T_Result],
        us_cap: typing.Callable[[], T_Result],
        us_fse: typing.Callable[[], T_Result],
        us_mbs: typing.Callable[[], T_Result],
        us_sdn: typing.Callable[[], T_Result],
        us_ssi: typing.Callable[[], T_Result],
        us_cmc: typing.Callable[[], T_Result],
        us_uvl: typing.Callable[[], T_Result],
        au_con: typing.Callable[[], T_Result],
        uk_hmc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityWatchlistCode.CA_CON:
            return ca_con()
        if self is EntityWatchlistCode.EU_CON:
            return eu_con()
        if self is EntityWatchlistCode.IZ_SOE:
            return iz_soe()
        if self is EntityWatchlistCode.IZ_UNC:
            return iz_unc()
        if self is EntityWatchlistCode.IZ_WBK:
            return iz_wbk()
        if self is EntityWatchlistCode.US_CAP:
            return us_cap()
        if self is EntityWatchlistCode.US_FSE:
            return us_fse()
        if self is EntityWatchlistCode.US_MBS:
            return us_mbs()
        if self is EntityWatchlistCode.US_SDN:
            return us_sdn()
        if self is EntityWatchlistCode.US_SSI:
            return us_ssi()
        if self is EntityWatchlistCode.US_CMC:
            return us_cmc()
        if self is EntityWatchlistCode.US_UVL:
            return us_uvl()
        if self is EntityWatchlistCode.AU_CON:
            return au_con()
        if self is EntityWatchlistCode.UK_HMC:
            return uk_hmc()
