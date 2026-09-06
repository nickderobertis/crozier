

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsTokenOptionsBearerAction(enum.StrEnum):
    """
    The action to perform on the bearer token. Optional. Defaults to ‘None’.
    """

    NONE = "None"
    RESET = "Reset"
    DISABLE = "Disable"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        reset: typing.Callable[[], T_Result],
        disable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApiModelsTokenOptionsBearerAction.NONE:
            return none()
        if self is ApiModelsTokenOptionsBearerAction.RESET:
            return reset()
        if self is ApiModelsTokenOptionsBearerAction.DISABLE:
            return disable()
