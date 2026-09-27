

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompanyType(enum.StrEnum):
    """
    The type of the company
    """

    EDUCATIONAL = "educational"
    GOVERNMENT = "government"
    NONPROFIT = "nonprofit"
    PRIVATE = "private"
    PUBLIC = "public"

    def visit(
        self,
        educational: typing.Callable[[], T_Result],
        government: typing.Callable[[], T_Result],
        nonprofit: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CompanyType.EDUCATIONAL:
            return educational()
        if self is CompanyType.GOVERNMENT:
            return government()
        if self is CompanyType.NONPROFIT:
            return nonprofit()
        if self is CompanyType.PRIVATE:
            return private()
        if self is CompanyType.PUBLIC:
            return public()
