

import typing

OauthScope = typing.Union[
    typing.Literal["openid", "offline_access", "expenses.card", "expenses.card.readonly"], typing.Any
]
