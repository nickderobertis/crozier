

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchoolType(enum.StrEnum):
    """
    The type of school
    """

    PRIMARY_SCHOOL = "primary school"
    POST_SECONDARY_INSTITUTION = "post-secondary institution"
    SECONDARY_SCHOOL = "secondary school"

    def visit(
        self,
        primary_school: typing.Callable[[], T_Result],
        post_secondary_institution: typing.Callable[[], T_Result],
        secondary_school: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchoolType.PRIMARY_SCHOOL:
            return primary_school()
        if self is SchoolType.POST_SECONDARY_INSTITUTION:
            return post_secondary_institution()
        if self is SchoolType.SECONDARY_SCHOOL:
            return secondary_school()
