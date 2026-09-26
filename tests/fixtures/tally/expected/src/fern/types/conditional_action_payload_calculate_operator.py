

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionalActionPayloadCalculateOperator(enum.StrEnum):
    """
    Math or assignment operator.
    """

    ADDITION = "ADDITION"
    SUBTRACTION = "SUBTRACTION"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    ASSIGNMENT = "ASSIGNMENT"

    def visit(
        self,
        addition: typing.Callable[[], T_Result],
        subtraction: typing.Callable[[], T_Result],
        multiplication: typing.Callable[[], T_Result],
        division: typing.Callable[[], T_Result],
        assignment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConditionalActionPayloadCalculateOperator.ADDITION:
            return addition()
        if self is ConditionalActionPayloadCalculateOperator.SUBTRACTION:
            return subtraction()
        if self is ConditionalActionPayloadCalculateOperator.MULTIPLICATION:
            return multiplication()
        if self is ConditionalActionPayloadCalculateOperator.DIVISION:
            return division()
        if self is ConditionalActionPayloadCalculateOperator.ASSIGNMENT:
            return assignment()
