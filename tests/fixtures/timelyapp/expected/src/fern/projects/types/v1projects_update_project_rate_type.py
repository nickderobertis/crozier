

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectsUpdateProjectRateType(enum.StrEnum):
    """
    Rate type for the project (e.g., project, user)
    """

    PROJECT = "project"
    USER = "user"
    NON_BILLABLE = "non-billable"

    def visit(
        self,
        project: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        non_billable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ProjectsUpdateProjectRateType.PROJECT:
            return project()
        if self is V1ProjectsUpdateProjectRateType.USER:
            return user()
        if self is V1ProjectsUpdateProjectRateType.NON_BILLABLE:
            return non_billable()
