

import typing

SurvivalPensionType = typing.Union[
    typing.Literal[
        "PGBL",
        "PRGP",
        "PAGP",
        "PRSA",
        "PRI",
        "PDR",
        "VGBL",
        "VRGP",
        "VAGP",
        "VRSA",
        "VRI",
        "VDR",
        "DEMAIS_PRODUTOS_PREVIDENCIA",
    ],
    typing.Any,
]
