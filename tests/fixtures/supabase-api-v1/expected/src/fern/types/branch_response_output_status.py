

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BranchResponseOutputStatus(enum.StrEnum):
    """
    This field is deprecated. List action runs to get branch status instead.
    """

    CREATING_PROJECT = "CREATING_PROJECT"
    RUNNING_MIGRATIONS = "RUNNING_MIGRATIONS"
    MIGRATIONS_PASSED = "MIGRATIONS_PASSED"
    MIGRATIONS_FAILED = "MIGRATIONS_FAILED"
    FUNCTIONS_DEPLOYED = "FUNCTIONS_DEPLOYED"
    FUNCTIONS_FAILED = "FUNCTIONS_FAILED"

    def visit(
        self,
        creating_project: typing.Callable[[], T_Result],
        running_migrations: typing.Callable[[], T_Result],
        migrations_passed: typing.Callable[[], T_Result],
        migrations_failed: typing.Callable[[], T_Result],
        functions_deployed: typing.Callable[[], T_Result],
        functions_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BranchResponseOutputStatus.CREATING_PROJECT:
            return creating_project()
        if self is BranchResponseOutputStatus.RUNNING_MIGRATIONS:
            return running_migrations()
        if self is BranchResponseOutputStatus.MIGRATIONS_PASSED:
            return migrations_passed()
        if self is BranchResponseOutputStatus.MIGRATIONS_FAILED:
            return migrations_failed()
        if self is BranchResponseOutputStatus.FUNCTIONS_DEPLOYED:
            return functions_deployed()
        if self is BranchResponseOutputStatus.FUNCTIONS_FAILED:
            return functions_failed()
