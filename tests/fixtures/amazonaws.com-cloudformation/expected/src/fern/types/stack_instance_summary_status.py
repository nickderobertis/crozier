

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackInstanceSummaryStatus(enum.StrEnum):
    """
    <p>The status of the stack instance, in terms of its synchronization with its associated stack set.</p> <ul> <li> <p> <code>INOPERABLE</code>: A <code>DeleteStackInstances</code> operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further <code>UpdateStackSet</code> operations. You might need to perform a <code>DeleteStackInstances</code> operation, with <code>RetainStacks</code> set to <code>true</code>, to delete the stack instance, and then delete the stack manually.</p> </li> <li> <p> <code>OUTDATED</code>: The stack isn't currently up to date with the stack set because:</p> <ul> <li> <p>The associated stack failed during a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation.</p> </li> <li> <p>The stack was part of a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation that failed or was stopped before the stack was created or updated.</p> </li> </ul> </li> <li> <p> <code>CURRENT</code>: The stack is currently up to date with the stack set.</p> </li> </ul>
    """

    CURRENT = "CURRENT"
    OUTDATED = "OUTDATED"
    INOPERABLE = "INOPERABLE"

    def visit(
        self,
        current: typing.Callable[[], T_Result],
        outdated: typing.Callable[[], T_Result],
        inoperable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackInstanceSummaryStatus.CURRENT:
            return current()
        if self is StackInstanceSummaryStatus.OUTDATED:
            return outdated()
        if self is StackInstanceSummaryStatus.INOPERABLE:
            return inoperable()
