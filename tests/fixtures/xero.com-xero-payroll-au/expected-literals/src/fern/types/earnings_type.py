

import typing

EarningsType = typing.Union[
    typing.Literal[
        "FIXED",
        "ORDINARYTIMEEARNINGS",
        "OVERTIMEEARNINGS",
        "ALLOWANCE",
        "LUMPSUMD",
        "EMPLOYMENTTERMINATIONPAYMENT",
        "LUMPSUMA",
        "LUMPSUMB",
        "BONUSESANDCOMMISSIONS",
        "LUMPSUME",
    ],
    typing.Any,
]
