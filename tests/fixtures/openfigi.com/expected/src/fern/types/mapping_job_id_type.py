

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MappingJobIdType(str, enum.Enum):
    ID_ISIN = "ID_ISIN"
    ID_BB_UNIQUE = "ID_BB_UNIQUE"
    ID_SEDOL = "ID_SEDOL"
    ID_COMMON = "ID_COMMON"
    ID_WERTPAPIER = "ID_WERTPAPIER"
    ID_CUSIP = "ID_CUSIP"
    ID_BB = "ID_BB"
    ID_ITALY = "ID_ITALY"
    ID_EXCH_SYMBOL = "ID_EXCH_SYMBOL"
    ID_FULL_EXCHANGE_SYMBOL = "ID_FULL_EXCHANGE_SYMBOL"
    COMPOSITE_ID_BB_GLOBAL = "COMPOSITE_ID_BB_GLOBAL"
    ID_BB_GLOBAL_SHARE_CLASS_LEVEL = "ID_BB_GLOBAL_SHARE_CLASS_LEVEL"
    ID_BB_SEC_NUM_DES = "ID_BB_SEC_NUM_DES"
    ID_BB_GLOBAL = "ID_BB_GLOBAL"
    TICKER = "TICKER"
    ID_CUSIP8CHR = "ID_CUSIP_8_CHR"
    OCC_SYMBOL = "OCC_SYMBOL"
    UNIQUE_ID_FUT_OPT = "UNIQUE_ID_FUT_OPT"
    OPRA_SYMBOL = "OPRA_SYMBOL"
    TRADING_SYSTEM_IDENTIFIER = "TRADING_SYSTEM_IDENTIFIER"
    ID_CINS = "ID_CINS"
    ID_SHORT_CODE = "ID_SHORT_CODE"
    BASE_TICKER = "BASE_TICKER"
    VENDOR_INDEX_CODE = "VENDOR_INDEX_CODE"

    def visit(
        self,
        id_isin: typing.Callable[[], T_Result],
        id_bb_unique: typing.Callable[[], T_Result],
        id_sedol: typing.Callable[[], T_Result],
        id_common: typing.Callable[[], T_Result],
        id_wertpapier: typing.Callable[[], T_Result],
        id_cusip: typing.Callable[[], T_Result],
        id_bb: typing.Callable[[], T_Result],
        id_italy: typing.Callable[[], T_Result],
        id_exch_symbol: typing.Callable[[], T_Result],
        id_full_exchange_symbol: typing.Callable[[], T_Result],
        composite_id_bb_global: typing.Callable[[], T_Result],
        id_bb_global_share_class_level: typing.Callable[[], T_Result],
        id_bb_sec_num_des: typing.Callable[[], T_Result],
        id_bb_global: typing.Callable[[], T_Result],
        ticker: typing.Callable[[], T_Result],
        id_cusip8chr: typing.Callable[[], T_Result],
        occ_symbol: typing.Callable[[], T_Result],
        unique_id_fut_opt: typing.Callable[[], T_Result],
        opra_symbol: typing.Callable[[], T_Result],
        trading_system_identifier: typing.Callable[[], T_Result],
        id_cins: typing.Callable[[], T_Result],
        id_short_code: typing.Callable[[], T_Result],
        base_ticker: typing.Callable[[], T_Result],
        vendor_index_code: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MappingJobIdType.ID_ISIN:
            return id_isin()
        if self is MappingJobIdType.ID_BB_UNIQUE:
            return id_bb_unique()
        if self is MappingJobIdType.ID_SEDOL:
            return id_sedol()
        if self is MappingJobIdType.ID_COMMON:
            return id_common()
        if self is MappingJobIdType.ID_WERTPAPIER:
            return id_wertpapier()
        if self is MappingJobIdType.ID_CUSIP:
            return id_cusip()
        if self is MappingJobIdType.ID_BB:
            return id_bb()
        if self is MappingJobIdType.ID_ITALY:
            return id_italy()
        if self is MappingJobIdType.ID_EXCH_SYMBOL:
            return id_exch_symbol()
        if self is MappingJobIdType.ID_FULL_EXCHANGE_SYMBOL:
            return id_full_exchange_symbol()
        if self is MappingJobIdType.COMPOSITE_ID_BB_GLOBAL:
            return composite_id_bb_global()
        if self is MappingJobIdType.ID_BB_GLOBAL_SHARE_CLASS_LEVEL:
            return id_bb_global_share_class_level()
        if self is MappingJobIdType.ID_BB_SEC_NUM_DES:
            return id_bb_sec_num_des()
        if self is MappingJobIdType.ID_BB_GLOBAL:
            return id_bb_global()
        if self is MappingJobIdType.TICKER:
            return ticker()
        if self is MappingJobIdType.ID_CUSIP8CHR:
            return id_cusip8chr()
        if self is MappingJobIdType.OCC_SYMBOL:
            return occ_symbol()
        if self is MappingJobIdType.UNIQUE_ID_FUT_OPT:
            return unique_id_fut_opt()
        if self is MappingJobIdType.OPRA_SYMBOL:
            return opra_symbol()
        if self is MappingJobIdType.TRADING_SYSTEM_IDENTIFIER:
            return trading_system_identifier()
        if self is MappingJobIdType.ID_CINS:
            return id_cins()
        if self is MappingJobIdType.ID_SHORT_CODE:
            return id_short_code()
        if self is MappingJobIdType.BASE_TICKER:
            return base_ticker()
        if self is MappingJobIdType.VENDOR_INDEX_CODE:
            return vendor_index_code()
