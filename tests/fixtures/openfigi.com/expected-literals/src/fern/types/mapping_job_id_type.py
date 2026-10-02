

import typing

MappingJobIdType = typing.Union[
    typing.Literal[
        "ID_ISIN",
        "ID_BB_UNIQUE",
        "ID_SEDOL",
        "ID_COMMON",
        "ID_WERTPAPIER",
        "ID_CUSIP",
        "ID_BB",
        "ID_ITALY",
        "ID_EXCH_SYMBOL",
        "ID_FULL_EXCHANGE_SYMBOL",
        "COMPOSITE_ID_BB_GLOBAL",
        "ID_BB_GLOBAL_SHARE_CLASS_LEVEL",
        "ID_BB_SEC_NUM_DES",
        "ID_BB_GLOBAL",
        "TICKER",
        "ID_CUSIP_8_CHR",
        "OCC_SYMBOL",
        "UNIQUE_ID_FUT_OPT",
        "OPRA_SYMBOL",
        "TRADING_SYSTEM_IDENTIFIER",
        "ID_CINS",
        "ID_SHORT_CODE",
        "BASE_TICKER",
        "VENDOR_INDEX_CODE",
    ],
    typing.Any,
]
