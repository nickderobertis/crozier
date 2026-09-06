

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListActivityLogsResponseItemsItemActorType(enum.StrEnum):
    """
    The type of actor responsible for the event. `user` for a human who directly triggered or accepted the action, `agent` for a fully autonomous AI agent, `workflow` for a user-created workflow that ran autonomously, and `rule` for an autonomous rule that fired on a trigger. `null` for legacy events.
    """

    USER = "user"
    AGENT = "agent"
    WORKFLOW = "workflow"
    RULE = "rule"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        agent: typing.Callable[[], T_Result],
        workflow: typing.Callable[[], T_Result],
        rule: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListActivityLogsResponseItemsItemActorType.USER:
            return user()
        if self is ListActivityLogsResponseItemsItemActorType.AGENT:
            return agent()
        if self is ListActivityLogsResponseItemsItemActorType.WORKFLOW:
            return workflow()
        if self is ListActivityLogsResponseItemsItemActorType.RULE:
            return rule()
