

import typing

LogUnifiedApi = typing.Union[
    typing.Literal[
        "crm",
        "lead",
        "proxy",
        "vault",
        "accounting",
        "hris",
        "ats",
        "ecommerce",
        "issue-tracking",
        "pos",
        "file-storage",
        "sms",
    ],
    typing.Any,
]
