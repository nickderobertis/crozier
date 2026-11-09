

import typing

DocketEntryDocketBadge = typing.Union[
    typing.Literal[
        "DOCKET",
        "CHARGE",
        "HEARING",
        "JUDGEMENT",
        "FINANCIAL",
        "DISPOSITION",
        "SENTENCE",
        "BOND",
        "BAIL",
        "CAUSE_OF_ACTION",
        "ARREST",
        "WARRANT",
        "SUMMON",
        "TICKLER",
        "OPINION",
    ],
    typing.Any,
]
