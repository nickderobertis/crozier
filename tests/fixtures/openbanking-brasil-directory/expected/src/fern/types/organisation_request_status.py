

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganisationRequestStatus(enum.StrEnum):
    """
    Status of the directory registration of an organisation
    """

    ACTIVE = "Active"
    PENDING = "Pending"
    WITHDRAWN = "Withdrawn"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        withdrawn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrganisationRequestStatus.ACTIVE:
            return active()
        if self is OrganisationRequestStatus.PENDING:
            return pending()
        if self is OrganisationRequestStatus.WITHDRAWN:
            return withdrawn()
