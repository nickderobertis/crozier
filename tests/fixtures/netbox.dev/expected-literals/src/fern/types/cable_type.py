

import typing

CableType = typing.Union[
    typing.Literal[
        "cat3",
        "cat5",
        "cat5e",
        "cat6",
        "cat6a",
        "cat7",
        "cat7a",
        "cat8",
        "dac-active",
        "dac-passive",
        "mrj21-trunk",
        "coaxial",
        "mmf",
        "mmf-om1",
        "mmf-om2",
        "mmf-om3",
        "mmf-om4",
        "mmf-om5",
        "smf",
        "smf-os1",
        "smf-os2",
        "aoc",
        "power",
    ],
    typing.Any,
]
