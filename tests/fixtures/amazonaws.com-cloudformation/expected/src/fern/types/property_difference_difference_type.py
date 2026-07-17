

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PropertyDifferenceDifferenceType(enum.StrEnum):
    """
    <p>The type of property difference.</p> <ul> <li> <p> <code>ADD</code>: A value has been added to a resource property that's an array or list data type.</p> </li> <li> <p> <code>REMOVE</code>: The property has been removed from the current resource configuration.</p> </li> <li> <p> <code>NOT_EQUAL</code>: The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).</p> </li> </ul>
    """

    ADD = "ADD"
    REMOVE = "REMOVE"
    NOT_EQUAL = "NOT_EQUAL"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        not_equal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PropertyDifferenceDifferenceType.ADD:
            return add()
        if self is PropertyDifferenceDifferenceType.REMOVE:
            return remove()
        if self is PropertyDifferenceDifferenceType.NOT_EQUAL:
            return not_equal()
