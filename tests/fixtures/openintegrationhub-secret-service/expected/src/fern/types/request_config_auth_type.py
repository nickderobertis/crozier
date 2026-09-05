

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequestConfigAuthType(enum.StrEnum):
    HEADER_AUTH = "HEADER_AUTH"
    BODY_AUTH = "BODY_AUTH"
    PARAMS_AUTH = "PARAMS_AUTH"
    FORM_AUTH = "FORM_AUTH"

    def visit(
        self,
        header_auth: typing.Callable[[], T_Result],
        body_auth: typing.Callable[[], T_Result],
        params_auth: typing.Callable[[], T_Result],
        form_auth: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RequestConfigAuthType.HEADER_AUTH:
            return header_auth()
        if self is RequestConfigAuthType.BODY_AUTH:
            return body_auth()
        if self is RequestConfigAuthType.PARAMS_AUTH:
            return params_auth()
        if self is RequestConfigAuthType.FORM_AUTH:
            return form_auth()
