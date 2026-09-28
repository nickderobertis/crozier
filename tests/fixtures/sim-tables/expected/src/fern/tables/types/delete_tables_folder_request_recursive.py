

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteTablesFolderRequestRecursive(enum.StrEnum):
    """
    Delete the folder's nested files and folders too. An empty folder deletes either way; a non-empty one needs this. The listed spellings are the whole accepted vocabulary and are case-sensitive; any other value is rejected.
    """

    TRUE = "true"
    ONE = "1"
    YES = "yes"
    ON = "on"
    Y = "y"
    ENABLED = "enabled"
    FALSE = "false"
    ZERO = "0"
    NO = "no"
    OFF = "off"
    N = "n"
    DISABLED = "disabled"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        one: typing.Callable[[], T_Result],
        yes: typing.Callable[[], T_Result],
        on: typing.Callable[[], T_Result],
        y: typing.Callable[[], T_Result],
        enabled: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        zero: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        off: typing.Callable[[], T_Result],
        n: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeleteTablesFolderRequestRecursive.TRUE:
            return true()
        if self is DeleteTablesFolderRequestRecursive.ONE:
            return one()
        if self is DeleteTablesFolderRequestRecursive.YES:
            return yes()
        if self is DeleteTablesFolderRequestRecursive.ON:
            return on()
        if self is DeleteTablesFolderRequestRecursive.Y:
            return y()
        if self is DeleteTablesFolderRequestRecursive.ENABLED:
            return enabled()
        if self is DeleteTablesFolderRequestRecursive.FALSE:
            return false()
        if self is DeleteTablesFolderRequestRecursive.ZERO:
            return zero()
        if self is DeleteTablesFolderRequestRecursive.NO:
            return no()
        if self is DeleteTablesFolderRequestRecursive.OFF:
            return off()
        if self is DeleteTablesFolderRequestRecursive.N:
            return n()
        if self is DeleteTablesFolderRequestRecursive.DISABLED:
            return disabled()
