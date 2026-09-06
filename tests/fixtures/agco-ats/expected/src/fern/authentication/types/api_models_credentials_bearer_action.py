

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsCredentialsBearerAction(enum.StrEnum):
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
        if self is ApiModelsCredentialsBearerAction.NONE:
            return none()
        if self is ApiModelsCredentialsBearerAction.RESET:
            return reset()
        if self is ApiModelsCredentialsBearerAction.DISABLE:
            return disable()
