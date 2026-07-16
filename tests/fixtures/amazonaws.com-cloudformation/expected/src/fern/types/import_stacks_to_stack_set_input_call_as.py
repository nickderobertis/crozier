

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImportStacksToStackSetInputCallAs(enum.StrEnum):
    """
    <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed stack sets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>
    """

    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"

    def visit(self, self_: typing.Callable[[], T_Result], delegated_admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImportStacksToStackSetInputCallAs.SELF:
            return self_()
        if self is ImportStacksToStackSetInputCallAs.DELEGATED_ADMIN:
            return delegated_admin()
