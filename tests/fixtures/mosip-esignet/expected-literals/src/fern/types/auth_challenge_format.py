

import typing

AuthChallengeFormat = typing.Union[
    typing.Literal["alpha-numeric", "jwt", "encoded-json", "number", "base64url-encoded-json"], typing.Any
]
