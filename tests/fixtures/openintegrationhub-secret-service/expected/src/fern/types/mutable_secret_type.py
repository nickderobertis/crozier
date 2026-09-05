

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MutableSecretType(enum.StrEnum):
    API_KEY = "API_KEY"
    OA1TWO_LEGGED = "OA1_TWO_LEGGED"
    OA1THREE_LEGGED = "OA1_THREE_LEGGED"
    OA2AUTHORIZATION_CODE = "OA2_AUTHORIZATION_CODE"
    SIMPLE = "SIMPLE"
    MIXED = "MIXED"
    SESSION_AUTH = "SESSION_AUTH"

    def visit(
        self,
        api_key: typing.Callable[[], T_Result],
        oa1two_legged: typing.Callable[[], T_Result],
        oa1three_legged: typing.Callable[[], T_Result],
        oa2authorization_code: typing.Callable[[], T_Result],
        simple: typing.Callable[[], T_Result],
        mixed: typing.Callable[[], T_Result],
        session_auth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MutableSecretType.API_KEY:
            return api_key()
        if self is MutableSecretType.OA1TWO_LEGGED:
            return oa1two_legged()
        if self is MutableSecretType.OA1THREE_LEGGED:
            return oa1three_legged()
        if self is MutableSecretType.OA2AUTHORIZATION_CODE:
            return oa2authorization_code()
        if self is MutableSecretType.SIMPLE:
            return simple()
        if self is MutableSecretType.MIXED:
            return mixed()
        if self is MutableSecretType.SESSION_AUTH:
            return session_auth()
