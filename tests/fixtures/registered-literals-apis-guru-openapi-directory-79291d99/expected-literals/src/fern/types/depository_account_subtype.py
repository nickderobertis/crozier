

import typing

DepositoryAccountSubtype = typing.Union[
    typing.Literal[
        "checking", "savings", "hsa", "cd", "money market", "paypal", "prepaid", "cash management", "ebt", "all"
    ],
    typing.Any,
]
