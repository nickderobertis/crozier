

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObjectReferenceNullishObjectType(enum.StrEnum):
    """
    Type of the object the event is originating from.
    """

    PROJECT_LOGS = "project_logs"
    EXPERIMENT = "experiment"
    DATASET = "dataset"
    PROMPT = "prompt"
    FUNCTION = "function"
    PROMPT_SESSION = "prompt_session"

    def visit(
        self,
        project_logs: typing.Callable[[], T_Result],
        experiment: typing.Callable[[], T_Result],
        dataset: typing.Callable[[], T_Result],
        prompt: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
        prompt_session: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObjectReferenceNullishObjectType.PROJECT_LOGS:
            return project_logs()
        if self is ObjectReferenceNullishObjectType.EXPERIMENT:
            return experiment()
        if self is ObjectReferenceNullishObjectType.DATASET:
            return dataset()
        if self is ObjectReferenceNullishObjectType.PROMPT:
            return prompt()
        if self is ObjectReferenceNullishObjectType.FUNCTION:
            return function()
        if self is ObjectReferenceNullishObjectType.PROMPT_SESSION:
            return prompt_session()
