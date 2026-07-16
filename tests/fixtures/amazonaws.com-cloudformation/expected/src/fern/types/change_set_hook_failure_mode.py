

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChangeSetHookFailureMode(str, enum.Enum):
    """
    <p>Specify the hook failure mode for non-compliant resources in the followings ways.</p> <ul> <li> <p> <code>FAIL</code> Stops provisioning resources.</p> </li> <li> <p> <code>WARN</code> Allows provisioning to continue with a warning message.</p> </li> </ul>
    """

    FAIL = "FAIL"
    WARN = "WARN"

    def visit(self, fail: typing.Callable[[], T_Result], warn: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChangeSetHookFailureMode.FAIL:
            return fail()
        if self is ChangeSetHookFailureMode.WARN:
            return warn()
