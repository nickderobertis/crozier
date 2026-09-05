

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MutableOa1ThreeLeggedClientType(enum.StrEnum):
    OA1TWO_LEGGED = "OA1_TWO_LEGGED"
    OA1THREE_LEGGED = "OA1_THREE_LEGGED"
    OA2AUTHORIZATION_CODE = "OA2_AUTHORIZATION_CODE"
    SESSION_AUTH = "SESSION_AUTH"

    def visit(
        self,
        oa1two_legged: typing.Callable[[], T_Result],
        oa1three_legged: typing.Callable[[], T_Result],
        oa2authorization_code: typing.Callable[[], T_Result],
        session_auth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MutableOa1ThreeLeggedClientType.OA1TWO_LEGGED:
            return oa1two_legged()
        if self is MutableOa1ThreeLeggedClientType.OA1THREE_LEGGED:
            return oa1three_legged()
        if self is MutableOa1ThreeLeggedClientType.OA2AUTHORIZATION_CODE:
            return oa2authorization_code()
        if self is MutableOa1ThreeLeggedClientType.SESSION_AUTH:
            return session_auth()
