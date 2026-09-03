

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthChallengeFormat(enum.StrEnum):
    """
    Format of the challenge provided.
    """

    ALPHA_NUMERIC = "alpha-numeric"
    JWT = "jwt"
    ENCODED_JSON = "encoded-json"
    NUMBER = "number"
    BASE64URL_ENCODED_JSON = "base64url-encoded-json"

    def visit(
        self,
        alpha_numeric: typing.Callable[[], T_Result],
        jwt: typing.Callable[[], T_Result],
        encoded_json: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        base64url_encoded_json: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthChallengeFormat.ALPHA_NUMERIC:
            return alpha_numeric()
        if self is AuthChallengeFormat.JWT:
            return jwt()
        if self is AuthChallengeFormat.ENCODED_JSON:
            return encoded_json()
        if self is AuthChallengeFormat.NUMBER:
            return number()
        if self is AuthChallengeFormat.BASE64URL_ENCODED_JSON:
            return base64url_encoded_json()
