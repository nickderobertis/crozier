

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiModelsCredentialsMacAction(enum.StrEnum):
    """
    The action to perform on the MAC token. Optional. Defaults to ‘None’.
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
        if self is ApiModelsCredentialsMacAction.NONE:
            return none()
        if self is ApiModelsCredentialsMacAction.RESET:
            return reset()
        if self is ApiModelsCredentialsMacAction.DISABLE:
            return disable()
