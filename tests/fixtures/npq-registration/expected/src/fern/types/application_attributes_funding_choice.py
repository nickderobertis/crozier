

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationAttributesFundingChoice(enum.StrEnum):
    """
    Indicates how this NPQ participant has said they will funded their training
    """

    SCHOOL = "school"
    TRUST = "trust"
    SELF = "self"
    ANOTHER = "another"
    EMPLOYER = "employer"

    def visit(
        self,
        school: typing.Callable[[], T_Result],
        trust: typing.Callable[[], T_Result],
        self_: typing.Callable[[], T_Result],
        another: typing.Callable[[], T_Result],
        employer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplicationAttributesFundingChoice.SCHOOL:
            return school()
        if self is ApplicationAttributesFundingChoice.TRUST:
            return trust()
        if self is ApplicationAttributesFundingChoice.SELF:
            return self_()
        if self is ApplicationAttributesFundingChoice.ANOTHER:
            return another()
        if self is ApplicationAttributesFundingChoice.EMPLOYER:
            return employer()
