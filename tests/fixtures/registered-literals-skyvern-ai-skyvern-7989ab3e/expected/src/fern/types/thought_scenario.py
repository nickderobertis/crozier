

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThoughtScenario(enum.StrEnum):
    """
    Scenario in which a thought was generated.

    Note: Stored as VARCHAR in the database (not a PostgreSQL ENUM), so new values
    can be added without database migrations. See observer_thoughts.observer_thought_scenario column.
    """

    GENERATE_PLAN = "generate_plan"
    USER_GOAL_CHECK = "user_goal_check"
    FAILURE_DESCRIBE = "failure_describe"
    SUMMARIZATION = "summarization"
    GENERATE_METADATA = "generate_metadata"
    EXTRACT_LOOP_VALUES = "extract_loop_values"
    GENERATE_TASK_IN_LOOP = "generate_task_in_loop"
    GENERATE_GENERAL_TASK = "generate_general_task"
    TERMINATION = "termination"

    def visit(
        self,
        generate_plan: typing.Callable[[], T_Result],
        user_goal_check: typing.Callable[[], T_Result],
        failure_describe: typing.Callable[[], T_Result],
        summarization: typing.Callable[[], T_Result],
        generate_metadata: typing.Callable[[], T_Result],
        extract_loop_values: typing.Callable[[], T_Result],
        generate_task_in_loop: typing.Callable[[], T_Result],
        generate_general_task: typing.Callable[[], T_Result],
        termination: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThoughtScenario.GENERATE_PLAN:
            return generate_plan()
        if self is ThoughtScenario.USER_GOAL_CHECK:
            return user_goal_check()
        if self is ThoughtScenario.FAILURE_DESCRIBE:
            return failure_describe()
        if self is ThoughtScenario.SUMMARIZATION:
            return summarization()
        if self is ThoughtScenario.GENERATE_METADATA:
            return generate_metadata()
        if self is ThoughtScenario.EXTRACT_LOOP_VALUES:
            return extract_loop_values()
        if self is ThoughtScenario.GENERATE_TASK_IN_LOOP:
            return generate_task_in_loop()
        if self is ThoughtScenario.GENERATE_GENERAL_TASK:
            return generate_general_task()
        if self is ThoughtScenario.TERMINATION:
            return termination()
