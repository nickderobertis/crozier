

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpirationDate(enum.StrEnum):
    """
    A description of whether the associated document was expired when the verification was performed.

    Note: In the case where an expiration date is not present on the document or failed to be extracted, this value will be `no_data`.
    """

    NOT_EXPIRED = "not_expired"
    EXPIRED = "expired"
    NO_DATA = "no_data"

    def visit(
        self,
        not_expired: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        no_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpirationDate.NOT_EXPIRED:
            return not_expired()
        if self is ExpirationDate.EXPIRED:
            return expired()
        if self is ExpirationDate.NO_DATA:
            return no_data()
