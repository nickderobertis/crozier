

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorsType(enum.StrEnum):
    """
    Key indicating type of error
    """

    INVALID_BEARER_TOKEN = "INVALID_BEARER_TOKEN"
    INVALID_USER_AGENT = "INVALID_USER_AGENT"
    NOT_ENOUGH_UNPAID_PAYOUTS = "NOT_ENOUGH_UNPAID_PAYOUTS"
    DUPLICATE_HEADERS = "DUPLICATE_HEADERS"

    def visit(
        self,
        invalid_bearer_token: typing.Callable[[], T_Result],
        invalid_user_agent: typing.Callable[[], T_Result],
        not_enough_unpaid_payouts: typing.Callable[[], T_Result],
        duplicate_headers: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BadRequestErrorsType.INVALID_BEARER_TOKEN:
            return invalid_bearer_token()
        if self is BadRequestErrorsType.INVALID_USER_AGENT:
            return invalid_user_agent()
        if self is BadRequestErrorsType.NOT_ENOUGH_UNPAID_PAYOUTS:
            return not_enough_unpaid_payouts()
        if self is BadRequestErrorsType.DUPLICATE_HEADERS:
            return duplicate_headers()
