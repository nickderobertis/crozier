

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoginStepCookiesCookiesFieldsItemType(enum.StrEnum):
    """
    The type of data to extract.
    """

    COOKIE = "cookie"
    LOCAL_STORAGE = "local_storage"
    REQUEST_HEADER = "request_header"
    REQUEST_BODY = "request_body"
    SPECIAL = "special"

    def visit(
        self,
        cookie: typing.Callable[[], T_Result],
        local_storage: typing.Callable[[], T_Result],
        request_header: typing.Callable[[], T_Result],
        request_body: typing.Callable[[], T_Result],
        special: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoginStepCookiesCookiesFieldsItemType.COOKIE:
            return cookie()
        if self is LoginStepCookiesCookiesFieldsItemType.LOCAL_STORAGE:
            return local_storage()
        if self is LoginStepCookiesCookiesFieldsItemType.REQUEST_HEADER:
            return request_header()
        if self is LoginStepCookiesCookiesFieldsItemType.REQUEST_BODY:
            return request_body()
        if self is LoginStepCookiesCookiesFieldsItemType.SPECIAL:
            return special()
