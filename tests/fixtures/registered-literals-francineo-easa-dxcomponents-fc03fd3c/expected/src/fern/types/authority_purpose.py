

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorityPurpose(enum.StrEnum):
    """
    Roles that an authority has in relation with the UAS zone, represented by
    a string with an enumerated list of values.
    """

    AUTHORIZATION = "AUTHORIZATION"
    NOTIFICATION = "NOTIFICATION"
    INFORMATION = "INFORMATION"

    def visit(
        self,
        authorization: typing.Callable[[], T_Result],
        notification: typing.Callable[[], T_Result],
        information: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorityPurpose.AUTHORIZATION:
            return authorization()
        if self is AuthorityPurpose.NOTIFICATION:
            return notification()
        if self is AuthorityPurpose.INFORMATION:
            return information()
