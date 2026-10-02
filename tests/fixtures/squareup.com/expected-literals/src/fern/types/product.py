

import typing

Product = typing.Union[
    typing.Literal[
        "SQUARE_POS",
        "EXTERNAL_API",
        "BILLING",
        "APPOINTMENTS",
        "INVOICES",
        "ONLINE_STORE",
        "PAYROLL",
        "DASHBOARD",
        "ITEM_LIBRARY_IMPORT",
        "OTHER",
    ],
    typing.Any,
]
