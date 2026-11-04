

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThoughtType(enum.StrEnum):
    """
    Type of thought recorded during task execution.

    Note: Stored as VARCHAR in the database (not a PostgreSQL ENUM), so new values
    can be added without database migrations. See observer_thoughts.observer_thought_type column.
    """

    PLAN = "plan"
    METADATA = "metadata"
    USER_GOAL_CHECK = "user_goal_check"
    INTERNAL_PLAN = "internal_plan"
    FAILURE_DESCRIBE = "failure_describe"
    TERMINATION = "termination"

    def visit(
        self,
        plan: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
        user_goal_check: typing.Callable[[], T_Result],
        internal_plan: typing.Callable[[], T_Result],
        failure_describe: typing.Callable[[], T_Result],
        termination: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThoughtType.PLAN:
            return plan()
        if self is ThoughtType.METADATA:
            return metadata()
        if self is ThoughtType.USER_GOAL_CHECK:
            return user_goal_check()
        if self is ThoughtType.INTERNAL_PLAN:
            return internal_plan()
        if self is ThoughtType.FAILURE_DESCRIBE:
            return failure_describe()
        if self is ThoughtType.TERMINATION:
            return termination()
